from abc import ABC, abstractmethod

from .moves import STRUGGLE, Move
from .pokemon import Pokemon
from .typechart import effect_message, effectiveness

STAB = 1.5
BOOST_FACTOR = 2


class UnknownMove(Exception):
    pass


class Creature(ABC):

    def __init__(self, pokemon: Pokemon, level: int,
                 moves: tuple[Move, ...]) -> None:
        self.name = pokemon.name
        self.elements = pokemon.elements
        self.level = level
        self.moves = moves
        self.max_hp = (2 * pokemon.hp * level) // 100 + level + 10
        self.current_hp = self.max_hp
        self.attack_stat = (2 * pokemon.attack * level) // 100 + 5
        self.defense_stat = (2 * pokemon.defense * level) // 100 + 5
        self.base_attack = self.attack_stat
        self.base_defense = self.defense_stat
        self.speed_stat = (2 * pokemon.speed * level) // 100 + 5
        self.pp = {move.name: move.pp for move in moves}
        self.boosted = False
        self.guarded = False
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
        stab = STAB if move.element in self.elements else 1.0
        chart = effectiveness(move.element, defender.elements)
        base = (2 * self.level / 5 + 2) * move.power
        base = base * self.attack_stat / defender.defense_stat
        return int((base / 50 + 2) * stab * chart)

    def best_move_against(self, defender: "Creature") -> Move:
        best = STRUGGLE
        score = -1
        for move in self.moves_with_effect("DAMAGE"):
            hit = self.damage_to(defender, move)
            if hit > score:
                best, score = move, hit
        return best

    def worst_move_against(self, defender: "Creature") -> Move:
        worst = STRUGGLE
        score = -1
        for move in self.moves_with_effect("DAMAGE"):
            hit = self.damage_to(defender, move)
            if score < 0 or hit < score:
                worst, score = move, hit
        return worst

    def spend(self, move: Move) -> None:
        if move.name in self.pp:
            self.pp[move.name] -= 1

    def take(self, amount: int) -> None:
        self.current_hp = max(0, self.current_hp - amount)

    def strike(self, defender: "Creature",
               move: Move | None = None) -> str:
        if move is None:
            move = self.best_move_against(defender)
        self.spend(move)
        if defender.protected:
            defender.protected = False
            return (f"{self.name} uses {move.name}!"
                    f" But {defender.name} protected itself!")
        hit = self.damage_to(defender, move)
        defender.take(hit)
        line = f"{self.name} uses {move.name}!"
        chart = effectiveness(move.element, defender.elements)
        note = effect_message(chart)
        if note:
            line = f"{line}\n{note}"
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
