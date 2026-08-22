from abc import ABC, abstractmethod

from . import roll
from .creature import (Creature, FireCreature, GrassCreature, WildCreature,
                       WaterCreature)
from .pokedex import (BASE_LEVEL, MAX_LEVEL, POKEDEX, by_number,
                      lookup)
from .pokemon import Pokemon, evolution_trigger, known_moves


def creature_class(pokemon: Pokemon) -> type[Creature]:
    element = pokemon.elements[0]
    if element == "Fire":
        return FireCreature
    if element == "Water":
        return WaterCreature
    if element == "Grass":
        return GrassCreature
    return WildCreature


def level_band(previous_at: int, own_at: int) -> tuple[int, int]:
    low = previous_at if previous_at else BASE_LEVEL
    high = own_at - 1 if own_at else MAX_LEVEL
    return low, high


class CreatureFactory(ABC):

    def __init__(self, base: Pokemon, level: int | None = None) -> None:
        self.fixed_level = level
        self.base = base
        nxt = base.evolves_into
        self.evolved = nxt if nxt is not None else base
        last = self.evolved.evolves_into
        self.final = last if last is not None else self.evolved

    def roll_base_level(self) -> int:
        if self.fixed_level is not None:
            return self.fixed_level
        low, high = level_band(0, self.base.evolves_at)
        return roll.between(low, high)

    def roll_evolved_level(self) -> int:
        if self.fixed_level is not None:
            return self.fixed_level
        low, high = level_band(self.base.evolves_at,
                               self.evolved.evolves_at)
        return roll.between(low, high)

    def roll_final_level(self) -> int:
        if self.fixed_level is not None:
            return self.fixed_level
        low, high = level_band(self.evolved.evolves_at,
                               self.final.evolves_at)
        return roll.between(low, high)

    def create_pokemon(self, pokemon: Pokemon, level: int) -> Creature:
        moves = known_moves(pokemon, level)
        maker = creature_class(pokemon)
        return maker(pokemon, level, moves)

    def evolution_message(self) -> str:
        if not self.base.evolves:
            return f"{self.base.name} does not evolve."
        base_name = self.base.name
        trigger = evolution_trigger(self.base)
        first_line = f"What? {base_name} is evolving!"
        second_line = (
            f"Congratulations! Your {base_name} evolved into "
            f"{self.evolved.name}!"
        )
        return f"{trigger}\n{first_line}\n{second_line}"

    def final_message(self) -> str:
        if not self.evolved.evolves:
            return f"{self.evolved.name} does not evolve."
        evolved_name = self.evolved.name
        trigger = evolution_trigger(self.evolved)
        first_line = f"What? {evolved_name} is evolving!"
        second_line = (
            f"Congratulations! Your {evolved_name} evolved into "
            f"{self.final.name}!"
        )
        return f"{trigger}\n{first_line}\n{second_line}"

    def message(self, creature: Creature) -> str:
        received = f"You received the {creature.name}!"
        return f"{received}\n{creature.describe()}"

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

    @abstractmethod
    def create_final(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    family = "Flame"

    def __init__(self, generation: int,
                 level: int | None = None) -> None:
        super().__init__(lookup(self.family, generation), level)

    def create_base(self) -> Creature:
        level = self.roll_base_level()
        return FireCreature(self.base, level,
                            known_moves(self.base, level))

    def create_evolved(self) -> Creature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return FireCreature(self.evolved, level,
                            known_moves(self.evolved, level))

    def create_final(self) -> Creature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return FireCreature(self.final, level,
                            known_moves(self.final, level))


class AquaFactory(CreatureFactory):

    family = "Aqua"

    def __init__(self, generation: int,
                 level: int | None = None) -> None:
        super().__init__(lookup(self.family, generation), level)

    def create_base(self) -> Creature:
        level = self.roll_base_level()
        return WaterCreature(self.base, level,
                             known_moves(self.base, level))

    def create_evolved(self) -> Creature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return WaterCreature(self.evolved, level,
                             known_moves(self.evolved, level))

    def create_final(self) -> Creature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return WaterCreature(self.final, level,
                             known_moves(self.final, level))


class FloraFactory(CreatureFactory):

    family = "Flora"

    def __init__(self, generation: int,
                 level: int | None = None) -> None:
        super().__init__(lookup(self.family, generation), level)

    def create_base(self) -> Creature:
        level = self.roll_base_level()
        return GrassCreature(self.base, level,
                             known_moves(self.base, level))

    def create_evolved(self) -> Creature:
        if not self.base.evolves:
            return self.create_base()
        level = self.roll_evolved_level()
        return GrassCreature(self.evolved, level,
                             known_moves(self.evolved, level))

    def create_final(self) -> Creature:
        if not self.evolved.evolves:
            return self.create_evolved()
        level = self.roll_final_level()
        return GrassCreature(self.final, level,
                             known_moves(self.final, level))


class PokedexFactory(CreatureFactory):

    def __init__(self, pokedex_nb: int,
                 level: int | None = None) -> None:
        super().__init__(by_number(pokedex_nb), level)

    def create_base(self) -> Creature:
        return self.create_pokemon(self.base, self.roll_base_level())

    def create_evolved(self) -> Creature:
        if not self.base.evolves:
            return self.create_base()
        return self.create_pokemon(self.evolved, self.roll_evolved_level())

    def create_final(self) -> Creature:
        if not self.evolved.evolves:
            return self.create_evolved()
        return self.create_pokemon(self.final, self.roll_final_level())

    def message(self, creature: Creature) -> str:
        caught = (f"You caught a {creature.name}"
                  f" at Lv.{creature.level}!")
        return f"{caught}\n{creature.describe()}"


class WildFactory(PokedexFactory):

    def __init__(self, level: int | None = None) -> None:
        super().__init__(roll.between(1, len(POKEDEX)), level)

    def message(self, creature: Creature) -> str:
        appeared = f"A wild {creature.name} appeared!"
        return f"{appeared}\n{super().message(creature)}"


class StartersFactory:

    def __init__(self, generation: int) -> None:
        self.generation = generation
        self.flame = FlameFactory(generation)
        self.aqua = AquaFactory(generation)
        self.flora = FloraFactory(generation)
        self.families = [self.flame, self.aqua, self.flora]

    def create_starters(self) -> list[Creature]:
        starters = []
        for factory in self.families:
            base = factory.create_base()
            starters.append(base)
        return starters

    def create_evolved(self) -> list[Creature]:
        evolutions = []
        for factory in self.families:
            evolved = factory.create_evolved()
            evolutions.append(evolved)
        return evolutions

    def create_final(self) -> list[Creature]:
        finals = []
        for factory in self.families:
            final = factory.create_final()
            finals.append(final)
        return finals
