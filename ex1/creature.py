from ex0.creature import Creature

from .capability import (DefendCapability, HealCapability,
                         TransformCapability)

HEAL_DIVISOR = 2
TRANSFORM_COST_DIVISOR = 2
TRANSFORM_MULTIPLIER = 2
BOOST_NUMERATOR = 3
BOOST_DENOMINATOR = 2
COSTLY_BOOST = "Belly Drum"
GUARD_MULTIPLIER = 2


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


def do_transform(self: Creature) -> str:
    available = self.moves_with_effect("BOOST")
    if not available:
        return f"{self.name} has no transform moves left!"
    move = available[0]
    if move.name != COSTLY_BOOST:
        self.spend(move)
        self.attack_stat = (self.base_attack * BOOST_NUMERATOR
                            // BOOST_DENOMINATOR)
        self.boosted = True
        return f"{self.name} uses {move.name}! (attack raised)"
    cost = self.max_hp // TRANSFORM_COST_DIVISOR
    if self.current_hp <= cost:
        return f"{self.name} is too weak to transform!"
    self.spend(move)
    self.current_hp -= cost
    self.attack_stat = self.base_attack * TRANSFORM_MULTIPLIER
    self.boosted = True
    return (f"{self.name} uses {move.name}! "
            f"(attack doubled, -{cost} HP)")


def do_revert(self: Creature) -> str:
    if not self.boosted:
        return f"{self.name} is already in its normal form."
    self.attack_stat = self.base_attack
    self.boosted = False
    return f"{self.name} returns to normal."


def do_guard(self: Creature) -> str:
    shields = self.moves_with_effect("PROTECT")
    if shields:
        move = shields[0]
        self.spend(move)
        self.protected = True
        return (f"{self.name} uses {move.name}!"
                f" (the next hit will not land)")
    available = self.moves_with_effect("GUARD")
    if not available:
        return f"{self.name} has nothing left to guard with!"
    move = available[0]
    self.spend(move)
    if self.guarded:
        return f"{self.name}'s defense is already raised!"
    self.defense_stat = self.base_defense * GUARD_MULTIPLIER
    self.guarded = True
    return (f"{self.name} uses {move.name}!"
            f" (incoming damage halved)")


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
