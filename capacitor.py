#!/usr/bin/env python3
"""Test script for the ex1 package: capabilities.

Run: python3 capacitor.py

Healing line : describe -> attack -> heal
Transform line: describe -> attack -> transform -> attack -> revert
"""

import typing

from ex0 import PokedexFactory
from ex0.creature import Creature
from ex0.roll import seed
from ex1 import HealingCreatureFactory, TransformCreatureFactory

HEAL_BANNER = "Testing Creature with healing capability"
TRANSFORM_BANNER = "Testing Creature with transform capability"
BASE_LABEL = " base:"
EVOLVED_LABEL = " evolved:"
SPARRING_PARTNER = 143
LEVEL = 50
SEED = 1
WOUND = 120


# Python has no intersection type, so neither `Creature` nor
# `HealCapability` alone can annotate "a Creature that ALSO heals".
# A Protocol describes the shape instead of the ancestry: anything
# with these methods satisfies it, whatever it inherits from.
# ex1 therefore does not need to expose the capability ABCs at all.


class Healer(typing.Protocol):

    def describe(self) -> str: ...

    def status(self) -> str: ...

    def take(self, amount: int) -> None: ...

    def attack(self, defender: Creature) -> str: ...

    def heal(self) -> str: ...


class Transformer(typing.Protocol):

    def describe(self) -> str: ...

    def status(self) -> str: ...

    def attack(self, defender: Creature) -> str: ...

    def transform(self) -> str: ...

    def revert(self) -> str: ...


def banner(title: str) -> None:
    print(f"{title}")


def sparring_partner() -> Creature:
    return PokedexFactory(SPARRING_PARTNER, LEVEL).create_base()


def show_healer(creature: Healer) -> None:
    """describe -> attack -> heal."""
    print(f"{creature.describe()}")
    print(f"{creature.attack(sparring_partner())}")
    creature.take(WOUND)
    print(f"{creature.status()}")
    print(f"{creature.heal()}")
    print(f"{creature.status()}")


def show_transformer(creature: Transformer) -> None:
    """describe -> attack -> transform -> attack -> revert."""
    target = sparring_partner()
    print(f"{creature.describe()}")
    print(f"{creature.attack(target)}")
    print(f"{creature.transform()}")
    print(f"{creature.attack(target)}")
    print(f"{creature.revert()}")


def test_healing() -> None:
    banner(HEAL_BANNER)
    factory = HealingCreatureFactory(LEVEL)
    print(f"{BASE_LABEL}")
    show_healer(factory.create_base())
    print(f"{EVOLVED_LABEL}")
    show_healer(factory.create_evolved())


def test_transform() -> None:
    banner(TRANSFORM_BANNER)
    factory = TransformCreatureFactory(LEVEL)
    print(f"{BASE_LABEL}")
    show_transformer(factory.create_base())
    print(f"{EVOLVED_LABEL}")
    show_transformer(factory.create_evolved())


def main() -> None:
    seed(SEED)
    test_healing()
    print()
    test_transform()


if __name__ == "__main__":
    main()
