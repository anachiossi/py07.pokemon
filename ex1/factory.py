from ex0.factory import CreatureFactory
from ex0.pokedex import by_number
from ex0.pokemon import known_moves

from .creature import (DefendingCreature, HealingCreature,
                       TransformCreature)

# examples of healing, transforming, and defending creatures for testing
CHANSEY = 113
MUNCHLAX = 446
SHELLDER = 90


class HealingCreatureFactory(CreatureFactory):

    def __init__(self, level: int | None = None,
                 number: int = CHANSEY) -> None:
        super().__init__(by_number(number), level)

    def create_base(self) -> HealingCreature:
        level = self.roll_base_level()
        return HealingCreature(self.base, level,
                               known_moves(self.base, level))

    def create_evolved(self) -> HealingCreature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return HealingCreature(self.evolved, level,
                               known_moves(self.evolved, level))

    def create_final(self) -> HealingCreature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return HealingCreature(self.final, level,
                               known_moves(self.final, level))


class TransformCreatureFactory(CreatureFactory):

    def __init__(self, level: int | None = None,
                 number: int = MUNCHLAX) -> None:
        super().__init__(by_number(number), level)

    def create_base(self) -> TransformCreature:
        level = self.roll_base_level()
        return TransformCreature(self.base, level,
                                 known_moves(self.base, level))

    def create_evolved(self) -> TransformCreature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return TransformCreature(self.evolved, level,
                                 known_moves(self.evolved, level))

    def create_final(self) -> TransformCreature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return TransformCreature(self.final, level,
                                 known_moves(self.final, level))


class DefendingCreatureFactory(CreatureFactory):

    def __init__(self, level: int | None = None,
                 number: int = SHELLDER) -> None:
        super().__init__(by_number(number), level)

    def create_base(self) -> DefendingCreature:
        level = self.roll_base_level()
        return DefendingCreature(self.base, level,
                                 known_moves(self.base, level))

    def create_evolved(self) -> DefendingCreature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return DefendingCreature(self.evolved, level,
                                 known_moves(self.evolved, level))

    def create_final(self) -> DefendingCreature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return DefendingCreature(self.final, level,
                                 known_moves(self.final, level))
