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

A move carries a `hits` range and an `accuracy` alongside its power.
Most moves are `(1, 1)` and 100; Double Kick and its ten relatives are
`(2, 2)`, Triple Kick is `(3, 3)`, Population Bomb is `(1, 10)`, and
twelve moves -- Bullet Seed, Pin Missile, Rock Blast and the rest -- are
`(2, 5)`, rolled on the game's own 35/35/15/15 odds rather than
uniformly. 47 moves carry a real sub-100 accuracy: Inferno and Zap
Cannon at 50, Blizzard and Focus Blast at 70, Hydro Pump at 80. Every
move not on that list is 100, which is true of most of the roster.

`strike` rolls accuracy once, then hit count, then the 85-100% damage
spread on each hit that lands, and stops early if the target faints
partway through. It reports the way the games do -- `Charizard's attack
missed!`, `Hit 3 time(s)!`. Move ranking goes through `expected_damage`,
which prices in both, so Inferno at 100 power and 50 accuracy scores
below Flamethrower at 90 and 100, exactly as it should. `damage_to`
itself stays pure and deterministic: rolling inside it would make the
strategies non-repeatable.

Struggle is the fallback when nothing has PP left, on both sides of the
screen. It ignores STAB and the type chart -- it will hit a Ghost that
is immune to Normal -- and costs its user a quarter of max HP.

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
Soft-Boiled, and `transform` and `guard` climb the real stat stages --
three of them, at 1.5x, 2x and 2.5x, capped there. Belly Drum still pays
half the user's HP, but it buys every remaining stage at once.
Protect-class moves cancel the next hit instead of raising anything.

Stages last for the rest of the battle; nothing decays them. The lines
are the game's own -- `Blastoise's Defense rose!`, `Scizor's Attack
won't go higher!`, `Snorlax cut its own HP and maximized its Attack!` --
rather than a parenthesised summary.

### ex2 -- Strategy

`BattleStrategy` is the ABC. `is_valid` decides whether a creature can
run the strategy, `act` runs one turn of it and returns the lines to
print.

- **Normal** picks the move with the best effectiveness against the
  defender.
- **Easy** picks the worst one, deliberately.
- **Aggressive** needs `transform`: one boost, then it fights. Stacking
  all three stages is a choice left to human players -- an AI that spends
  three of a four-round battle on Swords Dance is easier to beat than one
  that never boosts at all, measured at 62% against 52%.
- **Defensive** needs `heal`: it opens with a guard if it has one, then
  alternates heal and attack.

`is_valid` uses `hasattr` rather than `isinstance`, which matters more
than it looks -- see the finding below.

## What changed, and why

Everything here is a deviation from the letter of the subject.

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

Pick single player or two players sharing the terminal. Pick a Pokemon
by name or number, from the starters -- where a third menu lets you take
Charmander, Charmeleon or Charizard rather than always the last form --
or roll one; pick a level; against the machine, pick the strategy it
runs. Then fight with arrow keys, HP bars, type tags and per-move power.

The arithmetic is the mainline damage formula,
`(((2*L/5 + 2) * Power * A/D) / 50 + 2) * STAB * type * (0.85..1.00)`,
over the real
stat lines with 31 IVs and an even EV spread. One deviation: the result
is scaled by `DAMAGE_SCALE` in `ex0/creature.py`. Unscaled, against a
strategy that always picks its hardest-hitting move, the median battle
ended in two turns and 18% of openings were one-shot kills. At 0.6 the
median is four turns and one-shots are 1%.

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

**The capability belongs to the move, not to the creature.** A class is
chosen once, when the factory constructs the creature. A moveset is
recomputed at every level. Those are not the same clock, and the
capability follows the second one.

Bulbasaur learns Synthesis at level 27. A Bulbasaur built at level 26
cannot heal; the same species built at level 27 can. Nothing about the
class changed, and nothing about the class *could* have changed -- the
factory picks `HealingCreature` or it does not, and it has to pick before
it knows which moves the level will hand over. 125 species cross that
line somewhere between level 5 and level 100.

The code already admits this. `DefensiveStrategy` cannot ask whether its
creature is a `HealCapability` and stop there, because that answers "was
this class declared with a heal method", which is not the question. It
has to ask twice:

```python
def is_valid(self, creature: Creature) -> bool:
    return hasattr(creature, HEAL)              # can the class do it

def act(self, attacker: Creature, defender: Creature) -> list[str]:
    ...
    ready = attacker.moves_with_effect(HEAL_EFFECT)   # can this one, now
```

The first question is about the type. The second is about the four moves
this creature is carrying this turn. The subject's design promised that
one question would be enough, and every strategy in `ex2` had to ask the
second one anyway.

That is the seam. Four creatures could never have exposed it. 1025 could
not hide it.

## Verification

```
flake8 ex0/ ex1/ ex2/ *.py
mypy --strict ex0/ ex1/ ex2/ *.py
```

Both clean. 1025 species, 9 generations, 709 moves, 18 types, and every
`POKEDEX` key equal to its entry's `number`.
