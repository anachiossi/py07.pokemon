#!/usr/bin/env python3
"""Pokemon battle, played from the terminal.

Run: python3 game.py

Not part of the subject's file tree - this is the fun one.
"""

import sys
import termios
import time
import tty
import typing

from ex0 import PokedexFactory
from ex0.creature import Creature
from ex0.moves import Move
from ex0.pokedex import POKEDEX
from ex0.pokemon import Pokemon, known_moves
from ex0.roll import between, seed
from ex0.typechart import effect_message, effectiveness
from ex1.creature import VersatileCreature
from ex2 import (AggressiveStrategy, BattleStrategy, DefensiveStrategy,
                 EasyStrategy, NormalStrategy)
from ex2.strategy import Defender, Healer, Transformer

LEVEL = 100
HALF_LEVEL = 50
BAR_WIDTH = 20
FULL = "█"
EMPTY = "░"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
TINT = "\033[38;5;{0}m"
TYPE_COLOURS = {
    "Normal": 145, "Fire": 208, "Water": 33, "Electric": 220,
    "Grass": 40, "Ice": 51, "Fighting": 124, "Poison": 129,
    "Ground": 179, "Flying": 111, "Psychic": 198, "Bug": 106,
    "Rock": 137, "Ghost": 97, "Dragon": 63, "Dark": 240,
    "Steel": 152, "Fairy": 218,
}
BOLD = "\033[1m"
DIM = "\033[2m"
CLEAR_LINE = "\033[K"
UP_LINES = "\033[{0}A"
HOME = "\033[H"
CLEAR_DOWN = "\033[J"
LOG_LINES = 8
SCREEN_WIDTH = 46
BEAT = 0.55
FRAME = 0.035
DRAIN_STEPS = 12
RESET = "\033[0m"
CURSOR = ">"
HEALTHY = 0.5
HURT = 0.2
UP = "\x1b[A"
DOWN = "\x1b[B"
ENTER = ("\r", "\n")
QUIT = ("q", "Q", "\x03", "\x04")
FIRST_NUMBER = 1
LAST_NUMBER = 1025
TYPES = ("Fire", "Water", "Grass")
FAMILIES = {"Fire": "Flame", "Water": "Aqua", "Grass": "Flora"}
GENERATIONS = 9


def read_key() -> str:
    if not sys.stdin.isatty():
        return sys.stdin.readline().rstrip("\n")
    handle = sys.stdin.fileno()
    saved = termios.tcgetattr(handle)
    try:
        tty.setcbreak(handle)
        key = sys.stdin.read(1)
        if key == "\x1b":
            key += sys.stdin.read(2)
    finally:
        termios.tcsetattr(handle, termios.TCSADRAIN, saved)
    return key


def pick(title: str, options: list[str]) -> int:
    chosen = 0
    height = len(options) + 2
    redraw = sys.stdin.isatty()
    drawn = False
    print()
    while True:
        if drawn and redraw:
            print(UP_LINES.format(height), end="")
        drawn = True
        print(f"{BOLD}{title}{RESET}{CLEAR_LINE}")
        for index, option in enumerate(options):
            mark = f"{BOLD}{CURSOR}{RESET}" if index == chosen else " "
            print(f" {mark} {option}{CLEAR_LINE}")
        hint = (f"up/down + enter, press 1-{len(options)},"
                f" or q to quit")
        print(f"{DIM}   {hint}{RESET}{CLEAR_LINE}")
        key = read_key()
        if key in QUIT:
            raise KeyboardInterrupt
        if key == UP:
            chosen = (chosen - 1) % len(options)
        elif key == DOWN:
            chosen = (chosen + 1) % len(options)
        elif key in ENTER:
            return chosen
        elif key.isdigit() and 1 <= int(key) <= len(options):
            return int(key) - 1
        elif key.strip() == "":
            return chosen


def tag(element: str, width: int = 0) -> str:
    code = TYPE_COLOURS.get(element, TYPE_COLOURS["Normal"])
    return f"{TINT.format(code)}{element.upper():<{width}}{RESET}"


def tags(creature: Creature) -> str:
    return " ".join(tag(element) for element in creature.elements)


def tags_text(creature: Creature) -> str:
    return " ".join(element.upper() for element in creature.elements)


def beat(seconds: float = BEAT) -> None:
    if sys.stdin.isatty():
        time.sleep(seconds)


def bar_text(creature: Creature) -> str:
    return f"{FULL * BAR_WIDTH} {creature.current_hp}/{creature.max_hp}"


def right(plain: str, coloured: str) -> str:
    pad = max(0, SCREEN_WIDTH - len(plain))
    return " " * pad + coloured


