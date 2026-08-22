from abc import ABC, abstractmethod

from . import roll
from .moves import ONCE, STRUGGLE, TWO_TO_FIVE, Move
from .pokemon import Pokemon
from .typechart import effect_message, effectiveness

STAB = 1.5
MAX_STAGE = 3
STAGE_STEP = 2
HIT_ODDS = ((2, 35), (3, 70), (4, 85), (5, 100))
ODDS_MAX = 100
SPREAD_AVERAGE = 3.1
SPREAD_LOW = 85
RECOIL_DIVISOR = 4
IV = 31
EV_SHARE = 21
DAMAGE_SCALE = 0.6


def stat(base: int, level: int) -> int:
    return ((2 * base + IV + EV_SHARE) * level) // 100


def staged(base: int, stage: int) -> int:
    return base * (STAGE_STEP + stage) // STAGE_STEP


def roll_hits(move: Move) -> int:
    """How many times this move lands, rolled fresh on every use."""
    low, high = move.hits
    if low == high:
        return low
    if move.hits == TWO_TO_FIVE:
        chance = roll.between(1, ODDS_MAX)
        for hits, upto in HIT_ODDS:
            if chance <= upto:
                return hits
    return roll.between(low, high)


def varied(damage: int) -> int:
    """The game's 85-100% roll, applied to each hit that lands."""
    if damage <= 0:
        return 0
    return max(1, damage * roll.between(SPREAD_LOW, ODDS_MAX) // ODDS_MAX)


def average_hits(move: Move) -> float:
    """What a move is worth before it is rolled, for ranking moves."""
    low, high = move.hits
    if move.hits == TWO_TO_FIVE:
        return SPREAD_AVERAGE
    return (low + high) / 2


class UnknownMove(Exception):
    pass


class Creature(ABC):

    def __init__(self, pokemon: Pokemon, level: int,
                 moves: tuple[Move, ...]) -> None:
        self.name = pokemon.name
        self.elements = pokemon.elements
        self.level = level
        self.moves = moves
        self.max_hp = stat(pokemon.hp, level) + level + 10
        self.base_attack = stat(pokemon.attack, level) + 5
        self.base_defense = stat(pokemon.defense, level) + 5
        self.speed_stat = stat(pokemon.speed, level) + 5
        self.restore()

    def restore(self) -> None:
        """Back to the state a battle starts from."""
        self.current_hp = self.max_hp
        self.pp = {move.name: move.pp for move in self.moves}
        self.attack_stat = self.base_attack
        self.defense_stat = self.base_defense
        self.attack_stage = 0
        self.defense_stage = 0
        self.protected = False
        self.attacked = False

    def fainted(self) -> bool:
        return self.current_hp <= 0

    def move_at(self, slot: int) -> Move:
        if not self.moves:
            message = f"{self.name} has no moves recorded"
            raise UnknownMove(message)
        if slot < 1 or slot > len(self.moves):
            message = (f"{self.name} has no move in slot {slot}"
                       f" (slots are 1-{len(self.moves)})")
            raise UnknownMove(message)
        return self.moves[slot - 1]

    def has_pp(self, move: Move) -> bool:
        return self.pp.get(move.name, 0) > 0

    def moves_with_effect(self, effect: str) -> tuple[Move, ...]:
        found = []
        for move in self.moves:
            if move.effect == effect and self.has_pp(move):
                found.append(move)
        return tuple(found)

    def damage_to(self, defender: "Creature", move: Move) -> int:
        if not move.power:
            return 0
        if move is STRUGGLE:
            stab, chart = 1.0, 1.0
        else:
            stab = STAB if move.element in self.elements else 1.0
            chart = effectiveness(move.element, defender.elements)
        base = (2 * self.level / 5 + 2) * move.power
        base = base * self.attack_stat / defender.defense_stat
        return int((base / 50 + 2) * stab * chart * DAMAGE_SCALE)

    def expected_damage(self, defender: "Creature", move: Move) -> int:
        """What a move is worth once hits and accuracy are priced in."""
        per_hit = self.damage_to(defender, move) * average_hits(move)
        return int(per_hit * move.accuracy / ODDS_MAX)

    def best_move_against(self, defender: "Creature") -> Move:
        best = STRUGGLE
        score = -1
        for move in self.moves_with_effect("DAMAGE"):
            hit = self.expected_damage(defender, move)
            if hit > score:
                best, score = move, hit
        return best

    def worst_move_against(self, defender: "Creature") -> Move:
        worst = STRUGGLE
        score = -1
        for move in self.moves_with_effect("DAMAGE"):
            hit = self.expected_damage(defender, move)
            if score < 0 or hit < score:
                worst, score = move, hit
        return worst

    def spend(self, move: Move) -> None:
        if move.name in self.pp:
            self.pp[move.name] -= 1

    def take(self, amount: int) -> None:
        self.current_hp = max(0, self.current_hp - amount)

    def absorb(self, amount: int) -> int:
        """Heal, never past full, and report what actually went in."""
        gained = min(amount, self.max_hp - self.current_hp)
        self.current_hp += gained
        return gained

    def raise_attack(self, steps: int = 1) -> int:
        """Climb the attack stages, returning how many were gained."""
        room = MAX_STAGE - self.attack_stage
        gained = min(steps, room)
        self.attack_stage += gained
        self.attack_stat = staged(self.base_attack, self.attack_stage)
        return gained

    def raise_defense(self, steps: int = 1) -> int:
        room = MAX_STAGE - self.defense_stage
        gained = min(steps, room)
        self.defense_stage += gained
        self.defense_stat = staged(self.base_defense, self.defense_stage)
        return gained

    def reset_attack(self) -> None:
        self.attack_stage = 0
        self.attack_stat = self.base_attack

    def strike(self, defender: "Creature",
               move: Move | None = None) -> str:
        if move is None:
            move = self.best_move_against(defender)
        self.spend(move)
        line = f"{self.name} uses {move.name}!"
        if defender.protected:
            defender.protected = False
            return f"{line} But {defender.name} protected itself!"
        if roll.between(1, ODDS_MAX) > move.accuracy:
            return f"{line}\n{self.name}'s attack missed!"
        hit = self.damage_to(defender, move)
        landed = 0
        dealt = 0
        for _ in range(roll_hits(move)):
            if defender.fainted():
                break
            before = defender.current_hp
            defender.take(varied(hit))
            dealt += before - defender.current_hp
            landed += 1
        if move is not STRUGGLE:
            chart = effectiveness(move.element, defender.elements)
            note = effect_message(chart)
            if note:
                line = f"{line}\n{note}"
        if move.hits != ONCE:
            line = f"{line}\nHit {landed} time(s)!"
        if move.drain and dealt:
            self.absorb(dealt * move.drain // ODDS_MAX)
            line = f"{line}\n{defender.name} had its energy drained!"
        if move is STRUGGLE:
            self.take(self.max_hp // RECOIL_DIVISOR)
            line = f"{line}\n{self.name} is hit with recoil!"
        return line

    def describe(self) -> str:
        label = "/".join(self.elements)
        return f"{self.name} is a {label} type Creature"

    def status(self) -> str:
        return f"{self.name} {self.current_hp}/{self.max_hp} HP"

    @abstractmethod
    def attack(self, defender: "Creature") -> str:
        pass


class FireCreature(Creature):

    def attack(self, defender: "Creature") -> str:
        return self.strike(defender)


class WaterCreature(Creature):

    def attack(self, defender: "Creature") -> str:
        return self.strike(defender)


class GrassCreature(Creature):

    def attack(self, defender: "Creature") -> str:
        return self.strike(defender)


class WildCreature(Creature):

    def attack(self, defender: "Creature") -> str:
        return self.strike(defender)
