#!/usr/bin/env python3

from ex0 import (AquaFactory, CreatureFactory, FlameFactory, FloraFactory,
                 PokedexFactory, StartersFactory, WildFactory)
from ex0.creature import Creature, UnknownMove
from ex0.pokedex import GENERATIONS, UnknownGeneration
from ex0.roll import seed
from ex0.typechart import effect_message, effectiveness

EX_NAME = "Starter Pokedex"
FACTORY_BANNER = "Testing factory"
BATTLE_BANNER = "Testing battle"
SWEEP_BANNER = "Testing generation sweep (Fire)"
TABLE_BANNER = "Testing the professor's table"
DEX_BANNER = "Testing the pokedex factory"
WILD_BANNER = "Testing the wild factory"
CHART_BANNER = "Testing type chart"
MOVES_BANNER = "Testing move selection"
ERROR_BANNER = "Testing invalid generation"
VS_LABEL = " vs "
FIGHT_LABEL = " fight!"
ERROR_PREFIX = "Factory error:"
MOVE_ERROR_PREFIX = "Move error:"
SEED = 1
BAD_GENERATION = 12
BAD_SLOT = 0
SPARRING_PARTNER = 133
DEX_PICKS = (25, 133, 448)
WILD_ENCOUNTERS = 4


def banner(title: str) -> None:
    print(f"{title}")


def trade(attacker: Creature, defender: Creature) -> None:
    move = attacker.best_move_against(defender)
    print(f"{attacker.attack(defender)}")
    multiplier = effectiveness(move.element, defender.elements)
    message = effect_message(multiplier)
    if message:
        print(f"{message}")
    print(f"  {defender.status()}")


def test_factory(factory: CreatureFactory) -> None:
    banner(FACTORY_BANNER)
    dummy = PokedexFactory(SPARRING_PARTNER).create_base()
    base = factory.create_base()
    print(f"{factory.message(base)}")
    print(f"{base.attack(dummy)}")
    print(f"{factory.evolution_message()}")
    evolved = factory.create_evolved()
    print(f"{evolved.describe()}")
    print(f"{evolved.attack(dummy)}")
    print(f"{factory.final_message()}")
    final = factory.create_final()
    print(f"{final.describe()}")
    print(f"{final.attack(dummy)}")


def test_battle(left: CreatureFactory, right: CreatureFactory) -> None:
    banner(BATTLE_BANNER)
    first = left.create_base()
    second = right.create_base()
    print(f"{first.name}{VS_LABEL}{second.name}")
    print(f"{FIGHT_LABEL}")
    trade(first, second)
    trade(second, first)


def test_table(generation: int) -> None:
    banner(f"{TABLE_BANNER} - Gen {generation}")
    table = StartersFactory(generation)
    starters = table.create_starters()
    evolutions = table.create_evolved()
    finals = table.create_final()
    families = table.families
    for factory, base, evolved, final in zip(families, starters,
                                             evolutions, finals):
        print(f"{base.describe()}")
        step_one = f"{base.name} (Lv.{factory.base.evolves_at})"
        step_two = f"{evolved.name} (Lv.{factory.evolved.evolves_at})"
        print(f"  {step_one} -> {step_two} -> {final.name}")


def test_pokedex() -> None:
    banner(DEX_BANNER)
    for number in DEX_PICKS:
        factory = PokedexFactory(number)
        creature = factory.create_base()
        print(f"{factory.message(creature)}")
        print(f"  {creature.status()}")


def test_wild() -> None:
    banner(WILD_BANNER)
    for encounter in range(WILD_ENCOUNTERS):
        factory = WildFactory()
        creature = factory.create_base()
        print(f"{factory.message(creature)}")
        print(f"  {creature.status()}")


def test_sweep() -> None:
    banner(SWEEP_BANNER)
    for generation in GENERATIONS:
        factory = FlameFactory(generation)
        base = factory.base
        evolved = factory.evolved
        step_one = f"{base.name} (Lv.{base.evolves_at})"
        step_two = f"{evolved.name} (Lv.{evolved.evolves_at})"
        line = f"Gen {generation}: {step_one} -> {step_two}"
        print(f"{line} -> {factory.final.name}")


def matchup(attacker: Creature, defender: Creature) -> None:
    attack_element = attacker.best_move_against(defender).element
    multiplier = effectiveness(attack_element, defender.elements)
    label = "/".join(defender.elements)
    text = f"{attack_element} vs {defender.name} ({label})"
    print(f"{text}: x{multiplier:g}")


def test_chart() -> None:
    banner(CHART_BANNER)
    bulbasaur = FloraFactory(1).create_base()
    squirtle = AquaFactory(1).create_base()
    swampert = AquaFactory(3).create_final()
    charizard = FlameFactory(1).create_final()
    empoleon = AquaFactory(4).create_final()
    greninja = AquaFactory(6).create_final()
    matchup(bulbasaur, swampert)
    matchup(bulbasaur, charizard)
    matchup(bulbasaur, empoleon)
    matchup(bulbasaur, greninja)
    matchup(squirtle, charizard)


def test_moves() -> None:
    banner(MOVES_BANNER)
    attacker = FlameFactory(1).create_final()
    defender = FloraFactory(1).create_base()
    print(f"{attacker.name}{VS_LABEL}{defender.name}")
    for slot in range(1, len(attacker.moves) + 1):
        move = attacker.move_at(slot)
        multiplier = effectiveness(move.element, defender.elements)
        note = effect_message(multiplier) or "Normal damage."
        print(f"  slot {slot}: {move.name} ({move.element}) -> {note}")
    try:
        attacker.move_at(BAD_SLOT)
    except UnknownMove as error:
        print(f"  {MOVE_ERROR_PREFIX} {error}")


def test_bad_generation() -> None:
    banner(ERROR_BANNER)
    try:
        FlameFactory(BAD_GENERATION)
    except UnknownGeneration as error:
        print(f"{ERROR_PREFIX} {error}")


def main() -> None:
    seed(SEED)
    print(f"=== {EX_NAME} ===")
    print()
    test_factory(FlameFactory(1))
    print()
    test_factory(FloraFactory(7))
    print()
    test_table(1)
    print()
    test_table(9)
    print()
    test_battle(FlameFactory(1), FloraFactory(1))
    print()
    test_battle(FloraFactory(1), AquaFactory(1))
    print()
    test_battle(AquaFactory(1), FlameFactory(1))
    print()
    test_pokedex()
    print()
    test_wild()
    print()
    test_sweep()
    print()
    test_chart()
    print()
    test_moves()
    print()
    test_bad_generation()


if __name__ == "__main__":
    main()
