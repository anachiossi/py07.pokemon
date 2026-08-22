#!/usr/bin/env python3
"""Test script for the ex2 package: abstract strategies.

Run: python3 tournament.py

Every opponent is created at TOURNAMENT_LEVEL, so the strategy is the
only variable. Final forms fight - a Munchlax knows one damaging move
at Lv100, a Snorlax knows three.
"""

from ex0 import AquaFactory, CreatureFactory, FlameFactory, FloraFactory
from ex0.creature import Creature
from ex0.roll import seed
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (AggressiveStrategy, BattleStrategy, DefensiveStrategy,
                 InvalidStrategy, NormalStrategy)

TOURNAMENT_LEVEL = 100
TURN_LIMIT = 20
SEED = 1

TOURNAMENT_BANNER = "*** Tournament ***"
BATTLE_BANNER = "* Battle *"
OPPONENTS_LABEL = "opponents involved"
VS_LABEL = " vs "
FIGHT_LABEL = " now fight!"
ESCAPE_LABEL = "Got away safely!"
ERROR_PREFIX = "Battle error, aborting tournament:"

Opponent = tuple[CreatureFactory, BattleStrategy]


def turn(strategy: BattleStrategy, attacker: Creature,
         defender: Creature) -> bool:
    for line in strategy.act(attacker, defender):
        print(f"   {line}")
    print(f"   {defender.status()}")
    if defender.fainted():
        print(f"   {defender.name} fainted!")
        return True
    return False


def fight(left: Opponent, right: Opponent) -> None:
    first = left[0].create_final()
    second = right[0].create_final()
    print(f"{BATTLE_BANNER}")
    print(f"{first.name}{VS_LABEL}{second.name}")
    print(f"{FIGHT_LABEL}")
    quick, slow = left, right
    lead, trail = first, second
    if second.speed_stat > first.speed_stat:
        quick, slow = right, left
        lead, trail = second, first
    print(f"   {lead.name} is faster and moves first")
    for count in range(TURN_LIMIT):
        if turn(quick[1], lead, trail):
            return
        if turn(slow[1], trail, lead):
            return
    print(f"   {ESCAPE_LABEL}")


def battle(opponents: list[Opponent]) -> None:
    print(f"{TOURNAMENT_BANNER}")
    print(f"{len(opponents)} {OPPONENTS_LABEL}")
    try:
        for index, left in enumerate(opponents):
            for right in opponents[index + 1:]:
                print()
                fight(left, right)
    except InvalidStrategy as error:
        print(f"{ERROR_PREFIX} {error}")


def main() -> None:
    seed(SEED)
    level = TOURNAMENT_LEVEL
    flame = FlameFactory(1, level)
    aqua = AquaFactory(1, level)
    flora = FloraFactory(1, level)
    healer = HealingCreatureFactory(level)
    shifter = TransformCreatureFactory(level)
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Charizard+Normal), (Blissey+Defensive) ]")
    battle([(flame, normal), (healer, defensive)])

    print()
    print("Tournament 1 (error)")
    print(" [ (Charizard+Aggressive), (Blissey+Defensive) ]")
    battle([(flame, aggressive), (healer, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print(" [ (Blastoise+Normal), (Blissey+Defensive),"
          " (Snorlax+Aggressive) ]")
    battle([(aqua, normal), (healer, defensive), (shifter, aggressive)])

    print()
    print("Tournament 3 (all five)")
    battle([(flame, normal), (aqua, normal), (flora, normal),
            (healer, defensive), (shifter, aggressive)])


if __name__ == "__main__":
    main()
