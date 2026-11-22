# py07.pokemon

A Pokemon battle engine and a playable terminal game in pure Python:
1025 species, 709 moves, the full 18x18 type chart, the real damage
formula. Built to find out where a textbook design breaks at scale.

## Running it

```
python3 game.py         # the playable battle
python3 battle.py       # factories, evolution, type effectiveness
python3 capacitor.py    # heal / transform / guard
python3 tournament.py   # strategies driving full battles
```

No arguments, no install, no dependencies.

## The game

One or two players at the same keyboard. Pick a Pokemon by name, from the
starters -- choosing Charmander, Charmeleon *or* Charizard -- or at
random; pick a level; fight with arrow keys, HP bars and type tags.

## What is inside

| package | pattern | holds |
| --- | --- | --- |
| `ex0/` | Abstract Factory | species, moves, type chart, damage math |
| `ex1/` | capability mixins | heal, transform, guard |
| `ex2/` | Strategy | four battle AIs |

A factory takes an element and a generation, rolls a level inside the
band the evolution allows, and hands over the best four moves the species
has learned by then. Strategies return lines instead of printing them.

## Combat

```
(((2 * Level / 5 + 2) * Power * Attack / Defense) / 50 + 2)
    * STAB * type * (0.85 .. 1.00)
```

| property | what it does |
| --- | --- |
| `hits` | 25 moves land more than once -- twelve roll 2-5 on the game's 35/35/15/15 odds, Population Bomb up to ten |
| `accuracy` | 47 moves can miss: Inferno at 50%, Blizzard at 70%, Hydro Pump at 80% |
| `drain` | 12 moves heal from the damage they land -- Giga Drain 50%, Draining Kiss 75% |

Stat stages go three deep (1.5x, 2x, 2.5x) and last the whole battle.
Run out of PP on everything and you Struggle -- no type chart, and a
quarter of your own health.

`DAMAGE_SCALE` softens the result. Unscaled, the median battle ran two
turns with 18% one-shot kills; at 0.6 it runs four rounds with 1%.

## Two imports

```
$ grep -rh '^import \|^from ' ex0/ ex1/ ex2/ battle.py capacitor.py \
    tournament.py | grep -v '^from \.\|^from ex'
import typing
from abc import ABC, abstractmethod
```

That explains what looks deranged here: `ex0/roll.py` is a hand-written
random number generator because `random` is off the list, and the Pokedex
is 11,380 lines of literals because `json` and `open()` are too.

`game.py` is exempt -- it needs `termios` to read a keypress.

## What scale revealed

**Abstract Factory scaled fine.** 1021 more species changed no method
signature.

**Classes as data records did not.** One class per species means 1025
near-identical classes. Here a species is a `NamedTuple`: a hierarchy
should be as deep as the behaviour, not as deep as the data.

**Capabilities-as-inheritance broke.** 85 species carry two or more
capability moves at level 100. Hatterene knows Heal Pulse and Calm Mind;
whichever class you pick for it, one of the two is dead.

Neither class is wrong -- the model is. The fix is `VersatileCreature`,
which inherits all three and works. It is also the tell: when the answer
is "inherit everything", inheritance was not the right axis.

**The capability belongs to the move, not the creature.** A class is
chosen once, when the factory builds. A moveset is recomputed at every
level. Those are not the same clock.

Bulbasaur learns Synthesis at 27, so a Bulbasaur built at 26 cannot heal
and the same species at 27 can -- and the factory has to choose the class
before it knows. 125 species cross that line between level 5 and 100.

```python
def is_valid(self, creature: Creature) -> bool:
    return hasattr(creature, HEAL)                  # can the class

def act(self, attacker: Creature, defender: Creature) -> list[str]:
    ready = attacker.moves_with_effect(HEAL_EFFECT)  # can this one, now
```

Every strategy has to ask twice. The first question is about the type,
the second about the four moves this creature is carrying this turn. Four
creatures could never have exposed that; a thousand could not hide it.

## Verification

```
flake8 ex0/ ex1/ ex2/ *.py
mypy --strict ex0/ ex1/ ex2/ *.py
```

Both clean at 79 columns. 1025 species, 9 generations, 709 moves, 18
types, every `POKEDEX` key equal to its entry's `number`.

## Provenance

A fork of a 42 school exercise that teaches Abstract Factory, Strategy
and capability mixins on four invented creatures. Only the data was
swapped -- four creatures cannot tell you whether a design works.