def bar(creature: Creature, shown: int | None = None) -> str:
    value = creature.current_hp if shown is None else shown
    ratio = value / creature.max_hp
    filled = int(ratio * BAR_WIDTH)
    if ratio > HEALTHY:
        colour = GREEN
    elif ratio > HURT:
        colour = YELLOW
    else:
        colour = RED
    drawn = FULL * filled + EMPTY * (BAR_WIDTH - filled)
    return f"{colour}{drawn}{RESET} {value}/{creature.max_hp}"


def frame(player: Creature, rival: Creature, log: list[str],
          show_player: int | None, show_rival: int | None) -> list[str]:
    head = f"{rival.name} Lv.{rival.level}  {tags_text(rival)}"
    lines = [
        f"{BOLD}=== POKEMON BATTLE ==={RESET}",
        "",
        right(head, f"{BOLD}{rival.name}{RESET}"
                    f" Lv.{rival.level}  {tags(rival)}"),
        right(bar_text(rival), bar(rival, show_rival)),
        "",
        f"{BOLD}{player.name}{RESET}"
        f" Lv.{player.level}  {tags(player)}",
        f"{bar(player, show_player)}",
        f"{DIM}{'-' * SCREEN_WIDTH}{RESET}",
    ]
    recent = log[-LOG_LINES:]
    for line in recent:
        lines.append(f"  {line}")
    for _ in range(LOG_LINES - len(recent)):
        lines.append("")
    return lines


def render(player: Creature, rival: Creature, log: list[str],
           show_player: int | None = None,
           show_rival: int | None = None) -> None:
    lines = frame(player, rival, log, show_player, show_rival)
    if not sys.stdin.isatty():
        print("\n".join(lines))
        return
    body = "\n".join(line + CLEAR_LINE for line in lines)
    sys.stdout.write(HOME + body + "\n" + CLEAR_DOWN)
    sys.stdout.flush()


def ask_number() -> int:
    while True:
        print(f"\n{BOLD}Name or number{RESET}"
              f" {DIM}({FIRST_NUMBER}-{LAST_NUMBER}){RESET}: ", end="")
        sys.stdout.flush()
        answer = sys.stdin.readline().strip()
        if answer in QUIT:
            raise KeyboardInterrupt
        if answer.isdigit():
            number = int(answer)
            if FIRST_NUMBER <= number <= LAST_NUMBER:
                return number
        for entry in POKEDEX.values():
            if entry.name.lower() == answer.lower():
                return entry.number
        print(f"{RED}No such pokemon.{RESET}")


def ask_starter() -> int:
    element = TYPES[pick("Which type?", list(TYPES))]
    labels = [f"Generation {n}" for n in range(1, GENERATIONS + 1)]
    generation = pick("Which generation?", labels) + 1
    family = FAMILIES[element]
    for entry in POKEDEX.values():
        if entry.family == family and entry.generation == generation:
            if entry.starter and entry.evolves:
                if not any(other.evolves_into is entry
                           for other in POKEDEX.values()):
                    return entry.number
    return FIRST_NUMBER


def choose_level() -> int | None:
    index = pick("Battle level",
                 [f"Lv.{LEVEL}", f"Lv.{HALF_LEVEL}",
                  "Random (each side rolls its own)"])
    if index == 0:
        return LEVEL
    if index == 1:
        return HALF_LEVEL
    return None


def build_creature(number: int, level: int | None) -> Creature:
    final = PokedexFactory(number, level).create_final()
    return VersatileCreature(final_form(POKEDEX[number]),
                             final.level, final.moves)


def final_form(pokemon: Pokemon) -> Pokemon:
    while pokemon.evolves and pokemon.evolves_into is not None:
        pokemon = pokemon.evolves_into
    return pokemon


def candidates(effect: str, level: int | None) -> list[int]:
    found = []
    for entry in POKEDEX.values():
        grown = final_form(entry)
        moves = known_moves(grown, level or LEVEL)
        has_effect = any(m.effect == effect for m in moves)
        can_hit = any(m.effect == "DAMAGE" for m in moves)
        if has_effect and can_hit:
            found.append(entry.number)
    return found


def choose_number() -> int:
    index = pick("Choose your pokemon", ["From the whole pokedex",
                                         "From the starters",
                                         "Surprise me"])
    if index == 0:
        return ask_number()
    if index == 1:
        return ask_starter()
    return between(FIRST_NUMBER, LAST_NUMBER)


def choose_rival(level: int | None
                 ) -> tuple[Creature, BattleStrategy]:
    index = pick("What strategy should your opponent use?",
                 ["Easy", "Normal", "Aggressive", "Defensive"])
    if index == 0:
        number = between(FIRST_NUMBER, LAST_NUMBER)
        return PokedexFactory(number, level).create_final(), EasyStrategy()
    if index == 2:
        pool = candidates("BOOST", level)
        number = pool[between(0, len(pool) - 1)]
        return build_creature(number, level), AggressiveStrategy()
    if index == 3:
        pool = candidates("HEAL", level)
        number = pool[between(0, len(pool) - 1)]
        return build_creature(number, level), DefensiveStrategy()
    number = between(FIRST_NUMBER, LAST_NUMBER)
    plain = PokedexFactory(number, level)
    return plain.create_final(), NormalStrategy()


