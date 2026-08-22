from ex0.creature import MAX_STAGE, Creature
from ex0.moves import Move

from .capability import (DefendCapability, HealCapability,
                         TransformCapability)

HEAL_DIVISOR = 2
TRANSFORM_COST_DIVISOR = 2
COSTLY_BOOST = "Belly Drum"
ATTACK = "Attack"
DEFENSE = "Defense"
RISE = {1: "rose!", 2: "sharply rose!", 3: "rose drastically!"}


def rise_line(name: str, which: str, gained: int) -> str:
    """The line the real game prints when a stat stage moves."""
    if not gained:
        return f"{name}'s {which} won't go higher!"
    return f"{name}'s {which} {RISE[gained]}"


def do_heal(self: Creature) -> str:
    available = self.moves_with_effect("HEAL")
    if not available:
        return f"{self.name} has no healing left!"
    move = available[0]
    self.spend(move)
    room = self.max_hp - self.current_hp
    amount = min(room, self.max_hp // HEAL_DIVISOR)
    self.current_hp += amount
    return f"{self.name} uses {move.name}! (+{amount} HP)"


def do_belly_drum(self: Creature, move: Move) -> str:
    """Half the user's HP for every remaining attack stage at once."""
    self.spend(move)
    cost = self.max_hp // TRANSFORM_COST_DIVISOR
    if self.current_hp <= cost or self.attack_stage >= MAX_STAGE:
        return f"{self.name} uses {move.name}!\nBut it failed!"
    self.current_hp -= cost
    self.raise_attack(MAX_STAGE)
    return (f"{self.name} uses {move.name}!\n"
            f"{self.name} cut its own HP and maximized its Attack!")


def do_transform(self: Creature) -> str:
    available = self.moves_with_effect("BOOST")
    if not available:
        return f"{self.name} has no transform moves left!"
    move = available[0]
    if move.name == COSTLY_BOOST:
        return do_belly_drum(self, move)
    self.spend(move)
    gained = self.raise_attack()
    return (f"{self.name} uses {move.name}!\n"
            f"{rise_line(self.name, ATTACK, gained)}")


def do_revert(self: Creature) -> str:
    if not self.attack_stage:
        return f"{self.name} is already in its normal form."
    self.reset_attack()
    return f"{self.name} returns to normal."


def do_guard(self: Creature) -> str:
    shields = self.moves_with_effect("PROTECT")
    if shields:
        move = shields[0]
        self.spend(move)
        self.protected = True
        return (f"{self.name} uses {move.name}!\n"
                f"{self.name} protected itself!")
    available = self.moves_with_effect("GUARD")
    if not available:
        return f"{self.name} has nothing left to guard with!"
    move = available[0]
    self.spend(move)
    gained = self.raise_defense()
    return (f"{self.name} uses {move.name}!\n"
            f"{rise_line(self.name, DEFENSE, gained)}")


class HealingCreature(Creature, HealCapability):

    def attack(self, defender: Creature) -> str:
        return self.strike(defender)

    def heal(self) -> str:
        return do_heal(self)


class TransformCreature(Creature, TransformCapability):

    def attack(self, defender: Creature) -> str:
        return self.strike(defender)

    def transform(self) -> str:
        return do_transform(self)

    def revert(self) -> str:
        return do_revert(self)


class DefendingCreature(Creature, DefendCapability):

    def attack(self, defender: Creature) -> str:
        return self.strike(defender)

    def guard(self) -> str:
        return do_guard(self)


class VersatileCreature(Creature, HealCapability, TransformCapability,
                        DefendCapability):
    """Carries every capability, for a moveset that spans several."""

    def attack(self, defender: Creature) -> str:
        return self.strike(defender)

    def heal(self) -> str:
        return do_heal(self)

    def transform(self) -> str:
        return do_transform(self)

    def revert(self) -> str:
        return do_revert(self)

    def guard(self) -> str:
        return do_guard(self)
