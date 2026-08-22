# py07.pokemon

A parallel universe of Python module 07.

In the universe the subject describes, a `FlameFactory` builds a
`Flameling` that evolves into a `Pyrodon`, and a `Pyrodon` attacks by
printing a sentence. In this one, a `FlameFactory` builds Charmander,
Charmander evolves into Charmeleon at level 16, and the attack resolves
against a defender through the real type chart.

Same architecture. Same four patterns. Same constraints. The only thing
swapped out is the data, and the data was swapped out on purpose: the
subject teaches Abstract Factory, Strategy and capability mixins on four
invented creatures, and four creatures is a sample size that cannot tell
you whether the design works. So this fork runs the same design against
1025 Pokemon, 709 moves and the full 18x18 type chart, and reports what
broke.

Something did break. See [What the experiment found](#what-the-experiment-found).

## Running it

```
python3 battle.py       # ex0 -- factories, evolution, type effectiveness
python3 capacitor.py    # ex1 -- heal / transform / guard capabilities
python3 tournament.py   # ex2 -- strategies driving full battles
python3 game.py         # the playable version (see below)
```

All four run with no arguments and no third-party packages.

## The rules this keeps

The subject authorises `typing` and `abc`. Nothing else. Every file in
`ex0/`, `ex1/`, `ex2/`, plus `battle.py`, `capacitor.py` and
`tournament.py`, imports only those two and each other.

```
$ grep -rh '^import \|^from ' ex0/ ex1/ ex2/ battle.py capacitor.py tournament.py \
    | grep -v '^from \.\|^from ex'
import typing
from abc import ABC, abstractmethod
```

That constraint is the reason for two design choices that would
otherwise look strange:

- **`ex0/roll.py`** is a hand-written linear congruential generator,
  nineteen lines of it, because `import random` is not on the list. It
  is seeded once and threaded through the factories, which also makes
  every run reproducible from its seed.
- **The Pokedex is source code.** With no `json`, no `csv` and no
  `open()` in the authorised set, 1025 species and 709 moves have to be
  Python literals. `ex0/pokemon.py` is 11,380 lines of them.

Everything passes `flake8` at 79 columns and `mypy --strict`.

## Map to the subject

| The subject | Here |
| --- | --- |
| `Creature` (ABC, abstract `attack`) | same, in `ex0/creature.py` |
| `Flameling` -> `Pyrodon` | `FireCreature`, any Fire species |
| `Aquabub` -> `Torragon` | `WaterCreature`, any Water species |
| `FlameFactory`, `AquaFactory` | same names, plus `FloraFactory` |
| `create_base`, `create_evolved` | same, plus `create_final` |
| `HealCapability`, `TransformCapability` | same, plus `DefendCapability` |
| `HealingCreatureFactory` -> Sproutling | -> Chansey -> Blissey |
| `TransformCreatureFactory` -> Shiftling | -> Munchlax -> Snorlax |
| `BattleStrategy` + Normal / Aggressive / Defensive | same, plus `Easy` |

The invented names are gone; the class names the subject mandates are
all still there, doing the job the subject gives them.

## The three exercises

### ex0 -- Abstract Factory

`CreatureFactory` is the abstract factory. `FlameFactory`, `AquaFactory`
and `FloraFactory` are the concrete ones, and each takes a generation, so
`FlameFactory(1)` is the Charmander line and `FlameFactory(6)` is the
Fennekin line. `StartersFactory` sits above the three and dispatches by
element. `PokedexFactory` and `WildFactory` build any of the 1025 by
number.

The factory rolls a level inside the band the evolution allows, so a
Charmander comes out somewhere below 16 and its Charmeleon somewhere
between 16 and 36. Stats derive from the species base stats and that
level; the move set is whatever the species has actually learned by
then, best four.

`attack` is abstract, and `FireCreature`, `WaterCreature`,
`GrassCreature` and `WildCreature` each implement it. They implement it
*identically*, and that is not laziness -- see the note on abstract
`attack` below.

### ex1 -- capabilities

`HealCapability`, `TransformCapability` and `DefendCapability` are three
ABCs that do not inherit from `Creature`. Concrete classes mix one into
`Creature` to get `HealingCreature`, `TransformCreature`,
`DefendingCreature`.

The capabilities are wired to real moves rather than to flat numbers:
`heal` restores half of max HP but is gated by the PP of Recover or
Soft-Boiled, `transform` reads Belly Drum's actual cost of half the
user's HP for a doubled attack, and `guard` either halves incoming
damage or, for Protect-class moves, cancels the next hit outright.

### ex2 -- Strategy

`BattleStrategy` is the ABC. `is_valid` decides whether a creature can
run the strategy, `act` runs one turn of it and returns the lines to
print.

- **Normal** picks the move with the best effectiveness against the
  defender.
- **Easy** picks the worst one, deliberately.
- **Aggressive** needs `transform`: it boosts, attacks, then reverts.
- **Defensive** needs `heal`: it opens with a guard if it has one, then
  alternates heal and attack.

`is_valid` uses `hasattr` rather than `isinstance`, which matters more
than it looks -- see the finding below.

## What changed, and why

Everything here is a deviation from the letter of the subject. Each one
is listed with the reason, because at defense the reason is the point.

**`attack` takes a defender.** The subject's signature is
`attack(self) -> str` and returns a sentence. Here it is
`attack(self, defender) -> str`, because a damage number cannot be
computed without knowing who is being hit. This is the single deviation
with the widest blast radius, and it is what makes the type chart, the
Strategy exercise and the game possible at all.

**`act` returns `list[str]` instead of printing.** The subject's `act`
prints and returns `None`. Returning the lines instead lets `game.py`
render them into a frame rather than dump them to stdout, and lets
`tournament.py` print them itself. The strategies stay free of I/O.

**Extra files in `ex0/`.** The subject has `creature.py` and
`factory.py`. This adds `pokemon.py`, `moves.py`, `pokedex.py`,
`typechart.py` and `roll.py`. None of them contain architecture; they
contain data and two pure functions over it.

**Extra classes.** `FloraFactory` is invented to match `FlameFactory`
and `AquaFactory` in style, since Grass starters exist and the subject
only names two. `EasyStrategy`, `DefendCapability` and `create_final`
are additions in the same spirit. Nothing the subject mandates was
removed.

**A stricter gate.** The subject's `ex0/__init__.py` exports `Creature`.
This one exports the seven factories and nothing else, so the only way
to obtain a creature from outside the package is to ask a factory for
one. That is what Abstract Factory is for.

**Why `attack` is abstract when every implementation is the same.**
This was the hardest thing to justify and it is worth stating plainly:
in a world where every attack lands, the abstract method buys nothing,
and four identical overrides look like a code smell. It stops looking
like one the moment an element needs to behave differently -- a Fire
creature that cannot be burned, a Ghost that ignores Normal moves. The
abstract method is the seam where that difference goes. The identical
bodies are the honest state of a game that has not needed the seam yet,
not a claim that it never will.

## The one exemption: `game.py`

`game.py` is a playable terminal battle and it is **not** part of the
delivery. It imports `sys`, `termios`, `time` and `tty`, which the
subject does not authorise, and it exists for one reason: to put the
architecture under a human at a keyboard, where design mistakes surface
in seconds rather than in review.

It reads only through the public surface -- factories, `Creature`,
strategies. It does not reach past the gates and it does not patch
anything. Delete it and `ex0`, `ex1`, `ex2` and the three subject
scripts are unaffected.

Pick a Pokemon by name or number, or roll one; pick a level; pick the
strategy the opponent runs; then fight it with arrow keys, HP bars,
type tags and the real damage formula.

## What the experiment found

The point of running the subject's design against 1025 creatures instead
of four:

**The Abstract Factory scaled without complaint.** Adding a generation
parameter and 1021 more species changed no method signature. This part
of the subject is sound, and the fork is evidence for it rather than
against it.

**Using classes as data records did not scale.** The subject models each
species as its own class -- `Flameling`, `Pyrodon`. At 1025 species that
is 1025 nearly identical classes, so here the species became a
`NamedTuple` and the *behaviour* stayed in four element classes. The
class hierarchy should be as deep as the behaviour differences, not as
deep as the data.

**The same mistake repeats in ex1, and there it bites.** A capability is
a class you inherit, so a creature has exactly the capabilities its class
was declared with. But at level 100, 85 species carry two or more
capability moves in their best four, and 17 carry both a heal and a
boost. Hatterene knows Heal Pulse and Calm Mind. As a `HealingCreature`
it heals fine and Calm Mind prints "nothing happened"; as a
`TransformCreature`, the reverse. Neither class is wrong -- the model
is.

The fix in the code is `VersatileCreature`, which inherits all three
capabilities, and it works. It is also the tell: when the correct answer
is "inherit everything", inheritance was not the right axis.

**The capability belongs to the move, not to the creature.** What a
Pokemon can do is decided by the four moves it happens to know at that
level, which is data, and it changes when the moves change. Modelling it
as a class fixes at declaration time something that is only knowable at
runtime.

The code already admits this. `DefensiveStrategy` cannot ask
`isinstance(creature, HealCapability)` and stop there, because that
answers "was this class declared with a heal method", which is not the
question. It has to ask twice:

```python
if not hasattr(creature, "heal"):        # can the class do it
    ...
ready = attacker.moves_with_effect("HEAL")   # can this creature do it now
```

Two questions where the design promised one. That is the seam, and this
fork is 14,000 lines of finding it.

## Verification

```
flake8 ex0/ ex1/ ex2/ *.py
mypy --strict ex0/ ex1/ ex2/ *.py
```

Both clean. 1025 species, 9 generations, 709 moves, 18 types, and every
`POKEDEX` key equal to its entry's `number`.
# py07.pokemon