KINDS = {
    "DAMAGE": ("ATTACK", RESET),
    "HEAL": ("HEAL", GREEN),
    "BOOST": ("BOOST", YELLOW),
    "GUARD": ("GUARD", CYAN),
    "PROTECT": ("PROTECT", CYAN),
    "NONE": ("-", DIM),
}


def move_labels(creature: Creature) -> list[str]:
    labels = []
    for move in creature.moves:
        left = creature.pp[move.name]
        kind, tint = KINDS[move.effect]
        shade = RESET if left else RED
        labels.append(f"{move.name:<16}"
                      f"{tag(move.element, 9)}"
                      f"{tint}{kind:<8}{RESET}"
                      f"{shade}PP {left:>2}/{move.pp:<2}{RESET}")
    return labels


def choose_move(player: Creature) -> Move | None:
    names = move_labels(player)
    if not names:
        return None
    choice = pick(f"{player.name}, choose a move", names)
    return player.moves[choice]


def player_turn(player: Creature, rival: Creature,
                move: Move | None) -> list[str]:
    if move is None:
        return [f"{player.name} has no moves left!"]
    if not player.has_pp(move):
        return [f"{move.name} has no PP left!"]
    if move.effect == "HEAL" and hasattr(player, "heal"):
        return [typing.cast(Healer, player).heal()]
    if move.effect in ("GUARD", "PROTECT") and hasattr(player, "guard"):
        return [typing.cast(Defender, player).guard()]
    if move.effect == "BOOST" and hasattr(player, "transform"):
        return [typing.cast(Transformer, player).transform()]
    player.spend(move)
    if not move.power:
        return [f"{player.name} uses {move.name}!"
                f" But nothing happened!"]
    if rival.protected:
        rival.protected = False
        return [f"{player.name} uses {move.name}!"
                f" But {rival.name} protected itself!"]
    hit = player.damage_to(rival, move)
    rival.take(hit)
    lines = [f"{player.name} uses {move.name}!"]
    note = effect_message(effectiveness(move.element, rival.elements))
    if note:
        lines.append(note)
    return lines


def rival_turn(strategy: BattleStrategy, rival: Creature,
               player: Creature) -> list[str]:
    return strategy.act(rival, player)


def drain(player: Creature, rival: Creature, log: list[str],
          was_player: int, was_rival: int) -> None:
    if not sys.stdin.isatty():
        return
    for step in range(1, DRAIN_STEPS + 1):
        share = step / DRAIN_STEPS
        now_p = was_player + int((player.current_hp - was_player) * share)
        now_r = was_rival + int((rival.current_hp - was_rival) * share)
        render(player, rival, log, now_p, now_r)
        time.sleep(FRAME)


def resolve(player: Creature, rival: Creature, log: list[str],
            lines: list[str], was_player: int, was_rival: int) -> None:
    for line in unfold(lines):
        log.append(line)
        render(player, rival, log, was_player, was_rival)
        beat()
    drain(player, rival, log, was_player, was_rival)


def unfold(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        out.extend(line.splitlines())
    return out


def battle(player: Creature, rival: Creature,
           strategy: BattleStrategy) -> None:
    log: list[str] = []
    faster = player.speed_stat >= rival.speed_stat
    while True:
        render(player, rival, log)
        move = choose_move(player)
        if faster:
            order = (True, False)
        else:
            order = (False, True)
        for is_player in order:
            if is_player:
                was_p, was_r = player.current_hp, rival.current_hp
                resolve(player, rival, log,
                        player_turn(player, rival, move), was_p, was_r)
                if rival.fainted():
                    log.append(f"{GREEN}{rival.name} fainted."
                               f" You win!{RESET}")
                    render(player, rival, log)
                    return
            else:
                was_p, was_r = player.current_hp, rival.current_hp
                resolve(player, rival, log,
                        rival_turn(strategy, rival, player), was_p, was_r)
                if player.fainted():
                    log.append(f"{RED}{player.name} fainted."
                               f" You lose.{RESET}")
                    render(player, rival, log)
                    return


def main() -> None:
    seed(time.time_ns())
    print(f"{BOLD}=== POKEMON BATTLE ==={RESET}")
    number = choose_number()
    level = choose_level()
    player = build_creature(number, level)
    rival, strategy = choose_rival(level)
    print(f"\nYou chose {BOLD}{player.name}{RESET}.")
    print(f"Your opponent is {BOLD}{rival.name}{RESET}.")
    if pick("Are you ready to battle?", ["Yes", "No"]) == 1:
        print("Maybe next time.")
        return
    battle(player, rival, strategy)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{DIM}Got away safely!{RESET}")
