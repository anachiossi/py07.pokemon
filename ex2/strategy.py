import typing
from abc import ABC, abstractmethod

from ex0.creature import MAX_STAGE, Creature

from .errors import InvalidStrategy


SETUP_STAGES = 1
GUARD = "guard"
HEAL = "heal"
HEAL_EFFECT = "HEAL"
BOOST_EFFECT = "BOOST"
GUARD_EFFECT = "GUARD"
TRANSFORM = "transform"


class Healer(typing.Protocol):

    def heal(self) -> str: ...


class Defender(typing.Protocol):

    def guard(self) -> str: ...


class Transformer(typing.Protocol):

    def transform(self) -> str: ...

    def revert(self) -> str: ...


class BattleStrategy(ABC):

    label: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, attacker: Creature, defender: Creature) -> list[str]:
        pass

    def refuse(self, creature: Creature) -> InvalidStrategy:
        message = (f"'{creature.name} can't use "
                   f"{self.label} strategy")
        return InvalidStrategy(message)


class NormalStrategy(BattleStrategy):

    label = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, attacker: Creature, defender: Creature) -> list[str]:
        return [attacker.attack(defender)]


class EasyStrategy(BattleStrategy):

    label = "easy"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, attacker: Creature, defender: Creature) -> list[str]:
        move = attacker.worst_move_against(defender)
        return [attacker.strike(defender, move)]


class AggressiveStrategy(BattleStrategy):

    label = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, TRANSFORM)

    def act(self, attacker: Creature, defender: Creature) -> list[str]:
        if not self.is_valid(attacker):
            raise self.refuse(attacker)
        shifter = typing.cast(Transformer, attacker)
        ready = attacker.moves_with_effect(BOOST_EFFECT)
        if ready and attacker.attack_stage < SETUP_STAGES:
            return [shifter.transform()]
        return [attacker.attack(defender)]


class DefensiveStrategy(BattleStrategy):

    label = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, HEAL)

    def act(self, attacker: Creature, defender: Creature) -> list[str]:
        if not self.is_valid(attacker):
            raise self.refuse(attacker)
        shields = attacker.moves_with_effect(GUARD_EFFECT)
        if shields and attacker.defense_stage < MAX_STAGE:
            if hasattr(attacker, GUARD):
                attacker.attacked = True
                shell = typing.cast(Defender, attacker)
                return [shell.guard()]
        ready = attacker.moves_with_effect(HEAL_EFFECT)
        if attacker.attacked and ready:
            attacker.attacked = False
            healer = typing.cast(Healer, attacker)
            return [healer.heal()]
        attacker.attacked = True
        return [attacker.attack(defender)]
