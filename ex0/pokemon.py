import typing

from . import moves as mv
from .moves import Move


class Pokemon(typing.NamedTuple):

    number: int
    name: str
    generation: int
    starter: bool
    family: str
    elements: tuple[str, ...]
    hp: int
    attack: int
    defense: int
    speed: int
    pool: tuple[tuple[int, Move], ...]
    evolves_into: "Pokemon | None"
    evolves_at: int
    evolves: bool
    evolve_method: str


MOVE_SLOTS = 4


def evolution_trigger(pokemon: Pokemon) -> str:
    method = pokemon.evolve_method
    if pokemon.evolves_at:
        return f"{pokemon.name} reached Lv.{pokemon.evolves_at}!"
    if method.startswith("item:"):
        item = method[len("item:"):].replace("-", " ").title()
        return f"Used the {item} on {pokemon.name}!"
    if method == "happiness":
        return f"{pokemon.name} reached max Happiness!"
    if method == "trade":
        return f"{pokemon.name} was traded away!"
    if method:
        shown = method.replace("-", " ")
        return f"{pokemon.name} evolved by {shown}!"
    return f"{pokemon.name} grew stronger!"


def move_rank(entry: tuple[int, Move]) -> tuple[int, int]:
    learn_level, move = entry
    return (learn_level, move.power)


def known_moves(pokemon: Pokemon, level: int) -> tuple[Move, ...]:
    learned = []
    for learn_level, move in pokemon.pool:
        if learn_level <= level and move.effect != "NONE":
            learned.append((learn_level, move))
    learned.sort(key=move_rank)
    chosen = []
    for entry in learned[-MOVE_SLOTS:]:
        chosen.append(entry[1])
    return tuple(chosen)


# --- generation 1 ---
VENUSAUR = Pokemon(
    3, "Venusaur", 1, True,
    "Flora", ("Grass", "Poison"),
    80, 91, 91, 80,
    ((0, mv.PETAL_BLIZZARD), (1, mv.GROWL), (1, mv.GROWTH),
     (1, mv.PETAL_DANCE), (1, mv.TACKLE), (1, mv.VINE_WHIP),
     (9, mv.LEECH_SEED), (12, mv.RAZOR_LEAF), (15, mv.POISON_POWDER),
     (15, mv.SLEEP_POWDER), (20, mv.SEED_BOMB), (25, mv.TAKE_DOWN),
     (30, mv.SWEET_SCENT), (37, mv.SYNTHESIS), (44, mv.WORRY_SEED),
     (51, mv.POWER_WHIP), (58, mv.SOLAR_BEAM)),
    None, 0, False, "")

IVYSAUR = Pokemon(
    2, "Ivysaur", 1, True,
    "Flora", ("Grass", "Poison"),
    60, 71, 71, 60,
    ((1, mv.GROWL), (1, mv.GROWTH), (1, mv.TACKLE), (1, mv.VINE_WHIP),
     (9, mv.LEECH_SEED), (12, mv.RAZOR_LEAF), (15, mv.POISON_POWDER),
     (15, mv.SLEEP_POWDER), (20, mv.SEED_BOMB), (25, mv.TAKE_DOWN),
     (30, mv.SWEET_SCENT), (35, mv.SYNTHESIS), (40, mv.WORRY_SEED),
     (45, mv.POWER_WHIP), (50, mv.SOLAR_BEAM)),
    VENUSAUR, 32, True, "")

BULBASAUR = Pokemon(
    1, "Bulbasaur", 1, True,
    "Flora", ("Grass", "Poison"),
    45, 57, 57, 45,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.VINE_WHIP), (6, mv.GROWTH),
     (9, mv.LEECH_SEED), (12, mv.RAZOR_LEAF), (15, mv.POISON_POWDER),
     (15, mv.SLEEP_POWDER), (18, mv.SEED_BOMB), (21, mv.TAKE_DOWN),
     (24, mv.SWEET_SCENT), (27, mv.SYNTHESIS), (30, mv.WORRY_SEED),
     (33, mv.POWER_WHIP), (36, mv.SOLAR_BEAM)),
    IVYSAUR, 16, True, "")

CHARIZARD = Pokemon(
    6, "Charizard", 1, True,
    "Flame", ("Fire", "Flying"),
    78, 96, 81, 100,
    ((0, mv.AIR_SLASH), (1, mv.DRAGON_CLAW), (1, mv.EMBER), (1, mv.GROWL),
     (1, mv.HEAT_WAVE), (1, mv.SCRATCH), (1, mv.SMOKESCREEN),
     (12, mv.DRAGON_BREATH), (19, mv.FIRE_FANG), (24, mv.SLASH),
     (30, mv.FLAMETHROWER), (39, mv.SCARY_FACE), (46, mv.FIRE_SPIN),
     (54, mv.INFERNO), (62, mv.FLARE_BLITZ)),
    None, 0, False, "")

CHARMELEON = Pokemon(
    5, "Charmeleon", 1, True,
    "Flame", ("Fire",),
    58, 72, 61, 80,
    ((1, mv.EMBER), (1, mv.GROWL), (1, mv.SCRATCH), (1, mv.SMOKESCREEN),
     (12, mv.DRAGON_BREATH), (19, mv.FIRE_FANG), (24, mv.SLASH),
     (30, mv.FLAMETHROWER), (37, mv.SCARY_FACE), (48, mv.INFERNO),
     (54, mv.FLARE_BLITZ)),
    CHARIZARD, 36, True, "")

CHARMANDER = Pokemon(
    4, "Charmander", 1, True,
    "Flame", ("Fire",),
    39, 56, 46, 65,
    ((1, mv.GROWL), (1, mv.SCRATCH), (4, mv.EMBER), (8, mv.SMOKESCREEN),
     (12, mv.DRAGON_BREATH), (17, mv.FIRE_FANG), (20, mv.SLASH),
     (24, mv.FLAMETHROWER), (28, mv.SCARY_FACE), (32, mv.FIRE_SPIN),
     (36, mv.INFERNO), (40, mv.FLARE_BLITZ)),
    CHARMELEON, 16, True, "")

BLASTOISE = Pokemon(
    9, "Blastoise", 1, True,
    "Aqua", ("Water",),
    79, 84, 102, 78,
    ((0, mv.FLASH_CANNON), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.WATER_GUN), (1, mv.WITHDRAW), (9, mv.RAPID_SPIN), (12, mv.BITE),
     (15, mv.WATER_PULSE), (20, mv.PROTECT), (25, mv.RAIN_DANCE),
     (30, mv.AQUA_TAIL), (35, mv.SHELL_SMASH), (42, mv.IRON_DEFENSE),
     (49, mv.HYDRO_PUMP), (56, mv.WAVE_CRASH)),
    None, 0, False, "")

WARTORTLE = Pokemon(
    8, "Wartortle", 1, True,
    "Aqua", ("Water",),
    59, 64, 80, 58,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (1, mv.WITHDRAW),
     (9, mv.RAPID_SPIN), (12, mv.BITE), (15, mv.WATER_PULSE), (20, mv.PROTECT),
     (25, mv.RAIN_DANCE), (30, mv.AQUA_TAIL), (35, mv.SHELL_SMASH),
     (40, mv.IRON_DEFENSE), (45, mv.HYDRO_PUMP), (50, mv.WAVE_CRASH)),
    BLASTOISE, 36, True, "")

SQUIRTLE = Pokemon(
    7, "Squirtle", 1, True,
    "Aqua", ("Water",),
    44, 49, 64, 43,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (3, mv.WATER_GUN), (6, mv.WITHDRAW),
     (9, mv.RAPID_SPIN), (12, mv.BITE), (15, mv.WATER_PULSE), (18, mv.PROTECT),
     (21, mv.RAIN_DANCE), (24, mv.AQUA_TAIL), (27, mv.SHELL_SMASH),
     (30, mv.IRON_DEFENSE), (33, mv.HYDRO_PUMP), (36, mv.WAVE_CRASH)),
    WARTORTLE, 16, True, "")

BUTTERFREE = Pokemon(
    12, "Butterfree", 1, False,
    "", ("Bug", "Flying"),
    60, 67, 65, 70,
    ((1, mv.BUG_BITE), (1, mv.GUST), (1, mv.HARDEN), (1, mv.STRING_SHOT),
     (1, mv.TACKLE), (4, mv.SUPERSONIC), (8, mv.CONFUSION),
     (12, mv.POISON_POWDER), (12, mv.SLEEP_POWDER), (12, mv.STUN_SPORE),
     (16, mv.PSYBEAM), (20, mv.WHIRLWIND), (24, mv.AIR_SLASH),
     (28, mv.SAFEGUARD), (32, mv.BUG_BUZZ), (36, mv.TAILWIND),
     (40, mv.RAGE_POWDER), (44, mv.QUIVER_DANCE)),
    None, 0, False, "")

METAPOD = Pokemon(
    11, "Metapod", 1, False,
    "", ("Bug",),
    50, 22, 40, 30,
    ((1, mv.HARDEN),),
    BUTTERFREE, 10, True, "")

CATERPIE = Pokemon(
    10, "Caterpie", 1, False,
    "", ("Bug",),
    45, 25, 27, 45,
    ((1, mv.STRING_SHOT), (1, mv.TACKLE), (9, mv.BUG_BITE)),
    METAPOD, 7, True, "")

BEEDRILL = Pokemon(
    15, "Beedrill", 1, False,
    "", ("Bug", "Poison"),
    65, 67, 60, 75,
    ((1, mv.TWINEEDLE), (11, mv.FURY_ATTACK), (14, mv.RAGE), (17, mv.PURSUIT),
     (20, mv.FOCUS_ENERGY), (23, mv.VENOSHOCK), (26, mv.ASSURANCE),
     (29, mv.TOXIC_SPIKES), (32, mv.PIN_MISSILE), (35, mv.POISON_JAB),
     (38, mv.AGILITY), (41, mv.ENDEAVOR), (44, mv.FELL_STINGER)),
    None, 0, False, "")

KAKUNA = Pokemon(
    14, "Kakuna", 1, False,
    "", ("Bug", "Poison"),
    45, 25, 37, 35,
    ((0, mv.HARDEN),),
    BEEDRILL, 10, True, "")

WEEDLE = Pokemon(
    13, "Weedle", 1, False,
    "", ("Bug", "Poison"),
    40, 27, 25, 50,
    ((1, mv.POISON_STING), (1, mv.STRING_SHOT), (9, mv.BUG_BITE)),
    KAKUNA, 7, True, "")

PIDGEOT = Pokemon(
    18, "Pidgeot", 1, False,
    "", ("Normal", "Flying"),
    83, 75, 72, 101,
    ((1, mv.HURRICANE), (1, mv.SAND_ATTACK), (1, mv.TACKLE), (9, mv.GUST),
     (13, mv.QUICK_ATTACK), (17, mv.WHIRLWIND), (22, mv.TWISTER),
     (27, mv.FEATHER_DANCE), (32, mv.AGILITY), (38, mv.WING_ATTACK),
     (44, mv.ROOST), (50, mv.TAILWIND), (56, mv.MIRROR_MOVE),
     (62, mv.AIR_SLASH)),
    None, 0, False, "")

PIDGEOTTO = Pokemon(
    17, "Pidgeotto", 1, False,
    "", ("Normal", "Flying"),
    63, 55, 52, 71,
    ((1, mv.SAND_ATTACK), (1, mv.TACKLE), (9, mv.GUST), (13, mv.QUICK_ATTACK),
     (17, mv.WHIRLWIND), (22, mv.TWISTER), (27, mv.FEATHER_DANCE),
     (32, mv.AGILITY), (37, mv.WING_ATTACK), (42, mv.ROOST), (47, mv.TAILWIND),
     (52, mv.MIRROR_MOVE), (57, mv.AIR_SLASH), (62, mv.HURRICANE)),
    PIDGEOT, 36, True, "")

PIDGEY = Pokemon(
    16, "Pidgey", 1, False,
    "", ("Normal", "Flying"),
    40, 40, 37, 56,
    ((1, mv.TACKLE), (5, mv.SAND_ATTACK), (9, mv.GUST), (13, mv.QUICK_ATTACK),
     (17, mv.WHIRLWIND), (21, mv.TWISTER), (25, mv.FEATHER_DANCE),
     (29, mv.AGILITY), (33, mv.WING_ATTACK), (37, mv.ROOST), (41, mv.TAILWIND),
     (45, mv.MIRROR_MOVE), (49, mv.AIR_SLASH), (53, mv.HURRICANE)),
    PIDGEOTTO, 18, True, "")

RATICATE = Pokemon(
    20, "Raticate", 1, False,
    "", ("Normal",),
    55, 65, 65, 97,
    ((0, mv.SCARY_FACE), (1, mv.FOCUS_ENERGY), (1, mv.QUICK_ATTACK),
     (1, mv.SWORDS_DANCE), (1, mv.TACKLE), (1, mv.TAIL_WHIP), (10, mv.BITE),
     (13, mv.PURSUIT), (16, mv.HYPER_FANG), (19, mv.ASSURANCE),
     (24, mv.CRUNCH), (29, mv.SUCKER_PUNCH), (34, mv.SUPER_FANG),
     (39, mv.DOUBLE_EDGE), (44, mv.ENDEAVOR)),
    None, 0, False, "")

RATTATA = Pokemon(
    19, "Rattata", 1, False,
    "", ("Normal",),
    30, 40, 35, 72,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (4, mv.QUICK_ATTACK),
     (7, mv.FOCUS_ENERGY), (10, mv.BITE), (13, mv.PURSUIT),
     (16, mv.HYPER_FANG), (19, mv.ASSURANCE), (22, mv.CRUNCH),
     (25, mv.SUCKER_PUNCH), (28, mv.SUPER_FANG), (31, mv.DOUBLE_EDGE),
     (34, mv.ENDEAVOR)),
    RATICATE, 20, True, "")

FEAROW = Pokemon(
    22, "Fearow", 1, False,
    "", ("Normal", "Flying"),
    65, 75, 63, 100,
    ((1, mv.DRILL_RUN), (1, mv.GROWL), (1, mv.LEER), (1, mv.PECK),
     (1, mv.PLUCK), (8, mv.PURSUIT), (11, mv.FURY_ATTACK), (15, mv.AERIAL_ACE),
     (18, mv.MIRROR_MOVE), (23, mv.ASSURANCE), (27, mv.AGILITY),
     (32, mv.FOCUS_ENERGY), (36, mv.ROOST), (41, mv.DRILL_PECK)),
    None, 0, False, "")

SPEAROW = Pokemon(
    21, "Spearow", 1, False,
    "", ("Normal", "Flying"),
    40, 45, 30, 70,
    ((1, mv.GROWL), (1, mv.PECK), (4, mv.LEER), (8, mv.PURSUIT),
     (11, mv.FURY_ATTACK), (15, mv.AERIAL_ACE), (18, mv.MIRROR_MOVE),
     (22, mv.ASSURANCE), (25, mv.AGILITY), (29, mv.FOCUS_ENERGY),
     (32, mv.ROOST), (36, mv.DRILL_PECK)),
    FEAROW, 20, True, "")

ARBOK = Pokemon(
    24, "Arbok", 1, False,
    "", ("Poison",),
    60, 80, 74, 80,
    ((0, mv.CRUNCH), (1, mv.BITE), (1, mv.FIRE_FANG), (1, mv.ICE_FANG),
     (1, mv.LEER), (1, mv.POISON_STING), (1, mv.THUNDER_FANG), (1, mv.WRAP),
     (12, mv.GLARE), (17, mv.SCREECH), (20, mv.ACID), (27, mv.SPIT_UP),
     (27, mv.STOCKPILE), (27, mv.SWALLOW), (32, mv.ACID_SPRAY),
     (39, mv.SLUDGE_BOMB), (44, mv.GASTRO_ACID), (48, mv.BELCH), (51, mv.HAZE),
     (56, mv.COIL), (63, mv.GUNK_SHOT)),
    None, 0, False, "")

EKANS = Pokemon(
    23, "Ekans", 1, False,
    "", ("Poison",),
    35, 50, 49, 55,
    ((1, mv.LEER), (1, mv.WRAP), (4, mv.POISON_STING), (9, mv.BITE),
     (12, mv.GLARE), (17, mv.SCREECH), (20, mv.ACID), (25, mv.SPIT_UP),
     (25, mv.STOCKPILE), (25, mv.SWALLOW), (28, mv.ACID_SPRAY),
     (33, mv.SLUDGE_BOMB), (36, mv.GASTRO_ACID), (38, mv.BELCH), (41, mv.HAZE),
     (44, mv.COIL), (49, mv.GUNK_SHOT)),
    ARBOK, 22, True, "")

RAICHU = Pokemon(
    26, "Raichu", 1, False,
    "", ("Electric",),
    60, 90, 67, 110,
    ((0, mv.THUNDER_PUNCH), (1, mv.AGILITY), (1, mv.CHARM), (1, mv.DISCHARGE),
     (1, mv.DOUBLE_TEAM), (1, mv.ELECTRO_BALL), (1, mv.FEINT), (1, mv.GROWL),
     (1, mv.IRON_TAIL), (1, mv.LIGHT_SCREEN), (1, mv.NASTY_PLOT),
     (1, mv.NUZZLE), (1, mv.PLAY_NICE), (1, mv.QUICK_ATTACK), (1, mv.SPARK),
     (1, mv.SWEET_KISS), (1, mv.TAIL_WHIP), (1, mv.THUNDER),
     (1, mv.THUNDER_SHOCK), (1, mv.THUNDER_WAVE), (5, mv.THUNDERBOLT)),
    None, 0, False, "")

PIKACHU = Pokemon(
    25, "Pikachu", 1, False,
    "", ("Electric",),
    35, 52, 45, 90,
    ((1, mv.CHARM), (1, mv.GROWL), (1, mv.NASTY_PLOT), (1, mv.NUZZLE),
     (1, mv.PLAY_NICE), (1, mv.QUICK_ATTACK), (1, mv.SWEET_KISS),
     (1, mv.TAIL_WHIP), (1, mv.THUNDER_SHOCK), (4, mv.THUNDER_WAVE),
     (8, mv.DOUBLE_TEAM), (12, mv.ELECTRO_BALL), (16, mv.FEINT),
     (20, mv.SPARK), (24, mv.AGILITY), (28, mv.IRON_TAIL), (32, mv.DISCHARGE),
     (36, mv.THUNDERBOLT), (40, mv.LIGHT_SCREEN), (44, mv.THUNDER)),
    RAICHU, 0, True, "item:thunder-stone")

SANDSLASH = Pokemon(
    28, "Sandslash", 1, False,
    "", ("Ground",),
    75, 72, 82, 65,
    ((1, mv.CRUSH_CLAW), (1, mv.DEFENSE_CURL), (1, mv.POISON_STING),
     (1, mv.SAND_ATTACK), (1, mv.SCRATCH), (9, mv.ROLLOUT),
     (12, mv.FURY_CUTTER), (15, mv.RAPID_SPIN), (18, mv.BULLDOZE),
     (21, mv.SWIFT), (26, mv.FURY_SWIPES), (31, mv.SAND_TOMB), (36, mv.SLASH),
     (41, mv.DIG), (46, mv.GYRO_BALL), (51, mv.SWORDS_DANCE),
     (56, mv.SANDSTORM), (61, mv.EARTHQUAKE)),
    None, 0, False, "")

SANDSHREW = Pokemon(
    27, "Sandshrew", 1, False,
    "", ("Ground",),
    50, 47, 57, 40,
    ((1, mv.DEFENSE_CURL), (1, mv.SCRATCH), (3, mv.POISON_STING),
     (6, mv.SAND_ATTACK), (9, mv.ROLLOUT), (12, mv.FURY_CUTTER),
     (15, mv.RAPID_SPIN), (18, mv.BULLDOZE), (21, mv.SWIFT),
     (24, mv.FURY_SWIPES), (27, mv.AGILITY), (30, mv.SLASH), (33, mv.DIG),
     (36, mv.GYRO_BALL), (39, mv.SWORDS_DANCE), (42, mv.SANDSTORM),
     (45, mv.EARTHQUAKE)),
    SANDSLASH, 22, True, "")

NIDOQUEEN = Pokemon(
    31, "Nidoqueen", 1, False,
    "", ("Poison", "Ground"),
    90, 83, 86, 76,
    ((1, mv.BITE), (1, mv.CRUNCH), (1, mv.DOUBLE_KICK), (1, mv.EARTH_POWER),
     (1, mv.FLATTER), (1, mv.FURY_SWIPES), (1, mv.GROWL), (1, mv.HELPING_HAND),
     (1, mv.POISON_STING), (1, mv.SCRATCH), (1, mv.SUPERPOWER),
     (1, mv.TAIL_WHIP), (1, mv.TOXIC), (1, mv.TOXIC_SPIKES)),
    None, 0, False, "")

NIDORINA = Pokemon(
    30, "Nidorina", 1, False,
    "", ("Poison",),
    70, 58, 61, 56,
    ((1, mv.GROWL), (1, mv.POISON_STING), (1, mv.SCRATCH), (1, mv.TAIL_WHIP),
     (15, mv.FURY_SWIPES), (22, mv.TOXIC_SPIKES), (29, mv.DOUBLE_KICK),
     (36, mv.BITE), (43, mv.HELPING_HAND), (50, mv.TOXIC), (57, mv.FLATTER),
     (64, mv.CRUNCH), (71, mv.EARTH_POWER)),
    NIDOQUEEN, 0, True, "item:moon-stone")

NIDORAN_F = Pokemon(
    29, "Nidoran♀", 1, False,
    "", ("Poison",),
    55, 43, 46, 41,
    ((1, mv.GROWL), (1, mv.POISON_STING), (5, mv.SCRATCH), (10, mv.TAIL_WHIP),
     (15, mv.FURY_SWIPES), (20, mv.TOXIC_SPIKES), (25, mv.DOUBLE_KICK),
     (30, mv.BITE), (35, mv.HELPING_HAND), (40, mv.TOXIC), (45, mv.FLATTER),
     (50, mv.CRUNCH), (55, mv.EARTH_POWER)),
    NIDORINA, 16, True, "")

NIDOKING = Pokemon(
    34, "Nidoking", 1, False,
    "", ("Poison", "Ground"),
    81, 93, 76, 85,
    ((0, mv.MEGAHORN), (1, mv.DOUBLE_KICK), (1, mv.EARTH_POWER),
     (1, mv.FLATTER), (1, mv.FOCUS_ENERGY), (1, mv.FURY_ATTACK),
     (1, mv.HELPING_HAND), (1, mv.HORN_ATTACK), (1, mv.LEER), (1, mv.PECK),
     (1, mv.POISON_JAB), (1, mv.POISON_STING), (1, mv.TOXIC),
     (1, mv.TOXIC_SPIKES)),
    None, 0, False, "")

NIDORINO = Pokemon(
    33, "Nidorino", 1, False,
    "", ("Poison",),
    61, 63, 56, 65,
    ((1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.PECK), (1, mv.POISON_STING),
     (15, mv.FURY_ATTACK), (22, mv.TOXIC_SPIKES), (29, mv.DOUBLE_KICK),
     (36, mv.HORN_ATTACK), (43, mv.HELPING_HAND), (50, mv.TOXIC),
     (57, mv.FLATTER), (64, mv.POISON_JAB), (71, mv.EARTH_POWER)),
    NIDOKING, 0, True, "item:moon-stone")

NIDORAN_M = Pokemon(
    32, "Nidoran♂", 1, False,
    "", ("Poison",),
    46, 48, 40, 50,
    ((1, mv.LEER), (1, mv.POISON_STING), (5, mv.PECK), (10, mv.FOCUS_ENERGY),
     (15, mv.FURY_ATTACK), (20, mv.TOXIC_SPIKES), (25, mv.DOUBLE_KICK),
     (30, mv.HORN_ATTACK), (35, mv.HELPING_HAND), (40, mv.TOXIC),
     (45, mv.FLATTER), (50, mv.POISON_JAB), (55, mv.EARTH_POWER)),
    NIDORINO, 16, True, "")

CLEFABLE = Pokemon(
    36, "Clefable", 1, False,
    "", ("Fairy",),
    95, 82, 81, 60,
    ((1, mv.LIFE_DEW), (1, mv.METEOR_MASH), (1, mv.METRONOME),
     (1, mv.MOONBLAST)),
    None, 0, False, "")

CLEFAIRY = Pokemon(
    35, "Clefairy", 1, False,
    "", ("Fairy",),
    70, 52, 56, 35,
    ((1, mv.CHARM), (1, mv.COPYCAT), (1, mv.DEFENSE_CURL),
     (1, mv.DISARMING_VOICE), (1, mv.GROWL), (1, mv.POUND), (1, mv.SING),
     (1, mv.SPLASH), (1, mv.SWEET_KISS), (4, mv.STORED_POWER), (8, mv.ENCORE),
     (12, mv.AFTER_YOU), (16, mv.LIFE_DEW), (20, mv.METRONOME),
     (24, mv.MOONLIGHT), (28, mv.GRAVITY), (32, mv.METEOR_MASH),
     (36, mv.FOLLOW_ME), (40, mv.COSMIC_POWER), (44, mv.MOONBLAST),
     (48, mv.HEALING_WISH)),
    CLEFABLE, 0, True, "item:moon-stone")

NINETALES = Pokemon(
    38, "Ninetales", 1, False,
    "", ("Fire",),
    73, 78, 87, 100,
    ((1, mv.FLAMETHROWER), (1, mv.QUICK_ATTACK), (1, mv.TAIL_WHIP)),
    None, 0, False, "")

VULPIX = Pokemon(
    37, "Vulpix", 1, False,
    "", ("Fire",),
    38, 45, 52, 65,
    ((1, mv.EMBER), (1, mv.TAIL_WHIP), (4, mv.DISABLE), (8, mv.QUICK_ATTACK),
     (12, mv.SPITE), (16, mv.INCINERATE), (20, mv.CONFUSE_RAY),
     (24, mv.WILL_O_WISP), (28, mv.EXTRASENSORY), (32, mv.FLAMETHROWER),
     (36, mv.IMPRISON), (40, mv.FIRE_SPIN), (44, mv.SAFEGUARD),
     (48, mv.INFERNO), (52, mv.FIRE_BLAST)),
    NINETALES, 0, True, "item:fire-stone")

WIGGLYTUFF = Pokemon(
    40, "Wigglytuff", 1, False,
    "", ("Normal", "Fairy"),
    140, 77, 47, 45,
    ((1, mv.BODY_SLAM), (1, mv.CHARM), (1, mv.COPYCAT), (1, mv.COVET),
     (1, mv.DEFENSE_CURL), (1, mv.DISABLE), (1, mv.DISARMING_VOICE),
     (1, mv.DOUBLE_EDGE), (1, mv.ECHOED_VOICE), (1, mv.GYRO_BALL),
     (1, mv.HYPER_VOICE), (1, mv.MIMIC), (1, mv.POUND), (1, mv.REST),
     (1, mv.ROUND), (1, mv.SING), (1, mv.SPIT_UP), (1, mv.STOCKPILE),
     (1, mv.SWALLOW), (1, mv.SWEET_KISS), (5, mv.PLAY_ROUGH)),
    None, 0, False, "")

JIGGLYPUFF = Pokemon(
    39, "Jigglypuff", 1, False,
    "", ("Normal", "Fairy"),
    115, 45, 22, 20,
    ((1, mv.CHARM), (1, mv.COPYCAT), (1, mv.DEFENSE_CURL), (1, mv.DISABLE),
     (1, mv.DISARMING_VOICE), (1, mv.POUND), (1, mv.SING), (1, mv.SWEET_KISS),
     (4, mv.ECHOED_VOICE), (8, mv.COVET), (12, mv.SPIT_UP), (12, mv.STOCKPILE),
     (12, mv.SWALLOW), (16, mv.ROUND), (20, mv.REST), (24, mv.BODY_SLAM),
     (28, mv.MIMIC), (32, mv.GYRO_BALL), (36, mv.HYPER_VOICE),
     (44, mv.DOUBLE_EDGE)),
    WIGGLYTUFF, 0, True, "item:moon-stone")


# --- generation 2 ---

CROBAT = Pokemon(
    169, "Crobat", 2, False,
    "", ("Poison", "Flying"),
    85, 80, 80, 130,
    ((0, mv.CROSS_POISON), (1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.MEAN_LOOK),
     (1, mv.SCREECH), (1, mv.SUPERSONIC), (1, mv.TAILWIND), (1, mv.TOXIC),
     (15, mv.POISON_FANG), (20, mv.QUICK_GUARD), (27, mv.AIR_CUTTER),
     (34, mv.BITE), (41, mv.HAZE), (48, mv.VENOSHOCK), (55, mv.CONFUSE_RAY),
     (62, mv.AIR_SLASH), (69, mv.LEECH_LIFE)),
    None, 0, False, "")


# --- generation 1 ---

GOLBAT = Pokemon(
    42, "Golbat", 1, False,
    "", ("Poison", "Flying"),
    75, 72, 72, 90,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.MEAN_LOOK), (1, mv.SCREECH),
     (1, mv.SUPERSONIC), (15, mv.POISON_FANG), (20, mv.QUICK_GUARD),
     (27, mv.AIR_CUTTER), (34, mv.BITE), (41, mv.HAZE), (48, mv.VENOSHOCK),
     (55, mv.CONFUSE_RAY), (62, mv.AIR_SLASH), (69, mv.LEECH_LIFE)),
    CROBAT, 0, True, "happiness")

ZUBAT = Pokemon(
    41, "Zubat", 1, False,
    "", ("Poison", "Flying"),
    40, 37, 37, 55,
    ((1, mv.ABSORB), (1, mv.SUPERSONIC), (5, mv.ASTONISH), (10, mv.MEAN_LOOK),
     (15, mv.POISON_FANG), (20, mv.QUICK_GUARD), (25, mv.AIR_CUTTER),
     (30, mv.BITE), (35, mv.HAZE), (40, mv.VENOSHOCK), (45, mv.CONFUSE_RAY),
     (50, mv.AIR_SLASH), (55, mv.LEECH_LIFE)),
    GOLBAT, 22, True, "")


# --- generation 2 ---

BELLOSSOM = Pokemon(
    182, "Bellossom", 2, False,
    "", ("Grass",),
    75, 85, 97, 50,
    ((0, mv.PETAL_BLIZZARD), (1, mv.ABSORB), (1, mv.ACID), (1, mv.GIGA_DRAIN),
     (1, mv.GRASSY_TERRAIN), (1, mv.GROWTH), (1, mv.MEGA_DRAIN),
     (1, mv.MOONBLAST), (1, mv.MOONLIGHT), (1, mv.PETAL_DANCE),
     (1, mv.POISON_POWDER), (1, mv.QUIVER_DANCE), (1, mv.SLEEP_POWDER),
     (1, mv.STUN_SPORE), (1, mv.SWEET_SCENT), (1, mv.TOXIC)),
    None, 0, False, "")


# --- generation 1 ---

VILEPLUME = Pokemon(
    45, "Vileplume", 1, False,
    "", ("Grass", "Poison"),
    75, 95, 87, 50,
    ((0, mv.PETAL_BLIZZARD), (1, mv.ABSORB), (1, mv.ACID), (1, mv.GIGA_DRAIN),
     (1, mv.GRASSY_TERRAIN), (1, mv.GROWTH), (1, mv.MEGA_DRAIN),
     (1, mv.MOONBLAST), (1, mv.MOONLIGHT), (1, mv.PETAL_DANCE),
     (1, mv.POISON_POWDER), (1, mv.SLEEP_POWDER), (1, mv.STUN_SPORE),
     (1, mv.SWEET_SCENT), (1, mv.TOXIC)),
    BELLOSSOM, 0, True, "Use Sun Stone")

GLOOM = Pokemon(
    44, "Gloom", 1, False,
    "", ("Grass", "Poison"),
    60, 75, 72, 40,
    ((1, mv.ABSORB), (1, mv.ACID), (1, mv.GROWTH), (1, mv.SWEET_SCENT),
     (12, mv.MEGA_DRAIN), (14, mv.POISON_POWDER), (16, mv.STUN_SPORE),
     (18, mv.SLEEP_POWDER), (20, mv.GIGA_DRAIN), (26, mv.TOXIC),
     (32, mv.MOONBLAST), (38, mv.GRASSY_TERRAIN), (44, mv.MOONLIGHT),
     (50, mv.PETAL_DANCE)),
    VILEPLUME, 0, True, "item:sun-stone")

ODDISH = Pokemon(
    43, "Oddish", 1, False,
    "", ("Grass", "Poison"),
    45, 62, 60, 30,
    ((1, mv.ABSORB), (1, mv.GROWTH), (4, mv.ACID), (8, mv.SWEET_SCENT),
     (12, mv.MEGA_DRAIN), (14, mv.POISON_POWDER), (16, mv.STUN_SPORE),
     (18, mv.SLEEP_POWDER), (20, mv.GIGA_DRAIN), (24, mv.TOXIC),
     (28, mv.MOONBLAST), (32, mv.GRASSY_TERRAIN), (36, mv.MOONLIGHT),
     (40, mv.PETAL_DANCE)),
    GLOOM, 21, True, "")

PARASECT = Pokemon(
    47, "Parasect", 1, False,
    "", ("Bug", "Grass"),
    60, 77, 80, 30,
    ((1, mv.CROSS_POISON), (1, mv.POISON_POWDER), (1, mv.SCRATCH),
     (1, mv.STUN_SPORE), (11, mv.ABSORB), (17, mv.FURY_CUTTER), (22, mv.SPORE),
     (29, mv.SLASH), (37, mv.GROWTH), (44, mv.GIGA_DRAIN),
     (51, mv.AROMATHERAPY), (59, mv.RAGE_POWDER), (66, mv.X_SCISSOR)),
    None, 0, False, "")

PARAS = Pokemon(
    46, "Paras", 1, False,
    "", ("Bug", "Grass"),
    35, 57, 55, 25,
    ((1, mv.SCRATCH), (6, mv.POISON_POWDER), (6, mv.STUN_SPORE),
     (11, mv.ABSORB), (17, mv.FURY_CUTTER), (22, mv.SPORE), (27, mv.SLASH),
     (33, mv.GROWTH), (38, mv.GIGA_DRAIN), (43, mv.AROMATHERAPY),
     (49, mv.RAGE_POWDER), (54, mv.X_SCISSOR)),
    PARASECT, 24, True, "")

VENOMOTH = Pokemon(
    49, "Venomoth", 1, False,
    "", ("Bug", "Poison"),
    70, 77, 67, 90,
    ((0, mv.AIR_SLASH), (1, mv.DISABLE), (1, mv.QUIVER_DANCE),
     (1, mv.SUPERSONIC), (1, mv.TACKLE), (11, mv.CONFUSION),
     (13, mv.POISON_POWDER), (17, mv.PSYBEAM), (23, mv.STUN_SPORE),
     (25, mv.BUG_BUZZ), (29, mv.SLEEP_POWDER), (37, mv.LEECH_LIFE),
     (41, mv.ZEN_HEADBUTT), (47, mv.POISON_FANG), (55, mv.PSYCHIC)),
    None, 0, False, "")

VENONAT = Pokemon(
    48, "Venonat", 1, False,
    "", ("Bug", "Poison"),
    60, 47, 52, 45,
    ((1, mv.DISABLE), (1, mv.TACKLE), (5, mv.SUPERSONIC), (11, mv.CONFUSION),
     (13, mv.POISON_POWDER), (17, mv.PSYBEAM), (23, mv.STUN_SPORE),
     (25, mv.BUG_BUZZ), (29, mv.SLEEP_POWDER), (35, mv.LEECH_LIFE),
     (37, mv.ZEN_HEADBUTT), (41, mv.POISON_FANG), (47, mv.PSYCHIC)),
    VENOMOTH, 31, True, "")

DUGTRIO = Pokemon(
    51, "Dugtrio", 1, False,
    "", ("Ground",),
    35, 75, 60, 120,
    ((0, mv.SAND_TOMB), (1, mv.ASTONISH), (1, mv.GROWL), (1, mv.NIGHT_SLASH),
     (1, mv.SAND_ATTACK), (1, mv.SCRATCH), (1, mv.TRI_ATTACK),
     (12, mv.MUD_SLAP), (16, mv.BULLDOZE), (20, mv.SUCKER_PUNCH),
     (24, mv.SLASH), (30, mv.SANDSTORM), (36, mv.DIG), (42, mv.EARTH_POWER),
     (48, mv.EARTHQUAKE), (54, mv.FISSURE)),
    None, 0, False, "")

DIGLETT = Pokemon(
    50, "Diglett", 1, False,
    "", ("Ground",),
    10, 45, 35, 95,
    ((1, mv.SAND_ATTACK), (1, mv.SCRATCH), (4, mv.GROWL), (8, mv.ASTONISH),
     (12, mv.MUD_SLAP), (16, mv.BULLDOZE), (20, mv.SUCKER_PUNCH),
     (24, mv.SLASH), (28, mv.SANDSTORM), (32, mv.DIG), (36, mv.EARTH_POWER),
     (40, mv.EARTHQUAKE), (44, mv.FISSURE)),
    DUGTRIO, 26, True, "")

PERSIAN = Pokemon(
    53, "Persian", 1, False,
    "", ("Normal",),
    65, 67, 62, 115,
    ((0, mv.POWER_GEM), (1, mv.FAKE_OUT), (1, mv.FEINT), (1, mv.GROWL),
     (1, mv.SCRATCH), (1, mv.SWITCHEROO), (12, mv.PAY_DAY), (16, mv.BITE),
     (20, mv.TAUNT), (24, mv.ASSURANCE), (31, mv.FURY_SWIPES),
     (36, mv.SCREECH), (42, mv.SLASH), (48, mv.NASTY_PLOT),
     (54, mv.PLAY_ROUGH)),
    None, 0, False, "")

MEOWTH = Pokemon(
    52, "Meowth", 1, False,
    "", ("Normal",),
    40, 42, 37, 90,
    ((1, mv.FAKE_OUT), (1, mv.GROWL), (4, mv.FEINT), (8, mv.SCRATCH),
     (12, mv.PAY_DAY), (16, mv.BITE), (20, mv.TAUNT), (24, mv.ASSURANCE),
     (29, mv.FURY_SWIPES), (32, mv.SCREECH), (36, mv.SLASH),
     (40, mv.NASTY_PLOT), (44, mv.PLAY_ROUGH)),
    PERSIAN, 28, True, "")

GOLDUCK = Pokemon(
    55, "Golduck", 1, False,
    "", ("Water",),
    80, 88, 79, 85,
    ((1, mv.AQUA_JET), (1, mv.CONFUSION), (1, mv.SCRATCH), (1, mv.TAIL_WHIP),
     (1, mv.WATER_GUN), (9, mv.FURY_SWIPES), (12, mv.WATER_PULSE),
     (15, mv.DISABLE), (18, mv.ZEN_HEADBUTT), (21, mv.SCREECH),
     (24, mv.AQUA_TAIL), (27, mv.SOAK), (30, mv.PSYCH_UP), (36, mv.AMNESIA),
     (40, mv.HYDRO_PUMP), (45, mv.WONDER_ROOM)),
    None, 0, False, "")

PSYDUCK = Pokemon(
    54, "Psyduck", 1, False,
    "", ("Water",),
    50, 58, 49, 55,
    ((1, mv.SCRATCH), (1, mv.TAIL_WHIP), (3, mv.WATER_GUN), (6, mv.CONFUSION),
     (9, mv.FURY_SWIPES), (12, mv.WATER_PULSE), (15, mv.DISABLE),
     (18, mv.ZEN_HEADBUTT), (21, mv.SCREECH), (24, mv.AQUA_TAIL),
     (27, mv.SOAK), (30, mv.PSYCH_UP), (34, mv.AMNESIA), (39, mv.WONDER_ROOM)),
    GOLDUCK, 33, True, "")


# --- generation 9 ---

ANNIHILAPE = Pokemon(
    979, "Annihilape", 9, False,
    "", ("Fighting", "Ghost"),
    110, 82, 85, 90,
    ((0, mv.SHADOW_PUNCH), (1, mv.COUNTER), (1, mv.FLING),
     (1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.SCRATCH), (5, mv.FURY_SWIPES),
     (8, mv.LOW_KICK), (12, mv.SEISMIC_TOSS), (17, mv.SWAGGER),
     (22, mv.CROSS_CHOP), (26, mv.ASSURANCE), (30, mv.THRASH),
     (35, mv.RAGE_FIST), (39, mv.CLOSE_COMBAT), (44, mv.SCREECH),
     (48, mv.STOMPING_TANTRUM), (53, mv.OUTRAGE), (57, mv.FINAL_GAMBIT)),
    None, 0, False, "")


# --- generation 1 ---

PRIMEAPE = Pokemon(
    57, "Primeape", 1, False,
    "", ("Fighting",),
    65, 82, 65, 95,
    ((1, mv.FLING), (1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.SCRATCH),
     (5, mv.FURY_SWIPES), (8, mv.LOW_KICK), (15, mv.SEISMIC_TOSS),
     (17, mv.SWAGGER), (22, mv.CROSS_CHOP), (26, mv.ASSURANCE),
     (30, mv.THRASH), (35, mv.RAGE_FIST), (39, mv.CLOSE_COMBAT),
     (44, mv.SCREECH), (48, mv.STOMPING_TANTRUM), (53, mv.OUTRAGE),
     (57, mv.FINAL_GAMBIT)),
    ANNIHILAPE, 0, True, "use-move")

MANKEY = Pokemon(
    56, "Mankey", 1, False,
    "", ("Fighting",),
    40, 57, 40, 70,
    ((1, mv.COVET), (1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.SCRATCH),
     (5, mv.FURY_SWIPES), (8, mv.LOW_KICK), (12, mv.SEISMIC_TOSS),
     (17, mv.SWAGGER), (22, mv.CROSS_CHOP), (26, mv.ASSURANCE),
     (29, mv.THRASH), (33, mv.CLOSE_COMBAT), (36, mv.SCREECH),
     (40, mv.STOMPING_TANTRUM), (44, mv.OUTRAGE), (48, mv.FINAL_GAMBIT)),
    PRIMEAPE, 28, True, "")

ARCANINE = Pokemon(
    59, "Arcanine", 1, False,
    "", ("Fire",),
    90, 105, 80, 95,
    ((0, mv.EXTREME_SPEED), (1, mv.AGILITY), (1, mv.BITE), (1, mv.CRUNCH),
     (1, mv.EMBER), (1, mv.FIRE_FANG), (1, mv.FLAME_WHEEL),
     (1, mv.FLARE_BLITZ), (1, mv.HELPING_HAND), (1, mv.HOWL), (1, mv.LEER),
     (1, mv.PLAY_ROUGH), (1, mv.RETALIATE), (1, mv.REVERSAL), (1, mv.ROAR),
     (1, mv.TAKE_DOWN), (5, mv.FLAMETHROWER)),
    None, 0, False, "")

GROWLITHE = Pokemon(
    58, "Growlithe", 1, False,
    "", ("Fire",),
    55, 70, 47, 60,
    ((1, mv.EMBER), (1, mv.LEER), (4, mv.HOWL), (8, mv.BITE),
     (12, mv.FLAME_WHEEL), (16, mv.HELPING_HAND), (20, mv.AGILITY),
     (24, mv.FIRE_FANG), (28, mv.RETALIATE), (32, mv.CRUNCH),
     (36, mv.TAKE_DOWN), (40, mv.FLAMETHROWER), (44, mv.ROAR),
     (48, mv.PLAY_ROUGH), (52, mv.REVERSAL), (56, mv.FLARE_BLITZ)),
    ARCANINE, 0, True, "item:fire-stone")


# --- generation 2 ---

POLITOED = Pokemon(
    186, "Politoed", 2, False,
    "", ("Water",),
    90, 82, 87, 70,
    ((0, mv.BOUNCE), (1, mv.BELLY_DRUM), (1, mv.HYDRO_PUMP), (1, mv.POUND),
     (1, mv.RAIN_DANCE)),
    None, 0, False, "")


# --- generation 1 ---

POLIWRATH = Pokemon(
    62, "Poliwrath", 1, False,
    "", ("Water", "Fighting"),
    90, 82, 92, 70,
    ((0, mv.DYNAMIC_PUNCH), (1, mv.BODY_SLAM), (1, mv.BUBBLE_BEAM),
     (1, mv.HYPNOSIS)),
    POLITOED, 0, True, "Trade with  King's Rock")

POLIWHIRL = Pokemon(
    61, "Poliwhirl", 1, False,
    "", ("Water",),
    65, 57, 57, 90,
    ((1, mv.HYPNOSIS), (1, mv.MUD_SHOT), (1, mv.POUND), (1, mv.WATER_GUN),
     (18, mv.BUBBLE_BEAM), (24, mv.RAIN_DANCE), (32, mv.BODY_SLAM),
     (40, mv.EARTH_POWER), (48, mv.HYDRO_PUMP), (56, mv.BELLY_DRUM),
     (66, mv.DOUBLE_EDGE)),
    POLIWRATH, 0, True, "trade")

POLIWAG = Pokemon(
    60, "Poliwag", 1, False,
    "", ("Water",),
    40, 45, 40, 90,
    ((1, mv.HYPNOSIS), (1, mv.WATER_GUN), (6, mv.POUND), (12, mv.MUD_SHOT),
     (18, mv.BUBBLE_BEAM), (24, mv.RAIN_DANCE), (30, mv.BODY_SLAM),
     (36, mv.EARTH_POWER), (42, mv.HYDRO_PUMP), (48, mv.BELLY_DRUM),
     (54, mv.DOUBLE_EDGE)),
    POLIWHIRL, 25, True, "")

ALAKAZAM = Pokemon(
    65, "Alakazam", 1, False,
    "", ("Psychic",),
    55, 92, 70, 120,
    ((1, mv.CONFUSION), (1, mv.DISABLE), (1, mv.KINESIS), (1, mv.TELEPORT),
     (5, mv.PSYBEAM), (10, mv.REFLECT), (15, mv.ALLY_SWITCH),
     (20, mv.PSYCHO_CUT), (25, mv.RECOVER), (30, mv.PSYSHOCK),
     (35, mv.PSYCHIC), (40, mv.ROLE_PLAY), (45, mv.FUTURE_SIGHT),
     (50, mv.CALM_MIND)),
    None, 0, False, "")

KADABRA = Pokemon(
    64, "Kadabra", 1, False,
    "", ("Psychic",),
    40, 77, 50, 105,
    ((1, mv.CONFUSION), (1, mv.DISABLE), (1, mv.KINESIS), (1, mv.TELEPORT),
     (5, mv.PSYBEAM), (10, mv.REFLECT), (15, mv.ALLY_SWITCH),
     (20, mv.PSYCHO_CUT), (25, mv.RECOVER), (30, mv.PSYSHOCK),
     (35, mv.PSYCHIC), (40, mv.ROLE_PLAY), (45, mv.FUTURE_SIGHT),
     (50, mv.CALM_MIND)),
    ALAKAZAM, 0, True, "trade")

ABRA = Pokemon(
    63, "Abra", 1, False,
    "", ("Psychic",),
    25, 62, 35, 90,
    ((1, mv.TELEPORT),),
    KADABRA, 16, True, "")

MACHAMP = Pokemon(
    68, "Machamp", 1, False,
    "", ("Fighting",),
    90, 97, 82, 55,
    ((1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.LOW_KICK), (1, mv.REVENGE),
     (1, mv.WIDE_GUARD), (12, mv.LOW_SWEEP), (16, mv.KNOCK_OFF),
     (20, mv.SCARY_FACE), (24, mv.VITAL_THROW), (31, mv.STRENGTH),
     (36, mv.DUAL_CHOP), (42, mv.BULK_UP), (48, mv.SEISMIC_TOSS),
     (54, mv.DYNAMIC_PUNCH), (60, mv.CROSS_CHOP), (66, mv.DOUBLE_EDGE)),
    None, 0, False, "")

MACHOKE = Pokemon(
    67, "Machoke", 1, False,
    "", ("Fighting",),
    80, 75, 65, 45,
    ((1, mv.FOCUS_ENERGY), (1, mv.LEER), (1, mv.LOW_KICK), (1, mv.REVENGE),
     (12, mv.LOW_SWEEP), (16, mv.KNOCK_OFF), (20, mv.SCARY_FACE),
     (24, mv.VITAL_THROW), (31, mv.STRENGTH), (36, mv.DUAL_CHOP),
     (42, mv.BULK_UP), (48, mv.SEISMIC_TOSS), (54, mv.DYNAMIC_PUNCH),
     (60, mv.CROSS_CHOP), (66, mv.DOUBLE_EDGE)),
    MACHAMP, 0, True, "trade")

MACHOP = Pokemon(
    66, "Machop", 1, False,
    "", ("Fighting",),
    70, 57, 42, 35,
    ((1, mv.LEER), (1, mv.LOW_KICK), (4, mv.FOCUS_ENERGY), (8, mv.REVENGE),
     (12, mv.LOW_SWEEP), (16, mv.KNOCK_OFF), (20, mv.SCARY_FACE),
     (24, mv.VITAL_THROW), (29, mv.STRENGTH), (32, mv.DUAL_CHOP),
     (36, mv.BULK_UP), (40, mv.SEISMIC_TOSS), (44, mv.DYNAMIC_PUNCH),
     (48, mv.CROSS_CHOP), (52, mv.DOUBLE_EDGE)),
    MACHOKE, 28, True, "")

VICTREEBEL = Pokemon(
    71, "Victreebel", 1, False,
    "", ("Grass", "Poison"),
    80, 102, 67, 70,
    ((0, mv.LEAF_STORM), (1, mv.RAZOR_LEAF), (1, mv.SLEEP_POWDER),
     (1, mv.SWEET_SCENT), (1, mv.VINE_WHIP), (44, mv.LEAF_BLADE)),
    None, 0, False, "")

WEEPINBELL = Pokemon(
    70, "Weepinbell", 1, False,
    "", ("Grass", "Poison"),
    65, 87, 47, 55,
    ((1, mv.GROWTH), (1, mv.VINE_WHIP), (1, mv.WRAP), (13, mv.SLEEP_POWDER),
     (15, mv.POISON_POWDER), (17, mv.STUN_SPORE), (24, mv.ACID),
     (29, mv.KNOCK_OFF), (32, mv.SWEET_SCENT), (39, mv.GASTRO_ACID),
     (44, mv.RAZOR_LEAF), (47, mv.POISON_JAB), (54, mv.SLAM),
     (58, mv.POWER_WHIP)),
    VICTREEBEL, 0, True, "item:leaf-stone")

BELLSPROUT = Pokemon(
    69, "Bellsprout", 1, False,
    "", ("Grass", "Poison"),
    50, 72, 32, 40,
    ((1, mv.VINE_WHIP), (7, mv.GROWTH), (11, mv.WRAP), (13, mv.SLEEP_POWDER),
     (15, mv.POISON_POWDER), (17, mv.STUN_SPORE), (23, mv.ACID),
     (27, mv.KNOCK_OFF), (29, mv.SWEET_SCENT), (35, mv.GASTRO_ACID),
     (39, mv.RAZOR_LEAF), (41, mv.POISON_JAB), (47, mv.SLAM),
     (52, mv.POWER_WHIP)),
    WEEPINBELL, 21, True, "")

TENTACRUEL = Pokemon(
    73, "Tentacruel", 1, False,
    "", ("Water", "Poison"),
    80, 75, 92, 100,
    ((1, mv.ACID), (1, mv.POISON_STING), (1, mv.REFLECT_TYPE),
     (1, mv.WATER_GUN), (1, mv.WRAP), (12, mv.SUPERSONIC),
     (16, mv.WATER_PULSE), (20, mv.SCREECH), (24, mv.BUBBLE_BEAM),
     (28, mv.HEX), (34, mv.ACID_ARMOR), (40, mv.POISON_JAB), (46, mv.SURF),
     (52, mv.SLUDGE_WAVE), (58, mv.HYDRO_PUMP)),
    None, 0, False, "")

TENTACOOL = Pokemon(
    72, "Tentacool", 1, False,
    "", ("Water", "Poison"),
    40, 45, 67, 70,
    ((1, mv.POISON_STING), (1, mv.WATER_GUN), (4, mv.ACID), (8, mv.WRAP),
     (12, mv.SUPERSONIC), (16, mv.WATER_PULSE), (20, mv.SCREECH),
     (24, mv.BUBBLE_BEAM), (28, mv.HEX), (32, mv.ACID_ARMOR),
     (36, mv.POISON_JAB), (40, mv.SURF), (44, mv.SLUDGE_WAVE),
     (48, mv.HYDRO_PUMP)),
    TENTACRUEL, 30, True, "")

GOLEM = Pokemon(
    76, "Golem", 1, False,
    "", ("Rock", "Ground"),
    80, 87, 97, 45,
    ((1, mv.DEFENSE_CURL), (1, mv.HEAVY_SLAM), (1, mv.ROCK_POLISH),
     (1, mv.TACKLE), (16, mv.ROCK_THROW), (18, mv.SMACK_DOWN),
     (22, mv.BULLDOZE), (24, mv.SELF_DESTRUCT), (30, mv.STEALTH_ROCK),
     (34, mv.ROCK_BLAST), (40, mv.EARTHQUAKE), (44, mv.EXPLOSION),
     (50, mv.DOUBLE_EDGE), (54, mv.STONE_EDGE)),
    None, 0, False, "")

GRAVELER = Pokemon(
    75, "Graveler", 1, False,
    "", ("Rock", "Ground"),
    55, 70, 80, 35,
    ((1, mv.DEFENSE_CURL), (1, mv.ROCK_POLISH), (1, mv.TACKLE),
     (10, mv.ROLLOUT), (12, mv.BULLDOZE), (16, mv.ROCK_THROW),
     (18, mv.SMACK_DOWN), (24, mv.SELF_DESTRUCT), (30, mv.STEALTH_ROCK),
     (34, mv.ROCK_BLAST), (40, mv.EARTHQUAKE), (44, mv.EXPLOSION),
     (50, mv.DOUBLE_EDGE), (54, mv.STONE_EDGE)),
    GOLEM, 0, True, "trade")

GEODUDE = Pokemon(
    74, "Geodude", 1, False,
    "", ("Rock", "Ground"),
    40, 55, 65, 20,
    ((1, mv.DEFENSE_CURL), (1, mv.TACKLE), (6, mv.ROCK_POLISH),
     (10, mv.ROLLOUT), (12, mv.BULLDOZE), (16, mv.ROCK_THROW),
     (18, mv.SMACK_DOWN), (24, mv.SELF_DESTRUCT), (28, mv.STEALTH_ROCK),
     (30, mv.ROCK_BLAST), (34, mv.EARTHQUAKE), (36, mv.EXPLOSION),
     (40, mv.DOUBLE_EDGE), (42, mv.STONE_EDGE)),
    GRAVELER, 25, True, "")

RAPIDASH = Pokemon(
    78, "Rapidash", 1, False,
    "", ("Fire",),
    65, 90, 75, 105,
    ((1, mv.EMBER), (1, mv.GROWL), (1, mv.MEGAHORN), (1, mv.POISON_JAB),
     (1, mv.QUICK_ATTACK), (1, mv.SMART_STRIKE), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (15, mv.FLAME_CHARGE), (20, mv.AGILITY),
     (25, mv.FLAME_WHEEL), (30, mv.STOMP), (35, mv.FIRE_SPIN),
     (43, mv.TAKE_DOWN), (49, mv.INFERNO), (56, mv.FIRE_BLAST),
     (63, mv.FLARE_BLITZ)),
    None, 0, False, "")

PONYTA = Pokemon(
    77, "Ponyta", 1, False,
    "", ("Fire",),
    50, 75, 60, 90,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.TAIL_WHIP), (10, mv.EMBER),
     (15, mv.FLAME_CHARGE), (20, mv.AGILITY), (25, mv.FLAME_WHEEL),
     (30, mv.STOMP), (35, mv.FIRE_SPIN), (41, mv.TAKE_DOWN), (45, mv.INFERNO),
     (50, mv.FIRE_BLAST), (55, mv.FLARE_BLITZ)),
    RAPIDASH, 40, True, "")


# --- generation 2 ---

SLOWKING = Pokemon(
    199, "Slowking", 2, False,
    "", ("Water", "Psychic"),
    95, 87, 95, 30,
    ((1, mv.CURSE), (1, mv.GROWL), (1, mv.NASTY_PLOT), (1, mv.POWER_GEM),
     (1, mv.SWAGGER), (1, mv.TACKLE), (1, mv.WATER_GUN), (9, mv.YAWN),
     (12, mv.CONFUSION), (15, mv.DISABLE), (18, mv.WATER_PULSE),
     (21, mv.HEADBUTT), (27, mv.AMNESIA), (30, mv.SURF), (33, mv.SLACK_OFF),
     (36, mv.PSYCHIC), (39, mv.PSYCH_UP), (42, mv.RAIN_DANCE),
     (45, mv.HEAL_PULSE)),
    None, 0, False, "Slowpoke")


# --- generation 1 ---

SLOWBRO = Pokemon(
    80, "Slowbro", 1, False,
    "", ("Water", "Psychic"),
    95, 87, 95, 30,
    ((1, mv.CURSE), (1, mv.GROWL), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (1, mv.WITHDRAW), (9, mv.YAWN), (12, mv.CONFUSION), (15, mv.DISABLE),
     (18, mv.WATER_PULSE), (21, mv.HEADBUTT), (24, mv.ZEN_HEADBUTT),
     (27, mv.AMNESIA), (30, mv.SURF), (33, mv.SLACK_OFF), (36, mv.PSYCHIC),
     (41, mv.PSYCH_UP), (46, mv.RAIN_DANCE), (51, mv.HEAL_PULSE)),
    SLOWKING, 0, True, "Trade with  King's Rock")

SLOWPOKE = Pokemon(
    79, "Slowpoke", 1, False,
    "", ("Water", "Psychic"),
    90, 52, 52, 15,
    ((1, mv.CURSE), (1, mv.TACKLE), (3, mv.GROWL), (6, mv.WATER_GUN),
     (9, mv.YAWN), (12, mv.CONFUSION), (15, mv.DISABLE), (18, mv.WATER_PULSE),
     (21, mv.HEADBUTT), (24, mv.ZEN_HEADBUTT), (27, mv.AMNESIA), (30, mv.SURF),
     (33, mv.SLACK_OFF), (36, mv.PSYCHIC), (39, mv.PSYCH_UP),
     (42, mv.RAIN_DANCE), (45, mv.HEAL_PULSE)),
    SLOWBRO, 0, True, "item:galarica-wreath")


# --- generation 4 ---

MAGNEZONE = Pokemon(
    462, "Magnezone", 4, False,
    "", ("Electric", "Steel"),
    70, 100, 102, 60,
    ((1, mv.ELECTRIC_TERRAIN), (1, mv.MAGNETIC_FLUX), (1, mv.MIRROR_COAT),
     (1, mv.SUPERSONIC), (1, mv.TACKLE), (1, mv.THUNDER_SHOCK),
     (1, mv.THUNDER_WAVE), (1, mv.TRI_ATTACK), (12, mv.ELECTRO_BALL),
     (16, mv.GYRO_BALL), (20, mv.SPARK), (24, mv.SCREECH),
     (28, mv.MAGNET_RISE), (34, mv.FLASH_CANNON), (40, mv.DISCHARGE),
     (46, mv.METAL_SOUND), (52, mv.LIGHT_SCREEN), (58, mv.LOCK_ON),
     (64, mv.ZAP_CANNON)),
    None, 0, False, "")


# --- generation 1 ---

MAGNETON = Pokemon(
    82, "Magneton", 1, False,
    "", ("Electric", "Steel"),
    50, 90, 82, 70,
    ((0, mv.TRI_ATTACK), (1, mv.ELECTRIC_TERRAIN), (1, mv.SUPERSONIC),
     (1, mv.TACKLE), (1, mv.THUNDER_SHOCK), (1, mv.THUNDER_WAVE),
     (12, mv.ELECTRO_BALL), (16, mv.GYRO_BALL), (20, mv.SPARK),
     (24, mv.SCREECH), (28, mv.MAGNET_RISE), (34, mv.FLASH_CANNON),
     (40, mv.DISCHARGE), (46, mv.METAL_SOUND), (52, mv.LIGHT_SCREEN),
     (58, mv.LOCK_ON), (64, mv.ZAP_CANNON)),
    MAGNEZONE, 0, True, "level-up")

MAGNEMITE = Pokemon(
    81, "Magnemite", 1, False,
    "", ("Electric", "Steel"),
    25, 65, 62, 45,
    ((1, mv.TACKLE), (1, mv.THUNDER_SHOCK), (4, mv.SUPERSONIC),
     (8, mv.THUNDER_WAVE), (12, mv.ELECTRO_BALL), (16, mv.GYRO_BALL),
     (20, mv.SPARK), (24, mv.SCREECH), (28, mv.MAGNET_RISE),
     (32, mv.FLASH_CANNON), (36, mv.DISCHARGE), (40, mv.METAL_SOUND),
     (44, mv.LIGHT_SCREEN), (48, mv.LOCK_ON), (52, mv.ZAP_CANNON)),
    MAGNETON, 30, True, "")


# --- generation 8 ---

SIRFETCHD = Pokemon(
    865, "Sirfetch'd", 8, False,
    "", ("Fighting",),
    62, 101, 88, 65,
    ((1, mv.FIRST_IMPRESSION), (1, mv.FURY_CUTTER), (1, mv.IRON_DEFENSE),
     (1, mv.LEER), (1, mv.PECK), (1, mv.SAND_ATTACK), (15, mv.ROCK_SMASH),
     (20, mv.BRUTAL_SWING), (25, mv.DETECT), (30, mv.KNOCK_OFF),
     (35, mv.DEFOG), (40, mv.BRICK_BREAK), (45, mv.SWORDS_DANCE),
     (50, mv.SLAM), (55, mv.LEAF_BLADE), (60, mv.FINAL_GAMBIT),
     (65, mv.BRAVE_BIRD), (70, mv.METEOR_ASSAULT)),
    None, 0, False, "")


# --- generation 1 ---

FARFETCHD = Pokemon(
    83, "Farfetch'd", 1, False,
    "", ("Normal", "Flying"),
    52, 74, 58, 60,
    ((1, mv.PECK), (1, mv.SAND_ATTACK), (5, mv.LEER), (10, mv.FURY_CUTTER),
     (15, mv.CUT), (20, mv.AERIAL_ACE), (25, mv.AIR_CUTTER),
     (30, mv.KNOCK_OFF), (35, mv.FALSE_SWIPE), (40, mv.SLASH),
     (45, mv.SWORDS_DANCE), (50, mv.AIR_SLASH), (55, mv.LEAF_BLADE),
     (60, mv.AGILITY), (65, mv.BRAVE_BIRD)),
    SIRFETCHD, 0, True, "three-critical-hits")

DODRIO = Pokemon(
    85, "Dodrio", 1, False,
    "", ("Normal", "Flying"),
    60, 85, 65, 110,
    ((0, mv.TRI_ATTACK), (1, mv.GROWL), (1, mv.PECK), (1, mv.QUICK_ATTACK),
     (12, mv.FURY_ATTACK), (15, mv.PLUCK), (19, mv.DOUBLE_HIT),
     (23, mv.AGILITY), (26, mv.UPROAR), (30, mv.ACUPRESSURE),
     (34, mv.SWORDS_DANCE), (38, mv.DRILL_PECK), (43, mv.ENDEAVOR),
     (50, mv.THRASH)),
    None, 0, False, "")

DODUO = Pokemon(
    84, "Doduo", 1, False,
    "", ("Normal", "Flying"),
    35, 60, 40, 75,
    ((1, mv.GROWL), (1, mv.PECK), (5, mv.QUICK_ATTACK), (9, mv.FURY_ATTACK),
     (14, mv.PLUCK), (19, mv.DOUBLE_HIT), (23, mv.AGILITY), (27, mv.UPROAR),
     (30, mv.ACUPRESSURE), (33, mv.SWORDS_DANCE), (36, mv.DRILL_PECK),
     (39, mv.ENDEAVOR), (43, mv.THRASH)),
    DODRIO, 31, True, "")

DEWGONG = Pokemon(
    87, "Dewgong", 1, False,
    "", ("Water", "Ice"),
    90, 70, 87, 70,
    ((0, mv.SHEER_COLD), (1, mv.GROWL), (1, mv.HEADBUTT), (1, mv.ICY_WIND),
     (13, mv.ENCORE), (17, mv.ICE_SHARD), (21, mv.REST), (23, mv.AQUA_RING),
     (27, mv.AURORA_BEAM), (31, mv.AQUA_JET), (33, mv.BRINE),
     (39, mv.TAKE_DOWN), (45, mv.DIVE), (49, mv.AQUA_TAIL), (55, mv.ICE_BEAM),
     (61, mv.SAFEGUARD), (65, mv.SNOWSCAPE)),
    None, 0, False, "")

SEEL = Pokemon(
    86, "Seel", 1, False,
    "", ("Water",),
    65, 45, 62, 45,
    ((1, mv.HEADBUTT), (3, mv.GROWL), (7, mv.CHARM), (11, mv.ICY_WIND),
     (13, mv.ENCORE), (17, mv.ICE_SHARD), (21, mv.REST), (23, mv.AQUA_RING),
     (27, mv.AURORA_BEAM), (31, mv.AQUA_JET), (33, mv.BRINE),
     (37, mv.TAKE_DOWN), (41, mv.DIVE), (43, mv.AQUA_TAIL), (47, mv.ICE_BEAM),
     (51, mv.SAFEGUARD), (53, mv.SNOWSCAPE)),
    DEWGONG, 34, True, "")

MUK = Pokemon(
    89, "Muk", 1, False,
    "", ("Poison",),
    105, 85, 87, 50,
    ((1, mv.HARDEN), (1, mv.MUD_SLAP), (1, mv.POISON_GAS), (1, mv.POUND),
     (12, mv.DISABLE), (15, mv.SLUDGE), (18, mv.MUD_SHOT), (21, mv.MINIMIZE),
     (26, mv.TOXIC), (29, mv.SLUDGE_BOMB), (32, mv.SLUDGE_WAVE),
     (37, mv.SCREECH), (40, mv.GUNK_SHOT), (46, mv.ACID_ARMOR), (52, mv.BELCH),
     (57, mv.MEMENTO)),
    None, 0, False, "")

GRIMER = Pokemon(
    88, "Grimer", 1, False,
    "", ("Poison",),
    80, 60, 50, 25,
    ((1, mv.POISON_GAS), (1, mv.POUND), (4, mv.HARDEN), (7, mv.MUD_SLAP),
     (12, mv.DISABLE), (15, mv.SLUDGE), (18, mv.MUD_SHOT), (21, mv.MINIMIZE),
     (26, mv.TOXIC), (29, mv.SLUDGE_BOMB), (32, mv.SLUDGE_WAVE),
     (37, mv.SCREECH), (40, mv.GUNK_SHOT), (43, mv.ACID_ARMOR), (46, mv.BELCH),
     (48, mv.MEMENTO)),
    MUK, 38, True, "")

CLOYSTER = Pokemon(
    91, "Cloyster", 1, False,
    "", ("Water", "Ice"),
    50, 90, 112, 70,
    ((0, mv.ICICLE_SPEAR), (1, mv.AURORA_BEAM), (1, mv.HYDRO_PUMP),
     (1, mv.ICE_BEAM), (1, mv.ICE_SHARD), (1, mv.ICICLE_CRASH),
     (1, mv.IRON_DEFENSE), (1, mv.LEER), (1, mv.PROTECT), (1, mv.SHELL_SMASH),
     (1, mv.SPIKES), (1, mv.SUPERSONIC), (1, mv.TACKLE), (1, mv.TOXIC_SPIKES),
     (1, mv.WATER_GUN), (1, mv.WHIRLPOOL), (1, mv.WITHDRAW),
     (5, mv.RAZOR_SHELL)),
    None, 0, False, "")

SHELLDER = Pokemon(
    90, "Shellder", 1, False,
    "", ("Water",),
    30, 55, 62, 40,
    ((1, mv.TACKLE), (1, mv.WATER_GUN), (4, mv.WITHDRAW), (8, mv.ICE_SHARD),
     (12, mv.LEER), (16, mv.WHIRLPOOL), (20, mv.SUPERSONIC),
     (24, mv.AURORA_BEAM), (28, mv.PROTECT), (32, mv.RAZOR_SHELL),
     (36, mv.IRON_DEFENSE), (40, mv.ICE_BEAM), (44, mv.SHELL_SMASH),
     (48, mv.HYDRO_PUMP)),
    CLOYSTER, 0, True, "item:water-stone")

GENGAR = Pokemon(
    94, "Gengar", 1, False,
    "", ("Ghost", "Poison"),
    60, 97, 67, 110,
    ((1, mv.CONFUSE_RAY), (1, mv.HYPNOSIS), (1, mv.LICK), (1, mv.MEAN_LOOK),
     (1, mv.PERISH_SONG), (1, mv.REFLECT_TYPE), (1, mv.SHADOW_PUNCH),
     (12, mv.PAYBACK), (16, mv.SPITE), (20, mv.CURSE), (24, mv.HEX),
     (30, mv.NIGHT_SHADE), (36, mv.SUCKER_PUNCH), (42, mv.DARK_PULSE),
     (48, mv.SHADOW_BALL), (54, mv.DESTINY_BOND), (60, mv.DREAM_EATER)),
    None, 0, False, "")

HAUNTER = Pokemon(
    93, "Haunter", 1, False,
    "", ("Ghost", "Poison"),
    45, 82, 50, 95,
    ((0, mv.SHADOW_PUNCH), (1, mv.CONFUSE_RAY), (1, mv.HYPNOSIS), (1, mv.LICK),
     (1, mv.MEAN_LOOK), (12, mv.PAYBACK), (16, mv.SPITE), (20, mv.CURSE),
     (24, mv.HEX), (30, mv.NIGHT_SHADE), (36, mv.SUCKER_PUNCH),
     (42, mv.DARK_PULSE), (48, mv.SHADOW_BALL), (54, mv.DESTINY_BOND),
     (60, mv.DREAM_EATER)),
    GENGAR, 0, True, "trade")

GASTLY = Pokemon(
    92, "Gastly", 1, False,
    "", ("Ghost", "Poison"),
    30, 67, 32, 80,
    ((1, mv.CONFUSE_RAY), (1, mv.LICK), (4, mv.HYPNOSIS), (8, mv.MEAN_LOOK),
     (12, mv.PAYBACK), (16, mv.SPITE), (20, mv.CURSE), (24, mv.HEX),
     (28, mv.NIGHT_SHADE), (32, mv.SUCKER_PUNCH), (36, mv.DARK_PULSE),
     (40, mv.SHADOW_BALL), (44, mv.DESTINY_BOND), (48, mv.DREAM_EATER)),
    HAUNTER, 25, True, "")


# --- generation 2 ---

STEELIX = Pokemon(
    208, "Steelix", 2, False,
    "", ("Steel", "Ground"),
    75, 70, 132, 30,
    ((1, mv.BIND), (1, mv.CRUNCH), (1, mv.FIRE_FANG), (1, mv.HARDEN),
     (1, mv.ICE_FANG), (1, mv.ROCK_POLISH), (1, mv.ROCK_THROW), (1, mv.TACKLE),
     (1, mv.THUNDER_FANG), (4, mv.SMACK_DOWN), (8, mv.AUTOTOMIZE),
     (12, mv.DRAGON_BREATH), (16, mv.CURSE), (20, mv.ROCK_SLIDE),
     (24, mv.SCREECH), (28, mv.SAND_TOMB), (32, mv.STEALTH_ROCK),
     (36, mv.SLAM), (40, mv.SANDSTORM), (44, mv.DIG), (48, mv.IRON_TAIL),
     (52, mv.STONE_EDGE), (56, mv.DOUBLE_EDGE), (60, mv.MAGNET_RISE)),
    None, 0, False, "")


# --- generation 1 ---

ONIX = Pokemon(
    95, "Onix", 1, False,
    "", ("Rock", "Ground"),
    35, 37, 102, 70,
    ((1, mv.BIND), (1, mv.HARDEN), (1, mv.ROCK_THROW), (1, mv.TACKLE),
     (4, mv.SMACK_DOWN), (8, mv.ROCK_POLISH), (12, mv.DRAGON_BREATH),
     (16, mv.CURSE), (20, mv.ROCK_SLIDE), (24, mv.SCREECH), (28, mv.SAND_TOMB),
     (32, mv.STEALTH_ROCK), (36, mv.SLAM), (40, mv.SANDSTORM), (44, mv.DIG),
     (48, mv.IRON_TAIL), (52, mv.STONE_EDGE), (56, mv.DOUBLE_EDGE)),
    STEELIX, 0, True, "trade")

HYPNO = Pokemon(
    97, "Hypno", 1, False,
    "", ("Psychic",),
    85, 73, 92, 67,
    ((1, mv.CONFUSION), (1, mv.DISABLE), (1, mv.HYPNOSIS), (1, mv.POUND),
     (1, mv.SWITCHEROO), (13, mv.HEADBUTT), (17, mv.POISON_GAS),
     (21, mv.PSYBEAM), (25, mv.PSYCH_UP), (32, mv.ZEN_HEADBUTT),
     (37, mv.SWAGGER), (42, mv.PSYCHIC), (47, mv.NASTY_PLOT),
     (51, mv.PSYSHOCK), (56, mv.FUTURE_SIGHT)),
    None, 0, False, "")

DROWZEE = Pokemon(
    96, "Drowzee", 1, False,
    "", ("Psychic",),
    60, 45, 67, 42,
    ((1, mv.HYPNOSIS), (1, mv.POUND), (5, mv.DISABLE), (9, mv.CONFUSION),
     (13, mv.HEADBUTT), (17, mv.POISON_GAS), (21, mv.PSYBEAM),
     (25, mv.PSYCH_UP), (29, mv.ZEN_HEADBUTT), (33, mv.SWAGGER),
     (37, mv.PSYCHIC), (41, mv.NASTY_PLOT), (45, mv.PSYSHOCK),
     (49, mv.FUTURE_SIGHT)),
    HYPNO, 26, True, "")

KINGLER = Pokemon(
    99, "Kingler", 1, False,
    "", ("Water",),
    55, 90, 82, 75,
    ((1, mv.HAMMER_ARM), (1, mv.HARDEN), (1, mv.LEER), (1, mv.METAL_CLAW),
     (1, mv.WATER_GUN), (1, mv.WIDE_GUARD), (12, mv.MUD_SHOT),
     (16, mv.PROTECT), (20, mv.BUBBLE_BEAM), (24, mv.STOMP), (31, mv.FLAIL),
     (36, mv.RAZOR_SHELL), (42, mv.SLAM), (48, mv.SWORDS_DANCE),
     (54, mv.CRABHAMMER), (60, mv.GUILLOTINE)),
    None, 0, False, "")

KRABBY = Pokemon(
    98, "Krabby", 1, False,
    "", ("Water",),
    30, 65, 57, 50,
    ((1, mv.LEER), (1, mv.WATER_GUN), (4, mv.HARDEN), (8, mv.METAL_CLAW),
     (12, mv.MUD_SHOT), (16, mv.PROTECT), (20, mv.BUBBLE_BEAM), (24, mv.STOMP),
     (29, mv.FLAIL), (32, mv.RAZOR_SHELL), (36, mv.SLAM),
     (40, mv.SWORDS_DANCE), (44, mv.CRABHAMMER), (48, mv.GUILLOTINE)),
    KINGLER, 28, True, "")

ELECTRODE = Pokemon(
    101, "Electrode", 1, False,
    "", ("Electric",),
    60, 65, 75, 150,
    ((1, mv.CHARGE), (1, mv.EERIE_IMPULSE), (1, mv.MAGNETIC_FLUX),
     (1, mv.TACKLE), (1, mv.THUNDER_SHOCK), (9, mv.SPARK), (11, mv.ROLLOUT),
     (13, mv.SCREECH), (16, mv.CHARGE_BEAM), (20, mv.SWIFT),
     (22, mv.ELECTRO_BALL), (26, mv.SELF_DESTRUCT), (29, mv.LIGHT_SCREEN),
     (36, mv.MAGNET_RISE), (41, mv.DISCHARGE), (47, mv.EXPLOSION),
     (54, mv.GYRO_BALL), (58, mv.MIRROR_COAT)),
    None, 0, False, "")

VOLTORB = Pokemon(
    100, "Voltorb", 1, False,
    "", ("Electric",),
    40, 42, 52, 100,
    ((1, mv.CHARGE), (1, mv.TACKLE), (4, mv.THUNDER_SHOCK),
     (6, mv.EERIE_IMPULSE), (9, mv.SPARK), (11, mv.ROLLOUT), (13, mv.SCREECH),
     (16, mv.CHARGE_BEAM), (20, mv.SWIFT), (22, mv.ELECTRO_BALL),
     (26, mv.SELF_DESTRUCT), (29, mv.LIGHT_SCREEN), (34, mv.MAGNET_RISE),
     (37, mv.DISCHARGE), (41, mv.EXPLOSION), (46, mv.GYRO_BALL),
     (50, mv.MIRROR_COAT)),
    ELECTRODE, 30, True, "")

EXEGGUTOR = Pokemon(
    103, "Exeggutor", 1, False,
    "", ("Grass", "Psychic"),
    95, 110, 80, 55,
    ((0, mv.STOMP), (1, mv.ABSORB), (1, mv.BULLET_SEED), (1, mv.CONFUSION),
     (1, mv.EXTRASENSORY), (1, mv.GIGA_DRAIN), (1, mv.HYPNOSIS),
     (1, mv.LEAF_STORM), (1, mv.LEECH_SEED), (1, mv.MEGA_DRAIN),
     (1, mv.PSYSHOCK), (1, mv.REFLECT), (1, mv.SEED_BOMB), (1, mv.SOLAR_BEAM),
     (1, mv.SYNTHESIS), (1, mv.UPROAR), (1, mv.WOOD_HAMMER),
     (1, mv.WORRY_SEED)),
    None, 0, False, "")

EXEGGCUTE = Pokemon(
    102, "Exeggcute", 1, False,
    "", ("Grass", "Psychic"),
    60, 50, 62, 40,
    ((1, mv.ABSORB), (1, mv.HYPNOSIS), (5, mv.REFLECT), (10, mv.LEECH_SEED),
     (15, mv.MEGA_DRAIN), (20, mv.CONFUSION), (25, mv.SYNTHESIS),
     (30, mv.BULLET_SEED), (35, mv.GIGA_DRAIN), (40, mv.EXTRASENSORY),
     (45, mv.UPROAR), (50, mv.WORRY_SEED), (55, mv.SOLAR_BEAM)),
    EXEGGUTOR, 0, True, "item:leaf-stone")

MAROWAK = Pokemon(
    105, "Marowak", 1, False,
    "", ("Ground",),
    60, 65, 95, 45,
    ((1, mv.FALSE_SWIPE), (1, mv.GROWL), (1, mv.MUD_SLAP), (1, mv.TAIL_WHIP),
     (12, mv.HEADBUTT), (16, mv.RETALIATE), (20, mv.FLING),
     (24, mv.STOMPING_TANTRUM), (31, mv.BONE_RUSH), (36, mv.FOCUS_ENERGY),
     (42, mv.ENDEAVOR), (48, mv.BONEMERANG), (54, mv.THRASH),
     (60, mv.DOUBLE_EDGE)),
    None, 0, False, "")

CUBONE = Pokemon(
    104, "Cubone", 1, False,
    "", ("Ground",),
    50, 45, 72, 35,
    ((1, mv.GROWL), (1, mv.MUD_SLAP), (4, mv.TAIL_WHIP), (8, mv.FALSE_SWIPE),
     (12, mv.HEADBUTT), (16, mv.RETALIATE), (20, mv.FLING),
     (24, mv.STOMPING_TANTRUM), (29, mv.BONE_RUSH), (32, mv.FOCUS_ENERGY),
     (36, mv.ENDEAVOR), (40, mv.BONEMERANG), (44, mv.THRASH),
     (48, mv.DOUBLE_EDGE)),
    MAROWAK, 28, True, "")


# --- generation 2 ---

HITMONTOP = Pokemon(
    237, "Hitmontop", 2, False,
    "", ("Fighting",),
    50, 65, 102, 70,
    ((0, mv.TRIPLE_KICK), (1, mv.FAKE_OUT), (1, mv.FEINT),
     (1, mv.FOCUS_ENERGY), (1, mv.HELPING_HAND), (1, mv.TACKLE),
     (4, mv.QUICK_ATTACK), (8, mv.GYRO_BALL), (12, mv.DETECT),
     (16, mv.RAPID_SPIN), (21, mv.QUICK_GUARD), (21, mv.WIDE_GUARD),
     (24, mv.SUCKER_PUNCH), (28, mv.AGILITY), (32, mv.DIG),
     (36, mv.CLOSE_COMBAT), (40, mv.COUNTER), (44, mv.ENDEAVOR)),
    None, 0, False, "")


# --- generation 1 ---

HITMONLEE = Pokemon(
    106, "Hitmonlee", 1, False,
    "", ("Fighting",),
    50, 77, 81, 87,
    ((0, mv.BRICK_BREAK), (1, mv.FAKE_OUT), (1, mv.FOCUS_ENERGY),
     (1, mv.HELPING_HAND), (1, mv.LOW_SWEEP), (1, mv.TACKLE),
     (4, mv.DOUBLE_KICK), (8, mv.LOW_KICK), (12, mv.ENDURE),
     (16, mv.SUCKER_PUNCH), (21, mv.WIDE_GUARD), (24, mv.BLAZE_KICK),
     (28, mv.FEINT), (32, mv.MEGA_KICK), (36, mv.CLOSE_COMBAT),
     (40, mv.REVERSAL), (44, mv.HIGH_JUMP_KICK), (50, mv.AXE_KICK)),
    HITMONTOP, 0, True, "Attack = Defence at Level 20")

HITMONCHAN = Pokemon(
    107, "Hitmonchan", 1, False,
    "", ("Fighting",),
    50, 70, 94, 76,
    ((0, mv.DRAIN_PUNCH), (1, mv.FAKE_OUT), (1, mv.FEINT),
     (1, mv.FOCUS_ENERGY), (1, mv.HELPING_HAND), (1, mv.TACKLE),
     (4, mv.MACH_PUNCH), (8, mv.VACUUM_WAVE), (12, mv.DETECT),
     (16, mv.BULLET_PUNCH), (21, mv.QUICK_GUARD), (24, mv.FIRE_PUNCH),
     (24, mv.ICE_PUNCH), (24, mv.THUNDER_PUNCH), (28, mv.AGILITY),
     (32, mv.MEGA_PUNCH), (36, mv.CLOSE_COMBAT), (40, mv.COUNTER),
     (44, mv.FOCUS_PUNCH)),
    HITMONLEE, 0, True, "Attack > Defence at Level 20")


# --- generation 4 ---

LICKILICKY = Pokemon(
    463, "Lickilicky", 4, False,
    "", ("Normal",),
    110, 82, 95, 50,
    ((1, mv.DEFENSE_CURL), (1, mv.LICK), (1, mv.ROLLOUT), (1, mv.SUPERSONIC),
     (18, mv.WRAP), (24, mv.DISABLE), (30, mv.STOMP), (36, mv.KNOCK_OFF),
     (42, mv.SCREECH), (48, mv.SLAM), (54, mv.POWER_WHIP),
     (60, mv.BELLY_DRUM)),
    None, 0, False, "")


# --- generation 1 ---

LICKITUNG = Pokemon(
    108, "Lickitung", 1, False,
    "", ("Normal",),
    90, 57, 75, 30,
    ((1, mv.DEFENSE_CURL), (1, mv.LICK), (6, mv.ROLLOUT), (12, mv.SUPERSONIC),
     (18, mv.WRAP), (24, mv.DISABLE), (30, mv.STOMP), (36, mv.KNOCK_OFF),
     (42, mv.SCREECH), (48, mv.SLAM), (54, mv.POWER_WHIP),
     (60, mv.BELLY_DRUM)),
    LICKILICKY, 0, True, "level-up")

WEEZING = Pokemon(
    110, "Weezing", 1, False,
    "", ("Poison",),
    65, 87, 95, 60,
    ((0, mv.DOUBLE_HIT), (1, mv.HEAT_WAVE), (1, mv.POISON_GAS), (1, mv.SMOG),
     (1, mv.SMOKESCREEN), (1, mv.TACKLE), (12, mv.CLEAR_SMOG),
     (16, mv.ASSURANCE), (20, mv.SLUDGE), (24, mv.HAZE),
     (28, mv.SELF_DESTRUCT), (32, mv.SLUDGE_BOMB), (38, mv.TOXIC),
     (44, mv.BELCH), (50, mv.EXPLOSION), (56, mv.MEMENTO),
     (62, mv.DESTINY_BOND)),
    None, 0, False, "")

KOFFING = Pokemon(
    109, "Koffing", 1, False,
    "", ("Poison",),
    40, 62, 70, 35,
    ((1, mv.POISON_GAS), (1, mv.TACKLE), (4, mv.SMOG), (8, mv.SMOKESCREEN),
     (12, mv.CLEAR_SMOG), (16, mv.ASSURANCE), (20, mv.SLUDGE), (24, mv.HAZE),
     (28, mv.SELF_DESTRUCT), (32, mv.SLUDGE_BOMB), (36, mv.TOXIC),
     (40, mv.BELCH), (44, mv.EXPLOSION), (48, mv.MEMENTO),
     (52, mv.DESTINY_BOND)),
    WEEZING, 35, True, "")


# --- generation 4 ---

RHYPERIOR = Pokemon(
    464, "Rhyperior", 4, False,
    "", ("Ground", "Rock"),
    115, 97, 92, 40,
    ((1, mv.BULLDOZE), (1, mv.HAMMER_ARM), (1, mv.SMACK_DOWN), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (15, mv.HORN_ATTACK), (20, mv.SCARY_FACE),
     (25, mv.STOMP), (30, mv.ROCK_BLAST), (35, mv.DRILL_RUN),
     (40, mv.TAKE_DOWN), (47, mv.EARTHQUAKE), (54, mv.STONE_EDGE),
     (61, mv.MEGAHORN), (68, mv.HORN_DRILL), (75, mv.ROCK_WRECKER)),
    None, 0, False, "")


# --- generation 1 ---

RHYDON = Pokemon(
    112, "Rhydon", 1, False,
    "", ("Ground", "Rock"),
    105, 87, 82, 40,
    ((0, mv.HAMMER_ARM), (1, mv.BULLDOZE), (1, mv.SMACK_DOWN), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (15, mv.HORN_ATTACK), (20, mv.SCARY_FACE),
     (25, mv.STOMP), (30, mv.ROCK_BLAST), (35, mv.DRILL_RUN),
     (40, mv.TAKE_DOWN), (47, mv.EARTHQUAKE), (54, mv.STONE_EDGE),
     (61, mv.MEGAHORN), (68, mv.HORN_DRILL)),
    RHYPERIOR, 0, True, "trade")

RHYHORN = Pokemon(
    111, "Rhyhorn", 1, False,
    "", ("Ground", "Rock"),
    80, 57, 62, 25,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.SMACK_DOWN), (10, mv.BULLDOZE),
     (15, mv.HORN_ATTACK), (20, mv.SCARY_FACE), (25, mv.STOMP),
     (30, mv.ROCK_BLAST), (35, mv.DRILL_RUN), (40, mv.TAKE_DOWN),
     (45, mv.EARTHQUAKE), (50, mv.STONE_EDGE), (55, mv.MEGAHORN),
     (60, mv.HORN_DRILL)),
    RHYDON, 42, True, "")


# --- generation 2 ---

BLISSEY = Pokemon(
    242, "Blissey", 2, False,
    "", ("Normal",),
    255, 42, 72, 55,
    ((1, mv.CHARM), (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DEFENSE_CURL),
     (1, mv.DISARMING_VOICE), (1, mv.POUND), (1, mv.SWEET_KISS),
     (4, mv.TAIL_WHIP), (8, mv.ECHOED_VOICE), (12, mv.LIFE_DEW), (16, mv.SING),
     (20, mv.FLING), (24, mv.TAKE_DOWN), (28, mv.HEAL_PULSE),
     (32, mv.HELPING_HAND), (36, mv.LIGHT_SCREEN), (40, mv.DOUBLE_EDGE),
     (44, mv.SOFT_BOILED), (48, mv.LAST_RESORT), (52, mv.HEALING_WISH)),
    None, 0, False, "")


# --- generation 1 ---

CHANSEY = Pokemon(
    113, "Chansey", 1, False,
    "", ("Normal",),
    250, 20, 55, 50,
    ((1, mv.CHARM), (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DEFENSE_CURL),
     (1, mv.DISARMING_VOICE), (1, mv.POUND), (1, mv.SWEET_KISS),
     (4, mv.TAIL_WHIP), (8, mv.ECHOED_VOICE), (12, mv.LIFE_DEW), (16, mv.SING),
     (20, mv.FLING), (24, mv.TAKE_DOWN), (28, mv.HEAL_PULSE),
     (32, mv.HELPING_HAND), (36, mv.LIGHT_SCREEN), (40, mv.DOUBLE_EDGE),
     (44, mv.SOFT_BOILED), (48, mv.LAST_RESORT), (52, mv.HEALING_WISH)),
    BLISSEY, 0, True, "happiness")


# --- generation 4 ---

TANGROWTH = Pokemon(
    465, "Tangrowth", 4, False,
    "", ("Grass",),
    100, 105, 87, 50,
    ((1, mv.ABSORB), (1, mv.BIND), (1, mv.BLOCK), (1, mv.GROWTH),
     (1, mv.STUN_SPORE), (12, mv.MEGA_DRAIN), (16, mv.VINE_WHIP),
     (20, mv.POISON_POWDER), (24, mv.ANCIENT_POWER), (28, mv.KNOCK_OFF),
     (32, mv.GIGA_DRAIN), (36, mv.SLEEP_POWDER), (40, mv.SLAM),
     (44, mv.TICKLE), (48, mv.POWER_WHIP), (52, mv.INGRAIN),
     (56, mv.GRASSY_TERRAIN)),
    None, 0, False, "")


# --- generation 1 ---

TANGELA = Pokemon(
    114, "Tangela", 1, False,
    "", ("Grass",),
    65, 77, 77, 60,
    ((1, mv.ABSORB), (1, mv.BIND), (4, mv.STUN_SPORE), (8, mv.GROWTH),
     (12, mv.MEGA_DRAIN), (16, mv.VINE_WHIP), (20, mv.POISON_POWDER),
     (24, mv.ANCIENT_POWER), (28, mv.KNOCK_OFF), (32, mv.GIGA_DRAIN),
     (36, mv.SLEEP_POWDER), (40, mv.SLAM), (44, mv.TICKLE),
     (48, mv.POWER_WHIP), (52, mv.INGRAIN), (56, mv.GRASSY_TERRAIN)),
    TANGROWTH, 0, True, "level-up")

KANGASKHAN = Pokemon(
    115, "Kangaskhan", 1, False,
    "", ("Normal",),
    105, 67, 80, 90,
    ((1, mv.POUND), (1, mv.TAIL_WHIP), (4, mv.GROWL), (8, mv.FAKE_OUT),
     (12, mv.BITE), (16, mv.STOMP), (20, mv.FOCUS_ENERGY), (24, mv.HEADBUTT),
     (28, mv.SUCKER_PUNCH), (32, mv.DOUBLE_HIT), (36, mv.CRUNCH),
     (40, mv.ENDURE), (44, mv.REVERSAL), (48, mv.OUTRAGE),
     (52, mv.LAST_RESORT)),
    None, 0, False, "")


# --- generation 2 ---

KINGDRA = Pokemon(
    230, "Kingdra", 2, False,
    "", ("Water", "Dragon"),
    75, 95, 95, 85,
    ((1, mv.LEER), (1, mv.SMOKESCREEN), (1, mv.TWISTER), (1, mv.WATER_GUN),
     (1, mv.WHIRLPOOL), (1, mv.YAWN), (15, mv.FOCUS_ENERGY),
     (20, mv.DRAGON_BREATH), (25, mv.BUBBLE_BEAM), (30, mv.AGILITY),
     (37, mv.WATER_PULSE), (44, mv.DRAGON_PULSE), (51, mv.HYDRO_PUMP),
     (58, mv.DRAGON_DANCE), (65, mv.RAIN_DANCE), (72, mv.WAVE_CRASH)),
    None, 0, False, "")


# --- generation 1 ---

SEADRA = Pokemon(
    117, "Seadra", 1, False,
    "", ("Water",),
    55, 80, 70, 85,
    ((1, mv.LEER), (1, mv.SMOKESCREEN), (1, mv.TWISTER), (1, mv.WATER_GUN),
     (15, mv.FOCUS_ENERGY), (20, mv.DRAGON_BREATH), (25, mv.BUBBLE_BEAM),
     (30, mv.AGILITY), (37, mv.WATER_PULSE), (44, mv.DRAGON_PULSE),
     (51, mv.HYDRO_PUMP), (58, mv.DRAGON_DANCE), (65, mv.RAIN_DANCE)),
    KINGDRA, 0, True, "trade")

HORSEA = Pokemon(
    116, "Horsea", 1, False,
    "", ("Water",),
    30, 55, 47, 60,
    ((1, mv.LEER), (1, mv.WATER_GUN), (5, mv.SMOKESCREEN), (10, mv.TWISTER),
     (15, mv.FOCUS_ENERGY), (20, mv.DRAGON_BREATH), (25, mv.BUBBLE_BEAM),
     (30, mv.AGILITY), (35, mv.WATER_PULSE), (40, mv.DRAGON_PULSE),
     (45, mv.HYDRO_PUMP), (50, mv.DRAGON_DANCE), (55, mv.RAIN_DANCE)),
    SEADRA, 32, True, "")

SEAKING = Pokemon(
    119, "Seaking", 1, False,
    "", ("Water",),
    80, 78, 72, 68,
    ((1, mv.PECK), (1, mv.SUPERSONIC), (1, mv.TAIL_WHIP), (1, mv.WATER_PULSE),
     (15, mv.HORN_ATTACK), (20, mv.AGILITY), (25, mv.AQUA_RING),
     (30, mv.FLAIL), (37, mv.WATERFALL), (44, mv.SOAK), (51, mv.MEGAHORN),
     (58, mv.HORN_DRILL)),
    None, 0, False, "")

GOLDEEN = Pokemon(
    118, "Goldeen", 1, False,
    "", ("Water",),
    45, 51, 55, 63,
    ((1, mv.PECK), (1, mv.TAIL_WHIP), (5, mv.SUPERSONIC), (10, mv.WATER_PULSE),
     (15, mv.HORN_ATTACK), (20, mv.AGILITY), (25, mv.AQUA_RING),
     (30, mv.FLAIL), (35, mv.WATERFALL), (40, mv.SOAK), (45, mv.MEGAHORN),
     (50, mv.HORN_DRILL)),
    SEAKING, 33, True, "")

STARMIE = Pokemon(
    121, "Starmie", 1, False,
    "", ("Water", "Psychic"),
    60, 87, 85, 115,
    ((1, mv.BRINE), (1, mv.CONFUSE_RAY), (1, mv.COSMIC_POWER), (1, mv.HARDEN),
     (1, mv.HYDRO_PUMP), (1, mv.LIGHT_SCREEN), (1, mv.MINIMIZE),
     (1, mv.POWER_GEM), (1, mv.PSYBEAM), (1, mv.PSYCHIC), (1, mv.RAPID_SPIN),
     (1, mv.RECOVER), (1, mv.SURF), (1, mv.SWIFT), (1, mv.TACKLE),
     (1, mv.WATER_GUN)),
    None, 0, False, "")

STARYU = Pokemon(
    120, "Staryu", 1, False,
    "", ("Water",),
    30, 57, 55, 85,
    ((1, mv.HARDEN), (1, mv.TACKLE), (4, mv.WATER_GUN), (8, mv.CONFUSE_RAY),
     (12, mv.RAPID_SPIN), (16, mv.MINIMIZE), (20, mv.SWIFT), (24, mv.PSYBEAM),
     (28, mv.BRINE), (32, mv.LIGHT_SCREEN), (36, mv.POWER_GEM),
     (40, mv.PSYCHIC), (44, mv.SURF), (48, mv.RECOVER), (52, mv.COSMIC_POWER),
     (56, mv.HYDRO_PUMP)),
    STARMIE, 0, True, "item:water-stone")


# --- generation 8 ---

MR_RIME = Pokemon(
    866, "Mr. Rime", 8, False,
    "", ("Ice", "Psychic"),
    80, 97, 87, 70,
    ((1, mv.AFTER_YOU), (1, mv.BATON_PASS), (1, mv.BLOCK), (1, mv.COPYCAT),
     (1, mv.DAZZLING_GLEAM), (1, mv.ENCORE), (1, mv.FAKE_TEARS),
     (1, mv.ICE_SHARD), (1, mv.LIGHT_SCREEN), (1, mv.MIMIC),
     (1, mv.MISTY_TERRAIN), (1, mv.POUND), (1, mv.PROTECT), (1, mv.RAPID_SPIN),
     (1, mv.RECYCLE), (1, mv.REFLECT), (1, mv.ROLE_PLAY), (1, mv.SAFEGUARD),
     (1, mv.SLACK_OFF), (12, mv.CONFUSION), (16, mv.ALLY_SWITCH),
     (20, mv.ICY_WIND), (24, mv.DOUBLE_KICK), (28, mv.PSYBEAM),
     (32, mv.HYPNOSIS), (36, mv.MIRROR_COAT), (40, mv.SUCKER_PUNCH),
     (44, mv.FREEZE_DRY), (48, mv.PSYCHIC), (52, mv.TEETER_DANCE)),
    None, 0, False, "")


# --- generation 1 ---

MR_MIME = Pokemon(
    122, "Mr. Mime", 1, False,
    "", ("Psychic", "Fairy"),
    40, 72, 92, 90,
    ((1, mv.BATON_PASS), (1, mv.COPYCAT), (1, mv.ENCORE), (1, mv.GUARD_SWAP),
     (1, mv.POUND), (1, mv.POWER_SWAP), (1, mv.QUICK_GUARD),
     (1, mv.WIDE_GUARD), (12, mv.CONFUSION), (16, mv.ROLE_PLAY),
     (20, mv.PROTECT), (24, mv.RECYCLE), (28, mv.PSYBEAM), (32, mv.MIMIC),
     (36, mv.LIGHT_SCREEN), (36, mv.REFLECT), (36, mv.SAFEGUARD),
     (40, mv.SUCKER_PUNCH), (44, mv.DAZZLING_GLEAM), (48, mv.PSYCHIC),
     (52, mv.TEETER_DANCE)),
    MR_RIME, 42, True, "")


# --- generation 8 ---

KLEAVOR = Pokemon(
    900, "Kleavor", 8, False,
    "", ("Bug", "Rock"),
    70, 90, 82, 85,
    ((0, mv.STONE_AXE), (1, mv.LEER), (1, mv.QUICK_ATTACK),
     (4, mv.FURY_CUTTER), (8, mv.FALSE_SWIPE), (12, mv.SMACK_DOWN),
     (16, mv.DOUBLE_TEAM), (20, mv.DOUBLE_HIT), (24, mv.SLASH),
     (28, mv.FOCUS_ENERGY), (32, mv.AGILITY), (36, mv.ROCK_SLIDE),
     (40, mv.X_SCISSOR), (44, mv.SWORDS_DANCE)),
    None, 0, False, "")


# --- generation 2 ---

SCIZOR = Pokemon(
    212, "Scizor", 2, False,
    "", ("Bug", "Steel"),
    70, 92, 90, 65,
    ((0, mv.BULLET_PUNCH), (1, mv.AGILITY), (1, mv.AIR_SLASH),
     (1, mv.FALSE_SWIPE), (1, mv.FURY_CUTTER), (1, mv.LEER),
     (1, mv.QUICK_ATTACK), (1, mv.WING_ATTACK), (12, mv.METAL_CLAW),
     (16, mv.DOUBLE_TEAM), (20, mv.DOUBLE_HIT), (24, mv.SLASH),
     (28, mv.FOCUS_ENERGY), (32, mv.IRON_DEFENSE), (36, mv.IRON_HEAD),
     (40, mv.X_SCISSOR), (44, mv.SWORDS_DANCE)),
    KLEAVOR, 0, True, "Use Black Augurite")


# --- generation 1 ---

SCYTHER = Pokemon(
    123, "Scyther", 1, False,
    "", ("Bug", "Flying"),
    70, 82, 80, 105,
    ((1, mv.LEER), (1, mv.QUICK_ATTACK), (4, mv.FURY_CUTTER),
     (8, mv.FALSE_SWIPE), (12, mv.WING_ATTACK), (16, mv.DOUBLE_TEAM),
     (20, mv.DOUBLE_HIT), (24, mv.SLASH), (28, mv.FOCUS_ENERGY),
     (32, mv.AGILITY), (36, mv.AIR_SLASH), (40, mv.X_SCISSOR),
     (44, mv.SWORDS_DANCE)),
    SCIZOR, 0, True, "item:black-augurite")

JYNX = Pokemon(
    124, "Jynx", 1, False,
    "", ("Ice", "Psychic"),
    65, 82, 65, 95,
    ((1, mv.COPYCAT), (1, mv.LICK), (1, mv.POUND), (1, mv.POWDER_SNOW),
     (1, mv.SWEET_KISS), (12, mv.CONFUSION), (16, mv.COVET), (20, mv.SING),
     (24, mv.FAKE_TEARS), (28, mv.ICE_PUNCH), (34, mv.PSYCHIC),
     (40, mv.LOVELY_KISS), (46, mv.MEAN_LOOK), (52, mv.PERISH_SONG),
     (58, mv.BLIZZARD)),
    None, 0, False, "")


# --- generation 4 ---

ELECTIVIRE = Pokemon(
    466, "Electivire", 4, False,
    "", ("Electric",),
    75, 109, 76, 95,
    ((1, mv.CHARGE), (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.THUNDER_SHOCK),
     (12, mv.SWIFT), (16, mv.SHOCK_WAVE), (20, mv.THUNDER_WAVE),
     (24, mv.SCREECH), (28, mv.THUNDER_PUNCH), (34, mv.DISCHARGE),
     (40, mv.LOW_KICK), (46, mv.THUNDERBOLT), (52, mv.LIGHT_SCREEN),
     (58, mv.THUNDER), (64, mv.GIGA_IMPACT)),
    None, 0, False, "")


# --- generation 1 ---

ELECTABUZZ = Pokemon(
    125, "Electabuzz", 1, False,
    "", ("Electric",),
    65, 89, 71, 105,
    ((1, mv.CHARGE), (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.THUNDER_SHOCK),
     (12, mv.SWIFT), (16, mv.SHOCK_WAVE), (20, mv.THUNDER_WAVE),
     (24, mv.SCREECH), (28, mv.THUNDER_PUNCH), (34, mv.DISCHARGE),
     (40, mv.LOW_KICK), (46, mv.THUNDERBOLT), (52, mv.LIGHT_SCREEN),
     (58, mv.THUNDER), (64, mv.GIGA_IMPACT)),
    ELECTIVIRE, 0, True, "trade")


# --- generation 4 ---

MAGMORTAR = Pokemon(
    467, "Magmortar", 4, False,
    "", ("Fire",),
    75, 110, 81, 83,
    ((1, mv.EMBER), (1, mv.LEER), (1, mv.SMOG), (1, mv.SMOKESCREEN),
     (12, mv.CLEAR_SMOG), (16, mv.FLAME_WHEEL), (20, mv.CONFUSE_RAY),
     (24, mv.SCARY_FACE), (28, mv.FIRE_PUNCH), (34, mv.LAVA_PLUME),
     (40, mv.LOW_KICK), (46, mv.FLAMETHROWER), (52, mv.SUNNY_DAY),
     (58, mv.FIRE_BLAST), (64, mv.HYPER_BEAM)),
    None, 0, False, "")


# --- generation 1 ---

MAGMAR = Pokemon(
    126, "Magmar", 1, False,
    "", ("Fire",),
    65, 97, 71, 93,
    ((1, mv.EMBER), (1, mv.LEER), (1, mv.SMOG), (1, mv.SMOKESCREEN),
     (12, mv.CLEAR_SMOG), (16, mv.FLAME_WHEEL), (20, mv.CONFUSE_RAY),
     (24, mv.SCARY_FACE), (28, mv.FIRE_PUNCH), (34, mv.LAVA_PLUME),
     (40, mv.LOW_KICK), (46, mv.FLAMETHROWER), (52, mv.SUNNY_DAY),
     (58, mv.FIRE_BLAST), (64, mv.HYPER_BEAM)),
    MAGMORTAR, 0, True, "trade")

PINSIR = Pokemon(
    127, "Pinsir", 1, False,
    "", ("Bug",),
    65, 90, 85, 85,
    ((1, mv.HARDEN), (1, mv.VISE_GRIP), (4, mv.FOCUS_ENERGY), (8, mv.BIND),
     (12, mv.SEISMIC_TOSS), (16, mv.BUG_BITE), (20, mv.STORM_THROW),
     (24, mv.DOUBLE_HIT), (28, mv.VITAL_THROW), (32, mv.X_SCISSOR),
     (36, mv.STRENGTH), (40, mv.SWORDS_DANCE), (44, mv.SUBMISSION),
     (48, mv.GUILLOTINE), (52, mv.SUPERPOWER)),
    None, 0, False, "")

TAUROS = Pokemon(
    128, "Tauros", 1, False,
    "", ("Normal",),
    75, 70, 82, 110,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.WORK_UP), (10, mv.PAYBACK),
     (15, mv.ASSURANCE), (20, mv.HORN_ATTACK), (25, mv.SCARY_FACE),
     (30, mv.ZEN_HEADBUTT), (35, mv.RAGING_BULL), (40, mv.REST),
     (45, mv.SWAGGER), (50, mv.THRASH), (55, mv.DOUBLE_EDGE),
     (60, mv.GIGA_IMPACT)),
    None, 0, False, "")

GYARADOS = Pokemon(
    130, "Gyarados", 1, False,
    "", ("Water", "Flying"),
    95, 92, 89, 81,
    ((0, mv.BITE), (1, mv.FLAIL), (1, mv.LEER), (1, mv.SPLASH), (1, mv.TACKLE),
     (1, mv.TWISTER), (4, mv.WHIRLPOOL), (8, mv.ICE_FANG), (12, mv.BRINE),
     (16, mv.SCARY_FACE), (21, mv.WATERFALL), (24, mv.CRUNCH),
     (28, mv.RAIN_DANCE), (32, mv.AQUA_TAIL), (36, mv.DRAGON_DANCE),
     (40, mv.HYDRO_PUMP), (44, mv.HURRICANE), (48, mv.THRASH),
     (52, mv.HYPER_BEAM)),
    None, 0, False, "")

MAGIKARP = Pokemon(
    129, "Magikarp", 1, False,
    "", ("Water",),
    20, 12, 37, 80,
    ((1, mv.SPLASH), (15, mv.TACKLE), (25, mv.FLAIL)),
    GYARADOS, 20, True, "")

LAPRAS = Pokemon(
    131, "Lapras", 1, False,
    "", ("Water", "Ice"),
    130, 85, 87, 60,
    ((1, mv.GROWL), (1, mv.WATER_GUN), (5, mv.SING), (10, mv.MIST),
     (15, mv.LIFE_DEW), (20, mv.ICE_SHARD), (25, mv.CONFUSE_RAY),
     (30, mv.WATER_PULSE), (35, mv.BRINE), (40, mv.BODY_SLAM),
     (45, mv.ICE_BEAM), (50, mv.RAIN_DANCE), (55, mv.HYDRO_PUMP),
     (60, mv.PERISH_SONG), (65, mv.SHEER_COLD)),
    None, 0, False, "")

DITTO = Pokemon(
    132, "Ditto", 1, False,
    "", ("Normal",),
    48, 48, 48, 48,
    ((1, mv.TRANSFORM),),
    None, 0, False, "")

EEVEE = Pokemon(
    133, "Eevee", 1, False,
    "", ("Normal",),
    55, 50, 57, 55,
    ((1, mv.COVET), (1, mv.GROWL), (1, mv.HELPING_HAND), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.SWIFT), (25, mv.BITE), (30, mv.COPYCAT),
     (35, mv.BATON_PASS), (40, mv.TAKE_DOWN), (45, mv.CHARM),
     (50, mv.DOUBLE_EDGE), (55, mv.LAST_RESORT)),
    None, 0, False, "level-up")

VAPOREON = Pokemon(
    134, "Vaporeon", 1, False,
    "", ("Water",),
    130, 87, 77, 65,
    ((0, mv.WATER_GUN), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.HAZE), (25, mv.WATER_PULSE),
     (30, mv.AURORA_BEAM), (35, mv.AQUA_RING), (40, mv.MUDDY_WATER),
     (45, mv.ACID_ARMOR), (50, mv.HYDRO_PUMP), (55, mv.LAST_RESORT)),
    None, 0, False, "")

JOLTEON = Pokemon(
    135, "Jolteon", 1, False,
    "", ("Electric",),
    65, 87, 77, 130,
    ((0, mv.THUNDER_SHOCK), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.THUNDER_WAVE), (25, mv.DOUBLE_KICK),
     (30, mv.THUNDER_FANG), (35, mv.PIN_MISSILE), (40, mv.DISCHARGE),
     (45, mv.AGILITY), (50, mv.THUNDER), (55, mv.LAST_RESORT)),
    None, 0, False, "")

FLAREON = Pokemon(
    136, "Flareon", 1, False,
    "", ("Fire",),
    65, 112, 85, 65,
    ((0, mv.EMBER), (1, mv.BATON_PASS), (1, mv.CHARM), (1, mv.COPYCAT),
     (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL), (1, mv.HELPING_HAND),
     (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.TAKE_DOWN),
     (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK), (15, mv.BABY_DOLL_EYES),
     (20, mv.SMOG), (25, mv.BITE), (30, mv.FIRE_FANG), (35, mv.FIRE_SPIN),
     (40, mv.LAVA_PLUME), (45, mv.SCARY_FACE), (50, mv.FLARE_BLITZ),
     (55, mv.LAST_RESORT)),
    None, 0, False, "")


# --- generation 4 ---

PORYGON_Z = Pokemon(
    474, "Porygon-Z", 4, False,
    "", ("Normal",),
    85, 107, 72, 90,
    ((1, mv.CONVERSION), (1, mv.DEFENSE_CURL), (1, mv.MAGNET_RISE),
     (1, mv.NASTY_PLOT), (1, mv.RECYCLE), (1, mv.TACKLE), (1, mv.TRICK_ROOM),
     (15, mv.THUNDER_SHOCK), (20, mv.PSYBEAM), (25, mv.CONVERSION_2),
     (30, mv.AGILITY), (35, mv.RECOVER), (40, mv.DISCHARGE),
     (45, mv.TRI_ATTACK), (50, mv.DOUBLE_EDGE), (55, mv.LOCK_ON),
     (60, mv.ZAP_CANNON), (65, mv.HYPER_BEAM)),
    None, 0, False, "")


# --- generation 2 ---

PORYGON2 = Pokemon(
    233, "Porygon2", 2, False,
    "", ("Normal",),
    85, 92, 92, 60,
    ((1, mv.CONVERSION), (1, mv.DEFENSE_CURL), (1, mv.MAGNET_RISE),
     (1, mv.RECYCLE), (1, mv.TACKLE), (15, mv.THUNDER_SHOCK), (20, mv.PSYBEAM),
     (25, mv.CONVERSION_2), (30, mv.AGILITY), (35, mv.RECOVER),
     (40, mv.DISCHARGE), (45, mv.TRI_ATTACK), (50, mv.LOCK_ON),
     (55, mv.ZAP_CANNON), (60, mv.HYPER_BEAM)),
    PORYGON_Z, 0, True, "trade")


# --- generation 1 ---

PORYGON = Pokemon(
    137, "Porygon", 1, False,
    "", ("Normal",),
    65, 72, 72, 40,
    ((1, mv.CONVERSION), (1, mv.TACKLE), (5, mv.RECYCLE), (10, mv.MAGNET_RISE),
     (15, mv.THUNDER_SHOCK), (20, mv.PSYBEAM), (25, mv.CONVERSION_2),
     (30, mv.AGILITY), (35, mv.RECOVER), (40, mv.DISCHARGE),
     (45, mv.TRI_ATTACK), (50, mv.DOUBLE_EDGE), (55, mv.LOCK_ON),
     (60, mv.ZAP_CANNON)),
    PORYGON2, 0, True, "trade")

OMASTAR = Pokemon(
    139, "Omastar", 1, False,
    "", ("Rock", "Water"),
    70, 87, 97, 55,
    ((1, mv.BIND), (1, mv.CRUNCH), (1, mv.ROLLOUT), (1, mv.SAND_ATTACK),
     (1, mv.WITHDRAW), (15, mv.WATER_GUN), (20, mv.LEER), (25, mv.MUD_SHOT),
     (30, mv.ANCIENT_POWER), (35, mv.BRINE), (43, mv.PROTECT),
     (49, mv.ROCK_BLAST), (56, mv.SURF), (63, mv.SHELL_SMASH),
     (70, mv.HYDRO_PUMP)),
    None, 0, False, "")

OMANYTE = Pokemon(
    138, "Omanyte", 1, False,
    "", ("Rock", "Water"),
    35, 65, 77, 35,
    ((1, mv.BIND), (1, mv.WITHDRAW), (5, mv.ROLLOUT), (10, mv.SAND_ATTACK),
     (15, mv.WATER_GUN), (20, mv.LEER), (25, mv.MUD_SHOT),
     (30, mv.ANCIENT_POWER), (35, mv.BRINE), (41, mv.PROTECT),
     (45, mv.ROCK_BLAST), (50, mv.SURF), (55, mv.SHELL_SMASH),
     (60, mv.HYDRO_PUMP)),
    OMASTAR, 40, True, "")

KABUTOPS = Pokemon(
    141, "Kabutops", 1, False,
    "", ("Rock", "Water"),
    60, 90, 87, 80,
    ((0, mv.SLASH), (1, mv.ABSORB), (1, mv.FEINT), (1, mv.HARDEN),
     (1, mv.NIGHT_SLASH), (1, mv.SAND_ATTACK), (1, mv.SCRATCH),
     (15, mv.AQUA_JET), (20, mv.LEER), (25, mv.MUD_SHOT),
     (30, mv.ANCIENT_POWER), (35, mv.BRINE), (43, mv.PROTECT),
     (49, mv.LEECH_LIFE), (56, mv.LIQUIDATION), (63, mv.METAL_SOUND),
     (70, mv.STONE_EDGE)),
    None, 0, False, "")

KABUTO = Pokemon(
    140, "Kabuto", 1, False,
    "", ("Rock", "Water"),
    30, 67, 67, 55,
    ((1, mv.ABSORB), (1, mv.HARDEN), (5, mv.SCRATCH), (10, mv.SAND_ATTACK),
     (15, mv.AQUA_JET), (20, mv.LEER), (25, mv.MUD_SHOT),
     (30, mv.ANCIENT_POWER), (35, mv.BRINE), (41, mv.PROTECT),
     (45, mv.LEECH_LIFE), (50, mv.LIQUIDATION), (55, mv.METAL_SOUND),
     (60, mv.STONE_EDGE)),
    KABUTOPS, 40, True, "")

AERODACTYL = Pokemon(
    142, "Aerodactyl", 1, False,
    "", ("Rock", "Flying"),
    80, 82, 70, 130,
    ((1, mv.ANCIENT_POWER), (1, mv.BITE), (5, mv.SUPERSONIC),
     (10, mv.WING_ATTACK), (15, mv.SCARY_FACE), (20, mv.ROCK_SLIDE),
     (25, mv.ROAR), (30, mv.CRUNCH), (35, mv.IRON_HEAD), (40, mv.TAKE_DOWN),
     (45, mv.STONE_EDGE), (50, mv.AGILITY), (55, mv.HYPER_BEAM),
     (60, mv.GIGA_IMPACT)),
    None, 0, False, "")

SNORLAX = Pokemon(
    143, "Snorlax", 1, False,
    "", ("Normal",),
    160, 87, 87, 30,
    ((1, mv.BLOCK), (1, mv.COVET), (1, mv.DEFENSE_CURL), (1, mv.FLAIL),
     (1, mv.FLING), (1, mv.LAST_RESORT), (1, mv.LICK), (1, mv.METRONOME),
     (1, mv.RECYCLE), (1, mv.SCREECH), (1, mv.STOCKPILE), (1, mv.SWALLOW),
     (1, mv.TACKLE), (12, mv.YAWN), (16, mv.BITE), (20, mv.REST),
     (20, mv.SLEEP_TALK), (20, mv.SNORE), (24, mv.CRUNCH), (28, mv.BODY_SLAM),
     (32, mv.HEAVY_SLAM), (36, mv.AMNESIA), (40, mv.HIGH_HORSEPOWER),
     (44, mv.HAMMER_ARM), (48, mv.BELLY_DRUM), (52, mv.BELCH),
     (56, mv.GIGA_IMPACT)),
    None, 0, False, "")

ARTICUNO = Pokemon(
    144, "Articuno", 1, False,
    "", ("Ice", "Flying"),
    90, 90, 112, 85,
    ((1, mv.GUST), (1, mv.MIST), (5, mv.POWDER_SNOW), (10, mv.REFLECT),
     (15, mv.ICE_SHARD), (20, mv.AGILITY), (25, mv.ANCIENT_POWER),
     (30, mv.TAILWIND), (35, mv.FREEZE_DRY), (40, mv.ROOST), (45, mv.ICE_BEAM),
     (50, mv.SNOWSCAPE), (55, mv.HURRICANE), (60, mv.HAZE), (65, mv.BLIZZARD),
     (70, mv.SHEER_COLD)),
    None, 0, False, "")

ZAPDOS = Pokemon(
    145, "Zapdos", 1, False,
    "", ("Electric", "Flying"),
    90, 107, 87, 100,
    ((1, mv.PECK), (1, mv.THUNDER_WAVE), (5, mv.THUNDER_SHOCK),
     (10, mv.LIGHT_SCREEN), (15, mv.PLUCK), (20, mv.AGILITY),
     (25, mv.ANCIENT_POWER), (30, mv.CHARGE), (35, mv.DRILL_PECK),
     (40, mv.ROOST), (45, mv.DISCHARGE), (50, mv.RAIN_DANCE), (55, mv.THUNDER),
     (60, mv.DETECT), (65, mv.MAGNETIC_FLUX), (70, mv.ZAP_CANNON)),
    None, 0, False, "")

MOLTRES = Pokemon(
    146, "Moltres", 1, False,
    "", ("Fire", "Flying"),
    90, 112, 87, 90,
    ((1, mv.GUST), (1, mv.LEER), (5, mv.EMBER), (10, mv.SAFEGUARD),
     (15, mv.WING_ATTACK), (20, mv.AGILITY), (25, mv.ANCIENT_POWER),
     (30, mv.INCINERATE), (35, mv.AIR_SLASH), (40, mv.ROOST),
     (45, mv.HEAT_WAVE), (50, mv.SUNNY_DAY), (55, mv.HURRICANE),
     (60, mv.ENDURE), (65, mv.OVERHEAT), (70, mv.SKY_ATTACK)),
    None, 0, False, "")

DRAGONITE = Pokemon(
    149, "Dragonite", 1, False,
    "", ("Dragon", "Flying"),
    91, 117, 97, 80,
    ((0, mv.HURRICANE), (1, mv.EXTREME_SPEED), (1, mv.FIRE_PUNCH),
     (1, mv.LEER), (1, mv.ROOST), (1, mv.THUNDER_PUNCH), (1, mv.THUNDER_WAVE),
     (1, mv.TWISTER), (1, mv.WING_ATTACK), (1, mv.WRAP), (15, mv.DRAGON_TAIL),
     (20, mv.AGILITY), (25, mv.SLAM), (33, mv.AQUA_TAIL), (39, mv.DRAGON_RUSH),
     (41, mv.OUTRAGE), (46, mv.SAFEGUARD), (53, mv.RAIN_DANCE),
     (62, mv.DRAGON_DANCE), (80, mv.HYPER_BEAM)),
    None, 0, False, "")

DRAGONAIR = Pokemon(
    148, "Dragonair", 1, False,
    "", ("Dragon",),
    61, 77, 67, 70,
    ((1, mv.LEER), (1, mv.THUNDER_WAVE), (1, mv.TWISTER), (1, mv.WRAP),
     (15, mv.DRAGON_TAIL), (20, mv.AGILITY), (25, mv.SLAM), (33, mv.AQUA_TAIL),
     (39, mv.DRAGON_RUSH), (46, mv.SAFEGUARD), (53, mv.RAIN_DANCE),
     (60, mv.DRAGON_DANCE), (67, mv.OUTRAGE), (74, mv.HYPER_BEAM)),
    DRAGONITE, 55, True, "")

DRATINI = Pokemon(
    147, "Dratini", 1, False,
    "", ("Dragon",),
    41, 57, 47, 50,
    ((1, mv.LEER), (1, mv.WRAP), (5, mv.TWISTER), (10, mv.THUNDER_WAVE),
     (15, mv.DRAGON_TAIL), (20, mv.AGILITY), (25, mv.SLAM), (31, mv.AQUA_TAIL),
     (35, mv.DRAGON_RUSH), (40, mv.SAFEGUARD), (45, mv.RAIN_DANCE),
     (50, mv.DRAGON_DANCE), (55, mv.OUTRAGE), (60, mv.HYPER_BEAM)),
    DRAGONAIR, 30, True, "")

MEWTWO = Pokemon(
    150, "Mewtwo", 1, False,
    "", ("Psychic",),
    106, 132, 90, 130,
    ((1, mv.CONFUSION), (1, mv.DISABLE), (1, mv.LIFE_DEW), (1, mv.SWIFT),
     (8, mv.ANCIENT_POWER), (16, mv.PSYCHO_CUT), (24, mv.SAFEGUARD),
     (32, mv.AMNESIA), (40, mv.AURA_SPHERE), (48, mv.PSYCHIC),
     (56, mv.GUARD_SWAP), (56, mv.POWER_SWAP), (64, mv.MIST),
     (72, mv.PSYSTRIKE), (80, mv.RECOVER), (88, mv.FUTURE_SIGHT)),
    None, 0, False, "")

MEW = Pokemon(
    151, "Mew", 1, False,
    "", ("Psychic",),
    100, 100, 100, 100,
    ((1, mv.POUND), (1, mv.REFLECT_TYPE), (10, mv.AMNESIA),
     (20, mv.BATON_PASS), (30, mv.ANCIENT_POWER), (40, mv.LIFE_DEW),
     (50, mv.NASTY_PLOT), (60, mv.METRONOME), (70, mv.IMPRISON),
     (80, mv.TRANSFORM), (90, mv.AURA_SPHERE), (100, mv.PSYCHIC)),
    None, 0, False, "")


# --- generation 2 ---

MEGANIUM = Pokemon(
    154, "Meganium", 2, True,
    "Flora", ("Grass",),
    80, 82, 100, 80,
    ((0, mv.PETAL_DANCE), (1, mv.GROWL), (1, mv.PETAL_BLIZZARD),
     (1, mv.POISON_POWDER), (1, mv.RAZOR_LEAF), (1, mv.TACKLE),
     (12, mv.SYNTHESIS), (18, mv.REFLECT), (22, mv.MAGICAL_LEAF),
     (26, mv.LEECH_SEED), (34, mv.SWEET_SCENT), (40, mv.LIGHT_SCREEN),
     (46, mv.BODY_SLAM), (54, mv.SAFEGUARD), (60, mv.GIGA_DRAIN),
     (65, mv.SOLAR_BEAM)),
    None, 0, False, "")

BAYLEEF = Pokemon(
    153, "Bayleef", 2, True,
    "Flora", ("Grass",),
    60, 62, 80, 60,
    ((1, mv.GROWL), (1, mv.POISON_POWDER), (1, mv.RAZOR_LEAF), (1, mv.TACKLE),
     (12, mv.SYNTHESIS), (18, mv.REFLECT), (22, mv.MAGICAL_LEAF),
     (26, mv.LEECH_SEED), (32, mv.SWEET_SCENT), (36, mv.LIGHT_SCREEN),
     (40, mv.BODY_SLAM), (46, mv.SAFEGUARD), (50, mv.GIGA_DRAIN),
     (54, mv.SOLAR_BEAM)),
    MEGANIUM, 32, True, "")

CHIKORITA = Pokemon(
    152, "Chikorita", 2, True,
    "Flora", ("Grass",),
    45, 49, 65, 45,
    ((1, mv.GROWL), (1, mv.TACKLE), (6, mv.RAZOR_LEAF), (9, mv.POISON_POWDER),
     (12, mv.SYNTHESIS), (17, mv.REFLECT), (20, mv.MAGICAL_LEAF),
     (23, mv.LEECH_SEED), (28, mv.SWEET_SCENT), (31, mv.LIGHT_SCREEN),
     (34, mv.BODY_SLAM), (39, mv.SAFEGUARD), (42, mv.GIGA_DRAIN),
     (45, mv.SOLAR_BEAM)),
    BAYLEEF, 16, True, "")

TYPHLOSION = Pokemon(
    157, "Typhlosion", 2, True,
    "Flame", ("Fire",),
    78, 96, 81, 100,
    ((1, mv.DOUBLE_EDGE), (1, mv.EMBER), (1, mv.ERUPTION), (1, mv.GYRO_BALL),
     (1, mv.LEER), (1, mv.SMOKESCREEN), (1, mv.TACKLE), (13, mv.QUICK_ATTACK),
     (20, mv.FLAME_WHEEL), (24, mv.DEFENSE_CURL), (31, mv.SWIFT),
     (35, mv.FLAME_CHARGE), (43, mv.LAVA_PLUME), (48, mv.FLAMETHROWER),
     (56, mv.INFERNO), (61, mv.ROLLOUT), (74, mv.OVERHEAT)),
    None, 0, False, "")

QUILAVA = Pokemon(
    156, "Quilava", 2, True,
    "Flame", ("Fire",),
    58, 72, 61, 80,
    ((1, mv.LEER), (1, mv.SMOKESCREEN), (1, mv.TACKLE), (10, mv.EMBER),
     (13, mv.QUICK_ATTACK), (20, mv.FLAME_WHEEL), (24, mv.DEFENSE_CURL),
     (31, mv.SWIFT), (35, mv.FLAME_CHARGE), (42, mv.LAVA_PLUME),
     (46, mv.FLAMETHROWER), (53, mv.INFERNO), (57, mv.ROLLOUT),
     (64, mv.DOUBLE_EDGE), (68, mv.OVERHEAT), (75, mv.ERUPTION)),
    TYPHLOSION, 36, True, "")

CYNDAQUIL = Pokemon(
    155, "Cyndaquil", 2, True,
    "Flame", ("Fire",),
    39, 56, 46, 65,
    ((1, mv.LEER), (1, mv.TACKLE), (6, mv.SMOKESCREEN), (10, mv.EMBER),
     (13, mv.QUICK_ATTACK), (19, mv.FLAME_WHEEL), (22, mv.DEFENSE_CURL),
     (28, mv.FLAME_CHARGE), (31, mv.SWIFT), (37, mv.LAVA_PLUME),
     (40, mv.FLAMETHROWER), (46, mv.INFERNO), (49, mv.ROLLOUT),
     (55, mv.DOUBLE_EDGE), (58, mv.OVERHEAT), (64, mv.ERUPTION)),
    QUILAVA, 17, True, "")

FERALIGATR = Pokemon(
    160, "Feraligatr", 2, True,
    "Aqua", ("Water",),
    85, 92, 91, 78,
    ((1, mv.AGILITY), (1, mv.LEER), (1, mv.SCRATCH), (1, mv.WATER_GUN),
     (13, mv.BITE), (15, mv.SCARY_FACE), (21, mv.ICE_FANG), (24, mv.FLAIL),
     (32, mv.CRUNCH), (37, mv.SLASH), (44, mv.SCREECH), (51, mv.THRASH),
     (59, mv.AQUA_TAIL), (65, mv.SUPERPOWER), (70, mv.HYDRO_PUMP)),
    None, 0, False, "")

CROCONAW = Pokemon(
    159, "Croconaw", 2, True,
    "Aqua", ("Water",),
    65, 69, 71, 58,
    ((1, mv.LEER), (1, mv.SCRATCH), (1, mv.WATER_GUN), (13, mv.BITE),
     (15, mv.SCARY_FACE), (21, mv.ICE_FANG), (24, mv.FLAIL), (30, mv.CRUNCH),
     (34, mv.SLASH), (37, mv.SCREECH), (42, mv.THRASH), (47, mv.AQUA_TAIL),
     (50, mv.SUPERPOWER), (55, mv.HYDRO_PUMP)),
    FERALIGATR, 30, True, "")

TOTODILE = Pokemon(
    158, "Totodile", 2, True,
    "Aqua", ("Water",),
    50, 54, 56, 43,
    ((1, mv.LEER), (1, mv.SCRATCH), (6, mv.WATER_GUN), (9, mv.BITE),
     (13, mv.SCARY_FACE), (19, mv.ICE_FANG), (22, mv.FLAIL), (27, mv.CRUNCH),
     (30, mv.SLASH), (33, mv.SCREECH), (37, mv.THRASH), (41, mv.AQUA_TAIL),
     (45, mv.SUPERPOWER), (50, mv.HYDRO_PUMP)),
    CROCONAW, 18, True, "")

FURRET = Pokemon(
    162, "Furret", 2, False,
    "", ("Normal",),
    85, 60, 59, 90,
    ((0, mv.AGILITY), (1, mv.COIL), (1, mv.DEFENSE_CURL), (1, mv.QUICK_ATTACK),
     (1, mv.SCRATCH), (13, mv.FURY_SWIPES), (17, mv.HELPING_HAND),
     (21, mv.FOLLOW_ME), (28, mv.SLAM), (32, mv.REST), (36, mv.SUCKER_PUNCH),
     (42, mv.AMNESIA), (46, mv.BATON_PASS), (50, mv.DOUBLE_EDGE),
     (56, mv.HYPER_VOICE)),
    None, 0, False, "")

SENTRET = Pokemon(
    161, "Sentret", 2, False,
    "", ("Normal",),
    35, 40, 39, 20,
    ((1, mv.SCRATCH), (4, mv.DEFENSE_CURL), (7, mv.QUICK_ATTACK),
     (13, mv.FURY_SWIPES), (16, mv.HELPING_HAND), (19, mv.FOLLOW_ME),
     (25, mv.SLAM), (28, mv.REST), (31, mv.SUCKER_PUNCH), (36, mv.AMNESIA),
     (39, mv.BATON_PASS), (42, mv.DOUBLE_EDGE), (47, mv.HYPER_VOICE)),
    FURRET, 15, True, "")

NOCTOWL = Pokemon(
    164, "Noctowl", 2, False,
    "", ("Normal", "Flying"),
    100, 68, 73, 70,
    ((1, mv.ECHOED_VOICE), (1, mv.GROWL), (1, mv.PECK), (1, mv.SKY_ATTACK),
     (1, mv.TACKLE), (9, mv.CONFUSION), (12, mv.REFLECT), (18, mv.AIR_SLASH),
     (23, mv.EXTRASENSORY), (28, mv.TAKE_DOWN), (33, mv.UPROAR),
     (38, mv.ROOST), (43, mv.MOONBLAST), (48, mv.HYPNOSIS),
     (53, mv.DREAM_EATER)),
    None, 0, False, "")

HOOTHOOT = Pokemon(
    163, "Hoothoot", 2, False,
    "", ("Normal", "Flying"),
    60, 33, 43, 50,
    ((1, mv.GROWL), (1, mv.PECK), (3, mv.TACKLE), (6, mv.ECHOED_VOICE),
     (9, mv.CONFUSION), (12, mv.REFLECT), (15, mv.DEFOG), (18, mv.AIR_SLASH),
     (21, mv.EXTRASENSORY), (24, mv.TAKE_DOWN), (27, mv.UPROAR),
     (30, mv.ROOST), (33, mv.MOONBLAST), (36, mv.HYPNOSIS),
     (39, mv.DREAM_EATER)),
    NOCTOWL, 20, True, "")

LEDIAN = Pokemon(
    166, "Ledian", 2, False,
    "", ("Bug", "Flying"),
    55, 45, 80, 85,
    ((1, mv.TACKLE), (5, mv.SUPERSONIC), (8, mv.SWIFT), (12, mv.LIGHT_SCREEN),
     (12, mv.REFLECT), (12, mv.SAFEGUARD), (15, mv.MACH_PUNCH),
     (20, mv.SILVER_WIND), (24, mv.COMET_PUNCH), (29, mv.BATON_PASS),
     (33, mv.AGILITY), (38, mv.BUG_BUZZ), (42, mv.AIR_SLASH),
     (47, mv.DOUBLE_EDGE)),
    None, 0, False, "")

LEDYBA = Pokemon(
    165, "Ledyba", 2, False,
    "", ("Bug", "Flying"),
    40, 30, 55, 55,
    ((1, mv.TACKLE), (5, mv.SUPERSONIC), (8, mv.SWIFT), (12, mv.LIGHT_SCREEN),
     (12, mv.REFLECT), (12, mv.SAFEGUARD), (15, mv.MACH_PUNCH),
     (19, mv.SILVER_WIND), (22, mv.COMET_PUNCH), (26, mv.BATON_PASS),
     (29, mv.AGILITY), (33, mv.BUG_BUZZ), (36, mv.AIR_SLASH),
     (40, mv.DOUBLE_EDGE)),
    LEDIAN, 18, True, "")

ARIADOS = Pokemon(
    168, "Ariados", 2, False,
    "", ("Bug", "Poison"),
    70, 75, 70, 40,
    ((0, mv.SWORDS_DANCE), (1, mv.ABSORB), (1, mv.BUG_BITE),
     (1, mv.FELL_STINGER), (1, mv.FOCUS_ENERGY), (1, mv.POISON_STING),
     (1, mv.STRING_SHOT), (8, mv.INFESTATION), (12, mv.SCARY_FACE),
     (15, mv.NIGHT_SHADE), (19, mv.SHADOW_SNEAK), (23, mv.FURY_SWIPES),
     (28, mv.SUCKER_PUNCH), (31, mv.AGILITY), (35, mv.PIN_MISSILE),
     (41, mv.PSYCHIC), (46, mv.POISON_JAB), (50, mv.CROSS_POISON),
     (54, mv.STICKY_WEB), (59, mv.TOXIC_THREAD)),
    None, 0, False, "")

SPINARAK = Pokemon(
    167, "Spinarak", 2, False,
    "", ("Bug", "Poison"),
    40, 50, 40, 30,
    ((1, mv.POISON_STING), (1, mv.STRING_SHOT), (5, mv.ABSORB),
     (8, mv.INFESTATION), (12, mv.SCARY_FACE), (15, mv.NIGHT_SHADE),
     (19, mv.SHADOW_SNEAK), (22, mv.FURY_SWIPES), (26, mv.SUCKER_PUNCH),
     (29, mv.AGILITY), (33, mv.PIN_MISSILE), (36, mv.PSYCHIC),
     (40, mv.POISON_JAB), (44, mv.CROSS_POISON), (47, mv.STICKY_WEB),
     (51, mv.TOXIC_THREAD)),
    ARIADOS, 22, True, "")

LANTURN = Pokemon(
    171, "Lanturn", 2, False,
    "", ("Water", "Electric"),
    125, 67, 67, 67,
    ((0, mv.SPIT_UP), (0, mv.STOCKPILE), (0, mv.SWALLOW),
     (1, mv.EERIE_IMPULSE), (1, mv.ELECTRO_BALL), (1, mv.SUPERSONIC),
     (1, mv.THUNDER_WAVE), (1, mv.WATER_GUN), (12, mv.BUBBLE_BEAM),
     (16, mv.CONFUSE_RAY), (20, mv.SPARK), (24, mv.CHARGE), (30, mv.DISCHARGE),
     (36, mv.AQUA_RING), (42, mv.FLAIL), (48, mv.TAKE_DOWN),
     (54, mv.HYDRO_PUMP)),
    None, 0, False, "")

CHINCHOU = Pokemon(
    170, "Chinchou", 2, False,
    "", ("Water", "Electric"),
    75, 47, 47, 67,
    ((1, mv.SUPERSONIC), (1, mv.WATER_GUN), (4, mv.ELECTRO_BALL),
     (8, mv.THUNDER_WAVE), (12, mv.BUBBLE_BEAM), (16, mv.CONFUSE_RAY),
     (20, mv.SPARK), (24, mv.CHARGE), (28, mv.DISCHARGE), (32, mv.AQUA_RING),
     (36, mv.FLAIL), (40, mv.TAKE_DOWN), (44, mv.HYDRO_PUMP)),
    LANTURN, 27, True, "")

PICHU = Pokemon(
    172, "Pichu", 2, False,
    "", ("Electric",),
    20, 37, 25, 60,
    ((1, mv.TAIL_WHIP), (1, mv.THUNDER_SHOCK), (4, mv.PLAY_NICE),
     (8, mv.SWEET_KISS), (12, mv.NUZZLE), (16, mv.NASTY_PLOT), (20, mv.CHARM)),
    PIKACHU, 0, True, "happiness")

CLEFFA = Pokemon(
    173, "Cleffa", 2, False,
    "", ("Fairy",),
    50, 35, 41, 15,
    ((1, mv.COPYCAT), (1, mv.POUND), (1, mv.SPLASH), (4, mv.SING),
     (8, mv.SWEET_KISS), (12, mv.DISARMING_VOICE), (16, mv.ENCORE),
     (20, mv.CHARM)),
    CLEFAIRY, 0, True, "happiness")

IGGLYBUFF = Pokemon(
    174, "Igglybuff", 2, False,
    "", ("Normal", "Fairy"),
    90, 35, 17, 15,
    ((1, mv.COPYCAT), (1, mv.POUND), (1, mv.SING), (4, mv.DEFENSE_CURL),
     (8, mv.SWEET_KISS), (12, mv.DISARMING_VOICE), (16, mv.DISABLE),
     (20, mv.CHARM)),
    JIGGLYPUFF, 0, True, "happiness")


# --- generation 4 ---

TOGEKISS = Pokemon(
    468, "Togekiss", 4, False,
    "", ("Fairy", "Flying"),
    85, 85, 105, 80,
    ((0, mv.AIR_SLASH), (1, mv.AFTER_YOU), (1, mv.ANCIENT_POWER),
     (1, mv.AURA_SPHERE), (1, mv.BATON_PASS), (1, mv.CHARM),
     (1, mv.DOUBLE_EDGE), (1, mv.EXTREME_SPEED), (1, mv.FAIRY_WIND),
     (1, mv.FOLLOW_ME), (1, mv.GROWL), (1, mv.LAST_RESORT), (1, mv.LIFE_DEW),
     (1, mv.METRONOME), (1, mv.POUND), (1, mv.SAFEGUARD), (1, mv.SKY_ATTACK),
     (1, mv.SWEET_KISS), (1, mv.TRI_ATTACK), (1, mv.WISH), (1, mv.YAWN)),
    None, 0, False, "")


# --- generation 2 ---

TOGETIC = Pokemon(
    176, "Togetic", 2, False,
    "", ("Fairy", "Flying"),
    55, 60, 95, 40,
    ((1, mv.FAIRY_WIND), (1, mv.GROWL), (1, mv.LIFE_DEW), (1, mv.POUND),
     (1, mv.SWEET_KISS), (12, mv.CHARM), (16, mv.ANCIENT_POWER), (20, mv.YAWN),
     (24, mv.METRONOME), (28, mv.AFTER_YOU), (32, mv.DOUBLE_EDGE),
     (36, mv.SAFEGUARD), (40, mv.FOLLOW_ME), (44, mv.BATON_PASS),
     (48, mv.LAST_RESORT), (52, mv.WISH)),
    TOGEKISS, 0, True, "item:shiny-stone")

TOGEPI = Pokemon(
    175, "Togepi", 2, False,
    "", ("Fairy",),
    35, 30, 65, 20,
    ((1, mv.GROWL), (1, mv.POUND), (4, mv.SWEET_KISS), (8, mv.LIFE_DEW),
     (12, mv.CHARM), (16, mv.ANCIENT_POWER), (20, mv.YAWN), (24, mv.METRONOME),
     (28, mv.AFTER_YOU), (32, mv.DOUBLE_EDGE), (36, mv.SAFEGUARD),
     (40, mv.FOLLOW_ME), (44, mv.BATON_PASS), (48, mv.LAST_RESORT),
     (52, mv.WISH)),
    TOGETIC, 0, True, "happiness")

XATU = Pokemon(
    178, "Xatu", 2, False,
    "", ("Psychic", "Flying"),
    65, 85, 70, 95,
    ((1, mv.AIR_SLASH), (1, mv.LEER), (1, mv.PECK), (1, mv.STORED_POWER),
     (1, mv.TAILWIND), (1, mv.TELEPORT), (15, mv.CONFUSE_RAY),
     (20, mv.NIGHT_SHADE), (28, mv.PSYCHO_SHIFT), (34, mv.GUARD_SWAP),
     (34, mv.POWER_SWAP), (41, mv.PSYCHIC), (48, mv.WISH),
     (55, mv.FUTURE_SIGHT)),
    None, 0, False, "")

NATU = Pokemon(
    177, "Natu", 2, False,
    "", ("Psychic", "Flying"),
    40, 60, 45, 70,
    ((1, mv.LEER), (1, mv.PECK), (5, mv.STORED_POWER), (10, mv.TELEPORT),
     (15, mv.CONFUSE_RAY), (20, mv.NIGHT_SHADE), (26, mv.PSYCHO_SHIFT),
     (30, mv.POWER_SWAP), (35, mv.GUARD_SWAP), (35, mv.PSYCHIC), (40, mv.WISH),
     (45, mv.FUTURE_SIGHT)),
    XATU, 25, True, "")

AMPHAROS = Pokemon(
    181, "Ampharos", 2, False,
    "", ("Electric",),
    90, 95, 87, 55,
    ((0, mv.THUNDER_PUNCH), (1, mv.DRAGON_PULSE), (1, mv.FIRE_PUNCH),
     (1, mv.GROWL), (1, mv.MAGNETIC_FLUX), (1, mv.TACKLE),
     (1, mv.THUNDER_SHOCK), (1, mv.THUNDER_WAVE), (1, mv.ZAP_CANNON),
     (11, mv.COTTON_SPORE), (16, mv.CHARGE), (20, mv.TAKE_DOWN),
     (25, mv.ELECTRO_BALL), (29, mv.CONFUSE_RAY), (35, mv.POWER_GEM),
     (40, mv.DISCHARGE), (46, mv.COTTON_GUARD), (51, mv.DAZZLING_GLEAM),
     (57, mv.LIGHT_SCREEN), (62, mv.THUNDER)),
    None, 0, False, "")

FLAAFFY = Pokemon(
    180, "Flaaffy", 2, False,
    "", ("Electric",),
    70, 67, 57, 45,
    ((1, mv.GROWL), (1, mv.TACKLE), (6, mv.THUNDER_SHOCK),
     (9, mv.THUNDER_WAVE), (11, mv.COTTON_SPORE), (16, mv.CHARGE),
     (20, mv.TAKE_DOWN), (25, mv.ELECTRO_BALL), (29, mv.CONFUSE_RAY),
     (34, mv.POWER_GEM), (38, mv.DISCHARGE), (43, mv.COTTON_GUARD),
     (47, mv.DAZZLING_GLEAM), (52, mv.LIGHT_SCREEN), (56, mv.THUNDER)),
    AMPHAROS, 30, True, "")

MAREEP = Pokemon(
    179, "Mareep", 2, False,
    "", ("Electric",),
    55, 52, 42, 35,
    ((1, mv.GROWL), (1, mv.TACKLE), (4, mv.THUNDER_WAVE),
     (8, mv.THUNDER_SHOCK), (11, mv.COTTON_SPORE), (15, mv.CHARGE),
     (18, mv.TAKE_DOWN), (22, mv.ELECTRO_BALL), (25, mv.CONFUSE_RAY),
     (29, mv.POWER_GEM), (32, mv.DISCHARGE), (36, mv.COTTON_GUARD),
     (39, mv.DAZZLING_GLEAM), (43, mv.LIGHT_SCREEN), (46, mv.THUNDER)),
    FLAAFFY, 15, True, "")

AZUMARILL = Pokemon(
    184, "Azumarill", 2, False,
    "", ("Water", "Fairy"),
    100, 55, 80, 50,
    ((1, mv.DEFENSE_CURL), (1, mv.HELPING_HAND), (1, mv.ROLLOUT),
     (1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (6, mv.BUBBLE_BEAM),
     (9, mv.CHARM), (12, mv.SLAM), (15, mv.BOUNCE), (21, mv.AQUA_TAIL),
     (25, mv.PLAY_ROUGH), (30, mv.AQUA_RING), (35, mv.RAIN_DANCE),
     (40, mv.HYDRO_PUMP), (45, mv.DOUBLE_EDGE), (50, mv.SUPERPOWER)),
    None, 0, False, "")

MARILL = Pokemon(
    183, "Marill", 2, False,
    "", ("Water", "Fairy"),
    70, 20, 50, 40,
    ((1, mv.DEFENSE_CURL), (1, mv.HELPING_HAND), (1, mv.ROLLOUT),
     (1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (6, mv.BUBBLE_BEAM),
     (9, mv.CHARM), (12, mv.SLAM), (15, mv.BOUNCE), (19, mv.AQUA_TAIL),
     (21, mv.PLAY_ROUGH), (24, mv.AQUA_RING), (27, mv.RAIN_DANCE),
     (30, mv.HYDRO_PUMP), (33, mv.DOUBLE_EDGE), (36, mv.SUPERPOWER)),
    AZUMARILL, 18, True, "")

SUDOWOODO = Pokemon(
    185, "Sudowoodo", 2, False,
    "", ("Rock",),
    70, 65, 90, 30,
    ((0, mv.SLAM), (1, mv.COPYCAT), (1, mv.FAKE_TEARS), (1, mv.FLAIL),
     (1, mv.HAMMER_ARM), (1, mv.ROCK_THROW), (1, mv.STONE_EDGE),
     (1, mv.WOOD_HAMMER), (12, mv.BLOCK), (16, mv.MIMIC), (20, mv.ROCK_TOMB),
     (24, mv.TEARFUL_LOOK), (28, mv.SUCKER_PUNCH), (32, mv.ROCK_SLIDE),
     (36, mv.LOW_KICK), (40, mv.COUNTER), (44, mv.DOUBLE_EDGE),
     (48, mv.HEAD_SMASH)),
    None, 0, False, "")

JUMPLUFF = Pokemon(
    189, "Jumpluff", 2, False,
    "", ("Grass", "Flying"),
    75, 55, 82, 110,
    ((1, mv.ABSORB), (1, mv.SPLASH), (1, mv.SYNTHESIS), (1, mv.TAIL_WHIP),
     (8, mv.TACKLE), (10, mv.FAIRY_WIND), (12, mv.POISON_POWDER),
     (12, mv.SLEEP_POWDER), (12, mv.STUN_SPORE), (15, mv.BULLET_SEED),
     (20, mv.LEECH_SEED), (24, mv.MEGA_DRAIN), (30, mv.ACROBATICS),
     (35, mv.COTTON_SPORE), (39, mv.U_TURN), (43, mv.GIGA_DRAIN),
     (49, mv.BOUNCE), (55, mv.MEMENTO)),
    None, 0, False, "")

SKIPLOOM = Pokemon(
    188, "Skiploom", 2, False,
    "", ("Grass", "Flying"),
    55, 45, 57, 80,
    ((1, mv.ABSORB), (1, mv.SPLASH), (1, mv.SYNTHESIS), (1, mv.TAIL_WHIP),
     (8, mv.TACKLE), (10, mv.FAIRY_WIND), (12, mv.POISON_POWDER),
     (12, mv.SLEEP_POWDER), (12, mv.STUN_SPORE), (15, mv.BULLET_SEED),
     (20, mv.LEECH_SEED), (24, mv.MEGA_DRAIN), (28, mv.ACROBATICS),
     (31, mv.COTTON_SPORE), (34, mv.U_TURN), (37, mv.GIGA_DRAIN),
     (41, mv.BOUNCE), (44, mv.MEMENTO)),
    JUMPLUFF, 27, True, "")

HOPPIP = Pokemon(
    187, "Hoppip", 2, False,
    "", ("Grass", "Flying"),
    35, 35, 47, 50,
    ((1, mv.SPLASH), (1, mv.TACKLE), (4, mv.TAIL_WHIP), (6, mv.ABSORB),
     (8, mv.FAIRY_WIND), (10, mv.POISON_POWDER), (10, mv.SLEEP_POWDER),
     (10, mv.STUN_SPORE), (12, mv.BULLET_SEED), (15, mv.SYNTHESIS),
     (19, mv.LEECH_SEED), (22, mv.MEGA_DRAIN), (24, mv.ACROBATICS),
     (27, mv.COTTON_SPORE), (29, mv.U_TURN), (32, mv.GIGA_DRAIN),
     (35, mv.BOUNCE), (38, mv.MEMENTO)),
    SKIPLOOM, 18, True, "")


# --- generation 4 ---

AMBIPOM = Pokemon(
    424, "Ambipom", 4, False,
    "", ("Normal",),
    75, 80, 66, 115,
    ((1, mv.ASTONISH), (1, mv.SAND_ATTACK), (1, mv.SCRATCH), (1, mv.TAIL_WHIP),
     (11, mv.BATON_PASS), (15, mv.TICKLE), (18, mv.FURY_SWIPES),
     (22, mv.SWIFT), (25, mv.SCREECH), (29, mv.AGILITY), (32, mv.DOUBLE_HIT),
     (36, mv.FLING), (39, mv.NASTY_PLOT), (43, mv.LAST_RESORT)),
    None, 0, False, "")


# --- generation 2 ---

AIPOM = Pokemon(
    190, "Aipom", 2, False,
    "", ("Normal",),
    55, 55, 55, 85,
    ((1, mv.SCRATCH), (1, mv.TAIL_WHIP), (4, mv.SAND_ATTACK), (8, mv.ASTONISH),
     (11, mv.BATON_PASS), (15, mv.TICKLE), (18, mv.FURY_SWIPES),
     (22, mv.SWIFT), (25, mv.SCREECH), (29, mv.AGILITY), (32, mv.DOUBLE_HIT),
     (36, mv.FLING), (39, mv.NASTY_PLOT), (43, mv.LAST_RESORT)),
    AMBIPOM, 0, True, "level-up")

SUNFLORA = Pokemon(
    192, "Sunflora", 2, False,
    "", ("Grass",),
    75, 90, 70, 30,
    ((1, mv.GROWTH), (1, mv.POUND), (1, mv.TACKLE), (4, mv.INGRAIN),
     (7, mv.ABSORB), (10, mv.MEGA_DRAIN), (13, mv.LEECH_SEED),
     (16, mv.RAZOR_LEAF), (19, mv.WORRY_SEED), (22, mv.GIGA_DRAIN),
     (25, mv.BULLET_SEED), (28, mv.PETAL_DANCE), (31, mv.SOLAR_BEAM),
     (34, mv.DOUBLE_EDGE), (39, mv.SUNNY_DAY), (43, mv.LEAF_STORM),
     (50, mv.PETAL_BLIZZARD)),
    None, 0, False, "")

SUNKERN = Pokemon(
    191, "Sunkern", 2, False,
    "", ("Grass",),
    30, 30, 30, 30,
    ((1, mv.GROWTH), (1, mv.TACKLE), (7, mv.ABSORB), (10, mv.MEGA_DRAIN),
     (16, mv.RAZOR_LEAF), (19, mv.WORRY_SEED), (22, mv.GIGA_DRAIN),
     (25, mv.ENDEAVOR), (28, mv.SYNTHESIS), (31, mv.SOLAR_BEAM),
     (34, mv.DOUBLE_EDGE), (36, mv.SUNNY_DAY), (39, mv.SEED_BOMB)),
    SUNFLORA, 0, True, "item:sun-stone")


# --- generation 4 ---

YANMEGA = Pokemon(
    469, "Yanmega", 4, False,
    "", ("Bug", "Flying"),
    86, 96, 71, 95,
    ((1, mv.AIR_SLASH), (1, mv.BUG_BUZZ), (1, mv.DOUBLE_TEAM),
     (1, mv.NIGHT_SLASH), (1, mv.TACKLE), (14, mv.QUICK_ATTACK),
     (17, mv.DETECT), (22, mv.SUPERSONIC), (27, mv.UPROAR), (30, mv.BUG_BITE),
     (33, mv.ANCIENT_POWER), (38, mv.FEINT), (43, mv.SLASH), (46, mv.SCREECH),
     (49, mv.U_TURN)),
    None, 0, False, "")


# --- generation 2 ---

YANMA = Pokemon(
    193, "Yanma", 2, False,
    "", ("Bug", "Flying"),
    65, 70, 45, 95,
    ((1, mv.TACKLE), (6, mv.QUICK_ATTACK), (11, mv.DOUBLE_TEAM),
     (14, mv.AIR_CUTTER), (17, mv.DETECT), (22, mv.SUPERSONIC),
     (27, mv.UPROAR), (30, mv.BUG_BITE), (33, mv.ANCIENT_POWER),
     (38, mv.HYPNOSIS), (43, mv.WING_ATTACK), (46, mv.SCREECH),
     (49, mv.U_TURN), (54, mv.AIR_SLASH), (57, mv.BUG_BUZZ)),
    YANMEGA, 0, True, "level-up")


# --- generation 9 ---

CLODSIRE = Pokemon(
    980, "Clodsire", 9, False,
    "", ("Poison", "Ground"),
    130, 60, 80, 20,
    ((0, mv.AMNESIA), (1, mv.POISON_STING), (1, mv.TAIL_WHIP),
     (4, mv.TOXIC_SPIKES), (8, mv.MUD_SHOT), (12, mv.POISON_TAIL),
     (16, mv.SLAM), (21, mv.YAWN), (24, mv.POISON_JAB), (30, mv.SLUDGE_WAVE),
     (36, mv.MEGAHORN), (40, mv.TOXIC), (48, mv.EARTHQUAKE)),
    None, 0, False, "")


# --- generation 2 ---

QUAGSIRE = Pokemon(
    195, "Quagsire", 2, False,
    "", ("Water", "Ground"),
    95, 75, 75, 35,
    ((1, mv.MUD_SHOT), (1, mv.RAIN_DANCE), (1, mv.TAIL_WHIP),
     (1, mv.WATER_GUN), (12, mv.HAZE), (12, mv.MIST), (16, mv.SLAM),
     (23, mv.YAWN), (28, mv.AQUA_TAIL), (34, mv.MUDDY_WATER), (40, mv.AMNESIA),
     (46, mv.TOXIC), (52, mv.EARTHQUAKE)),
    CLODSIRE, 0, True, "Level 20")

WOOPER = Pokemon(
    194, "Wooper", 2, False,
    "", ("Water", "Ground"),
    55, 35, 35, 15,
    ((1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (4, mv.RAIN_DANCE),
     (8, mv.MUD_SHOT), (12, mv.HAZE), (12, mv.MIST), (16, mv.SLAM),
     (21, mv.YAWN), (24, mv.AQUA_TAIL), (28, mv.MUDDY_WATER), (32, mv.AMNESIA),
     (36, mv.TOXIC), (40, mv.EARTHQUAKE)),
    QUAGSIRE, 20, True, "")

ESPEON = Pokemon(
    196, "Espeon", 2, False,
    "", ("Psychic",),
    65, 97, 77, 110,
    ((0, mv.CONFUSION), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.SWIFT), (25, mv.PSYBEAM),
     (30, mv.MORNING_SUN), (35, mv.POWER_SWAP), (40, mv.PSYCHIC),
     (45, mv.PSYCH_UP), (50, mv.FUTURE_SIGHT), (55, mv.LAST_RESORT)),
    None, 0, False, "")

UMBREON = Pokemon(
    197, "Umbreon", 2, False,
    "", ("Dark",),
    95, 62, 120, 65,
    ((0, mv.SNARL), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.CONFUSE_RAY), (25, mv.ASSURANCE),
     (30, mv.MOONLIGHT), (35, mv.GUARD_SWAP), (40, mv.DARK_PULSE),
     (45, mv.SCREECH), (50, mv.MEAN_LOOK), (55, mv.LAST_RESORT)),
    None, 0, False, "")


# --- generation 4 ---

HONCHKROW = Pokemon(
    430, "Honchkrow", 4, False,
    "", ("Dark", "Flying"),
    100, 115, 52, 71,
    ((1, mv.ASTONISH), (1, mv.HAZE), (1, mv.NIGHT_SLASH), (1, mv.QUASH),
     (1, mv.SUCKER_PUNCH), (1, mv.WING_ATTACK), (25, mv.SWAGGER),
     (35, mv.NASTY_PLOT), (45, mv.FOUL_PLAY), (55, mv.DARK_PULSE),
     (65, mv.COMEUPPANCE)),
    None, 0, False, "")


# --- generation 2 ---

MURKROW = Pokemon(
    198, "Murkrow", 2, False,
    "", ("Dark", "Flying"),
    60, 85, 42, 91,
    ((1, mv.ASTONISH), (1, mv.PECK), (5, mv.GUST), (11, mv.HAZE),
     (15, mv.WING_ATTACK), (21, mv.NIGHT_SHADE), (25, mv.ASSURANCE),
     (31, mv.TAUNT), (35, mv.MEAN_LOOK), (40, mv.FOUL_PLAY),
     (50, mv.SUCKER_PUNCH), (55, mv.TORMENT), (60, mv.QUASH)),
    HONCHKROW, 0, True, "item:dusk-stone")


# --- generation 4 ---

MISMAGIUS = Pokemon(
    429, "Mismagius", 4, False,
    "", ("Ghost",),
    60, 82, 82, 105,
    ((1, mv.ASTONISH), (1, mv.GROWL), (1, mv.MAGICAL_LEAF),
     (1, mv.MYSTICAL_FIRE), (1, mv.PHANTOM_FORCE), (1, mv.POWER_GEM),
     (1, mv.SPITE)),
    None, 0, False, "")


# --- generation 2 ---

MISDREAVUS = Pokemon(
    200, "Misdreavus", 2, False,
    "", ("Ghost",),
    60, 72, 72, 85,
    ((1, mv.CONFUSION), (1, mv.GROWL), (10, mv.ASTONISH), (14, mv.CONFUSE_RAY),
     (19, mv.MEAN_LOOK), (23, mv.HEX), (28, mv.PSYBEAM), (32, mv.PAIN_SPLIT),
     (37, mv.PAYBACK), (41, mv.SHADOW_BALL), (46, mv.PERISH_SONG),
     (50, mv.POWER_GEM)),
    MISMAGIUS, 0, True, "item:dusk-stone")

UNOWN = Pokemon(
    201, "Unown", 2, False,
    "", ("Psychic",),
    48, 72, 48, 48,
    ((1, mv.HIDDEN_POWER),),
    None, 0, False, "")

WOBBUFFET = Pokemon(
    202, "Wobbuffet", 2, False,
    "", ("Psychic",),
    190, 33, 58, 33,
    ((0, mv.MIRROR_COAT), (0, mv.SAFEGUARD), (1, mv.AMNESIA), (1, mv.CHARM),
     (1, mv.COUNTER), (1, mv.DESTINY_BOND), (1, mv.ENCORE), (1, mv.SPLASH)),
    None, 0, False, "")


# --- generation 9 ---

FARIGIRAF = Pokemon(
    981, "Farigiraf", 9, False,
    "", ("Normal", "Psychic"),
    120, 100, 70, 60,
    ((1, mv.ASTONISH), (1, mv.GROWL), (1, mv.GUARD_SWAP), (1, mv.POWER_SWAP),
     (1, mv.TACKLE), (5, mv.CONFUSION), (10, mv.ASSURANCE), (14, mv.STOMP),
     (19, mv.PSYBEAM), (23, mv.AGILITY), (28, mv.DOUBLE_HIT),
     (32, mv.TWIN_BEAM), (37, mv.CRUNCH), (41, mv.BATON_PASS),
     (46, mv.NASTY_PLOT), (50, mv.PSYCHIC)),
    None, 0, False, "")


# --- generation 2 ---

GIRAFARIG = Pokemon(
    203, "Girafarig", 2, False,
    "", ("Normal", "Psychic"),
    70, 85, 65, 85,
    ((1, mv.ASTONISH), (1, mv.GROWL), (1, mv.GUARD_SWAP), (1, mv.POWER_SWAP),
     (1, mv.TACKLE), (5, mv.CONFUSION), (10, mv.ASSURANCE), (14, mv.STOMP),
     (19, mv.PSYBEAM), (23, mv.AGILITY), (28, mv.DOUBLE_HIT),
     (32, mv.TWIN_BEAM), (37, mv.CRUNCH), (41, mv.BATON_PASS),
     (46, mv.NASTY_PLOT), (50, mv.PSYCHIC)),
    FARIGIRAF, 0, True, "level-up")

FORRETRESS = Pokemon(
    205, "Forretress", 2, False,
    "", ("Bug", "Steel"),
    75, 75, 100, 40,
    ((0, mv.HEAVY_SLAM), (1, mv.BUG_BITE), (1, mv.MAGNET_RISE),
     (1, mv.PROTECT), (1, mv.SELF_DESTRUCT), (1, mv.TACKLE),
     (1, mv.TOXIC_SPIKES), (1, mv.ZAP_CANNON), (12, mv.TAKE_DOWN),
     (17, mv.RAPID_SPIN), (20, mv.ROLLOUT), (23, mv.CURSE), (28, mv.SPIKES),
     (32, mv.PAYBACK), (36, mv.EXPLOSION), (42, mv.IRON_DEFENSE),
     (46, mv.GYRO_BALL), (50, mv.DOUBLE_EDGE)),
    None, 0, False, "")

PINECO = Pokemon(
    204, "Pineco", 2, False,
    "", ("Bug",),
    50, 50, 62, 15,
    ((1, mv.PROTECT), (1, mv.TACKLE), (6, mv.SELF_DESTRUCT), (9, mv.BUG_BITE),
     (12, mv.TAKE_DOWN), (17, mv.RAPID_SPIN), (20, mv.ROLLOUT), (23, mv.CURSE),
     (28, mv.SPIKES), (31, mv.PAYBACK), (34, mv.EXPLOSION),
     (39, mv.IRON_DEFENSE), (42, mv.GYRO_BALL), (45, mv.DOUBLE_EDGE)),
    FORRETRESS, 31, True, "")


# --- generation 9 ---

DUDUNSPARCE = Pokemon(
    982, "Dudunsparce", 9, False,
    "", ("Normal",),
    125, 92, 77, 55,
    ((1, mv.DEFENSE_CURL), (1, mv.FLAIL), (4, mv.MUD_SLAP), (8, mv.ROLLOUT),
     (12, mv.GLARE), (16, mv.SCREECH), (20, mv.ANCIENT_POWER),
     (24, mv.DRILL_RUN), (28, mv.YAWN), (32, mv.HYPER_DRILL), (36, mv.ROOST),
     (40, mv.DRAGON_RUSH), (44, mv.COIL), (48, mv.DOUBLE_EDGE),
     (52, mv.ENDEAVOR), (56, mv.HURRICANE), (62, mv.BOOMBURST)),
    None, 0, False, "")


# --- generation 2 ---

DUNSPARCE = Pokemon(
    206, "Dunsparce", 2, False,
    "", ("Normal",),
    100, 67, 67, 45,
    ((1, mv.DEFENSE_CURL), (1, mv.FLAIL), (4, mv.MUD_SLAP), (8, mv.ROLLOUT),
     (12, mv.GLARE), (16, mv.SCREECH), (20, mv.ANCIENT_POWER),
     (24, mv.DRILL_RUN), (28, mv.YAWN), (32, mv.HYPER_DRILL), (36, mv.ROOST),
     (40, mv.DRAGON_RUSH), (44, mv.COIL), (48, mv.DOUBLE_EDGE),
     (52, mv.ENDEAVOR)),
    DUDUNSPARCE, 0, True, "level-up")


# --- generation 4 ---

GLISCOR = Pokemon(
    472, "Gliscor", 4, False,
    "", ("Ground", "Flying"),
    75, 70, 100, 95,
    ((1, mv.FIRE_FANG), (1, mv.HARDEN), (1, mv.ICE_FANG), (1, mv.POISON_JAB),
     (1, mv.SAND_ATTACK), (1, mv.THUNDER_FANG), (13, mv.QUICK_ATTACK),
     (16, mv.FURY_CUTTER), (19, mv.KNOCK_OFF), (22, mv.ACROBATICS),
     (27, mv.NIGHT_SLASH), (30, mv.U_TURN), (35, mv.SCREECH),
     (40, mv.X_SCISSOR), (45, mv.CRABHAMMER), (50, mv.SWORDS_DANCE)),
    None, 0, False, "")


# --- generation 2 ---

GLIGAR = Pokemon(
    207, "Gligar", 2, False,
    "", ("Ground", "Flying"),
    65, 55, 85, 85,
    ((1, mv.POISON_STING), (4, mv.SAND_ATTACK), (7, mv.HARDEN),
     (10, mv.KNOCK_OFF), (13, mv.QUICK_ATTACK), (16, mv.FURY_CUTTER),
     (19, mv.POISON_TAIL), (22, mv.ACROBATICS), (27, mv.SLASH),
     (30, mv.U_TURN), (35, mv.SCREECH), (40, mv.X_SCISSOR),
     (45, mv.CRABHAMMER), (50, mv.SWORDS_DANCE)),
    GLISCOR, 0, True, "level-up")

GRANBULL = Pokemon(
    210, "Granbull", 2, False,
    "", ("Fairy",),
    90, 90, 67, 45,
    ((1, mv.CHARM), (1, mv.FIRE_FANG), (1, mv.GROWL), (1, mv.ICE_FANG),
     (1, mv.OUTRAGE), (1, mv.SCARY_FACE), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.THUNDER_FANG), (7, mv.BITE), (13, mv.LICK), (19, mv.HEADBUTT),
     (27, mv.ROAR), (35, mv.LAST_RESORT), (43, mv.PLAY_ROUGH),
     (51, mv.PAYBACK), (59, mv.CRUNCH)),
    None, 0, False, "")

SNUBBULL = Pokemon(
    209, "Snubbull", 2, False,
    "", ("Fairy",),
    60, 60, 45, 30,
    ((1, mv.CHARM), (1, mv.FIRE_FANG), (1, mv.GROWL), (1, mv.ICE_FANG),
     (1, mv.SCARY_FACE), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.THUNDER_FANG), (7, mv.BITE), (13, mv.LICK), (19, mv.HEADBUTT),
     (25, mv.ROAR), (31, mv.LAST_RESORT), (37, mv.PLAY_ROUGH),
     (43, mv.PAYBACK), (49, mv.CRUNCH)),
    GRANBULL, 23, True, "")


# --- generation 8 ---

OVERQWIL = Pokemon(
    904, "Overqwil", 8, False,
    "", ("Dark", "Poison"),
    85, 90, 80, 85,
    ((1, mv.POISON_STING), (1, mv.TACKLE), (4, mv.HARDEN), (8, mv.BITE),
     (12, mv.FELL_STINGER), (16, mv.MINIMIZE), (20, mv.SPIKES), (24, mv.BRINE),
     (28, mv.BARB_BARRAGE), (32, mv.PIN_MISSILE), (36, mv.TOXIC_SPIKES),
     (40, mv.SPIT_UP), (40, mv.STOCKPILE), (44, mv.TOXIC), (48, mv.CRUNCH),
     (52, mv.ACUPRESSURE), (56, mv.DESTINY_BOND)),
    None, 0, False, "")


# --- generation 2 ---

QWILFISH = Pokemon(
    211, "Qwilfish", 2, False,
    "", ("Water", "Poison"),
    65, 75, 70, 85,
    ((1, mv.POISON_STING), (1, mv.TACKLE), (4, mv.HARDEN), (8, mv.WATER_GUN),
     (12, mv.FELL_STINGER), (16, mv.MINIMIZE), (20, mv.SPIKES), (24, mv.BRINE),
     (28, mv.POISON_JAB), (32, mv.PIN_MISSILE), (36, mv.TOXIC_SPIKES),
     (40, mv.SPIT_UP), (40, mv.STOCKPILE), (44, mv.TOXIC), (48, mv.AQUA_TAIL),
     (52, mv.ACUPRESSURE), (56, mv.DESTINY_BOND)),
    OVERQWIL, 0, True, "use-move")

SHUCKLE = Pokemon(
    213, "Shuckle", 2, False,
    "", ("Bug", "Rock"),
    20, 10, 230, 5,
    ((1, mv.WITHDRAW), (1, mv.WRAP), (5, mv.ROLLOUT), (10, mv.STRUGGLE_BUG),
     (15, mv.ROCK_THROW), (20, mv.SAFEGUARD), (25, mv.REST), (30, mv.BUG_BITE),
     (35, mv.GUARD_SPLIT), (35, mv.POWER_SPLIT), (40, mv.ROCK_SLIDE),
     (45, mv.GASTRO_ACID), (50, mv.STICKY_WEB), (55, mv.POWER_TRICK),
     (60, mv.STONE_EDGE), (65, mv.SHELL_SMASH)),
    None, 0, False, "")

HERACROSS = Pokemon(
    214, "Heracross", 2, False,
    "", ("Bug", "Fighting"),
    80, 82, 85, 85,
    ((1, mv.ARM_THRUST), (1, mv.LEER), (1, mv.TACKLE), (5, mv.FURY_ATTACK),
     (10, mv.ENDURE), (15, mv.AERIAL_ACE), (20, mv.HORN_ATTACK),
     (25, mv.COUNTER), (30, mv.BRICK_BREAK), (35, mv.PIN_MISSILE),
     (40, mv.THROAT_CHOP), (45, mv.THRASH), (50, mv.SWORDS_DANCE),
     (55, mv.MEGAHORN), (60, mv.CLOSE_COMBAT)),
    None, 0, False, "")


# --- generation 8 ---

SNEASLER = Pokemon(
    903, "Sneasler", 8, False,
    "", ("Fighting", "Poison"),
    80, 85, 70, 120,
    ((0, mv.DIRE_CLAW), (1, mv.FLING), (1, mv.LEER), (1, mv.ROCK_SMASH),
     (1, mv.SCRATCH), (6, mv.TAUNT), (12, mv.QUICK_ATTACK),
     (18, mv.METAL_CLAW), (24, mv.POISON_JAB), (30, mv.BRICK_BREAK),
     (36, mv.HONE_CLAWS), (42, mv.SLASH), (48, mv.AGILITY), (54, mv.SCREECH),
     (60, mv.CLOSE_COMBAT)),
    None, 0, False, "")


# --- generation 4 ---

WEAVILE = Pokemon(
    461, "Weavile", 4, False,
    "", ("Dark", "Ice"),
    70, 82, 75, 125,
    ((1, mv.AGILITY), (1, mv.ASSURANCE), (1, mv.BEAT_UP), (1, mv.ICE_SHARD),
     (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.SCRATCH), (1, mv.SLASH),
     (1, mv.TAUNT), (18, mv.METAL_CLAW), (24, mv.ICY_WIND),
     (30, mv.FURY_SWIPES), (36, mv.HONE_CLAWS), (42, mv.FLING),
     (48, mv.NASTY_PLOT), (54, mv.SCREECH), (60, mv.NIGHT_SLASH),
     (66, mv.DARK_PULSE)),
    SNEASLER, 0, True, "Use Razor Claw during the day")


# --- generation 2 ---

SNEASEL = Pokemon(
    215, "Sneasel", 2, False,
    "", ("Dark", "Ice"),
    55, 65, 65, 115,
    ((1, mv.LEER), (1, mv.SCRATCH), (6, mv.TAUNT), (12, mv.QUICK_ATTACK),
     (18, mv.METAL_CLAW), (24, mv.ICY_WIND), (30, mv.FURY_SWIPES),
     (36, mv.HONE_CLAWS), (42, mv.BEAT_UP), (48, mv.AGILITY), (54, mv.SCREECH),
     (60, mv.SLASH)),
    WEAVILE, 0, True, "level-up")


# --- generation 8 ---

URSALUNA = Pokemon(
    901, "Ursaluna", 8, False,
    "", ("Ground", "Normal"),
    130, 92, 92, 50,
    ((0, mv.HEADLONG_RUSH), (1, mv.COVET), (1, mv.FAKE_TEARS), (1, mv.LEER),
     (1, mv.LICK), (1, mv.SCRATCH), (8, mv.FURY_SWIPES), (13, mv.PAYBACK),
     (17, mv.SWEET_SCENT), (22, mv.SLASH), (25, mv.PLAY_NICE),
     (29, mv.PLAY_ROUGH), (35, mv.SCARY_FACE), (41, mv.REST), (41, mv.SNORE),
     (48, mv.HIGH_HORSEPOWER), (56, mv.THRASH), (64, mv.HAMMER_ARM)),
    None, 0, False, "")


# --- generation 2 ---

URSARING = Pokemon(
    217, "Ursaring", 2, False,
    "", ("Normal",),
    90, 102, 75, 55,
    ((1, mv.COVET), (1, mv.FAKE_TEARS), (1, mv.LEER), (1, mv.LICK),
     (1, mv.SCRATCH), (8, mv.FURY_SWIPES), (13, mv.PAYBACK),
     (17, mv.SWEET_SCENT), (22, mv.SLASH), (25, mv.PLAY_NICE),
     (29, mv.PLAY_ROUGH), (35, mv.SCARY_FACE), (41, mv.REST), (41, mv.SNORE),
     (48, mv.HIGH_HORSEPOWER), (56, mv.THRASH), (64, mv.HAMMER_ARM)),
    URSALUNA, 0, True, "item:peat-block")

TEDDIURSA = Pokemon(
    216, "Teddiursa", 2, False,
    "", ("Normal",),
    60, 65, 50, 40,
    ((1, mv.BABY_DOLL_EYES), (1, mv.COVET), (1, mv.FLING), (1, mv.LICK),
     (1, mv.SCRATCH), (8, mv.FURY_SWIPES), (13, mv.PAYBACK),
     (17, mv.SWEET_SCENT), (22, mv.SLASH), (25, mv.PLAY_NICE),
     (29, mv.PLAY_ROUGH), (33, mv.CHARM), (37, mv.REST), (37, mv.SNORE),
     (41, mv.THRASH)),
    URSARING, 30, True, "")

MAGCARGO = Pokemon(
    219, "Magcargo", 2, False,
    "", ("Fire", "Rock"),
    60, 70, 100, 30,
    ((0, mv.SHELL_SMASH), (1, mv.EARTH_POWER), (1, mv.EMBER),
     (1, mv.ROCK_THROW), (1, mv.SMOG), (1, mv.YAWN), (13, mv.HARDEN),
     (20, mv.CLEAR_SMOG), (22, mv.ANCIENT_POWER), (27, mv.INCINERATE),
     (29, mv.ROCK_SLIDE), (34, mv.LAVA_PLUME), (36, mv.AMNESIA),
     (43, mv.BODY_SLAM), (47, mv.RECOVER), (54, mv.FLAMETHROWER)),
    None, 0, False, "")

SLUGMA = Pokemon(
    218, "Slugma", 2, False,
    "", ("Fire",),
    40, 55, 40, 20,
    ((1, mv.SMOG), (1, mv.YAWN), (6, mv.EMBER), (8, mv.ROCK_THROW),
     (13, mv.HARDEN), (20, mv.CLEAR_SMOG), (22, mv.ANCIENT_POWER),
     (27, mv.INCINERATE), (29, mv.ROCK_SLIDE), (34, mv.LAVA_PLUME),
     (36, mv.AMNESIA), (41, mv.BODY_SLAM), (43, mv.RECOVER),
     (48, mv.FLAMETHROWER), (50, mv.EARTH_POWER)),
    MAGCARGO, 38, True, "")


# --- generation 4 ---

MAMOSWINE = Pokemon(
    473, "Mamoswine", 4, False,
    "", ("Ice", "Ground"),
    110, 100, 70, 80,
    ((0, mv.DOUBLE_HIT), (1, mv.ANCIENT_POWER), (1, mv.FLAIL),
     (1, mv.ICE_FANG), (1, mv.MUD_SLAP), (1, mv.POWDER_SNOW), (1, mv.TACKLE),
     (15, mv.ICE_SHARD), (20, mv.MIST), (25, mv.ENDURE), (30, mv.ICY_WIND),
     (37, mv.AMNESIA), (44, mv.TAKE_DOWN), (51, mv.EARTHQUAKE),
     (58, mv.BLIZZARD), (65, mv.THRASH)),
    None, 0, False, "")


# --- generation 2 ---

PILOSWINE = Pokemon(
    221, "Piloswine", 2, False,
    "", ("Ice", "Ground"),
    100, 80, 70, 50,
    ((0, mv.ICE_FANG), (1, mv.ANCIENT_POWER), (1, mv.FLAIL), (1, mv.MUD_SLAP),
     (1, mv.POWDER_SNOW), (1, mv.TACKLE), (15, mv.ICE_SHARD), (20, mv.MIST),
     (25, mv.ENDURE), (30, mv.ICY_WIND), (37, mv.AMNESIA), (44, mv.TAKE_DOWN),
     (51, mv.EARTHQUAKE), (58, mv.BLIZZARD), (65, mv.THRASH)),
    MAMOSWINE, 0, True, "level-up")

SWINUB = Pokemon(
    220, "Swinub", 2, False,
    "", ("Ice", "Ground"),
    50, 40, 35, 50,
    ((1, mv.MUD_SLAP), (1, mv.TACKLE), (5, mv.POWDER_SNOW), (10, mv.FLAIL),
     (15, mv.ICE_SHARD), (20, mv.MIST), (25, mv.ENDURE), (30, mv.ICY_WIND),
     (35, mv.AMNESIA), (40, mv.TAKE_DOWN), (45, mv.EARTHQUAKE),
     (50, mv.BLIZZARD)),
    PILOSWINE, 33, True, "")


# --- generation 8 ---

CURSOLA = Pokemon(
    864, "Cursola", 8, False,
    "", ("Ghost",),
    60, 120, 90, 30,
    ((1, mv.ASTONISH), (1, mv.DISABLE), (1, mv.HARDEN), (1, mv.PERISH_SONG),
     (1, mv.TACKLE), (15, mv.SPITE), (20, mv.ANCIENT_POWER), (25, mv.HEX),
     (30, mv.CURSE), (35, mv.STRENGTH_SAP), (40, mv.POWER_GEM),
     (45, mv.NIGHT_SHADE), (50, mv.GRUDGE), (55, mv.MIRROR_COAT)),
    None, 0, False, "")


# --- generation 2 ---

CORSOLA = Pokemon(
    222, "Corsola", 2, False,
    "", ("Water", "Rock"),
    65, 60, 95, 35,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.WATER_GUN), (10, mv.AQUA_RING),
     (15, mv.ENDURE), (20, mv.ANCIENT_POWER), (25, mv.BUBBLE_BEAM),
     (30, mv.FLAIL), (35, mv.LIFE_DEW), (40, mv.POWER_GEM),
     (45, mv.EARTH_POWER), (50, mv.RECOVER), (55, mv.MIRROR_COAT)),
    CURSOLA, 38, True, "")

OCTILLERY = Pokemon(
    224, "Octillery", 2, False,
    "", ("Water",),
    75, 105, 75, 45,
    ((0, mv.OCTAZOOKA), (1, mv.FOCUS_ENERGY), (1, mv.GUNK_SHOT),
     (1, mv.HELPING_HAND), (1, mv.ROCK_BLAST), (1, mv.WATER_GUN),
     (1, mv.WATER_PULSE), (1, mv.WRAP), (12, mv.PSYBEAM), (16, mv.AURORA_BEAM),
     (20, mv.BUBBLE_BEAM), (24, mv.LOCK_ON), (30, mv.BULLET_SEED),
     (36, mv.ICE_BEAM), (42, mv.HYDRO_PUMP), (48, mv.SOAK),
     (54, mv.HYPER_BEAM)),
    None, 0, False, "")

REMORAID = Pokemon(
    223, "Remoraid", 2, False,
    "", ("Water",),
    35, 65, 35, 65,
    ((1, mv.HELPING_HAND), (1, mv.WATER_GUN), (4, mv.WATER_PULSE),
     (8, mv.FOCUS_ENERGY), (12, mv.PSYBEAM), (16, mv.AURORA_BEAM),
     (20, mv.BUBBLE_BEAM), (24, mv.LOCK_ON), (28, mv.BULLET_SEED),
     (32, mv.ICE_BEAM), (36, mv.HYDRO_PUMP), (40, mv.SOAK),
     (44, mv.HYPER_BEAM)),
    OCTILLERY, 25, True, "")

DELIBIRD = Pokemon(
    225, "Delibird", 2, False,
    "", ("Ice", "Flying"),
    45, 60, 45, 75,
    ((1, mv.PRESENT), (25, mv.DRILL_PECK)),
    None, 0, False, "")

MANTINE = Pokemon(
    226, "Mantine", 2, False,
    "", ("Water", "Flying"),
    85, 60, 105, 70,
    ((1, mv.BULLET_SEED), (1, mv.PSYBEAM), (1, mv.ROOST), (1, mv.SUPERSONIC),
     (1, mv.TACKLE), (1, mv.WATER_GUN), (1, mv.WING_ATTACK),
     (12, mv.WATER_PULSE), (16, mv.WIDE_GUARD), (20, mv.AGILITY),
     (24, mv.BUBBLE_BEAM), (28, mv.HEADBUTT), (32, mv.AIR_SLASH),
     (36, mv.AQUA_RING), (40, mv.BOUNCE), (44, mv.TAKE_DOWN),
     (48, mv.HYDRO_PUMP)),
    None, 0, False, "")

SKARMORY = Pokemon(
    227, "Skarmory", 2, False,
    "", ("Steel", "Flying"),
    65, 60, 105, 70,
    ((1, mv.LEER), (1, mv.PECK), (4, mv.SAND_ATTACK), (8, mv.FURY_ATTACK),
     (12, mv.METAL_CLAW), (16, mv.AGILITY), (20, mv.WING_ATTACK),
     (24, mv.SLASH), (28, mv.STEEL_WING), (32, mv.PAYBACK),
     (36, mv.DRILL_PECK), (40, mv.METAL_SOUND), (44, mv.SPIKES),
     (48, mv.IRON_DEFENSE), (52, mv.BRAVE_BIRD)),
    None, 0, False, "")

HOUNDOOM = Pokemon(
    229, "Houndoom", 2, False,
    "", ("Dark", "Fire"),
    75, 100, 65, 95,
    ((1, mv.EMBER), (1, mv.HOWL), (1, mv.LEER), (1, mv.NASTY_PLOT),
     (1, mv.SMOG), (1, mv.THUNDER_FANG), (13, mv.ROAR), (16, mv.BITE),
     (20, mv.INCINERATE), (26, mv.BEAT_UP), (30, mv.FIRE_FANG),
     (35, mv.TORMENT), (41, mv.COMEUPPANCE), (45, mv.FOUL_PLAY),
     (50, mv.FLAMETHROWER), (56, mv.CRUNCH), (62, mv.INFERNO)),
    None, 0, False, "")

HOUNDOUR = Pokemon(
    228, "Houndour", 2, False,
    "", ("Dark", "Fire"),
    45, 70, 40, 65,
    ((1, mv.EMBER), (1, mv.LEER), (4, mv.HOWL), (8, mv.SMOG), (13, mv.ROAR),
     (16, mv.BITE), (20, mv.INCINERATE), (25, mv.BEAT_UP), (28, mv.FIRE_FANG),
     (32, mv.TORMENT), (37, mv.COMEUPPANCE), (40, mv.FOUL_PLAY),
     (44, mv.FLAMETHROWER), (49, mv.CRUNCH), (52, mv.NASTY_PLOT),
     (56, mv.INFERNO)),
    HOUNDOOM, 24, True, "")

DONPHAN = Pokemon(
    232, "Donphan", 2, False,
    "", ("Ground",),
    90, 90, 90, 50,
    ((0, mv.FURY_ATTACK), (1, mv.BULLDOZE), (1, mv.DEFENSE_CURL),
     (1, mv.FIRE_FANG), (1, mv.GROWL), (1, mv.HORN_ATTACK),
     (1, mv.THUNDER_FANG), (6, mv.RAPID_SPIN), (10, mv.ROLLOUT),
     (15, mv.ASSURANCE), (19, mv.KNOCK_OFF), (24, mv.SLAM),
     (30, mv.STOMPING_TANTRUM), (37, mv.SCARY_FACE), (43, mv.EARTHQUAKE),
     (50, mv.GIGA_IMPACT)),
    None, 0, False, "")

PHANPY = Pokemon(
    231, "Phanpy", 2, False,
    "", ("Ground",),
    90, 50, 50, 40,
    ((1, mv.DEFENSE_CURL), (1, mv.GROWL), (1, mv.TACKLE), (6, mv.FLAIL),
     (10, mv.ROLLOUT), (15, mv.BULLDOZE), (19, mv.ENDURE), (24, mv.SLAM),
     (28, mv.TAKE_DOWN), (33, mv.CHARM), (37, mv.LAST_RESORT),
     (42, mv.DOUBLE_EDGE)),
    DONPHAN, 25, True, "")


# --- generation 8 ---

WYRDEER = Pokemon(
    899, "Wyrdeer", 8, False,
    "", ("Normal", "Psychic"),
    103, 105, 73, 65,
    ((0, mv.PSYSHIELD_BASH), (1, mv.TACKLE), (3, mv.LEER), (7, mv.ASTONISH),
     (10, mv.HYPNOSIS), (13, mv.STOMP), (16, mv.SAND_ATTACK),
     (21, mv.TAKE_DOWN), (23, mv.CONFUSE_RAY), (27, mv.CALM_MIND),
     (32, mv.ROLE_PLAY), (37, mv.ZEN_HEADBUTT), (49, mv.IMPRISON),
     (55, mv.DOUBLE_EDGE), (62, mv.MEGAHORN)),
    None, 0, False, "")


# --- generation 2 ---

STANTLER = Pokemon(
    234, "Stantler", 2, False,
    "", ("Normal",),
    73, 90, 63, 85,
    ((1, mv.TACKLE), (3, mv.LEER), (7, mv.ASTONISH), (10, mv.HYPNOSIS),
     (13, mv.STOMP), (16, mv.SAND_ATTACK), (21, mv.TAKE_DOWN),
     (23, mv.CONFUSE_RAY), (27, mv.CALM_MIND), (32, mv.ROLE_PLAY),
     (37, mv.ZEN_HEADBUTT), (49, mv.IMPRISON), (55, mv.DOUBLE_EDGE)),
    WYRDEER, 0, True, "agile-style-move")

SMEARGLE = Pokemon(
    235, "Smeargle", 2, False,
    "", ("Normal",),
    55, 20, 40, 75,
    ((1, mv.SKETCH),),
    None, 0, False, "")

TYROGUE = Pokemon(
    236, "Tyrogue", 2, False,
    "", ("Fighting",),
    35, 35, 35, 35,
    ((1, mv.FAKE_OUT), (1, mv.FOCUS_ENERGY), (1, mv.HELPING_HAND),
     (1, mv.TACKLE)),
    HITMONLEE, 20, True, "")

SMOOCHUM = Pokemon(
    238, "Smoochum", 2, False,
    "", ("Ice", "Psychic"),
    45, 57, 40, 65,
    ((1, mv.LICK), (1, mv.POUND), (4, mv.POWDER_SNOW), (8, mv.COPYCAT),
     (12, mv.CONFUSION), (16, mv.COVET), (20, mv.SING), (24, mv.FAKE_TEARS),
     (28, mv.ICE_PUNCH), (32, mv.PSYCHIC), (36, mv.SWEET_KISS),
     (40, mv.MEAN_LOOK), (44, mv.PERISH_SONG), (48, mv.BLIZZARD)),
    JYNX, 30, True, "")

ELEKID = Pokemon(
    239, "Elekid", 2, False,
    "", ("Electric",),
    45, 64, 46, 95,
    ((1, mv.LEER), (1, mv.QUICK_ATTACK), (4, mv.THUNDER_SHOCK), (8, mv.CHARGE),
     (12, mv.SWIFT), (16, mv.SHOCK_WAVE), (20, mv.THUNDER_WAVE),
     (24, mv.SCREECH), (28, mv.THUNDER_PUNCH), (32, mv.DISCHARGE),
     (36, mv.LOW_KICK), (40, mv.THUNDERBOLT), (44, mv.LIGHT_SCREEN),
     (48, mv.THUNDER)),
    ELECTABUZZ, 30, True, "")

MAGBY = Pokemon(
    240, "Magby", 2, False,
    "", ("Fire",),
    45, 72, 46, 83,
    ((1, mv.LEER), (1, mv.SMOG), (4, mv.EMBER), (8, mv.SMOKESCREEN),
     (12, mv.CLEAR_SMOG), (16, mv.FLAME_WHEEL), (20, mv.CONFUSE_RAY),
     (24, mv.SCARY_FACE), (28, mv.FIRE_PUNCH), (32, mv.LAVA_PLUME),
     (36, mv.LOW_KICK), (40, mv.FLAMETHROWER), (44, mv.SUNNY_DAY),
     (48, mv.FIRE_BLAST)),
    MAGMAR, 30, True, "")

MILTANK = Pokemon(
    241, "Miltank", 2, False,
    "", ("Normal",),
    95, 60, 87, 100,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.ROLLOUT), (10, mv.DEFENSE_CURL),
     (15, mv.STOMP), (20, mv.HEAL_BELL), (25, mv.HEADBUTT),
     (30, mv.ZEN_HEADBUTT), (35, mv.MILK_DRINK), (40, mv.BODY_SLAM),
     (45, mv.PLAY_ROUGH), (50, mv.CHARM), (55, mv.HIGH_HORSEPOWER)),
    None, 0, False, "")

RAIKOU = Pokemon(
    243, "Raikou", 2, False,
    "", ("Electric",),
    90, 100, 87, 115,
    ((1, mv.CHARGE), (1, mv.EXTREME_SPEED), (1, mv.LEER), (1, mv.QUICK_ATTACK),
     (1, mv.THUNDER_SHOCK), (6, mv.SPARK), (12, mv.BITE), (18, mv.CALM_MIND),
     (24, mv.ROAR), (30, mv.THUNDER_FANG), (36, mv.HOWL), (42, mv.CRUNCH),
     (48, mv.EXTRASENSORY), (54, mv.DISCHARGE), (60, mv.REFLECT),
     (66, mv.RAIN_DANCE), (72, mv.THUNDER), (78, mv.ZAP_CANNON)),
    None, 0, False, "")

ENTEI = Pokemon(
    244, "Entei", 2, False,
    "", ("Fire",),
    115, 102, 80, 100,
    ((1, mv.EMBER), (1, mv.LEER), (1, mv.SMOKESCREEN), (1, mv.STOMP),
     (6, mv.FLAME_WHEEL), (12, mv.BITE), (18, mv.CALM_MIND), (24, mv.ROAR),
     (30, mv.FIRE_FANG), (36, mv.SCARY_FACE), (42, mv.CRUNCH),
     (48, mv.EXTRASENSORY), (54, mv.LAVA_PLUME), (60, mv.SWAGGER),
     (66, mv.SUNNY_DAY), (72, mv.FIRE_BLAST), (78, mv.ERUPTION)),
    None, 0, False, "")

SUICUNE = Pokemon(
    245, "Suicune", 2, False,
    "", ("Water",),
    100, 82, 115, 85,
    ((1, mv.GUST), (1, mv.LEER), (1, mv.MIST), (1, mv.WATER_GUN),
     (6, mv.WATER_PULSE), (12, mv.BITE), (18, mv.CALM_MIND), (24, mv.ROAR),
     (30, mv.ICE_FANG), (36, mv.TAILWIND), (42, mv.CRUNCH),
     (48, mv.EXTRASENSORY), (54, mv.SURF), (60, mv.MIRROR_COAT),
     (66, mv.RAIN_DANCE), (72, mv.HYDRO_PUMP), (78, mv.BLIZZARD)),
    None, 0, False, "")

TYRANITAR = Pokemon(
    248, "Tyranitar", 2, False,
    "", ("Rock", "Dark"),
    100, 114, 105, 61,
    ((1, mv.DARK_PULSE), (1, mv.FIRE_FANG), (1, mv.ICE_FANG),
     (1, mv.IRON_DEFENSE), (1, mv.LEER), (1, mv.PAYBACK), (1, mv.ROCK_THROW),
     (1, mv.TACKLE), (1, mv.THUNDER_FANG), (9, mv.BITE), (12, mv.SCARY_FACE),
     (15, mv.ROCK_SLIDE), (18, mv.STOMPING_TANTRUM), (21, mv.SCREECH),
     (24, mv.SMACK_DOWN), (27, mv.CRUNCH), (33, mv.EARTHQUAKE),
     (37, mv.STONE_EDGE), (42, mv.THRASH), (47, mv.SANDSTORM),
     (52, mv.HYPER_BEAM), (59, mv.GIGA_IMPACT)),
    None, 0, False, "")

PUPITAR = Pokemon(
    247, "Pupitar", 2, False,
    "", ("Rock", "Ground"),
    70, 74, 70, 51,
    ((0, mv.IRON_DEFENSE), (1, mv.LEER), (1, mv.PAYBACK), (1, mv.ROCK_THROW),
     (1, mv.TACKLE), (9, mv.BITE), (12, mv.SCARY_FACE), (15, mv.ROCK_SLIDE),
     (18, mv.STOMPING_TANTRUM), (21, mv.SCREECH), (24, mv.SMACK_DOWN),
     (27, mv.CRUNCH), (33, mv.EARTHQUAKE), (37, mv.STONE_EDGE),
     (42, mv.THRASH), (47, mv.SANDSTORM), (52, mv.HYPER_BEAM)),
    TYRANITAR, 55, True, "")

LARVITAR = Pokemon(
    246, "Larvitar", 2, False,
    "", ("Rock", "Ground"),
    50, 54, 50, 41,
    ((1, mv.LEER), (1, mv.TACKLE), (3, mv.ROCK_THROW), (6, mv.PAYBACK),
     (9, mv.BITE), (12, mv.SCARY_FACE), (15, mv.ROCK_SLIDE),
     (18, mv.STOMPING_TANTRUM), (21, mv.SCREECH), (24, mv.SMACK_DOWN),
     (27, mv.CRUNCH), (31, mv.EARTHQUAKE), (33, mv.STONE_EDGE),
     (36, mv.THRASH), (39, mv.SANDSTORM), (42, mv.HYPER_BEAM)),
    PUPITAR, 30, True, "")

LUGIA = Pokemon(
    249, "Lugia", 2, False,
    "", ("Psychic", "Flying"),
    106, 90, 142, 110,
    ((1, mv.ANCIENT_POWER), (1, mv.GUST), (1, mv.WEATHER_BALL),
     (1, mv.WHIRLWIND), (9, mv.MIST), (18, mv.SAFEGUARD), (27, mv.CALM_MIND),
     (36, mv.EXTRASENSORY), (45, mv.RECOVER), (54, mv.AEROBLAST),
     (63, mv.RAIN_DANCE), (72, mv.HYDRO_PUMP), (81, mv.FUTURE_SIGHT),
     (90, mv.SKY_ATTACK)),
    None, 0, False, "")

HO_OH = Pokemon(
    250, "Ho-Oh", 2, False,
    "", ("Fire", "Flying"),
    106, 120, 122, 90,
    ((1, mv.ANCIENT_POWER), (1, mv.GUST), (1, mv.WEATHER_BALL),
     (1, mv.WHIRLWIND), (9, mv.LIFE_DEW), (18, mv.SAFEGUARD),
     (27, mv.CALM_MIND), (36, mv.EXTRASENSORY), (45, mv.RECOVER),
     (54, mv.SACRED_FIRE), (63, mv.SUNNY_DAY), (72, mv.FIRE_BLAST),
     (81, mv.FUTURE_SIGHT), (90, mv.SKY_ATTACK), (99, mv.OVERHEAT)),
    None, 0, False, "")

CELEBI = Pokemon(
    251, "Celebi", 2, False,
    "", ("Psychic", "Grass"),
    100, 100, 100, 100,
    ((1, mv.CONFUSION), (1, mv.HEAL_BELL), (10, mv.MAGICAL_LEAF),
     (20, mv.BATON_PASS), (30, mv.ANCIENT_POWER), (40, mv.LIFE_DEW),
     (50, mv.LEECH_SEED), (60, mv.RECOVER), (70, mv.FUTURE_SIGHT),
     (80, mv.HEALING_WISH), (90, mv.LEAF_STORM), (100, mv.PERISH_SONG)),
    None, 0, False, "")


# --- generation 3 ---

SCEPTILE = Pokemon(
    254, "Sceptile", 3, True,
    "Flora", ("Grass",),
    70, 95, 75, 120,
    ((0, mv.LEAF_BLADE), (1, mv.LEAFAGE), (1, mv.LEER), (1, mv.POUND),
     (1, mv.QUICK_ATTACK), (5, mv.MEGA_DRAIN), (12, mv.DETECT),
     (15, mv.QUICK_GUARD), (20, mv.ASSURANCE), (25, mv.GIGA_DRAIN),
     (30, mv.SLAM), (35, mv.DOUBLE_TEAM), (42, mv.SCREECH), (49, mv.ENDEAVOR),
     (56, mv.LEAF_STORM)),
    None, 0, False, "")

GROVYLE = Pokemon(
    253, "Grovyle", 3, True,
    "Flora", ("Grass",),
    50, 75, 55, 95,
    ((1, mv.LEAFAGE), (1, mv.LEER), (1, mv.POUND), (1, mv.QUICK_ATTACK),
     (9, mv.MEGA_DRAIN), (12, mv.DETECT), (15, mv.QUICK_GUARD),
     (20, mv.ASSURANCE), (25, mv.GIGA_DRAIN), (30, mv.SLAM),
     (35, mv.DOUBLE_TEAM), (40, mv.LEAF_BLADE), (45, mv.SCREECH),
     (50, mv.ENDEAVOR), (55, mv.LEAF_STORM)),
    SCEPTILE, 36, True, "")

TREECKO = Pokemon(
    252, "Treecko", 3, True,
    "Flora", ("Grass",),
    40, 55, 45, 70,
    ((1, mv.LEER), (1, mv.POUND), (3, mv.LEAFAGE), (6, mv.QUICK_ATTACK),
     (9, mv.MEGA_DRAIN), (12, mv.DETECT), (15, mv.QUICK_GUARD),
     (18, mv.ASSURANCE), (21, mv.GIGA_DRAIN), (24, mv.SLAM),
     (27, mv.DOUBLE_TEAM), (30, mv.ENERGY_BALL), (33, mv.SCREECH),
     (36, mv.ENDEAVOR), (39, mv.LEAF_STORM)),
    GROVYLE, 16, True, "")

BLAZIKEN = Pokemon(
    257, "Blaziken", 3, True,
    "Flame", ("Fire", "Fighting"),
    80, 115, 70, 80,
    ((0, mv.BLAZE_KICK), (1, mv.DOUBLE_KICK), (1, mv.GROWL),
     (1, mv.QUICK_ATTACK), (1, mv.SCRATCH), (9, mv.FLAME_CHARGE),
     (12, mv.DETECT), (15, mv.SAND_ATTACK), (20, mv.AERIAL_ACE),
     (25, mv.SLASH), (30, mv.BOUNCE), (35, mv.FOCUS_ENERGY), (42, mv.BULK_UP),
     (49, mv.REVERSAL), (56, mv.FLARE_BLITZ), (63, mv.BRAVE_BIRD)),
    None, 0, False, "")

COMBUSKEN = Pokemon(
    256, "Combusken", 3, True,
    "Flame", ("Fire", "Fighting"),
    60, 85, 60, 55,
    ((0, mv.DOUBLE_KICK), (1, mv.EMBER), (1, mv.GROWL), (1, mv.QUICK_ATTACK),
     (1, mv.SCRATCH), (9, mv.FLAME_CHARGE), (12, mv.DETECT),
     (15, mv.SAND_ATTACK), (20, mv.AERIAL_ACE), (25, mv.SLASH),
     (30, mv.BOUNCE), (35, mv.FOCUS_ENERGY), (40, mv.BLAZE_KICK),
     (45, mv.BULK_UP), (50, mv.REVERSAL), (55, mv.FLARE_BLITZ)),
    BLAZIKEN, 36, True, "")

TORCHIC = Pokemon(
    255, "Torchic", 3, True,
    "Flame", ("Fire",),
    45, 65, 45, 45,
    ((1, mv.GROWL), (1, mv.SCRATCH), (3, mv.EMBER), (6, mv.QUICK_ATTACK),
     (9, mv.FLAME_CHARGE), (12, mv.DETECT), (15, mv.SAND_ATTACK),
     (18, mv.AERIAL_ACE), (21, mv.SLASH), (24, mv.BOUNCE),
     (27, mv.FOCUS_ENERGY), (30, mv.FLAMETHROWER), (33, mv.FEATHER_DANCE),
     (36, mv.REVERSAL), (39, mv.FLARE_BLITZ)),
    COMBUSKEN, 16, True, "")

SWAMPERT = Pokemon(
    260, "Swampert", 3, True,
    "Aqua", ("Water", "Ground"),
    100, 97, 90, 60,
    ((1, mv.GROWL), (1, mv.MUD_SHOT), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (9, mv.ROCK_THROW), (12, mv.PROTECT), (15, mv.SUPERSONIC),
     (20, mv.WATER_PULSE), (25, mv.ROCK_SLIDE), (30, mv.TAKE_DOWN),
     (35, mv.AMNESIA), (42, mv.MUDDY_WATER), (49, mv.SCREECH),
     (56, mv.ENDEAVOR), (63, mv.HYDRO_PUMP)),
    None, 0, False, "")

MARSHTOMP = Pokemon(
    259, "Marshtomp", 3, True,
    "Aqua", ("Water", "Ground"),
    70, 72, 70, 50,
    ((0, mv.MUD_SHOT), (1, mv.GROWL), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (9, mv.ROCK_THROW), (12, mv.PROTECT), (15, mv.SUPERSONIC),
     (20, mv.WATER_PULSE), (25, mv.ROCK_SLIDE), (30, mv.TAKE_DOWN),
     (35, mv.AMNESIA), (40, mv.MUDDY_WATER), (45, mv.SCREECH),
     (50, mv.ENDEAVOR), (55, mv.HYDRO_PUMP)),
    SWAMPERT, 36, True, "")

MUDKIP = Pokemon(
    258, "Mudkip", 3, True,
    "Aqua", ("Water",),
    50, 60, 50, 40,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.WATER_GUN), (6, mv.ROCK_SMASH),
     (9, mv.ROCK_THROW), (12, mv.PROTECT), (15, mv.SUPERSONIC),
     (18, mv.WATER_PULSE), (21, mv.ROCK_SLIDE), (24, mv.TAKE_DOWN),
     (27, mv.AMNESIA), (30, mv.SURF), (33, mv.SCREECH), (36, mv.ENDEAVOR),
     (39, mv.HYDRO_PUMP)),
    MARSHTOMP, 16, True, "")

MIGHTYENA = Pokemon(
    262, "Mightyena", 3, False,
    "", ("Dark",),
    70, 75, 65, 70,
    ((0, mv.SNARL), (1, mv.BITE), (1, mv.CRUNCH), (1, mv.FIRE_FANG),
     (1, mv.ICE_FANG), (1, mv.SAND_ATTACK), (1, mv.TACKLE), (1, mv.THIEF),
     (1, mv.THUNDER_FANG), (13, mv.HOWL), (13, mv.LEER), (16, mv.ROAR),
     (20, mv.SWAGGER), (24, mv.ASSURANCE), (28, mv.SCARY_FACE), (36, mv.TAUNT),
     (44, mv.YAWN), (48, mv.TAKE_DOWN), (52, mv.SUCKER_PUNCH),
     (56, mv.PLAY_ROUGH)),
    None, 0, False, "")

POOCHYENA = Pokemon(
    261, "Poochyena", 3, False,
    "", ("Dark",),
    35, 42, 32, 35,
    ((1, mv.TACKLE), (4, mv.HOWL), (7, mv.SAND_ATTACK), (10, mv.BITE),
     (13, mv.LEER), (16, mv.ROAR), (19, mv.SWAGGER), (22, mv.ASSURANCE),
     (25, mv.SCARY_FACE), (28, mv.TAUNT), (31, mv.CRUNCH), (34, mv.YAWN),
     (36, mv.TAKE_DOWN), (40, mv.SUCKER_PUNCH), (44, mv.PLAY_ROUGH)),
    MIGHTYENA, 18, True, "")


# --- generation 8 ---

OBSTAGOON = Pokemon(
    862, "Obstagoon", 8, False,
    "", ("Dark", "Normal"),
    93, 75, 91, 95,
    ((1, mv.BABY_DOLL_EYES), (1, mv.CROSS_CHOP), (1, mv.LEER), (1, mv.LICK),
     (1, mv.NIGHT_SLASH), (1, mv.OBSTRUCT), (1, mv.PIN_MISSILE),
     (1, mv.SAND_ATTACK), (1, mv.SUBMISSION), (1, mv.SWITCHEROO),
     (1, mv.TACKLE), (9, mv.SNARL), (12, mv.HEADBUTT), (15, mv.HONE_CLAWS),
     (18, mv.FURY_SWIPES), (23, mv.REST), (28, mv.TAKE_DOWN),
     (35, mv.SCARY_FACE), (42, mv.COUNTER), (49, mv.TAUNT),
     (56, mv.DOUBLE_EDGE)),
    None, 0, False, "")


# --- generation 3 ---

LINOONE = Pokemon(
    264, "Linoone", 3, False,
    "", ("Normal",),
    78, 60, 61, 100,
    ((1, mv.BABY_DOLL_EYES), (1, mv.GROWL), (1, mv.PIN_MISSILE),
     (1, mv.SAND_ATTACK), (1, mv.SLASH), (1, mv.SWITCHEROO), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (9, mv.COVET), (12, mv.HEADBUTT), (15, mv.HONE_CLAWS),
     (18, mv.FURY_SWIPES), (23, mv.REST), (28, mv.TAKE_DOWN), (33, mv.FLING),
     (38, mv.FLAIL), (43, mv.BELLY_DRUM), (48, mv.DOUBLE_EDGE)),
    OBSTAGOON, 35, True, "")

ZIGZAGOON = Pokemon(
    263, "Zigzagoon", 3, False,
    "", ("Normal",),
    38, 30, 41, 60,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.SAND_ATTACK), (6, mv.TAIL_WHIP),
     (9, mv.COVET), (12, mv.HEADBUTT), (15, mv.BABY_DOLL_EYES),
     (18, mv.PIN_MISSILE), (21, mv.REST), (24, mv.TAKE_DOWN), (27, mv.FLING),
     (30, mv.FLAIL), (33, mv.BELLY_DRUM), (36, mv.DOUBLE_EDGE)),
    LINOONE, 20, True, "")

BEAUTIFLY = Pokemon(
    267, "Beautifly", 3, False,
    "", ("Bug", "Flying"),
    60, 85, 50, 65,
    ((0, mv.GUST), (12, mv.ABSORB), (15, mv.STUN_SPORE), (17, mv.MORNING_SUN),
     (20, mv.AIR_CUTTER), (22, mv.MEGA_DRAIN), (25, mv.SILVER_WIND),
     (27, mv.ATTRACT), (30, mv.WHIRLWIND), (32, mv.GIGA_DRAIN),
     (35, mv.BUG_BUZZ), (37, mv.RAGE), (40, mv.QUIVER_DANCE)),
    None, 0, False, "")

SILCOON = Pokemon(
    266, "Silcoon", 3, False,
    "", ("Bug",),
    50, 30, 40, 15,
    ((1, mv.HARDEN),),
    BEAUTIFLY, 10, True, "")

WURMPLE = Pokemon(
    265, "Wurmple", 3, False,
    "", ("Bug",),
    45, 32, 32, 20,
    ((1, mv.STRING_SHOT), (1, mv.TACKLE), (5, mv.POISON_STING),
     (15, mv.BUG_BITE)),
    SILCOON, 7, True, "")

CASCOON = Pokemon(
    268, "Cascoon", 3, False,
    "", ("Bug",),
    50, 30, 40, 15,
    ((1, mv.HARDEN),),
    None, 10, False, "")

DUSTOX = Pokemon(
    269, "Dustox", 3, False,
    "", ("Bug", "Poison"),
    60, 50, 80, 65,
    ((0, mv.GUST), (12, mv.CONFUSION), (15, mv.POISON_POWDER),
     (17, mv.MOONLIGHT), (20, mv.VENOSHOCK), (22, mv.PSYBEAM),
     (25, mv.SILVER_WIND), (27, mv.LIGHT_SCREEN), (30, mv.WHIRLWIND),
     (32, mv.TOXIC), (35, mv.BUG_BUZZ), (37, mv.PROTECT),
     (40, mv.QUIVER_DANCE)),
    None, 0, False, "")

LUDICOLO = Pokemon(
    272, "Ludicolo", 3, False,
    "", ("Water", "Grass"),
    80, 80, 85, 70,
    ((1, mv.BUBBLE_BEAM), (1, mv.FAKE_OUT), (1, mv.RAIN_DANCE)),
    None, 0, False, "")

LOMBRE = Pokemon(
    271, "Lombre", 3, False,
    "", ("Water", "Grass"),
    60, 55, 60, 50,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.FAKE_OUT), (1, mv.FLAIL),
     (1, mv.GROWL), (1, mv.KNOCK_OFF), (1, mv.TEETER_DANCE), (1, mv.WATER_GUN),
     (9, mv.MIST), (12, mv.MEGA_DRAIN), (18, mv.FURY_SWIPES),
     (24, mv.BUBBLE_BEAM), (30, mv.LEECH_SEED), (36, mv.GIGA_DRAIN),
     (50, mv.ZEN_HEADBUTT), (57, mv.ENERGY_BALL), (64, mv.HYDRO_PUMP)),
    LUDICOLO, 0, True, "item:water-stone")

LOTAD = Pokemon(
    270, "Lotad", 3, False,
    "", ("Water", "Grass"),
    40, 35, 40, 30,
    ((1, mv.ASTONISH), (1, mv.GROWL), (3, mv.ABSORB), (6, mv.WATER_GUN),
     (9, mv.MIST), (12, mv.MEGA_DRAIN), (16, mv.FLAIL), (20, mv.BUBBLE_BEAM),
     (24, mv.LEECH_SEED), (28, mv.GIGA_DRAIN), (33, mv.RAIN_DANCE),
     (38, mv.ZEN_HEADBUTT), (43, mv.ENERGY_BALL)),
    LOMBRE, 14, True, "")

SHIFTRY = Pokemon(
    275, "Shiftry", 3, False,
    "", ("Grass", "Dark"),
    90, 95, 60, 80,
    ((0, mv.LEAF_BLADE), (1, mv.AIR_CUTTER), (1, mv.HURRICANE),
     (1, mv.PAYBACK), (1, mv.SUNNY_DAY)),
    None, 0, False, "")

NUZLEAF = Pokemon(
    274, "Nuzleaf", 3, False,
    "", ("Grass", "Dark"),
    70, 65, 40, 60,
    ((0, mv.RAZOR_LEAF), (1, mv.ABSORB), (1, mv.AIR_CUTTER), (1, mv.ASTONISH),
     (1, mv.EXPLOSION), (1, mv.FAKE_OUT), (1, mv.HARDEN), (1, mv.SWAGGER),
     (1, mv.TACKLE), (1, mv.TORMENT), (9, mv.GROWTH), (12, mv.ROLLOUT),
     (18, mv.MEGA_DRAIN), (24, mv.PAYBACK), (30, mv.SYNTHESIS),
     (36, mv.SUNNY_DAY), (43, mv.EXTRASENSORY), (50, mv.SUCKER_PUNCH),
     (57, mv.LEAF_BLADE)),
    SHIFTRY, 0, True, "item:leaf-stone")

SEEDOT = Pokemon(
    273, "Seedot", 3, False,
    "", ("Grass",),
    40, 35, 40, 30,
    ((1, mv.HARDEN), (1, mv.TACKLE), (3, mv.ABSORB), (6, mv.ASTONISH),
     (9, mv.GROWTH), (12, mv.ROLLOUT), (15, mv.MEGA_DRAIN), (18, mv.PAYBACK),
     (21, mv.HEADBUTT), (24, mv.SUNNY_DAY), (27, mv.SYNTHESIS),
     (30, mv.SUCKER_PUNCH), (33, mv.EXPLOSION)),
    NUZLEAF, 14, True, "")

SWELLOW = Pokemon(
    277, "Swellow", 3, False,
    "", ("Normal", "Flying"),
    60, 80, 55, 125,
    ((1, mv.FOCUS_ENERGY), (1, mv.GROWL), (1, mv.PECK), (1, mv.PLUCK),
     (9, mv.QUICK_ATTACK), (13, mv.WING_ATTACK), (17, mv.DOUBLE_TEAM),
     (21, mv.AERIAL_ACE), (27, mv.QUICK_GUARD), (33, mv.AGILITY),
     (39, mv.AIR_SLASH), (45, mv.ENDEAVOR), (51, mv.BRAVE_BIRD),
     (57, mv.REVERSAL)),
    None, 0, False, "")

TAILLOW = Pokemon(
    276, "Taillow", 3, False,
    "", ("Normal", "Flying"),
    40, 42, 30, 85,
    ((1, mv.GROWL), (1, mv.PECK), (5, mv.FOCUS_ENERGY), (9, mv.QUICK_ATTACK),
     (13, mv.WING_ATTACK), (17, mv.DOUBLE_TEAM), (21, mv.AERIAL_ACE),
     (25, mv.QUICK_GUARD), (29, mv.AGILITY), (33, mv.AIR_SLASH),
     (37, mv.ENDEAVOR), (41, mv.BRAVE_BIRD), (45, mv.REVERSAL)),
    SWELLOW, 22, True, "")

PELIPPER = Pokemon(
    279, "Pelipper", 3, False,
    "", ("Water", "Flying"),
    60, 72, 85, 65,
    ((1, mv.AGILITY), (1, mv.AIR_SLASH), (1, mv.GROWL), (1, mv.PROTECT),
     (1, mv.QUICK_ATTACK), (1, mv.SOAK), (1, mv.SUPERSONIC), (1, mv.TAILWIND),
     (1, mv.WATER_GUN), (15, mv.WING_ATTACK), (20, mv.WATER_PULSE),
     (28, mv.SPIT_UP), (28, mv.STOCKPILE), (28, mv.SWALLOW), (34, mv.FLING),
     (41, mv.MIST), (48, mv.ROOST), (55, mv.HURRICANE), (62, mv.HYDRO_PUMP)),
    None, 0, False, "")

WINGULL = Pokemon(
    278, "Wingull", 3, False,
    "", ("Water", "Flying"),
    40, 42, 30, 85,
    ((1, mv.GROWL), (1, mv.WATER_GUN), (5, mv.QUICK_ATTACK),
     (10, mv.SUPERSONIC), (15, mv.WING_ATTACK), (20, mv.WATER_PULSE),
     (26, mv.AGILITY), (30, mv.AIR_SLASH), (35, mv.MIST), (40, mv.ROOST),
     (45, mv.HURRICANE)),
    PELIPPER, 25, True, "")


# --- generation 4 ---

GALLADE = Pokemon(
    475, "Gallade", 4, False,
    "", ("Psychic", "Fighting"),
    68, 95, 90, 80,
    ((0, mv.SLASH), (1, mv.AQUA_CUTTER), (1, mv.CALM_MIND), (1, mv.CHARM),
     (1, mv.CONFUSION), (1, mv.DISARMING_VOICE), (1, mv.DOUBLE_TEAM),
     (1, mv.DRAINING_KISS), (1, mv.DREAM_EATER), (1, mv.FURY_CUTTER),
     (1, mv.FUTURE_SIGHT), (1, mv.GROWL), (1, mv.HYPNOSIS), (1, mv.IMPRISON),
     (1, mv.LEAF_BLADE), (1, mv.LEER), (1, mv.LIFE_DEW), (1, mv.NIGHT_SLASH),
     (1, mv.PSYBEAM), (1, mv.PSYCHIC), (1, mv.SACRED_SWORD),
     (9, mv.HELPING_HAND), (12, mv.FEINT), (15, mv.TELEPORT),
     (18, mv.AERIAL_ACE), (23, mv.FALSE_SWIPE), (28, mv.PROTECT),
     (35, mv.SWORDS_DANCE), (42, mv.PSYCHO_CUT), (49, mv.HEAL_PULSE),
     (56, mv.QUICK_GUARD), (56, mv.WIDE_GUARD), (63, mv.CLOSE_COMBAT)),
    None, 0, False, "")


# --- generation 3 ---

GARDEVOIR = Pokemon(
    282, "Gardevoir", 3, False,
    "", ("Psychic", "Fairy"),
    68, 95, 90, 80,
    ((0, mv.DAZZLING_GLEAM), (1, mv.CHARM), (1, mv.CONFUSION),
     (1, mv.DISARMING_VOICE), (1, mv.DOUBLE_TEAM), (1, mv.GROWL),
     (1, mv.HEALING_WISH), (1, mv.HEAL_PULSE), (1, mv.MISTY_TERRAIN),
     (1, mv.MYSTICAL_FIRE), (9, mv.HYPNOSIS), (12, mv.DRAINING_KISS),
     (15, mv.TELEPORT), (18, mv.PSYBEAM), (23, mv.LIFE_DEW), (28, mv.WISH),
     (35, mv.CALM_MIND), (42, mv.PSYCHIC), (49, mv.MOONBLAST),
     (56, mv.DREAM_EATER), (63, mv.FUTURE_SIGHT)),
    GALLADE, 0, True, "On Male Pokémon, use Dawn Stone")

KIRLIA = Pokemon(
    281, "Kirlia", 3, False,
    "", ("Psychic", "Fairy"),
    38, 50, 45, 50,
    ((1, mv.CONFUSION), (1, mv.DISARMING_VOICE), (1, mv.DOUBLE_TEAM),
     (1, mv.GROWL), (9, mv.HYPNOSIS), (12, mv.DRAINING_KISS),
     (15, mv.TELEPORT), (18, mv.PSYBEAM), (23, mv.LIFE_DEW), (28, mv.CHARM),
     (33, mv.CALM_MIND), (38, mv.PSYCHIC), (43, mv.HEAL_PULSE),
     (48, mv.DREAM_EATER), (53, mv.FUTURE_SIGHT)),
    GARDEVOIR, 0, True, "item:dawn-stone")

RALTS = Pokemon(
    280, "Ralts", 3, False,
    "", ("Psychic", "Fairy"),
    28, 35, 30, 40,
    ((1, mv.DISARMING_VOICE), (1, mv.GROWL), (3, mv.DOUBLE_TEAM),
     (6, mv.CONFUSION), (9, mv.HYPNOSIS), (12, mv.DRAINING_KISS),
     (15, mv.TELEPORT), (18, mv.PSYBEAM), (21, mv.LIFE_DEW), (24, mv.CHARM),
     (27, mv.CALM_MIND), (30, mv.PSYCHIC), (33, mv.HEAL_PULSE),
     (36, mv.DREAM_EATER), (39, mv.FUTURE_SIGHT)),
    KIRLIA, 20, True, "")

MASQUERAIN = Pokemon(
    284, "Masquerain", 3, False,
    "", ("Bug", "Flying"),
    70, 80, 72, 80,
    ((1, mv.QUICK_ATTACK), (1, mv.SOAK), (1, mv.SWEET_SCENT),
     (1, mv.WATER_GUN), (1, mv.WHIRLWIND), (17, mv.GUST), (22, mv.AIR_CUTTER),
     (22, mv.SCARY_FACE), (26, mv.STUN_SPORE), (32, mv.AIR_SLASH),
     (38, mv.GIGA_DRAIN), (44, mv.BUG_BUZZ), (52, mv.QUIVER_DANCE)),
    None, 0, False, "")

SURSKIT = Pokemon(
    283, "Surskit", 3, False,
    "", ("Bug", "Water"),
    40, 40, 42, 65,
    ((1, mv.WATER_GUN), (6, mv.QUICK_ATTACK), (9, mv.SWEET_SCENT),
     (14, mv.SOAK), (17, mv.BUBBLE_BEAM), (22, mv.AGILITY), (25, mv.HAZE),
     (25, mv.MIST), (35, mv.BATON_PASS), (38, mv.STICKY_WEB)),
    MASQUERAIN, 22, True, "")

BRELOOM = Pokemon(
    286, "Breloom", 3, False,
    "", ("Grass", "Fighting"),
    60, 95, 70, 70,
    ((0, mv.MACH_PUNCH), (1, mv.ABSORB), (1, mv.GROWTH), (1, mv.LEECH_SEED),
     (1, mv.POISON_POWDER), (1, mv.STUN_SPORE), (1, mv.TACKLE), (1, mv.TOXIC),
     (12, mv.MEGA_DRAIN), (15, mv.HEADBUTT), (19, mv.FEINT), (22, mv.COUNTER),
     (28, mv.FORCE_PALM), (33, mv.WORRY_SEED), (39, mv.BRICK_BREAK),
     (44, mv.SEED_BOMB), (50, mv.DYNAMIC_PUNCH), (55, mv.FOCUS_PUNCH)),
    None, 0, False, "")

SHROOMISH = Pokemon(
    285, "Shroomish", 3, False,
    "", ("Grass",),
    60, 40, 60, 35,
    ((1, mv.ABSORB), (1, mv.TACKLE), (5, mv.STUN_SPORE), (8, mv.LEECH_SEED),
     (12, mv.MEGA_DRAIN), (15, mv.HEADBUTT), (19, mv.POISON_POWDER),
     (26, mv.GIGA_DRAIN), (29, mv.GROWTH), (33, mv.TOXIC), (36, mv.SEED_BOMB),
     (40, mv.SPORE)),
    BRELOOM, 23, True, "")

SLAKING = Pokemon(
    289, "Slaking", 3, False,
    "", ("Normal",),
    150, 127, 82, 100,
    ((0, mv.SWAGGER), (1, mv.ENCORE), (1, mv.SCRATCH), (1, mv.SLACK_OFF),
     (1, mv.SUCKER_PUNCH), (1, mv.YAWN), (17, mv.AMNESIA), (23, mv.COVET),
     (27, mv.THROAT_CHOP), (33, mv.COUNTER), (39, mv.FLAIL), (45, mv.FLING),
     (52, mv.MEGA_KICK), (63, mv.HAMMER_ARM)),
    None, 0, False, "")

VIGOROTH = Pokemon(
    288, "Vigoroth", 3, False,
    "", ("Normal",),
    80, 67, 67, 90,
    ((1, mv.ENCORE), (1, mv.FOCUS_ENERGY), (1, mv.SCRATCH), (1, mv.UPROAR),
     (14, mv.FURY_SWIPES), (17, mv.ENDURE), (23, mv.SLASH),
     (27, mv.THROAT_CHOP), (33, mv.COUNTER), (37, mv.FOCUS_PUNCH),
     (43, mv.REVERSAL)),
    SLAKING, 36, True, "")

SLAKOTH = Pokemon(
    287, "Slakoth", 3, False,
    "", ("Normal",),
    60, 47, 47, 30,
    ((1, mv.SCRATCH), (1, mv.YAWN), (6, mv.ENCORE), (9, mv.SLACK_OFF),
     (14, mv.HEADBUTT), (17, mv.AMNESIA), (22, mv.COVET), (25, mv.THROAT_CHOP),
     (30, mv.COUNTER), (33, mv.FLAIL), (38, mv.PLAY_ROUGH)),
    VIGOROTH, 18, True, "")

SHEDINJA = Pokemon(
    292, "Shedinja", 3, False,
    "", ("Bug", "Ghost"),
    1, 60, 37, 40,
    ((1, mv.DIG), (1, mv.FALSE_SWIPE), (1, mv.GRUDGE), (1, mv.HARDEN),
     (1, mv.METAL_CLAW), (1, mv.MUD_SLAP), (1, mv.SAND_ATTACK),
     (1, mv.SCRATCH), (1, mv.SHADOW_CLAW), (15, mv.CONFUSE_RAY),
     (23, mv.ABSORB), (29, mv.SHADOW_SNEAK), (36, mv.FURY_SWIPES),
     (43, mv.MIND_READER), (50, mv.SHADOW_BALL), (57, mv.SPITE),
     (64, mv.PHANTOM_FORCE)),
    None, 0, False, "")

NINJASK = Pokemon(
    291, "Ninjask", 3, False,
    "", ("Bug", "Flying"),
    61, 70, 47, 160,
    ((0, mv.DOUBLE_TEAM), (0, mv.FURY_CUTTER), (1, mv.AERIAL_ACE),
     (1, mv.BATON_PASS), (1, mv.DIG), (1, mv.FALSE_SWIPE), (1, mv.HARDEN),
     (1, mv.METAL_CLAW), (1, mv.MUD_SLAP), (1, mv.SAND_ATTACK),
     (1, mv.SCRATCH), (1, mv.SCREECH), (15, mv.AGILITY), (23, mv.ABSORB),
     (29, mv.BUG_BITE), (36, mv.FURY_SWIPES), (43, mv.MIND_READER),
     (50, mv.SLASH), (57, mv.SWORDS_DANCE), (64, mv.X_SCISSOR)),
    SHEDINJA, 0, True, "Empty Slot in PartyLevel")

NINCADA = Pokemon(
    290, "Nincada", 3, False,
    "", ("Bug", "Ground"),
    31, 37, 60, 40,
    ((1, mv.SAND_ATTACK), (1, mv.SCRATCH), (5, mv.HARDEN),
     (10, mv.FALSE_SWIPE), (15, mv.MUD_SLAP), (21, mv.ABSORB),
     (25, mv.METAL_CLAW), (30, mv.FURY_SWIPES), (35, mv.MIND_READER),
     (40, mv.DIG)),
    NINJASK, 0, True, "shed")

EXPLOUD = Pokemon(
    295, "Exploud", 3, False,
    "", ("Normal",),
    104, 91, 68, 68,
    ((0, mv.CRUNCH), (1, mv.ASTONISH), (1, mv.BITE), (1, mv.ECHOED_VOICE),
     (1, mv.FIRE_FANG), (1, mv.HOWL), (1, mv.ICE_FANG), (1, mv.POUND),
     (1, mv.THUNDER_FANG), (15, mv.REST), (15, mv.SLEEP_TALK), (23, mv.STOMP),
     (29, mv.ROAR), (36, mv.SUPERSONIC), (45, mv.UPROAR), (54, mv.SCREECH),
     (63, mv.HYPER_VOICE), (72, mv.BOOMBURST), (81, mv.HYPER_BEAM)),
    None, 0, False, "")

LOUDRED = Pokemon(
    294, "Loudred", 3, False,
    "", ("Normal",),
    84, 71, 43, 48,
    ((1, mv.ASTONISH), (1, mv.BITE), (1, mv.ECHOED_VOICE), (1, mv.HOWL),
     (1, mv.POUND), (15, mv.REST), (15, mv.SLEEP_TALK), (23, mv.STOMP),
     (29, mv.ROAR), (36, mv.SUPERSONIC), (43, mv.UPROAR), (50, mv.SCREECH),
     (57, mv.HYPER_VOICE)),
    EXPLOUD, 40, True, "")

WHISMUR = Pokemon(
    293, "Whismur", 3, False,
    "", ("Normal",),
    64, 51, 23, 28,
    ((1, mv.ASTONISH), (1, mv.POUND), (5, mv.ECHOED_VOICE), (10, mv.HOWL),
     (15, mv.REST), (15, mv.SLEEP_TALK), (21, mv.STOMP), (25, mv.ROAR),
     (30, mv.SUPERSONIC), (35, mv.UPROAR), (40, mv.SCREECH),
     (45, mv.HYPER_VOICE)),
    LOUDRED, 20, True, "")

HARIYAMA = Pokemon(
    297, "Hariyama", 3, False,
    "", ("Fighting",),
    144, 80, 60, 50,
    ((1, mv.ARM_THRUST), (1, mv.BRINE), (1, mv.FOCUS_ENERGY),
     (1, mv.SAND_ATTACK), (1, mv.TACKLE), (10, mv.FAKE_OUT),
     (13, mv.FORCE_PALM), (16, mv.WHIRLWIND), (19, mv.KNOCK_OFF),
     (22, mv.BULK_UP), (26, mv.BELLY_DRUM), (30, mv.DETECT),
     (34, mv.SEISMIC_TOSS), (38, mv.FOCUS_PUNCH), (42, mv.ENDURE),
     (46, mv.CLOSE_COMBAT), (50, mv.REVERSAL), (54, mv.HEAVY_SLAM),
     (60, mv.HEADLONG_RUSH)),
    None, 0, False, "")

MAKUHITA = Pokemon(
    296, "Makuhita", 3, False,
    "", ("Fighting",),
    72, 40, 30, 25,
    ((1, mv.FOCUS_ENERGY), (1, mv.TACKLE), (4, mv.SAND_ATTACK),
     (7, mv.ARM_THRUST), (10, mv.FAKE_OUT), (13, mv.FORCE_PALM),
     (16, mv.WHIRLWIND), (19, mv.KNOCK_OFF), (22, mv.BULK_UP),
     (25, mv.BELLY_DRUM), (28, mv.DETECT), (31, mv.SEISMIC_TOSS),
     (34, mv.FOCUS_PUNCH), (37, mv.ENDURE), (40, mv.CLOSE_COMBAT),
     (43, mv.REVERSAL), (46, mv.HEAVY_SLAM)),
    HARIYAMA, 24, True, "")

AZURILL = Pokemon(
    298, "Azurill", 3, False,
    "", ("Normal", "Fairy"),
    50, 20, 40, 20,
    ((1, mv.SPLASH), (1, mv.TAIL_WHIP), (1, mv.WATER_GUN),
     (3, mv.HELPING_HAND), (6, mv.BUBBLE_BEAM), (9, mv.CHARM), (12, mv.SLAM),
     (15, mv.BOUNCE)),
    MARILL, 0, True, "happiness")


# --- generation 4 ---

PROBOPASS = Pokemon(
    476, "Probopass", 4, False,
    "", ("Rock", "Steel"),
    60, 65, 147, 40,
    ((0, mv.TRI_ATTACK), (1, mv.BLOCK), (1, mv.GRAVITY), (1, mv.IRON_DEFENSE),
     (1, mv.MAGNETIC_FLUX), (1, mv.MAGNET_RISE), (1, mv.TACKLE),
     (1, mv.WIDE_GUARD), (13, mv.THUNDER_WAVE), (16, mv.REST), (19, mv.SPARK),
     (22, mv.ROCK_SLIDE), (25, mv.POWER_GEM), (28, mv.ROCK_BLAST),
     (31, mv.DISCHARGE), (34, mv.SANDSTORM), (37, mv.EARTH_POWER),
     (40, mv.STONE_EDGE), (43, mv.LOCK_ON), (43, mv.ZAP_CANNON)),
    None, 0, False, "")


# --- generation 3 ---

NOSEPASS = Pokemon(
    299, "Nosepass", 3, False,
    "", ("Rock",),
    30, 45, 112, 30,
    ((1, mv.TACKLE), (4, mv.HARDEN), (7, mv.BLOCK), (10, mv.ROCK_THROW),
     (13, mv.THUNDER_WAVE), (16, mv.REST), (19, mv.SPARK), (22, mv.ROCK_SLIDE),
     (25, mv.POWER_GEM), (28, mv.ROCK_BLAST), (31, mv.DISCHARGE),
     (34, mv.SANDSTORM), (37, mv.EARTH_POWER), (40, mv.STONE_EDGE),
     (43, mv.LOCK_ON), (43, mv.ZAP_CANNON)),
    PROBOPASS, 0, True, "level-up")

DELCATTY = Pokemon(
    301, "Delcatty", 3, False,
    "", ("Normal",),
    70, 60, 60, 90,
    ((1, mv.ATTRACT), (1, mv.DOUBLE_SLAP), (1, mv.FAKE_OUT), (1, mv.SING)),
    None, 0, False, "")

SKITTY = Pokemon(
    300, "Skitty", 3, False,
    "", ("Normal",),
    50, 40, 40, 50,
    ((1, mv.FAKE_OUT), (1, mv.GROWL), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (4, mv.FORESIGHT), (7, mv.SING), (10, mv.ATTRACT),
     (13, mv.DISARMING_VOICE), (16, mv.DOUBLE_SLAP), (19, mv.COPYCAT),
     (22, mv.FEINT_ATTACK), (25, mv.CHARM), (28, mv.WAKE_UP_SLAP),
     (31, mv.ASSIST), (34, mv.COVET), (37, mv.HEAL_BELL), (40, mv.DOUBLE_EDGE),
     (43, mv.CAPTIVATE), (46, mv.PLAY_ROUGH)),
    DELCATTY, 0, True, "item:moon-stone")

SABLEYE = Pokemon(
    302, "Sableye", 3, False,
    "", ("Dark", "Ghost"),
    50, 70, 70, 50,
    ((1, mv.LEER), (1, mv.SCRATCH), (3, mv.ASTONISH), (9, mv.SHADOW_SNEAK),
     (12, mv.FAKE_OUT), (15, mv.DISABLE), (18, mv.DETECT),
     (21, mv.NIGHT_SHADE), (24, mv.FURY_SWIPES), (27, mv.KNOCK_OFF),
     (30, mv.QUASH), (33, mv.SHADOW_CLAW), (36, mv.MEAN_LOOK),
     (39, mv.POWER_GEM), (42, mv.ZEN_HEADBUTT), (45, mv.SHADOW_BALL),
     (48, mv.FOUL_PLAY)),
    None, 0, False, "")

MAWILE = Pokemon(
    303, "Mawile", 3, False,
    "", ("Steel", "Fairy"),
    50, 70, 70, 50,
    ((1, mv.ASTONISH), (1, mv.GROWL), (4, mv.FAIRY_WIND), (8, mv.BATON_PASS),
     (12, mv.BITE), (16, mv.SPIT_UP), (16, mv.STOCKPILE), (16, mv.SWALLOW),
     (20, mv.SUCKER_PUNCH), (24, mv.IRON_DEFENSE), (28, mv.CRUNCH),
     (32, mv.SWEET_SCENT), (36, mv.IRON_HEAD), (40, mv.TAUNT),
     (44, mv.FAKE_TEARS), (48, mv.PLAY_ROUGH)),
    None, 0, False, "")

AGGRON = Pokemon(
    306, "Aggron", 3, False,
    "", ("Steel", "Rock"),
    70, 85, 120, 50,
    ((1, mv.HARDEN), (1, mv.METAL_CLAW), (1, mv.ROCK_TOMB), (1, mv.TACKLE),
     (12, mv.ROAR), (16, mv.HEADBUTT), (20, mv.PROTECT), (24, mv.ROCK_SLIDE),
     (28, mv.IRON_HEAD), (35, mv.METAL_SOUND), (40, mv.TAKE_DOWN),
     (48, mv.AUTOTOMIZE), (56, mv.IRON_TAIL), (64, mv.IRON_DEFENSE),
     (72, mv.HEAVY_SLAM), (80, mv.DOUBLE_EDGE), (88, mv.METAL_BURST)),
    None, 0, False, "")

LAIRON = Pokemon(
    305, "Lairon", 3, False,
    "", ("Steel", "Rock"),
    60, 70, 95, 40,
    ((1, mv.HARDEN), (1, mv.METAL_CLAW), (1, mv.ROCK_TOMB), (1, mv.TACKLE),
     (12, mv.ROAR), (16, mv.HEADBUTT), (20, mv.PROTECT), (24, mv.ROCK_SLIDE),
     (28, mv.IRON_HEAD), (35, mv.METAL_SOUND), (40, mv.TAKE_DOWN),
     (46, mv.AUTOTOMIZE), (52, mv.IRON_TAIL), (58, mv.IRON_DEFENSE),
     (64, mv.HEAVY_SLAM), (70, mv.DOUBLE_EDGE), (76, mv.METAL_BURST)),
    AGGRON, 42, True, "")

ARON = Pokemon(
    304, "Aron", 3, False,
    "", ("Steel", "Rock"),
    50, 55, 70, 30,
    ((1, mv.HARDEN), (1, mv.TACKLE), (4, mv.METAL_CLAW), (8, mv.ROCK_TOMB),
     (12, mv.ROAR), (16, mv.HEADBUTT), (20, mv.PROTECT), (24, mv.ROCK_SLIDE),
     (28, mv.IRON_HEAD), (33, mv.METAL_SOUND), (36, mv.TAKE_DOWN),
     (40, mv.AUTOTOMIZE), (44, mv.IRON_TAIL), (48, mv.IRON_DEFENSE),
     (52, mv.HEAVY_SLAM), (56, mv.DOUBLE_EDGE), (60, mv.METAL_BURST)),
    LAIRON, 32, True, "")

MEDICHAM = Pokemon(
    308, "Medicham", 3, False,
    "", ("Fighting", "Psychic"),
    60, 60, 75, 80,
    ((1, mv.CONFUSION), (1, mv.DETECT), (1, mv.FIRE_PUNCH), (1, mv.ICE_PUNCH),
     (1, mv.THUNDER_PUNCH), (1, mv.WORK_UP), (12, mv.ENDURE), (15, mv.FEINT),
     (17, mv.FORCE_PALM), (20, mv.PSYBEAM), (23, mv.CALM_MIND),
     (25, mv.ZEN_HEADBUTT), (28, mv.HIGH_JUMP_KICK), (31, mv.PSYCH_UP),
     (33, mv.ACUPRESSURE), (36, mv.POWER_TRICK), (47, mv.RECOVER),
     (53, mv.AXE_KICK), (53, mv.COUNTER)),
    None, 0, False, "")

MEDITITE = Pokemon(
    307, "Meditite", 3, False,
    "", ("Fighting", "Psychic"),
    30, 40, 55, 60,
    ((1, mv.CONFUSION), (1, mv.WORK_UP), (9, mv.DETECT), (12, mv.ENDURE),
     (15, mv.FEINT), (17, mv.FORCE_PALM), (20, mv.PSYBEAM), (23, mv.CALM_MIND),
     (25, mv.ZEN_HEADBUTT), (28, mv.HIGH_JUMP_KICK), (31, mv.PSYCH_UP),
     (33, mv.ACUPRESSURE), (36, mv.POWER_TRICK), (39, mv.REVERSAL),
     (41, mv.RECOVER), (44, mv.COUNTER)),
    MEDICHAM, 37, True, "")

MANECTRIC = Pokemon(
    310, "Manectric", 3, False,
    "", ("Electric",),
    70, 90, 60, 105,
    ((1, mv.FIRE_FANG), (1, mv.HOWL), (1, mv.LEER), (1, mv.TACKLE),
     (1, mv.THUNDER_WAVE), (12, mv.QUICK_ATTACK), (16, mv.SHOCK_WAVE),
     (20, mv.BITE), (24, mv.THUNDER_FANG), (30, mv.ROAR), (36, mv.DISCHARGE),
     (42, mv.CHARGE), (48, mv.WILD_CHARGE), (54, mv.THUNDER),
     (60, mv.ELECTRIC_TERRAIN)),
    None, 0, False, "")

ELECTRIKE = Pokemon(
    309, "Electrike", 3, False,
    "", ("Electric",),
    40, 55, 40, 65,
    ((1, mv.TACKLE), (1, mv.THUNDER_WAVE), (4, mv.LEER), (8, mv.HOWL),
     (12, mv.QUICK_ATTACK), (16, mv.SHOCK_WAVE), (20, mv.BITE),
     (24, mv.THUNDER_FANG), (28, mv.ROAR), (32, mv.DISCHARGE), (36, mv.CHARGE),
     (40, mv.WILD_CHARGE), (44, mv.THUNDER)),
    MANECTRIC, 26, True, "")

PLUSLE = Pokemon(
    311, "Plusle", 3, False,
    "", ("Electric",),
    60, 67, 57, 95,
    ((1, mv.GROWL), (1, mv.PLAY_NICE), (1, mv.QUICK_ATTACK),
     (1, mv.THUNDER_WAVE), (4, mv.HELPING_HAND), (7, mv.SPARK),
     (10, mv.ENCORE), (13, mv.SWITCHEROO), (16, mv.SWIFT),
     (19, mv.ELECTRO_BALL), (22, mv.COPYCAT), (26, mv.CHARGE),
     (31, mv.DISCHARGE), (34, mv.BATON_PASS), (37, mv.AGILITY),
     (40, mv.LAST_RESORT), (43, mv.THUNDER), (46, mv.NASTY_PLOT),
     (49, mv.ENTRAINMENT)),
    None, 0, False, "")

MINUN = Pokemon(
    312, "Minun", 3, False,
    "", ("Electric",),
    60, 57, 67, 95,
    ((1, mv.GROWL), (1, mv.PLAY_NICE), (1, mv.QUICK_ATTACK),
     (1, mv.THUNDER_WAVE), (4, mv.HELPING_HAND), (7, mv.SPARK),
     (10, mv.ENCORE), (13, mv.SWITCHEROO), (16, mv.SWIFT),
     (19, mv.ELECTRO_BALL), (22, mv.COPYCAT), (26, mv.CHARGE),
     (31, mv.DISCHARGE), (34, mv.BATON_PASS), (37, mv.AGILITY),
     (40, mv.LAST_RESORT), (43, mv.THUNDER), (46, mv.NASTY_PLOT),
     (49, mv.ENTRAINMENT)),
    None, 0, False, "")

VOLBEAT = Pokemon(
    313, "Volbeat", 3, False,
    "", ("Bug",),
    65, 60, 80, 85,
    ((1, mv.TACKLE), (5, mv.DOUBLE_TEAM), (8, mv.CONFUSE_RAY),
     (12, mv.QUICK_ATTACK), (15, mv.STRUGGLE_BUG), (19, mv.MOONLIGHT),
     (22, mv.TAIL_GLOW), (26, mv.PROTECT), (29, mv.ZEN_HEADBUTT),
     (33, mv.HELPING_HAND), (36, mv.BUG_BUZZ), (40, mv.PLAY_ROUGH),
     (43, mv.DOUBLE_EDGE), (47, mv.INFESTATION)),
    None, 0, False, "")

ILLUMISE = Pokemon(
    314, "Illumise", 3, False,
    "", ("Bug",),
    65, 60, 80, 85,
    ((1, mv.PLAY_NICE), (1, mv.TACKLE), (5, mv.SWEET_SCENT), (9, mv.CHARM),
     (12, mv.QUICK_ATTACK), (15, mv.STRUGGLE_BUG), (19, mv.MOONLIGHT),
     (22, mv.WISH), (26, mv.ENCORE), (29, mv.FLATTER), (33, mv.ZEN_HEADBUTT),
     (36, mv.HELPING_HAND), (40, mv.BUG_BUZZ), (43, mv.PLAY_ROUGH),
     (47, mv.INFESTATION)),
    None, 0, False, "")


# --- generation 4 ---

ROSERADE = Pokemon(
    407, "Roserade", 4, False,
    "", ("Grass", "Poison"),
    60, 97, 85, 90,
    ((1, mv.ABSORB), (1, mv.AROMATHERAPY), (1, mv.GIGA_DRAIN),
     (1, mv.GRASSY_TERRAIN), (1, mv.GROWTH), (1, mv.INGRAIN),
     (1, mv.LEECH_SEED), (1, mv.MAGICAL_LEAF), (1, mv.MEGA_DRAIN),
     (1, mv.PETAL_BLIZZARD), (1, mv.PETAL_DANCE), (1, mv.POISON_STING),
     (1, mv.STUN_SPORE), (1, mv.SWEET_SCENT), (1, mv.SYNTHESIS), (1, mv.TOXIC),
     (1, mv.TOXIC_SPIKES), (1, mv.VENOM_DRENCH), (1, mv.WORRY_SEED)),
    None, 0, False, "")


# --- generation 3 ---

ROSELIA = Pokemon(
    315, "Roselia", 3, False,
    "", ("Grass", "Poison"),
    50, 80, 62, 65,
    ((0, mv.POISON_STING), (1, mv.ABSORB), (1, mv.GROWTH), (1, mv.STUN_SPORE),
     (1, mv.WORRY_SEED), (5, mv.MEGA_DRAIN), (10, mv.LEECH_SEED),
     (15, mv.MAGICAL_LEAF), (20, mv.TOXIC_SPIKES), (25, mv.SWEET_SCENT),
     (30, mv.GIGA_DRAIN), (35, mv.SYNTHESIS), (40, mv.TOXIC),
     (45, mv.PETAL_BLIZZARD), (50, mv.AROMATHERAPY), (55, mv.INGRAIN),
     (60, mv.PETAL_DANCE)),
    ROSERADE, 0, True, "item:shiny-stone")

SWALOT = Pokemon(
    317, "Swalot", 3, False,
    "", ("Poison",),
    100, 73, 83, 55,
    ((0, mv.BODY_SLAM), (1, mv.GUNK_SHOT), (1, mv.POISON_GAS), (1, mv.POUND),
     (1, mv.SLUDGE), (1, mv.YAWN), (12, mv.AMNESIA), (17, mv.ACID_SPRAY),
     (20, mv.ENCORE), (25, mv.TOXIC), (30, mv.SPIT_UP), (30, mv.STOCKPILE),
     (30, mv.SWALLOW), (37, mv.SLUDGE_BOMB), (42, mv.GASTRO_ACID),
     (49, mv.BELCH)),
    None, 0, False, "")

GULPIN = Pokemon(
    316, "Gulpin", 3, False,
    "", ("Poison",),
    70, 43, 53, 40,
    ((1, mv.POUND), (5, mv.YAWN), (8, mv.POISON_GAS), (10, mv.SLUDGE),
     (12, mv.AMNESIA), (17, mv.ACID_SPRAY), (20, mv.ENCORE), (25, mv.TOXIC),
     (28, mv.SPIT_UP), (28, mv.STOCKPILE), (28, mv.SWALLOW),
     (33, mv.SLUDGE_BOMB), (36, mv.GASTRO_ACID), (41, mv.BELCH),
     (44, mv.PAIN_SPLIT), (49, mv.GUNK_SHOT)),
    SWALOT, 26, True, "")

SHARPEDO = Pokemon(
    319, "Sharpedo", 3, False,
    "", ("Water", "Dark"),
    70, 107, 40, 95,
    ((0, mv.SLASH), (1, mv.AQUA_JET), (1, mv.FOCUS_ENERGY), (1, mv.LEER),
     (1, mv.NIGHT_SLASH), (1, mv.POISON_FANG), (12, mv.SCARY_FACE),
     (16, mv.BITE), (20, mv.ICE_FANG), (24, mv.SCREECH), (28, mv.SWAGGER),
     (34, mv.CRUNCH), (40, mv.AGILITY), (46, mv.LIQUIDATION),
     (52, mv.TAKE_DOWN)),
    None, 0, False, "")

CARVANHA = Pokemon(
    318, "Carvanha", 3, False,
    "", ("Water", "Dark"),
    45, 77, 20, 65,
    ((1, mv.AQUA_JET), (1, mv.LEER), (4, mv.POISON_FANG), (8, mv.FOCUS_ENERGY),
     (12, mv.SCARY_FACE), (16, mv.BITE), (20, mv.ICE_FANG), (24, mv.SCREECH),
     (28, mv.SWAGGER), (32, mv.CRUNCH), (36, mv.AGILITY), (40, mv.LIQUIDATION),
     (44, mv.TAKE_DOWN)),
    SHARPEDO, 30, True, "")

WAILORD = Pokemon(
    321, "Wailord", 3, False,
    "", ("Water",),
    170, 90, 45, 60,
    ((1, mv.ASTONISH), (1, mv.GROWL), (1, mv.NOBLE_ROAR), (1, mv.SOAK),
     (1, mv.SPLASH), (1, mv.WATER_GUN), (15, mv.MIST), (18, mv.WATER_PULSE),
     (21, mv.HEAVY_SLAM), (24, mv.BRINE), (27, mv.WHIRLPOOL), (30, mv.DIVE),
     (33, mv.BOUNCE), (36, mv.BODY_SLAM), (39, mv.REST), (44, mv.AMNESIA),
     (49, mv.HYDRO_PUMP), (54, mv.WATER_SPOUT)),
    None, 0, False, "")

WAILMER = Pokemon(
    320, "Wailmer", 3, False,
    "", ("Water",),
    130, 70, 35, 60,
    ((1, mv.SPLASH), (3, mv.GROWL), (6, mv.ASTONISH), (12, mv.WATER_GUN),
     (15, mv.MIST), (18, mv.WATER_PULSE), (21, mv.HEAVY_SLAM), (24, mv.BRINE),
     (27, mv.WHIRLPOOL), (30, mv.DIVE), (33, mv.BOUNCE), (36, mv.BODY_SLAM),
     (39, mv.REST), (42, mv.AMNESIA), (45, mv.HYDRO_PUMP),
     (48, mv.WATER_SPOUT)),
    WAILORD, 40, True, "")

CAMERUPT = Pokemon(
    323, "Camerupt", 3, False,
    "", ("Fire", "Ground"),
    70, 102, 72, 40,
    ((0, mv.ROCK_SLIDE), (1, mv.EMBER), (1, mv.ERUPTION), (1, mv.FISSURE),
     (1, mv.FOCUS_ENERGY), (1, mv.GROWL), (1, mv.TACKLE), (12, mv.BULLDOZE),
     (15, mv.INCINERATE), (19, mv.AMNESIA), (22, mv.LAVA_PLUME),
     (26, mv.EARTH_POWER), (29, mv.CURSE), (31, mv.TAKE_DOWN), (39, mv.YAWN),
     (46, mv.EARTHQUAKE)),
    None, 0, False, "")

NUMEL = Pokemon(
    322, "Numel", 3, False,
    "", ("Fire", "Ground"),
    60, 62, 42, 35,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.EMBER), (8, mv.FOCUS_ENERGY),
     (12, mv.BULLDOZE), (15, mv.INCINERATE), (19, mv.AMNESIA),
     (22, mv.LAVA_PLUME), (26, mv.EARTH_POWER), (29, mv.CURSE),
     (31, mv.TAKE_DOWN), (40, mv.EARTHQUAKE), (43, mv.FLAMETHROWER),
     (47, mv.DOUBLE_EDGE)),
    CAMERUPT, 33, True, "")

TORKOAL = Pokemon(
    324, "Torkoal", 3, False,
    "", ("Fire",),
    70, 85, 105, 20,
    ((1, mv.EMBER), (1, mv.SMOG), (4, mv.WITHDRAW), (8, mv.RAPID_SPIN),
     (12, mv.SMOKESCREEN), (16, mv.CLEAR_SMOG), (20, mv.FLAME_WHEEL),
     (24, mv.PROTECT), (28, mv.LAVA_PLUME), (32, mv.BODY_SLAM),
     (36, mv.IRON_DEFENSE), (40, mv.FLAMETHROWER), (44, mv.CURSE),
     (48, mv.HEAT_WAVE), (52, mv.AMNESIA), (56, mv.INFERNO),
     (60, mv.SHELL_SMASH), (64, mv.ERUPTION)),
    None, 0, False, "")

GRUMPIG = Pokemon(
    326, "Grumpig", 3, False,
    "", ("Psychic",),
    80, 67, 87, 80,
    ((0, mv.TEETER_DANCE), (1, mv.BELCH), (1, mv.CONFUSION), (1, mv.PSYBEAM),
     (1, mv.SPLASH), (18, mv.PSYCH_UP), (22, mv.CONFUSE_RAY),
     (26, mv.ZEN_HEADBUTT), (29, mv.POWER_GEM), (35, mv.REST), (35, mv.SNORE),
     (42, mv.PSYSHOCK), (46, mv.PAYBACK), (52, mv.PSYCHIC), (60, mv.BOUNCE)),
    None, 0, False, "")

SPOINK = Pokemon(
    325, "Spoink", 3, False,
    "", ("Psychic",),
    60, 47, 57, 60,
    ((1, mv.SPLASH), (7, mv.CONFUSION), (10, mv.GROWL), (14, mv.PSYBEAM),
     (18, mv.PSYCH_UP), (22, mv.CONFUSE_RAY), (29, mv.POWER_GEM),
     (29, mv.REST), (33, mv.SNORE), (38, mv.PSYSHOCK), (40, mv.PAYBACK),
     (44, mv.PSYCHIC), (50, mv.BOUNCE)),
    GRUMPIG, 32, True, "")

SPINDA = Pokemon(
    327, "Spinda", 3, False,
    "", ("Normal",),
    60, 60, 60, 60,
    ((1, mv.TACKLE), (5, mv.COPYCAT), (10, mv.FEINT_ATTACK), (14, mv.PSYBEAM),
     (19, mv.HYPNOSIS), (23, mv.DIZZY_PUNCH), (28, mv.SUCKER_PUNCH),
     (32, mv.TEETER_DANCE), (37, mv.UPROAR), (41, mv.PSYCH_UP),
     (46, mv.DOUBLE_EDGE), (50, mv.FLAIL), (55, mv.THRASH)),
    None, 0, False, "")

FLYGON = Pokemon(
    330, "Flygon", 3, False,
    "", ("Ground", "Dragon"),
    80, 90, 80, 100,
    ((0, mv.DRAGON_CLAW), (1, mv.BULLDOZE), (1, mv.DRAGON_BREATH),
     (1, mv.SAND_ATTACK), (1, mv.SUPERSONIC), (12, mv.MUD_SLAP),
     (16, mv.SAND_TOMB), (20, mv.DRAGON_TAIL), (24, mv.SCREECH),
     (28, mv.BUG_BUZZ), (32, mv.SANDSTORM), (38, mv.EARTH_POWER),
     (44, mv.EARTHQUAKE), (52, mv.UPROAR), (60, mv.DRAGON_RUSH),
     (68, mv.BOOMBURST)),
    None, 0, False, "")

VIBRAVA = Pokemon(
    329, "Vibrava", 3, False,
    "", ("Ground", "Dragon"),
    50, 60, 50, 70,
    ((0, mv.DRAGON_BREATH), (1, mv.BITE), (1, mv.DIG), (1, mv.SAND_ATTACK),
     (12, mv.MUD_SLAP), (16, mv.SAND_TOMB), (20, mv.DRAGON_TAIL),
     (24, mv.SCREECH), (28, mv.BUG_BUZZ), (32, mv.SANDSTORM),
     (38, mv.EARTH_POWER), (44, mv.EARTHQUAKE), (50, mv.UPROAR),
     (56, mv.DRAGON_RUSH), (62, mv.BOOMBURST)),
    FLYGON, 45, True, "")

TRAPINCH = Pokemon(
    328, "Trapinch", 3, False,
    "", ("Ground",),
    45, 72, 45, 10,
    ((1, mv.ASTONISH), (1, mv.SAND_ATTACK), (8, mv.BITE), (12, mv.MUD_SLAP),
     (16, mv.SAND_TOMB), (20, mv.BULLDOZE), (24, mv.DIG), (28, mv.CRUNCH),
     (32, mv.SANDSTORM), (36, mv.EARTH_POWER), (40, mv.EARTHQUAKE),
     (44, mv.SUPERPOWER), (48, mv.FISSURE)),
    VIBRAVA, 35, True, "")

CACTURNE = Pokemon(
    332, "Cacturne", 3, False,
    "", ("Grass", "Dark"),
    70, 115, 60, 55,
    ((0, mv.SPIKY_SHIELD), (1, mv.ABSORB), (1, mv.DESTINY_BOND),
     (1, mv.GROWTH), (1, mv.LEER), (1, mv.POISON_STING), (10, mv.LEECH_SEED),
     (13, mv.SAND_ATTACK), (16, mv.BULLET_SEED), (19, mv.POWER_TRIP),
     (22, mv.INGRAIN), (26, mv.PAYBACK), (30, mv.SPIKES),
     (35, mv.SUCKER_PUNCH), (38, mv.PIN_MISSILE), (44, mv.ENERGY_BALL),
     (49, mv.COTTON_SPORE), (54, mv.SANDSTORM)),
    None, 0, False, "")

CACNEA = Pokemon(
    331, "Cacnea", 3, False,
    "", ("Grass",),
    50, 85, 40, 35,
    ((1, mv.LEER), (1, mv.POISON_STING), (4, mv.ABSORB), (7, mv.GROWTH),
     (10, mv.LEECH_SEED), (13, mv.SAND_ATTACK), (16, mv.BULLET_SEED),
     (19, mv.POWER_TRIP), (22, mv.INGRAIN), (26, mv.PAYBACK), (30, mv.SPIKES),
     (34, mv.SUCKER_PUNCH), (38, mv.PIN_MISSILE), (42, mv.ENERGY_BALL),
     (46, mv.COTTON_SPORE), (50, mv.SANDSTORM), (54, mv.DESTINY_BOND)),
    CACTURNE, 32, True, "")

ALTARIA = Pokemon(
    334, "Altaria", 3, False,
    "", ("Dragon", "Flying"),
    75, 70, 97, 80,
    ((0, mv.DRAGON_PULSE), (1, mv.DISARMING_VOICE), (1, mv.GROWL),
     (1, mv.MIST), (1, mv.PECK), (1, mv.PLUCK), (12, mv.FURY_ATTACK),
     (16, mv.ROUND), (20, mv.DRAGON_BREATH), (24, mv.SAFEGUARD), (28, mv.SING),
     (32, mv.COTTON_GUARD), (38, mv.TAKE_DOWN), (44, mv.MOONBLAST),
     (50, mv.PERISH_SONG), (56, mv.SKY_ATTACK)),
    None, 0, False, "")

SWABLU = Pokemon(
    333, "Swablu", 3, False,
    "", ("Normal", "Flying"),
    45, 40, 67, 50,
    ((1, mv.GROWL), (1, mv.PECK), (4, mv.DISARMING_VOICE), (8, mv.MIST),
     (12, mv.FURY_ATTACK), (16, mv.ROUND), (20, mv.DRAGON_BREATH),
     (24, mv.SAFEGUARD), (28, mv.SING), (32, mv.COTTON_GUARD),
     (36, mv.TAKE_DOWN), (40, mv.MOONBLAST), (44, mv.PERISH_SONG)),
    ALTARIA, 35, True, "")

ZANGOOSE = Pokemon(
    335, "Zangoose", 3, False,
    "", ("Normal",),
    73, 87, 60, 90,
    ((1, mv.LEER), (1, mv.SCRATCH), (5, mv.QUICK_ATTACK), (8, mv.FURY_CUTTER),
     (12, mv.METAL_CLAW), (15, mv.HONE_CLAWS), (19, mv.SLASH),
     (22, mv.POWER_TRIP), (26, mv.CRUSH_CLAW), (29, mv.FALSE_SWIPE),
     (33, mv.SWITCHEROO), (36, mv.DETECT), (40, mv.X_SCISSOR), (43, mv.TAUNT),
     (47, mv.SWORDS_DANCE), (50, mv.CLOSE_COMBAT)),
    None, 0, False, "")

SEVIPER = Pokemon(
    336, "Seviper", 3, False,
    "", ("Poison",),
    73, 100, 60, 65,
    ((1, mv.SWAGGER), (1, mv.WRAP), (4, mv.BITE), (6, mv.LICK),
     (9, mv.POISON_TAIL), (11, mv.FEINT), (14, mv.SCREECH), (19, mv.GLARE),
     (21, mv.POISON_FANG), (24, mv.VENOSHOCK), (29, mv.GASTRO_ACID),
     (31, mv.POISON_JAB), (34, mv.HAZE), (39, mv.CRUNCH), (41, mv.BELCH),
     (44, mv.COIL), (46, mv.SLUDGE_BOMB)),
    None, 0, False, "")

LUNATONE = Pokemon(
    337, "Lunatone", 3, False,
    "", ("Rock", "Psychic"),
    90, 75, 75, 70,
    ((1, mv.CONFUSION), (1, mv.HARDEN), (1, mv.MOONBLAST), (1, mv.MOONLIGHT),
     (1, mv.ROCK_THROW), (1, mv.TACKLE), (5, mv.HYPNOSIS),
     (10, mv.ROCK_POLISH), (15, mv.ROCK_SLIDE), (20, mv.PSYSHOCK),
     (25, mv.COSMIC_POWER), (30, mv.PSYCHIC), (35, mv.STONE_EDGE),
     (40, mv.FUTURE_SIGHT), (45, mv.MAGIC_ROOM), (50, mv.EXPLOSION)),
    None, 0, False, "")

SOLROCK = Pokemon(
    338, "Solrock", 3, False,
    "", ("Rock", "Psychic"),
    90, 75, 75, 70,
    ((1, mv.CONFUSION), (1, mv.FLARE_BLITZ), (1, mv.HARDEN),
     (1, mv.MORNING_SUN), (1, mv.ROCK_THROW), (1, mv.TACKLE), (5, mv.HYPNOSIS),
     (10, mv.ROCK_POLISH), (15, mv.ROCK_SLIDE), (20, mv.ZEN_HEADBUTT),
     (25, mv.COSMIC_POWER), (30, mv.PSYCHIC), (35, mv.STONE_EDGE),
     (40, mv.SOLAR_BEAM), (45, mv.WONDER_ROOM), (50, mv.EXPLOSION)),
    None, 0, False, "")

WHISCASH = Pokemon(
    340, "Whiscash", 3, False,
    "", ("Water", "Ground"),
    110, 77, 72, 60,
    ((0, mv.THRASH), (1, mv.BELCH), (1, mv.MUD_SLAP), (1, mv.REST),
     (1, mv.SNORE), (1, mv.TICKLE), (1, mv.WATER_GUN), (1, mv.ZEN_HEADBUTT),
     (12, mv.WATER_PULSE), (18, mv.AMNESIA), (24, mv.AQUA_TAIL),
     (33, mv.MUDDY_WATER), (40, mv.EARTHQUAKE), (48, mv.FUTURE_SIGHT),
     (56, mv.FISSURE)),
    None, 0, False, "")

BARBOACH = Pokemon(
    339, "Barboach", 3, False,
    "", ("Water", "Ground"),
    50, 47, 42, 60,
    ((1, mv.MUD_SLAP), (1, mv.WATER_GUN), (6, mv.REST), (6, mv.SNORE),
     (12, mv.WATER_PULSE), (18, mv.AMNESIA), (24, mv.AQUA_TAIL),
     (31, mv.MUDDY_WATER), (36, mv.EARTHQUAKE), (42, mv.FUTURE_SIGHT),
     (48, mv.FISSURE)),
    WHISCASH, 30, True, "")

CRAWDAUNT = Pokemon(
    342, "Crawdaunt", 3, False,
    "", ("Water", "Dark"),
    63, 105, 70, 55,
    ((0, mv.SWIFT), (1, mv.HARDEN), (1, mv.LEER), (1, mv.TAUNT),
     (1, mv.WATER_GUN), (12, mv.BUBBLE_BEAM), (16, mv.KNOCK_OFF),
     (20, mv.DOUBLE_HIT), (24, mv.PROTECT), (28, mv.NIGHT_SLASH),
     (34, mv.RAZOR_SHELL), (40, mv.SWORDS_DANCE), (46, mv.CRUNCH),
     (52, mv.CRABHAMMER), (58, mv.ENDEAVOR), (64, mv.GUILLOTINE)),
    None, 0, False, "")

CORPHISH = Pokemon(
    341, "Corphish", 3, False,
    "", ("Water",),
    43, 65, 50, 35,
    ((1, mv.HARDEN), (1, mv.WATER_GUN), (4, mv.LEER), (8, mv.TAUNT),
     (12, mv.BUBBLE_BEAM), (16, mv.KNOCK_OFF), (20, mv.DOUBLE_HIT),
     (24, mv.PROTECT), (28, mv.NIGHT_SLASH), (32, mv.RAZOR_SHELL),
     (36, mv.SWORDS_DANCE), (40, mv.CRUNCH), (44, mv.CRABHAMMER),
     (48, mv.ENDEAVOR), (52, mv.GUILLOTINE)),
    CRAWDAUNT, 30, True, "")

CLAYDOL = Pokemon(
    344, "Claydol", 3, False,
    "", ("Ground", "Psychic"),
    60, 70, 112, 75,
    ((0, mv.HYPER_BEAM), (1, mv.CONFUSION), (1, mv.HARDEN), (1, mv.MUD_SLAP),
     (1, mv.RAPID_SPIN), (1, mv.TELEPORT), (9, mv.ROCK_TOMB),
     (12, mv.POWER_TRICK), (15, mv.PSYBEAM), (18, mv.ANCIENT_POWER),
     (21, mv.IMPRISON), (24, mv.COSMIC_POWER), (27, mv.EXTRASENSORY),
     (30, mv.EARTH_POWER), (33, mv.SELF_DESTRUCT), (38, mv.GUARD_SPLIT),
     (38, mv.POWER_SPLIT), (43, mv.SANDSTORM), (48, mv.EXPLOSION)),
    None, 0, False, "")

BALTOY = Pokemon(
    343, "Baltoy", 3, False,
    "", ("Ground", "Psychic"),
    40, 40, 62, 55,
    ((1, mv.HARDEN), (1, mv.MUD_SLAP), (3, mv.RAPID_SPIN), (6, mv.CONFUSION),
     (9, mv.ROCK_TOMB), (12, mv.POWER_TRICK), (15, mv.PSYBEAM),
     (18, mv.ANCIENT_POWER), (21, mv.IMPRISON), (24, mv.COSMIC_POWER),
     (27, mv.EXTRASENSORY), (30, mv.EARTH_POWER), (33, mv.SELF_DESTRUCT),
     (36, mv.GUARD_SPLIT), (36, mv.POWER_SPLIT), (39, mv.SANDSTORM),
     (42, mv.EXPLOSION)),
    CLAYDOL, 36, True, "")

CRADILY = Pokemon(
    346, "Cradily", 3, False,
    "", ("Rock", "Grass"),
    86, 81, 102, 43,
    ((1, mv.ACID), (1, mv.ASTONISH), (1, mv.CONFUSE_RAY), (1, mv.LEECH_SEED),
     (1, mv.WRAP), (12, mv.INGRAIN), (16, mv.ANCIENT_POWER),
     (20, mv.MEGA_DRAIN), (24, mv.BRINE), (28, mv.AMNESIA),
     (32, mv.GASTRO_ACID), (36, mv.GIGA_DRAIN), (43, mv.SPIT_UP),
     (43, mv.STOCKPILE), (43, mv.SWALLOW), (48, mv.ENERGY_BALL)),
    None, 0, False, "")

LILEEP = Pokemon(
    345, "Lileep", 3, False,
    "", ("Rock", "Grass"),
    66, 51, 82, 23,
    ((1, mv.ASTONISH), (1, mv.WRAP), (4, mv.ACID), (8, mv.CONFUSE_RAY),
     (12, mv.INGRAIN), (16, mv.ANCIENT_POWER), (20, mv.MEGA_DRAIN),
     (24, mv.BRINE), (28, mv.AMNESIA), (32, mv.GASTRO_ACID),
     (36, mv.GIGA_DRAIN), (41, mv.SPIT_UP), (41, mv.STOCKPILE),
     (41, mv.SWALLOW), (44, mv.ENERGY_BALL)),
    CRADILY, 40, True, "")

ARMALDO = Pokemon(
    348, "Armaldo", 3, False,
    "", ("Rock", "Bug"),
    75, 97, 90, 45,
    ((1, mv.FURY_CUTTER), (1, mv.HARDEN), (1, mv.SMACK_DOWN),
     (1, mv.WATER_GUN), (12, mv.METAL_CLAW), (16, mv.ANCIENT_POWER),
     (20, mv.BUG_BITE), (24, mv.BRINE), (28, mv.SLASH), (32, mv.CRUSH_CLAW),
     (36, mv.ROCK_BLAST), (43, mv.PROTECT), (48, mv.X_SCISSOR)),
    None, 0, False, "")

ANORITH = Pokemon(
    347, "Anorith", 3, False,
    "", ("Rock", "Bug"),
    45, 67, 50, 75,
    ((1, mv.FURY_CUTTER), (1, mv.HARDEN), (4, mv.WATER_GUN),
     (8, mv.SMACK_DOWN), (12, mv.METAL_CLAW), (16, mv.ANCIENT_POWER),
     (20, mv.BUG_BITE), (24, mv.BRINE), (28, mv.SLASH), (32, mv.CRUSH_CLAW),
     (36, mv.ROCK_BLAST), (41, mv.PROTECT), (44, mv.X_SCISSOR)),
    ARMALDO, 40, True, "")

MILOTIC = Pokemon(
    350, "Milotic", 3, False,
    "", ("Water",),
    95, 80, 102, 81,
    ((0, mv.WATER_PULSE), (1, mv.FLAIL), (1, mv.SPLASH), (1, mv.TACKLE),
     (1, mv.WATER_GUN), (1, mv.WRAP), (4, mv.DISARMING_VOICE), (8, mv.TWISTER),
     (12, mv.AQUA_RING), (16, mv.ATTRACT), (20, mv.LIFE_DEW),
     (24, mv.DRAGON_TAIL), (28, mv.RECOVER), (32, mv.AQUA_TAIL),
     (36, mv.SAFEGUARD), (40, mv.SURF), (44, mv.RAIN_DANCE), (48, mv.COIL),
     (52, mv.HYDRO_PUMP)),
    None, 0, False, "")

FEEBAS = Pokemon(
    349, "Feebas", 3, False,
    "", ("Water",),
    20, 12, 37, 80,
    ((1, mv.SPLASH), (15, mv.TACKLE), (25, mv.FLAIL)),
    MILOTIC, 0, True, "trade")

CASTFORM = Pokemon(
    351, "Castform", 3, False,
    "", ("Normal",),
    70, 70, 70, 70,
    ((1, mv.TACKLE), (10, mv.EMBER), (10, mv.POWDER_SNOW), (10, mv.WATER_GUN),
     (15, mv.HEADBUTT), (20, mv.HAIL), (20, mv.RAIN_DANCE), (20, mv.SUNNY_DAY),
     (25, mv.WEATHER_BALL), (35, mv.BLIZZARD), (35, mv.FIRE_BLAST),
     (35, mv.HYDRO_PUMP), (45, mv.HURRICANE)),
    None, 0, False, "")

KECLEON = Pokemon(
    352, "Kecleon", 3, False,
    "", ("Normal",),
    60, 75, 95, 40,
    ((1, mv.ASTONISH), (1, mv.LICK), (1, mv.SCRATCH), (1, mv.TAIL_WHIP),
     (1, mv.THIEF), (4, mv.BIND), (7, mv.SHADOW_SNEAK), (10, mv.FEINT),
     (13, mv.FURY_SWIPES), (16, mv.FEINT_ATTACK), (18, mv.PSYBEAM),
     (21, mv.ANCIENT_POWER), (25, mv.SLASH), (30, mv.CAMOUFLAGE),
     (33, mv.SHADOW_CLAW), (38, mv.SCREECH), (42, mv.SUBSTITUTE),
     (46, mv.SUCKER_PUNCH), (50, mv.SYNCHRONOISE)),
    None, 0, False, "")

BANETTE = Pokemon(
    354, "Banette", 3, False,
    "", ("Ghost",),
    64, 99, 64, 65,
    ((0, mv.KNOCK_OFF), (1, mv.NIGHT_SHADE), (1, mv.SCREECH), (1, mv.SPITE),
     (16, mv.WILL_O_WISP), (19, mv.SHADOW_SNEAK), (22, mv.HEX), (26, mv.CURSE),
     (30, mv.SHADOW_BALL), (34, mv.ROLE_PLAY), (40, mv.SUCKER_PUNCH),
     (46, mv.TRICK), (53, mv.PHANTOM_FORCE)),
    None, 0, False, "")

SHUPPET = Pokemon(
    353, "Shuppet", 3, False,
    "", ("Ghost",),
    44, 69, 34, 45,
    ((1, mv.ASTONISH), (4, mv.SCREECH), (7, mv.NIGHT_SHADE), (10, mv.SPITE),
     (16, mv.WILL_O_WISP), (19, mv.SHADOW_SNEAK), (22, mv.HEX), (26, mv.CURSE),
     (30, mv.SHADOW_BALL), (34, mv.ROLE_PLAY), (38, mv.SUCKER_PUNCH),
     (42, mv.TRICK), (48, mv.PHANTOM_FORCE)),
    BANETTE, 37, True, "")


# --- generation 4 ---

DUSKNOIR = Pokemon(
    477, "Dusknoir", 4, False,
    "", ("Ghost",),
    45, 82, 135, 45,
    ((1, mv.ASTONISH), (1, mv.BIND), (1, mv.DISABLE), (1, mv.FIRE_PUNCH),
     (1, mv.GRAVITY), (1, mv.ICE_PUNCH), (1, mv.LEER), (1, mv.SHADOW_PUNCH),
     (1, mv.SHADOW_SNEAK), (1, mv.THUNDER_PUNCH), (12, mv.CONFUSE_RAY),
     (16, mv.NIGHT_SHADE), (20, mv.PAYBACK), (24, mv.WILL_O_WISP),
     (28, mv.MEAN_LOOK), (32, mv.HEX), (36, mv.CURSE), (42, mv.SHADOW_BALL),
     (48, mv.FUTURE_SIGHT), (54, mv.DESTINY_BOND)),
    None, 0, False, "")


# --- generation 3 ---

DUSCLOPS = Pokemon(
    356, "Dusclops", 3, False,
    "", ("Ghost",),
    40, 65, 130, 25,
    ((0, mv.SHADOW_PUNCH), (1, mv.ASTONISH), (1, mv.BIND), (1, mv.DISABLE),
     (1, mv.FIRE_PUNCH), (1, mv.GRAVITY), (1, mv.ICE_PUNCH), (1, mv.LEER),
     (1, mv.SHADOW_SNEAK), (1, mv.THUNDER_PUNCH), (12, mv.CONFUSE_RAY),
     (16, mv.NIGHT_SHADE), (20, mv.PAYBACK), (24, mv.WILL_O_WISP),
     (28, mv.MEAN_LOOK), (32, mv.HEX), (36, mv.CURSE), (42, mv.SHADOW_BALL),
     (48, mv.FUTURE_SIGHT)),
    DUSKNOIR, 0, True, "trade")

DUSKULL = Pokemon(
    355, "Duskull", 3, False,
    "", ("Ghost",),
    20, 35, 90, 25,
    ((1, mv.ASTONISH), (1, mv.LEER), (4, mv.DISABLE), (8, mv.SHADOW_SNEAK),
     (12, mv.CONFUSE_RAY), (16, mv.NIGHT_SHADE), (20, mv.PAYBACK),
     (24, mv.WILL_O_WISP), (28, mv.MEAN_LOOK), (32, mv.HEX), (36, mv.CURSE),
     (40, mv.SHADOW_BALL), (44, mv.FUTURE_SIGHT)),
    DUSCLOPS, 37, True, "")

TROPIUS = Pokemon(
    357, "Tropius", 3, False,
    "", ("Grass", "Flying"),
    99, 70, 85, 51,
    ((1, mv.GROWTH), (1, mv.GUST), (1, mv.LEAF_STORM), (1, mv.LEER),
     (1, mv.RAZOR_LEAF), (6, mv.SWEET_SCENT), (10, mv.STOMP),
     (16, mv.MAGICAL_LEAF), (21, mv.WHIRLWIND), (30, mv.WIDE_GUARD),
     (36, mv.AIR_SLASH), (41, mv.BODY_SLAM), (46, mv.OUTRAGE),
     (50, mv.SYNTHESIS), (56, mv.SOLAR_BEAM)),
    None, 0, False, "")

CHIMECHO = Pokemon(
    358, "Chimecho", 3, False,
    "", ("Psychic",),
    75, 72, 85, 65,
    ((1, mv.ASTONISH), (1, mv.CONFUSION), (1, mv.GROWL), (1, mv.HEALING_WISH),
     (1, mv.WRAP), (13, mv.YAWN), (16, mv.STORED_POWER), (19, mv.TAKE_DOWN),
     (22, mv.EXTRASENSORY), (27, mv.HEAL_BELL), (32, mv.UPROAR),
     (37, mv.SAFEGUARD), (42, mv.DOUBLE_EDGE), (47, mv.HEAL_PULSE)),
    None, 0, False, "")

ABSOL = Pokemon(
    359, "Absol", 3, False,
    "", ("Dark",),
    65, 102, 60, 75,
    ((1, mv.LEER), (1, mv.QUICK_ATTACK), (5, mv.DOUBLE_TEAM),
     (10, mv.KNOCK_OFF), (15, mv.DETECT), (20, mv.TAUNT), (25, mv.SLASH),
     (30, mv.NIGHT_SLASH), (35, mv.FOCUS_ENERGY), (40, mv.SUCKER_PUNCH),
     (45, mv.SWORDS_DANCE), (50, mv.FUTURE_SIGHT), (55, mv.PERISH_SONG)),
    None, 0, False, "")

WYNAUT = Pokemon(
    360, "Wynaut", 3, False,
    "", ("Psychic",),
    95, 23, 48, 23,
    ((1, mv.AMNESIA), (1, mv.CHARM), (1, mv.COUNTER), (1, mv.DESTINY_BOND),
     (1, mv.ENCORE), (1, mv.MIRROR_COAT), (1, mv.SAFEGUARD), (1, mv.SPLASH)),
    WOBBUFFET, 15, True, "")


# --- generation 4 ---

FROSLASS = Pokemon(
    478, "Froslass", 4, False,
    "", ("Ice", "Ghost"),
    70, 80, 70, 110,
    ((0, mv.HEX), (1, mv.ASTONISH), (1, mv.BITE), (1, mv.CRUNCH),
     (1, mv.DESTINY_BOND), (1, mv.DOUBLE_TEAM), (1, mv.HEADBUTT),
     (1, mv.ICE_FANG), (1, mv.LEER), (1, mv.POWDER_SNOW), (1, mv.PROTECT),
     (15, mv.ICE_SHARD), (20, mv.DRAINING_KISS), (25, mv.ICY_WIND),
     (30, mv.FROST_BREATH), (35, mv.CONFUSE_RAY), (40, mv.SNOWSCAPE),
     (47, mv.WILL_O_WISP), (54, mv.AURORA_VEIL), (61, mv.SHADOW_BALL),
     (68, mv.BLIZZARD)),
    None, 0, False, "")


# --- generation 3 ---

GLALIE = Pokemon(
    362, "Glalie", 3, False,
    "", ("Ice",),
    80, 80, 80, 80,
    ((0, mv.FREEZE_DRY), (1, mv.ASTONISH), (1, mv.DOUBLE_TEAM),
     (1, mv.HEADBUTT), (1, mv.LEER), (1, mv.POWDER_SNOW), (1, mv.SHEER_COLD),
     (15, mv.ICE_SHARD), (20, mv.PROTECT), (25, mv.ICY_WIND),
     (30, mv.FROST_BREATH), (35, mv.BITE), (40, mv.ICE_FANG),
     (47, mv.SNOWSCAPE), (54, mv.WEATHER_BALL), (61, mv.CRUNCH),
     (68, mv.BLIZZARD)),
    FROSLASS, 0, True, "On Female Pokémon, use Dawn Stone")

SNORUNT = Pokemon(
    361, "Snorunt", 3, False,
    "", ("Ice",),
    50, 50, 50, 50,
    ((1, mv.ASTONISH), (1, mv.HEADBUTT), (1, mv.POWDER_SNOW), (5, mv.LEER),
     (10, mv.DOUBLE_TEAM), (15, mv.ICE_SHARD), (20, mv.PROTECT),
     (25, mv.ICY_WIND), (30, mv.FROST_BREATH), (35, mv.BITE),
     (40, mv.ICE_FANG), (45, mv.SNOWSCAPE), (50, mv.WEATHER_BALL),
     (55, mv.CRUNCH), (60, mv.BLIZZARD)),
    GLALIE, 0, True, "item:dawn-stone")

WALREIN = Pokemon(
    365, "Walrein", 3, False,
    "", ("Ice", "Water"),
    110, 87, 90, 65,
    ((1, mv.CRUNCH), (1, mv.DEFENSE_CURL), (1, mv.GROWL), (1, mv.ICE_FANG),
     (1, mv.ROLLOUT), (1, mv.SWAGGER), (1, mv.WATER_GUN), (12, mv.POWDER_SNOW),
     (16, mv.REST), (20, mv.SNORE), (24, mv.BRINE), (28, mv.AURORA_BEAM),
     (35, mv.ENCORE), (40, mv.BODY_SLAM), (48, mv.SURF), (56, mv.BLIZZARD),
     (64, mv.HAIL), (72, mv.SHEER_COLD)),
    None, 0, False, "")

SEALEO = Pokemon(
    364, "Sealeo", 3, False,
    "", ("Ice", "Water"),
    90, 67, 70, 45,
    ((0, mv.SWAGGER), (1, mv.DEFENSE_CURL), (1, mv.GROWL), (1, mv.ROLLOUT),
     (1, mv.WATER_GUN), (12, mv.POWDER_SNOW), (16, mv.REST), (20, mv.SNORE),
     (24, mv.BRINE), (28, mv.AURORA_BEAM), (35, mv.ENCORE), (40, mv.BODY_SLAM),
     (46, mv.SURF), (52, mv.BLIZZARD), (58, mv.HAIL), (64, mv.SHEER_COLD)),
    WALREIN, 44, True, "")

SPHEAL = Pokemon(
    363, "Spheal", 3, False,
    "", ("Ice", "Water"),
    70, 47, 50, 25,
    ((1, mv.DEFENSE_CURL), (1, mv.ROLLOUT), (4, mv.GROWL), (8, mv.WATER_GUN),
     (12, mv.POWDER_SNOW), (16, mv.REST), (20, mv.SNORE), (24, mv.BRINE),
     (28, mv.AURORA_BEAM), (33, mv.ENCORE), (36, mv.BODY_SLAM), (40, mv.SURF),
     (44, mv.BLIZZARD), (48, mv.HAIL), (52, mv.SHEER_COLD)),
    SEALEO, 32, True, "")

GOREBYSS = Pokemon(
    368, "Gorebyss", 3, False,
    "", ("Water",),
    55, 99, 90, 52,
    ((1, mv.CONFUSION), (1, mv.WHIRLPOOL), (5, mv.WATER_SPORT),
     (9, mv.AGILITY), (11, mv.DRAINING_KISS), (14, mv.WATER_PULSE),
     (16, mv.AMNESIA), (19, mv.AQUA_RING), (23, mv.CAPTIVATE), (26, mv.DIVE),
     (29, mv.BATON_PASS), (34, mv.PSYCHIC), (39, mv.AQUA_TAIL), (45, mv.COIL),
     (50, mv.HYDRO_PUMP)),
    None, 0, False, "")

HUNTAIL = Pokemon(
    367, "Huntail", 3, False,
    "", ("Water",),
    55, 99, 90, 52,
    ((1, mv.BITE), (1, mv.WHIRLPOOL), (5, mv.SCREECH), (9, mv.SCARY_FACE),
     (11, mv.FEINT_ATTACK), (14, mv.WATER_PULSE), (16, mv.ICE_FANG),
     (19, mv.BRINE), (23, mv.SUCKER_PUNCH), (26, mv.DIVE), (29, mv.BATON_PASS),
     (34, mv.CRUNCH), (39, mv.AQUA_TAIL), (45, mv.COIL), (50, mv.HYDRO_PUMP)),
    GOREBYSS, 0, True, "Trade with  Deep Sea Scale")

CLAMPERL = Pokemon(
    366, "Clamperl", 3, False,
    "", ("Water",),
    35, 69, 70, 32,
    ((1, mv.CLAMP), (1, mv.IRON_DEFENSE), (1, mv.WATER_GUN), (1, mv.WHIRLPOOL),
     (50, mv.SHELL_SMASH)),
    HUNTAIL, 0, True, "trade")

RELICANTH = Pokemon(
    369, "Relicanth", 3, False,
    "", ("Water", "Rock"),
    100, 67, 97, 55,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.WATER_GUN), (10, mv.ANCIENT_POWER),
     (15, mv.YAWN), (20, mv.DIVE), (25, mv.TAKE_DOWN), (30, mv.AQUA_TAIL),
     (35, mv.REST), (40, mv.FLAIL), (45, mv.HYDRO_PUMP), (50, mv.DOUBLE_EDGE),
     (55, mv.HEAD_SMASH)),
    None, 0, False, "")

LUVDISC = Pokemon(
    370, "Luvdisc", 3, False,
    "", ("Water",),
    43, 35, 60, 97,
    ((1, mv.CHARM), (1, mv.TACKLE), (4, mv.WATER_GUN), (7, mv.AGILITY),
     (13, mv.WISH), (17, mv.WATER_PULSE), (20, mv.ATTRACT),
     (22, mv.DRAINING_KISS), (26, mv.FLAIL), (31, mv.SWEET_KISS),
     (34, mv.TAKE_DOWN), (37, mv.BABY_DOLL_EYES), (40, mv.AQUA_RING),
     (42, mv.SOAK), (46, mv.HYDRO_PUMP), (49, mv.SAFEGUARD)),
    None, 0, False, "")

SALAMENCE = Pokemon(
    373, "Salamence", 3, False,
    "", ("Dragon", "Flying"),
    95, 122, 80, 100,
    ((0, mv.FLY), (1, mv.BITE), (1, mv.DRAGON_BREATH), (1, mv.DRAGON_TAIL),
     (1, mv.DUAL_WINGBEAT), (1, mv.EMBER), (1, mv.LEER), (1, mv.PROTECT),
     (1, mv.ROOST), (15, mv.HEADBUTT), (20, mv.SCARY_FACE), (25, mv.CRUNCH),
     (33, mv.DRAGON_CLAW), (39, mv.ZEN_HEADBUTT), (46, mv.FOCUS_ENERGY),
     (55, mv.FLAMETHROWER), (73, mv.DOUBLE_EDGE)),
    None, 0, False, "")

SHELGON = Pokemon(
    372, "Shelgon", 3, False,
    "", ("Dragon",),
    65, 77, 75, 50,
    ((0, mv.PROTECT), (1, mv.BITE), (1, mv.DRAGON_BREATH), (1, mv.EMBER),
     (1, mv.LEER), (15, mv.HEADBUTT), (20, mv.SCARY_FACE), (25, mv.CRUNCH),
     (33, mv.DRAGON_CLAW), (39, mv.ZEN_HEADBUTT), (46, mv.FOCUS_ENERGY),
     (53, mv.FLAMETHROWER), (60, mv.OUTRAGE), (67, mv.DOUBLE_EDGE)),
    SALAMENCE, 50, True, "")

BAGON = Pokemon(
    371, "Bagon", 3, False,
    "", ("Dragon",),
    45, 57, 45, 50,
    ((1, mv.EMBER), (1, mv.LEER), (5, mv.BITE), (10, mv.DRAGON_BREATH),
     (15, mv.HEADBUTT), (20, mv.SCARY_FACE), (25, mv.CRUNCH),
     (31, mv.DRAGON_CLAW), (35, mv.ZEN_HEADBUTT), (40, mv.FOCUS_ENERGY),
     (45, mv.FLAMETHROWER), (50, mv.OUTRAGE), (55, mv.DOUBLE_EDGE)),
    SHELGON, 30, True, "")

METAGROSS = Pokemon(
    376, "Metagross", 3, False,
    "", ("Steel", "Psychic"),
    80, 115, 110, 70,
    ((0, mv.HAMMER_ARM), (1, mv.BULLET_PUNCH), (1, mv.CONFUSION),
     (1, mv.METAL_CLAW), (1, mv.TACKLE), (6, mv.ZEN_HEADBUTT),
     (12, mv.MAGNET_RISE), (16, mv.FLASH_CANNON), (26, mv.TAKE_DOWN),
     (34, mv.PSYCHIC), (42, mv.SCARY_FACE), (52, mv.METEOR_MASH),
     (62, mv.IRON_DEFENSE), (72, mv.AGILITY), (82, mv.HYPER_BEAM)),
    None, 0, False, "")

METANG = Pokemon(
    375, "Metang", 3, False,
    "", ("Steel", "Psychic"),
    60, 65, 90, 50,
    ((0, mv.CONFUSION), (0, mv.METAL_CLAW), (1, mv.BULLET_PUNCH),
     (1, mv.HONE_CLAWS), (1, mv.TACKLE), (6, mv.ZEN_HEADBUTT),
     (12, mv.MAGNET_RISE), (18, mv.FLASH_CANNON), (26, mv.TAKE_DOWN),
     (34, mv.PSYCHIC), (42, mv.SCARY_FACE), (50, mv.METEOR_MASH),
     (58, mv.IRON_DEFENSE), (66, mv.AGILITY), (74, mv.HYPER_BEAM)),
    METAGROSS, 45, True, "")

BELDUM = Pokemon(
    374, "Beldum", 3, False,
    "", ("Steel", "Psychic"),
    40, 45, 70, 30,
    ((1, mv.TACKLE),),
    METANG, 20, True, "")

REGIROCK = Pokemon(
    377, "Regirock", 3, False,
    "", ("Rock",),
    80, 75, 150, 50,
    ((1, mv.CHARGE_BEAM), (1, mv.ROCK_THROW), (6, mv.BULLDOZE),
     (12, mv.ANCIENT_POWER), (18, mv.STOMP), (24, mv.ROCK_SLIDE),
     (30, mv.CURSE), (36, mv.IRON_DEFENSE), (42, mv.HAMMER_ARM),
     (48, mv.STONE_EDGE), (54, mv.SUPERPOWER), (60, mv.LOCK_ON),
     (66, mv.ZAP_CANNON), (72, mv.HYPER_BEAM), (78, mv.EXPLOSION)),
    None, 0, False, "")

REGICE = Pokemon(
    378, "Regice", 3, False,
    "", ("Ice",),
    80, 75, 150, 50,
    ((1, mv.CHARGE_BEAM), (1, mv.ICY_WIND), (6, mv.BULLDOZE),
     (12, mv.ANCIENT_POWER), (18, mv.STOMP), (24, mv.ICE_BEAM), (30, mv.CURSE),
     (36, mv.AMNESIA), (42, mv.HAMMER_ARM), (48, mv.BLIZZARD),
     (54, mv.SUPERPOWER), (60, mv.LOCK_ON), (66, mv.ZAP_CANNON),
     (72, mv.HYPER_BEAM), (78, mv.EXPLOSION)),
    None, 0, False, "")

REGISTEEL = Pokemon(
    379, "Registeel", 3, False,
    "", ("Steel",),
    80, 75, 150, 50,
    ((1, mv.CHARGE_BEAM), (1, mv.METAL_CLAW), (6, mv.BULLDOZE),
     (12, mv.ANCIENT_POWER), (18, mv.STOMP), (24, mv.FLASH_CANNON),
     (24, mv.IRON_HEAD), (30, mv.CURSE), (36, mv.AMNESIA),
     (36, mv.IRON_DEFENSE), (42, mv.HAMMER_ARM), (48, mv.HEAVY_SLAM),
     (54, mv.SUPERPOWER), (60, mv.LOCK_ON), (66, mv.ZAP_CANNON),
     (72, mv.HYPER_BEAM), (78, mv.EXPLOSION)),
    None, 0, False, "")

LATIAS = Pokemon(
    380, "Latias", 3, False,
    "", ("Dragon", "Psychic"),
    80, 95, 110, 110,
    ((1, mv.CHARM), (1, mv.STORED_POWER), (5, mv.HELPING_HAND),
     (10, mv.RECOVER), (15, mv.CONFUSION), (20, mv.TAILWIND),
     (25, mv.DRAGON_BREATH), (30, mv.WISH), (35, mv.MIST_BALL),
     (40, mv.ZEN_HEADBUTT), (45, mv.DRAGON_PULSE), (50, mv.HEAL_PULSE),
     (55, mv.REFLECT_TYPE), (60, mv.PSYCHIC), (65, mv.GUARD_SPLIT),
     (70, mv.HEALING_WISH)),
    None, 0, False, "")

LATIOS = Pokemon(
    381, "Latios", 3, False,
    "", ("Dragon", "Psychic"),
    80, 110, 95, 110,
    ((1, mv.DRAGON_DANCE), (1, mv.STORED_POWER), (5, mv.HELPING_HAND),
     (10, mv.RECOVER), (15, mv.CONFUSION), (20, mv.TAILWIND),
     (25, mv.DRAGON_BREATH), (30, mv.ALLY_SWITCH), (35, mv.LUSTER_PURGE),
     (40, mv.ZEN_HEADBUTT), (45, mv.DRAGON_PULSE), (50, mv.HEAL_PULSE),
     (55, mv.SIMPLE_BEAM), (60, mv.PSYCHIC), (65, mv.POWER_SPLIT),
     (70, mv.MEMENTO)),
    None, 0, False, "")

KYOGRE = Pokemon(
    382, "Kyogre", 3, False,
    "", ("Water",),
    100, 125, 115, 90,
    ((1, mv.ANCIENT_POWER), (1, mv.BODY_SLAM), (1, mv.ORIGIN_PULSE),
     (1, mv.SCARY_FACE), (1, mv.WATER_PULSE), (9, mv.AQUA_TAIL),
     (18, mv.CALM_MIND), (27, mv.MUDDY_WATER), (36, mv.ICE_BEAM),
     (45, mv.SHEER_COLD), (54, mv.AQUA_RING), (72, mv.HYDRO_PUMP),
     (81, mv.DOUBLE_EDGE), (90, mv.WATER_SPOUT)),
    None, 0, False, "")

GROUDON = Pokemon(
    383, "Groudon", 3, False,
    "", ("Ground",),
    100, 125, 115, 90,
    ((1, mv.ANCIENT_POWER), (1, mv.LAVA_PLUME), (1, mv.MUD_SHOT),
     (1, mv.PRECIPICE_BLADES), (1, mv.SCARY_FACE), (9, mv.EARTH_POWER),
     (18, mv.BULK_UP), (27, mv.EARTHQUAKE), (36, mv.HAMMER_ARM),
     (45, mv.FISSURE), (54, mv.REST), (72, mv.FIRE_BLAST), (81, mv.SOLAR_BEAM),
     (90, mv.ERUPTION)),
    None, 0, False, "")

RAYQUAZA = Pokemon(
    384, "Rayquaza", 3, False,
    "", ("Dragon", "Flying"),
    105, 150, 90, 95,
    ((1, mv.AIR_SLASH), (1, mv.ANCIENT_POWER), (1, mv.DRAGON_ASCENT),
     (1, mv.SCARY_FACE), (1, mv.TWISTER), (9, mv.CRUNCH),
     (18, mv.DRAGON_DANCE), (27, mv.EXTREME_SPEED), (36, mv.DRAGON_PULSE),
     (45, mv.HYPER_VOICE), (54, mv.REST), (63, mv.FLY), (72, mv.HURRICANE),
     (81, mv.OUTRAGE), (90, mv.HYPER_BEAM)),
    None, 0, False, "")

JIRACHI = Pokemon(
    385, "Jirachi", 3, False,
    "", ("Steel", "Psychic"),
    100, 100, 100, 100,
    ((1, mv.CONFUSION), (1, mv.WISH), (7, mv.SWIFT), (21, mv.LIFE_DEW),
     (28, mv.ZEN_HEADBUTT), (35, mv.GRAVITY), (42, mv.PSYCHIC),
     (49, mv.METEOR_MASH), (56, mv.HEALING_WISH), (63, mv.REST),
     (70, mv.FUTURE_SIGHT), (77, mv.DOUBLE_EDGE), (84, mv.COSMIC_POWER),
     (91, mv.LAST_RESORT), (98, mv.DOOM_DESIRE)),
    None, 0, False, "")

DEOXYS = Pokemon(
    386, "Deoxys", 3, False,
    "", ("Psychic",),
    50, 150, 50, 150,
    ((1, mv.LEER), (1, mv.WRAP), (7, mv.NIGHT_SHADE), (13, mv.TELEPORT),
     (19, mv.KNOCK_OFF), (25, mv.PSYSHOCK), (31, mv.PSYCHIC), (37, mv.GRAVITY),
     (43, mv.SKILL_SWAP), (49, mv.ZEN_HEADBUTT), (55, mv.COSMIC_POWER),
     (61, mv.RECOVER), (67, mv.PSYCHO_BOOST), (73, mv.HYPER_BEAM)),
    None, 0, False, "")


# --- generation 4 ---

TORTERRA = Pokemon(
    389, "Torterra", 4, True,
    "Flora", ("Grass", "Ground"),
    95, 92, 95, 56,
    ((0, mv.EARTHQUAKE), (1, mv.ABSORB), (1, mv.RAZOR_LEAF), (1, mv.TACKLE),
     (1, mv.WITHDRAW), (1, mv.WOOD_HAMMER), (17, mv.CURSE), (22, mv.BITE),
     (27, mv.MEGA_DRAIN), (33, mv.LEECH_SEED), (39, mv.SYNTHESIS),
     (45, mv.CRUNCH), (51, mv.GIGA_DRAIN), (57, mv.LEAF_STORM),
     (63, mv.HEADLONG_RUSH)),
    None, 0, False, "")

GROTLE = Pokemon(
    388, "Grotle", 4, True,
    "Flora", ("Grass",),
    75, 72, 75, 36,
    ((1, mv.ABSORB), (1, mv.TACKLE), (1, mv.WITHDRAW), (13, mv.RAZOR_LEAF),
     (17, mv.CURSE), (22, mv.BITE), (27, mv.MEGA_DRAIN), (32, mv.LEECH_SEED),
     (37, mv.SYNTHESIS), (42, mv.CRUNCH), (47, mv.GIGA_DRAIN),
     (52, mv.LEAF_STORM)),
    TORTERRA, 32, True, "")

TURTWIG = Pokemon(
    387, "Turtwig", 4, True,
    "Flora", ("Grass",),
    55, 56, 59, 31,
    ((1, mv.TACKLE), (5, mv.WITHDRAW), (9, mv.ABSORB), (13, mv.RAZOR_LEAF),
     (17, mv.CURSE), (21, mv.BITE), (25, mv.MEGA_DRAIN), (29, mv.LEECH_SEED),
     (33, mv.SYNTHESIS), (37, mv.CRUNCH), (41, mv.GIGA_DRAIN),
     (45, mv.LEAF_STORM)),
    GROTLE, 18, True, "")

INFERNAPE = Pokemon(
    392, "Infernape", 4, True,
    "Flame", ("Fire", "Fighting"),
    76, 104, 71, 108,
    ((0, mv.CLOSE_COMBAT), (1, mv.EMBER), (1, mv.LEER), (1, mv.MACH_PUNCH),
     (1, mv.SCRATCH), (16, mv.FURY_SWIPES), (19, mv.FLAME_WHEEL),
     (26, mv.FEINT), (29, mv.TORMENT), (42, mv.FIRE_SPIN),
     (47, mv.FLARE_BLITZ), (52, mv.ACROBATICS), (58, mv.CALM_MIND),
     (65, mv.RAGING_FURY)),
    None, 0, False, "")

MONFERNO = Pokemon(
    391, "Monferno", 4, True,
    "Flame", ("Fire", "Fighting"),
    64, 78, 52, 81,
    ((0, mv.MACH_PUNCH), (1, mv.EMBER), (1, mv.LEER), (1, mv.SCRATCH),
     (9, mv.TAUNT), (16, mv.FURY_SWIPES), (19, mv.FLAME_WHEEL), (26, mv.FEINT),
     (29, mv.TORMENT), (36, mv.CLOSE_COMBAT), (39, mv.FIRE_SPIN),
     (46, mv.ACROBATICS), (49, mv.SLACK_OFF), (56, mv.FLARE_BLITZ)),
    INFERNAPE, 36, True, "")

CHIMCHAR = Pokemon(
    390, "Chimchar", 4, True,
    "Flame", ("Fire",),
    44, 58, 44, 61,
    ((1, mv.LEER), (1, mv.SCRATCH), (7, mv.EMBER), (9, mv.TAUNT),
     (15, mv.FURY_SWIPES), (17, mv.FLAME_WHEEL), (23, mv.NASTY_PLOT),
     (25, mv.TORMENT), (31, mv.FACADE), (33, mv.FIRE_SPIN),
     (39, mv.ACROBATICS), (41, mv.SLACK_OFF), (47, mv.FLAMETHROWER)),
    MONFERNO, 14, True, "")

EMPOLEON = Pokemon(
    395, "Empoleon", 4, True,
    "Aqua", ("Water", "Steel"),
    84, 98, 94, 60,
    ((0, mv.AQUA_JET), (1, mv.GROWL), (1, mv.METAL_CLAW), (1, mv.TACKLE),
     (1, mv.WATER_GUN), (11, mv.SWORDS_DANCE), (15, mv.PECK),
     (19, mv.BUBBLE_BEAM), (24, mv.SWAGGER), (28, mv.FURY_ATTACK),
     (33, mv.BRINE), (39, mv.WHIRLPOOL), (46, mv.MIST), (52, mv.DRILL_PECK),
     (59, mv.HYDRO_PUMP), (66, mv.WAVE_CRASH)),
    None, 0, False, "")

PRINPLUP = Pokemon(
    394, "Prinplup", 4, True,
    "Aqua", ("Water",),
    64, 73, 72, 50,
    ((0, mv.METAL_CLAW), (1, mv.GROWL), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (15, mv.PECK), (19, mv.BUBBLE_BEAM), (24, mv.SWAGGER),
     (28, mv.FURY_ATTACK), (33, mv.BRINE), (37, mv.WHIRLPOOL), (42, mv.MIST),
     (46, mv.DRILL_PECK), (50, mv.HYDRO_PUMP)),
    EMPOLEON, 36, True, "")

PIPLUP = Pokemon(
    393, "Piplup", 4, True,
    "Aqua", ("Water",),
    53, 56, 54, 40,
    ((1, mv.POUND), (4, mv.GROWL), (8, mv.WATER_GUN), (11, mv.CHARM),
     (15, mv.PECK), (18, mv.BUBBLE_BEAM), (22, mv.SWAGGER),
     (25, mv.FURY_ATTACK), (29, mv.BRINE), (32, mv.WHIRLPOOL), (36, mv.MIST),
     (39, mv.DRILL_PECK), (43, mv.HYDRO_PUMP)),
    PRINPLUP, 16, True, "")

STARAPTOR = Pokemon(
    398, "Staraptor", 4, False,
    "", ("Normal", "Flying"),
    85, 85, 65, 100,
    ((0, mv.CLOSE_COMBAT), (1, mv.GROWL), (1, mv.QUICK_ATTACK), (1, mv.TACKLE),
     (1, mv.WING_ATTACK), (13, mv.DOUBLE_TEAM), (18, mv.ENDEAVOR),
     (23, mv.WHIRLWIND), (28, mv.AERIAL_ACE), (33, mv.TAKE_DOWN),
     (41, mv.AGILITY), (49, mv.BRAVE_BIRD), (57, mv.FINAL_GAMBIT)),
    None, 0, False, "")

STARAVIA = Pokemon(
    397, "Staravia", 4, False,
    "", ("Normal", "Flying"),
    55, 57, 45, 80,
    ((1, mv.GROWL), (1, mv.QUICK_ATTACK), (1, mv.TACKLE), (9, mv.WING_ATTACK),
     (13, mv.DOUBLE_TEAM), (18, mv.ENDEAVOR), (23, mv.WHIRLWIND),
     (28, mv.AERIAL_ACE), (33, mv.TAKE_DOWN), (38, mv.AGILITY),
     (43, mv.BRAVE_BIRD), (48, mv.FINAL_GAMBIT)),
    STARAPTOR, 34, True, "")

STARLY = Pokemon(
    396, "Starly", 4, False,
    "", ("Normal", "Flying"),
    40, 42, 30, 60,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.QUICK_ATTACK), (9, mv.WING_ATTACK),
     (13, mv.DOUBLE_TEAM), (17, mv.ENDEAVOR), (21, mv.WHIRLWIND),
     (25, mv.AERIAL_ACE), (29, mv.TAKE_DOWN), (33, mv.AGILITY),
     (37, mv.BRAVE_BIRD), (41, mv.FINAL_GAMBIT)),
    STARAVIA, 14, True, "")

BIBAREL = Pokemon(
    400, "Bibarel", 4, False,
    "", ("Normal", "Water"),
    79, 70, 60, 71,
    ((1, mv.AQUA_JET), (1, mv.GROWL), (1, mv.ROTOTILLER), (1, mv.TACKLE),
     (1, mv.WATER_GUN), (5, mv.DEFENSE_CURL), (9, mv.ROLLOUT),
     (13, mv.HEADBUTT), (18, mv.HYPER_FANG), (23, mv.YAWN), (28, mv.CRUNCH),
     (33, mv.TAKE_DOWN), (38, mv.SUPER_FANG), (43, mv.SWORDS_DANCE),
     (48, mv.AMNESIA), (53, mv.SUPERPOWER), (58, mv.CURSE)),
    None, 0, False, "")

BIDOOF = Pokemon(
    399, "Bidoof", 4, False,
    "", ("Normal",),
    59, 40, 40, 31,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.DEFENSE_CURL), (9, mv.ROLLOUT),
     (13, mv.HEADBUTT), (17, mv.HYPER_FANG), (21, mv.YAWN), (25, mv.CRUNCH),
     (29, mv.TAKE_DOWN), (33, mv.SUPER_FANG), (37, mv.SWORDS_DANCE),
     (41, mv.AMNESIA), (45, mv.SUPERPOWER), (49, mv.CURSE)),
    BIBAREL, 15, True, "")

KRICKETUNE = Pokemon(
    402, "Kricketune", 4, False,
    "", ("Bug",),
    77, 70, 51, 65,
    ((0, mv.FURY_CUTTER), (1, mv.GROWL), (1, mv.TACKLE), (14, mv.ABSORB),
     (18, mv.SING), (22, mv.FOCUS_ENERGY), (26, mv.SLASH), (30, mv.X_SCISSOR),
     (34, mv.SCREECH), (36, mv.FELL_STINGER), (38, mv.TAUNT),
     (42, mv.NIGHT_SLASH), (44, mv.STICKY_WEB), (46, mv.BUG_BUZZ),
     (50, mv.PERISH_SONG)),
    None, 0, False, "")

KRICKETOT = Pokemon(
    401, "Kricketot", 4, False,
    "", ("Bug",),
    37, 25, 41, 25,
    ((1, mv.GROWL), (1, mv.TACKLE), (6, mv.STRUGGLE_BUG), (16, mv.BUG_BITE)),
    KRICKETUNE, 10, True, "")

LUXRAY = Pokemon(
    405, "Luxray", 4, False,
    "", ("Electric",),
    80, 107, 79, 70,
    ((1, mv.CHARGE), (1, mv.ELECTRIC_TERRAIN), (1, mv.LEER), (1, mv.TACKLE),
     (1, mv.THUNDER_SHOCK), (12, mv.BITE), (18, mv.SPARK), (24, mv.ROAR),
     (33, mv.VOLT_SWITCH), (40, mv.SCARY_FACE), (48, mv.THUNDER_WAVE),
     (56, mv.CRUNCH), (64, mv.DISCHARGE), (72, mv.SWAGGER),
     (80, mv.WILD_CHARGE)),
    None, 0, False, "")

LUXIO = Pokemon(
    404, "Luxio", 4, False,
    "", ("Electric",),
    60, 72, 49, 60,
    ((1, mv.CHARGE), (1, mv.LEER), (1, mv.TACKLE), (1, mv.THUNDER_SHOCK),
     (12, mv.BITE), (18, mv.SPARK), (24, mv.ROAR), (31, mv.VOLT_SWITCH),
     (36, mv.SCARY_FACE), (42, mv.THUNDER_WAVE), (48, mv.CRUNCH),
     (54, mv.DISCHARGE), (60, mv.SWAGGER), (68, mv.WILD_CHARGE)),
    LUXRAY, 30, True, "")

SHINX = Pokemon(
    403, "Shinx", 4, False,
    "", ("Electric",),
    45, 52, 34, 45,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.THUNDER_SHOCK), (8, mv.CHARGE),
     (12, mv.BITE), (16, mv.SPARK), (20, mv.ROAR), (24, mv.VOLT_SWITCH),
     (28, mv.SCARY_FACE), (32, mv.THUNDER_WAVE), (36, mv.CRUNCH),
     (40, mv.DISCHARGE), (44, mv.SWAGGER), (48, mv.WILD_CHARGE)),
    LUXIO, 15, True, "")

BUDEW = Pokemon(
    406, "Budew", 4, False,
    "", ("Grass", "Poison"),
    40, 40, 52, 55,
    ((1, mv.ABSORB), (1, mv.GROWTH), (1, mv.STUN_SPORE), (1, mv.WORRY_SEED)),
    ROSELIA, 0, True, "happiness")

RAMPARDOS = Pokemon(
    409, "Rampardos", 4, False,
    "", ("Rock",),
    97, 115, 55, 58,
    ((0, mv.ENDEAVOR), (1, mv.FOCUS_ENERGY), (1, mv.HEADBUTT), (1, mv.LEER),
     (10, mv.ROCK_SMASH), (15, mv.TAKE_DOWN), (19, mv.SCARY_FACE),
     (24, mv.ASSURANCE), (28, mv.SLAM), (36, mv.ANCIENT_POWER),
     (43, mv.ZEN_HEADBUTT), (51, mv.SCREECH), (58, mv.HEAD_SMASH)),
    None, 0, False, "")

CRANIDOS = Pokemon(
    408, "Cranidos", 4, False,
    "", ("Rock",),
    67, 77, 35, 58,
    ((1, mv.HEADBUTT), (1, mv.LEER), (6, mv.FOCUS_ENERGY), (10, mv.ROCK_SMASH),
     (15, mv.TAKE_DOWN), (19, mv.SCARY_FACE), (24, mv.ASSURANCE),
     (28, mv.SLAM), (33, mv.ANCIENT_POWER), (37, mv.ZEN_HEADBUTT),
     (42, mv.SCREECH), (46, mv.HEAD_SMASH)),
    RAMPARDOS, 30, True, "")

BASTIODON = Pokemon(
    411, "Bastiodon", 4, False,
    "", ("Rock", "Steel"),
    60, 49, 153, 30,
    ((0, mv.BLOCK), (1, mv.METAL_SOUND), (1, mv.PROTECT), (1, mv.TACKLE),
     (1, mv.TAUNT), (15, mv.TAKE_DOWN), (19, mv.IRON_DEFENSE),
     (24, mv.SWAGGER), (28, mv.ANCIENT_POWER), (36, mv.ENDURE),
     (43, mv.METAL_BURST), (51, mv.IRON_HEAD), (58, mv.HEAVY_SLAM)),
    None, 0, False, "")

SHIELDON = Pokemon(
    410, "Shieldon", 4, False,
    "", ("Rock", "Steel"),
    30, 42, 103, 30,
    ((1, mv.PROTECT), (1, mv.TACKLE), (6, mv.TAUNT), (10, mv.METAL_SOUND),
     (15, mv.TAKE_DOWN), (19, mv.IRON_DEFENSE), (24, mv.SWAGGER),
     (28, mv.ANCIENT_POWER), (33, mv.ENDURE), (37, mv.METAL_BURST),
     (42, mv.IRON_HEAD), (46, mv.HEAVY_SLAM)),
    BASTIODON, 30, True, "")

MOTHIM = Pokemon(
    414, "Mothim", 4, False,
    "", ("Bug", "Flying"),
    70, 94, 50, 66,
    ((0, mv.QUIVER_DANCE), (1, mv.BUG_BITE), (1, mv.TACKLE), (10, mv.PROTECT),
     (20, mv.HIDDEN_POWER), (23, mv.CONFUSION), (26, mv.GUST),
     (29, mv.POISON_POWDER), (32, mv.PSYBEAM), (35, mv.CAMOUFLAGE),
     (38, mv.SILVER_WIND), (41, mv.AIR_SLASH), (44, mv.PSYCHIC),
     (47, mv.LUNGE), (50, mv.BUG_BUZZ)),
    None, 0, False, "")

WORMADAM = Pokemon(
    413, "Wormadam", 4, False,
    "", ("Bug", "Grass"),
    60, 69, 95, 36,
    ((0, mv.QUIVER_DANCE), (1, mv.BUG_BITE), (1, mv.PROTECT),
     (1, mv.SUCKER_PUNCH), (1, mv.TACKLE), (20, mv.HIDDEN_POWER),
     (23, mv.CONFUSION), (26, mv.RAZOR_LEAF), (29, mv.GROWTH),
     (32, mv.PSYBEAM), (35, mv.CAPTIVATE), (38, mv.FLAIL), (41, mv.ATTRACT),
     (44, mv.PSYCHIC), (47, mv.LEAF_STORM), (50, mv.BUG_BUZZ)),
    MOTHIM, 0, True, "Male at Level")

BURMY = Pokemon(
    412, "Burmy", 4, False,
    "", ("Bug",),
    40, 29, 45, 36,
    ((1, mv.PROTECT), (10, mv.TACKLE), (15, mv.BUG_BITE),
     (20, mv.HIDDEN_POWER)),
    WORMADAM, 20, True, "")

VESPIQUEN = Pokemon(
    416, "Vespiquen", 4, False,
    "", ("Bug", "Flying"),
    70, 80, 102, 40,
    ((0, mv.SLASH), (1, mv.BUG_BITE), (1, mv.CONFUSE_RAY), (1, mv.GUST),
     (1, mv.POISON_STING), (1, mv.STRUGGLE_BUG), (1, mv.SWEET_SCENT),
     (4, mv.FURY_CUTTER), (8, mv.AROMATIC_MIST), (12, mv.FELL_STINGER),
     (16, mv.FURY_SWIPES), (20, mv.SWAGGER), (24, mv.ROOST),
     (28, mv.AIR_SLASH), (32, mv.POWER_GEM), (36, mv.TOXIC),
     (40, mv.ATTACK_ORDER), (40, mv.DEFEND_ORDER), (44, mv.DESTINY_BOND)),
    None, 0, False, "")

COMBEE = Pokemon(
    415, "Combee", 4, False,
    "", ("Bug", "Flying"),
    30, 30, 42, 70,
    ((1, mv.BUG_BITE), (1, mv.GUST), (1, mv.STRUGGLE_BUG),
     (1, mv.SWEET_SCENT)),
    VESPIQUEN, 21, True, "")

PACHIRISU = Pokemon(
    417, "Pachirisu", 4, False,
    "", ("Electric",),
    60, 45, 80, 95,
    ((1, mv.GROWL), (1, mv.THUNDER_SHOCK), (5, mv.QUICK_ATTACK), (9, mv.CHARM),
     (13, mv.SPARK), (17, mv.ENDURE), (19, mv.NUZZLE), (21, mv.SWIFT),
     (25, mv.ELECTRO_BALL), (29, mv.SWEET_KISS), (33, mv.THUNDER_WAVE),
     (37, mv.SUPER_FANG), (41, mv.DISCHARGE), (45, mv.LAST_RESORT),
     (49, mv.THUNDER)),
    None, 0, False, "")

FLOATZEL = Pokemon(
    419, "Floatzel", 4, False,
    "", ("Water",),
    85, 95, 52, 115,
    ((1, mv.CRUNCH), (1, mv.GROWL), (1, mv.ICE_FANG), (1, mv.QUICK_ATTACK),
     (1, mv.SOAK), (15, mv.WATER_GUN), (18, mv.BITE), (21, mv.SWIFT),
     (24, mv.AQUA_JET), (29, mv.DOUBLE_HIT), (35, mv.WHIRLPOOL),
     (41, mv.LIQUIDATION), (46, mv.AQUA_TAIL), (51, mv.AGILITY),
     (57, mv.HYDRO_PUMP), (62, mv.WAVE_CRASH)),
    None, 0, False, "")

BUIZEL = Pokemon(
    418, "Buizel", 4, False,
    "", ("Water",),
    55, 62, 32, 85,
    ((1, mv.TACKLE), (4, mv.GROWL), (7, mv.SOAK), (11, mv.QUICK_ATTACK),
     (15, mv.WATER_GUN), (18, mv.BITE), (21, mv.SWIFT), (24, mv.AQUA_JET),
     (27, mv.DOUBLE_HIT), (31, mv.WHIRLPOOL), (35, mv.LIQUIDATION),
     (38, mv.AQUA_TAIL), (41, mv.AGILITY), (45, mv.HYDRO_PUMP),
     (49, mv.WAVE_CRASH)),
    FLOATZEL, 26, True, "")

CHERRIM = Pokemon(
    421, "Cherrim", 4, False,
    "", ("Grass",),
    70, 73, 74, 85,
    ((0, mv.SUNNY_DAY), (1, mv.FLOWER_SHIELD), (1, mv.GROWTH), (1, mv.LEAFAGE),
     (1, mv.MORNING_SUN), (1, mv.TACKLE), (15, mv.HELPING_HAND),
     (20, mv.MAGICAL_LEAF), (28, mv.LEECH_SEED), (34, mv.TAKE_DOWN),
     (41, mv.PETAL_BLIZZARD), (48, mv.WORRY_SEED), (55, mv.SOLAR_BEAM),
     (62, mv.PETAL_DANCE)),
    None, 0, False, "")

CHERUBI = Pokemon(
    420, "Cherubi", 4, False,
    "", ("Grass",),
    45, 48, 49, 35,
    ((1, mv.MORNING_SUN), (1, mv.TACKLE), (5, mv.LEAFAGE), (10, mv.GROWTH),
     (15, mv.HELPING_HAND), (20, mv.MAGICAL_LEAF), (26, mv.LEECH_SEED),
     (30, mv.TAKE_DOWN), (35, mv.PETAL_BLIZZARD), (40, mv.WORRY_SEED),
     (45, mv.SOLAR_BEAM)),
    CHERRIM, 25, True, "")

GASTRODON = Pokemon(
    423, "Gastrodon", 4, False,
    "", ("Water", "Ground"),
    111, 87, 75, 39,
    ((1, mv.HARDEN), (1, mv.MUD_SLAP), (1, mv.RECOVER), (1, mv.WATER_GUN),
     (15, mv.WATER_PULSE), (20, mv.ANCIENT_POWER), (25, mv.BODY_SLAM),
     (33, mv.MUDDY_WATER), (39, mv.EARTH_POWER), (46, mv.RAIN_DANCE),
     (53, mv.MEMENTO)),
    None, 0, False, "")

SHELLOS = Pokemon(
    422, "Shellos", 4, False,
    "", ("Water",),
    76, 52, 55, 34,
    ((1, mv.MUD_SLAP), (1, mv.WATER_GUN), (5, mv.HARDEN), (10, mv.RECOVER),
     (15, mv.WATER_PULSE), (20, mv.ANCIENT_POWER), (25, mv.BODY_SLAM),
     (31, mv.MUDDY_WATER), (35, mv.EARTH_POWER), (40, mv.RAIN_DANCE),
     (45, mv.MEMENTO)),
    GASTRODON, 30, True, "")

DRIFBLIM = Pokemon(
    426, "Drifblim", 4, False,
    "", ("Ghost", "Flying"),
    150, 85, 49, 80,
    ((0, mv.PHANTOM_FORCE), (1, mv.ASTONISH), (1, mv.FOCUS_ENERGY),
     (1, mv.GUST), (1, mv.MINIMIZE), (1, mv.STRENGTH_SAP), (12, mv.PAYBACK),
     (16, mv.HEX), (20, mv.SHADOW_BALL), (24, mv.SPIT_UP), (24, mv.STOCKPILE),
     (24, mv.SWALLOW), (31, mv.SELF_DESTRUCT), (36, mv.DESTINY_BOND),
     (42, mv.BATON_PASS), (48, mv.TAILWIND), (54, mv.EXPLOSION)),
    None, 0, False, "")

DRIFLOON = Pokemon(
    425, "Drifloon", 4, False,
    "", ("Ghost", "Flying"),
    90, 55, 39, 70,
    ((1, mv.ASTONISH), (1, mv.MINIMIZE), (4, mv.GUST), (8, mv.FOCUS_ENERGY),
     (12, mv.PAYBACK), (16, mv.HEX), (20, mv.SHADOW_BALL), (24, mv.SPIT_UP),
     (24, mv.STOCKPILE), (24, mv.SWALLOW), (29, mv.SELF_DESTRUCT),
     (32, mv.DESTINY_BOND), (36, mv.BATON_PASS), (40, mv.TAILWIND),
     (44, mv.EXPLOSION)),
    DRIFBLIM, 28, True, "")

LOPUNNY = Pokemon(
    428, "Lopunny", 4, False,
    "", ("Normal",),
    65, 65, 90, 105,
    ((1, mv.BABY_DOLL_EYES), (1, mv.DEFENSE_CURL), (1, mv.MAGIC_COAT),
     (1, mv.MIRROR_COAT), (1, mv.POUND), (1, mv.SPLASH), (12, mv.AFTER_YOU),
     (16, mv.QUICK_ATTACK), (20, mv.DOUBLE_KICK), (24, mv.CHARM),
     (28, mv.BATON_PASS), (32, mv.HEADBUTT), (36, mv.AGILITY),
     (40, mv.ENTRAINMENT), (44, mv.FLATTER), (48, mv.BOUNCE),
     (52, mv.HEALING_WISH), (56, mv.HIGH_JUMP_KICK)),
    None, 0, False, "")

BUNEARY = Pokemon(
    427, "Buneary", 4, False,
    "", ("Normal",),
    55, 55, 50, 85,
    ((1, mv.POUND), (1, mv.SPLASH), (4, mv.DEFENSE_CURL),
     (8, mv.BABY_DOLL_EYES), (12, mv.AFTER_YOU), (16, mv.QUICK_ATTACK),
     (20, mv.DOUBLE_KICK), (24, mv.CHARM), (28, mv.BATON_PASS),
     (32, mv.HEADBUTT), (36, mv.AGILITY), (40, mv.ENTRAINMENT),
     (44, mv.FLATTER), (48, mv.BOUNCE), (52, mv.HEALING_WISH)),
    LOPUNNY, 0, True, "happiness")

PURUGLY = Pokemon(
    432, "Purugly", 4, False,
    "", ("Normal",),
    71, 73, 61, 112,
    ((0, mv.SWAGGER), (1, mv.FAKE_OUT), (5, mv.SCRATCH), (8, mv.GROWL),
     (13, mv.HYPNOSIS), (17, mv.FEINT_ATTACK), (20, mv.FURY_SWIPES),
     (25, mv.CHARM), (29, mv.ASSIST), (32, mv.CAPTIVATE), (37, mv.SLASH),
     (45, mv.BODY_SLAM), (52, mv.ATTRACT), (60, mv.HONE_CLAWS)),
    None, 0, False, "")

GLAMEOW = Pokemon(
    431, "Glameow", 4, False,
    "", ("Normal",),
    49, 48, 39, 85,
    ((1, mv.FAKE_OUT), (5, mv.SCRATCH), (8, mv.GROWL), (13, mv.HYPNOSIS),
     (17, mv.FEINT_ATTACK), (20, mv.FURY_SWIPES), (25, mv.CHARM),
     (29, mv.ASSIST), (32, mv.CAPTIVATE), (37, mv.SLASH),
     (41, mv.SUCKER_PUNCH), (44, mv.ATTRACT), (48, mv.HONE_CLAWS),
     (50, mv.PLAY_ROUGH)),
    PURUGLY, 38, True, "")

CHINGLING = Pokemon(
    433, "Chingling", 4, False,
    "", ("Psychic",),
    45, 47, 50, 45,
    ((1, mv.WRAP), (4, mv.GROWL), (7, mv.ASTONISH), (10, mv.CONFUSION),
     (13, mv.YAWN), (16, mv.LAST_RESORT), (19, mv.ENTRAINMENT),
     (32, mv.UPROAR)),
    CHIMECHO, 0, True, "happiness")

SKUNTANK = Pokemon(
    435, "Skuntank", 4, False,
    "", ("Poison", "Dark"),
    103, 82, 64, 84,
    ((0, mv.FLAMETHROWER), (1, mv.FEINT), (1, mv.POISON_GAS), (1, mv.SCRATCH),
     (1, mv.SMOKESCREEN), (12, mv.FURY_SWIPES), (15, mv.FOCUS_ENERGY),
     (18, mv.BITE), (21, mv.VENOSHOCK), (24, mv.SCREECH), (27, mv.TOXIC),
     (30, mv.SUCKER_PUNCH), (33, mv.MEMENTO), (38, mv.NIGHT_SLASH),
     (43, mv.BELCH), (48, mv.EXPLOSION)),
    None, 0, False, "")

STUNKY = Pokemon(
    434, "Stunky", 4, False,
    "", ("Poison", "Dark"),
    63, 52, 44, 74,
    ((1, mv.POISON_GAS), (1, mv.SCRATCH), (3, mv.FEINT), (6, mv.SMOKESCREEN),
     (9, mv.ACID_SPRAY), (12, mv.FURY_SWIPES), (15, mv.FOCUS_ENERGY),
     (18, mv.BITE), (21, mv.VENOSHOCK), (24, mv.SCREECH), (27, mv.TOXIC),
     (30, mv.SUCKER_PUNCH), (33, mv.MEMENTO), (36, mv.NIGHT_SLASH),
     (39, mv.BELCH), (42, mv.EXPLOSION)),
    SKUNTANK, 34, True, "")

BRONZONG = Pokemon(
    437, "Bronzong", 4, False,
    "", ("Steel", "Psychic"),
    67, 84, 116, 33,
    ((0, mv.BLOCK), (1, mv.CONFUSE_RAY), (1, mv.CONFUSION), (1, mv.PAYBACK),
     (1, mv.SUNNY_DAY), (1, mv.TACKLE), (1, mv.WEATHER_BALL),
     (12, mv.IMPRISON), (16, mv.GYRO_BALL), (20, mv.HYPNOSIS),
     (24, mv.SAFEGUARD), (28, mv.EXTRASENSORY), (32, mv.HEAVY_SLAM),
     (38, mv.IRON_DEFENSE), (44, mv.METAL_SOUND), (50, mv.FUTURE_SIGHT),
     (56, mv.RAIN_DANCE)),
    None, 0, False, "")

BRONZOR = Pokemon(
    436, "Bronzor", 4, False,
    "", ("Steel", "Psychic"),
    57, 24, 86, 23,
    ((1, mv.CONFUSION), (1, mv.TACKLE), (4, mv.CONFUSE_RAY), (8, mv.PAYBACK),
     (12, mv.IMPRISON), (16, mv.GYRO_BALL), (20, mv.HYPNOSIS),
     (24, mv.SAFEGUARD), (28, mv.EXTRASENSORY), (32, mv.HEAVY_SLAM),
     (36, mv.IRON_DEFENSE), (40, mv.METAL_SOUND), (44, mv.FUTURE_SIGHT)),
    BRONZONG, 33, True, "")

BONSLY = Pokemon(
    438, "Bonsly", 4, False,
    "", ("Rock",),
    50, 45, 70, 10,
    ((1, mv.COPYCAT), (1, mv.FAKE_TEARS), (4, mv.FLAIL), (8, mv.ROCK_THROW),
     (12, mv.BLOCK), (16, mv.MIMIC), (20, mv.ROCK_TOMB), (24, mv.TEARFUL_LOOK),
     (28, mv.SUCKER_PUNCH), (32, mv.ROCK_SLIDE), (36, mv.LOW_KICK),
     (40, mv.COUNTER), (44, mv.DOUBLE_EDGE)),
    SUDOWOODO, 0, True, "level-up")

MIME_JR = Pokemon(
    439, "Mime Jr.", 4, False,
    "", ("Psychic", "Fairy"),
    20, 47, 67, 60,
    ((1, mv.COPYCAT), (1, mv.POUND), (4, mv.BATON_PASS), (8, mv.ENCORE),
     (12, mv.CONFUSION), (16, mv.ROLE_PLAY), (20, mv.PROTECT),
     (24, mv.RECYCLE), (28, mv.PSYBEAM), (32, mv.MIMIC), (36, mv.LIGHT_SCREEN),
     (36, mv.REFLECT), (36, mv.SAFEGUARD), (40, mv.SUCKER_PUNCH),
     (44, mv.DAZZLING_GLEAM), (48, mv.PSYCHIC), (52, mv.TEETER_DANCE)),
    MR_MIME, 0, True, "level-up")

HAPPINY = Pokemon(
    440, "Happiny", 4, False,
    "", ("Normal",),
    100, 10, 35, 30,
    ((1, mv.COPYCAT), (1, mv.POUND), (4, mv.DEFENSE_CURL), (8, mv.SWEET_KISS),
     (12, mv.DISARMING_VOICE), (16, mv.COVET), (20, mv.CHARM)),
    CHANSEY, 0, True, "level-up")

CHATOT = Pokemon(
    441, "Chatot", 4, False,
    "", ("Normal", "Flying"),
    76, 78, 43, 91,
    ((1, mv.CONFIDE), (1, mv.PECK), (1, mv.TAUNT), (5, mv.GROWL),
     (9, mv.MIRROR_MOVE), (13, mv.SING), (17, mv.FURY_ATTACK),
     (21, mv.CHATTER), (29, mv.ROUND), (33, mv.MIMIC), (37, mv.ECHOED_VOICE),
     (41, mv.ROOST), (45, mv.UPROAR), (49, mv.SYNCHRONOISE),
     (50, mv.FEATHER_DANCE), (57, mv.HYPER_VOICE)),
    None, 0, False, "")

SPIRITOMB = Pokemon(
    442, "Spiritomb", 4, False,
    "", ("Ghost", "Dark"),
    50, 92, 108, 35,
    ((1, mv.CONFUSE_RAY), (1, mv.NIGHT_SHADE), (5, mv.SHADOW_SNEAK),
     (10, mv.SPITE), (15, mv.PAYBACK), (20, mv.NASTY_PLOT), (25, mv.HEX),
     (30, mv.MEMENTO), (35, mv.SUCKER_PUNCH), (40, mv.CURSE),
     (45, mv.SHADOW_BALL), (50, mv.DARK_PULSE), (55, mv.HYPNOSIS),
     (60, mv.DREAM_EATER)),
    None, 0, False, "")

GARCHOMP = Pokemon(
    445, "Garchomp", 4, False,
    "", ("Dragon", "Ground"),
    108, 105, 90, 102,
    ((0, mv.CRUNCH), (1, mv.DRAGON_BREATH), (1, mv.SAND_ATTACK),
     (1, mv.SAND_TOMB), (1, mv.TACKLE), (18, mv.BULLDOZE), (27, mv.BITE),
     (34, mv.SLASH), (42, mv.DRAGON_CLAW), (52, mv.DIG), (62, mv.SANDSTORM),
     (72, mv.TAKE_DOWN), (82, mv.DRAGON_RUSH)),
    None, 0, False, "")

GABITE = Pokemon(
    444, "Gabite", 4, False,
    "", ("Dragon", "Ground"),
    68, 70, 60, 82,
    ((1, mv.DRAGON_BREATH), (1, mv.SAND_ATTACK), (1, mv.SAND_TOMB),
     (1, mv.TACKLE), (18, mv.BULLDOZE), (27, mv.BITE), (34, mv.SLASH),
     (42, mv.DRAGON_CLAW), (50, mv.DIG), (58, mv.SANDSTORM),
     (66, mv.TAKE_DOWN), (74, mv.DRAGON_RUSH)),
    GARCHOMP, 48, True, "")

GIBLE = Pokemon(
    443, "Gible", 4, False,
    "", ("Dragon", "Ground"),
    58, 55, 45, 42,
    ((1, mv.SAND_TOMB), (1, mv.TACKLE), (6, mv.SAND_ATTACK),
     (12, mv.DRAGON_BREATH), (18, mv.BULLDOZE), (25, mv.BITE), (30, mv.SLASH),
     (36, mv.DRAGON_CLAW), (42, mv.DIG), (48, mv.SANDSTORM),
     (54, mv.TAKE_DOWN), (60, mv.DRAGON_RUSH)),
    GABITE, 24, True, "")

MUNCHLAX = Pokemon(
    446, "Munchlax", 4, False,
    "", ("Normal",),
    135, 62, 62, 5,
    ((1, mv.LICK), (1, mv.TACKLE), (4, mv.DEFENSE_CURL), (8, mv.RECYCLE),
     (12, mv.COVET), (16, mv.BITE), (20, mv.STOCKPILE), (20, mv.SWALLOW),
     (24, mv.SCREECH), (28, mv.BODY_SLAM), (32, mv.FLING), (36, mv.AMNESIA),
     (40, mv.METRONOME), (44, mv.FLAIL), (48, mv.BELLY_DRUM),
     (52, mv.LAST_RESORT)),
    SNORLAX, 0, True, "happiness")

LUCARIO = Pokemon(
    448, "Lucario", 4, False,
    "", ("Fighting", "Steel"),
    70, 112, 70, 90,
    ((0, mv.AURA_SPHERE), (1, mv.COPYCAT), (1, mv.DETECT), (1, mv.FEINT),
     (1, mv.FINAL_GAMBIT), (1, mv.HELPING_HAND), (1, mv.LIFE_DEW),
     (1, mv.METAL_CLAW), (1, mv.QUICK_ATTACK), (1, mv.REVERSAL),
     (1, mv.ROCK_SMASH), (1, mv.SCREECH), (1, mv.VACUUM_WAVE),
     (12, mv.COUNTER), (16, mv.WORK_UP), (20, mv.FORCE_PALM),
     (24, mv.CALM_MIND), (28, mv.METAL_SOUND), (32, mv.QUICK_GUARD),
     (36, mv.BONE_RUSH), (40, mv.SWORDS_DANCE), (44, mv.HEAL_PULSE),
     (48, mv.METEOR_MASH), (52, mv.DRAGON_PULSE), (56, mv.EXTREME_SPEED),
     (60, mv.CLOSE_COMBAT)),
    None, 0, False, "")

RIOLU = Pokemon(
    447, "Riolu", 4, False,
    "", ("Fighting",),
    40, 52, 40, 60,
    ((1, mv.ENDURE), (1, mv.QUICK_ATTACK), (4, mv.FEINT), (8, mv.METAL_CLAW),
     (12, mv.COUNTER), (16, mv.WORK_UP), (20, mv.ROCK_SMASH),
     (24, mv.VACUUM_WAVE), (28, mv.SCREECH), (32, mv.QUICK_GUARD),
     (36, mv.FORCE_PALM), (40, mv.SWORDS_DANCE), (44, mv.HELPING_HAND),
     (48, mv.COPYCAT), (52, mv.FINAL_GAMBIT), (56, mv.REVERSAL)),
    LUCARIO, 0, True, "happiness")

HIPPOWDON = Pokemon(
    450, "Hippowdon", 4, False,
    "", ("Ground",),
    108, 90, 95, 47,
    ((1, mv.BITE), (1, mv.FIRE_FANG), (1, mv.ICE_FANG), (1, mv.SAND_ATTACK),
     (1, mv.TACKLE), (1, mv.THUNDER_FANG), (1, mv.YAWN), (12, mv.SAND_TOMB),
     (16, mv.DIG), (20, mv.CRUNCH), (24, mv.SANDSTORM), (28, mv.TAKE_DOWN),
     (32, mv.ROAR), (38, mv.REST), (44, mv.EARTHQUAKE), (50, mv.DOUBLE_EDGE),
     (56, mv.FISSURE), (62, mv.SLACK_OFF)),
    None, 0, False, "")

HIPPOPOTAS = Pokemon(
    449, "Hippopotas", 4, False,
    "", ("Ground",),
    68, 55, 60, 32,
    ((1, mv.SAND_ATTACK), (1, mv.TACKLE), (4, mv.BITE), (8, mv.YAWN),
     (12, mv.SAND_TOMB), (16, mv.DIG), (20, mv.CRUNCH), (24, mv.SANDSTORM),
     (28, mv.TAKE_DOWN), (32, mv.ROAR), (36, mv.REST), (40, mv.EARTHQUAKE),
     (44, mv.DOUBLE_EDGE), (48, mv.FISSURE), (52, mv.SLACK_OFF)),
    HIPPOWDON, 34, True, "")

DRAPION = Pokemon(
    452, "Drapion", 4, False,
    "", ("Poison", "Dark"),
    70, 75, 92, 95,
    ((1, mv.FELL_STINGER), (1, mv.FIRE_FANG), (1, mv.HONE_CLAWS),
     (1, mv.ICE_FANG), (1, mv.LEER), (1, mv.POISON_STING),
     (1, mv.THUNDER_FANG), (9, mv.POISON_FANG), (12, mv.BITE),
     (15, mv.TOXIC_SPIKES), (18, mv.BUG_BITE), (21, mv.VENOSHOCK),
     (24, mv.KNOCK_OFF), (27, mv.SCARY_FACE), (30, mv.PIN_MISSILE),
     (33, mv.TOXIC), (36, mv.NIGHT_SLASH), (39, mv.CROSS_POISON),
     (44, mv.X_SCISSOR), (49, mv.ACUPRESSURE), (54, mv.CRUNCH)),
    None, 0, False, "")

SKORUPI = Pokemon(
    451, "Skorupi", 4, False,
    "", ("Poison", "Bug"),
    40, 40, 72, 65,
    ((1, mv.LEER), (1, mv.POISON_STING), (3, mv.HONE_CLAWS),
     (6, mv.FELL_STINGER), (9, mv.POISON_FANG), (12, mv.BITE),
     (15, mv.TOXIC_SPIKES), (18, mv.BUG_BITE), (21, mv.VENOSHOCK),
     (24, mv.KNOCK_OFF), (27, mv.SCARY_FACE), (30, mv.PIN_MISSILE),
     (33, mv.TOXIC), (36, mv.NIGHT_SLASH), (39, mv.CROSS_POISON),
     (42, mv.X_SCISSOR), (45, mv.ACUPRESSURE), (48, mv.CRUNCH)),
    DRAPION, 40, True, "")

TOXICROAK = Pokemon(
    454, "Toxicroak", 4, False,
    "", ("Poison", "Fighting"),
    83, 96, 65, 85,
    ((1, mv.ASTONISH), (1, mv.MUD_SLAP), (1, mv.POISON_STING), (1, mv.TAUNT),
     (12, mv.FLATTER), (16, mv.LOW_KICK), (20, mv.VENOSHOCK),
     (24, mv.SUCKER_PUNCH), (28, mv.SWAGGER), (32, mv.POISON_JAB),
     (36, mv.TOXIC), (42, mv.NASTY_PLOT), (48, mv.SLUDGE_BOMB),
     (54, mv.BELCH)),
    None, 0, False, "")

CROAGUNK = Pokemon(
    453, "Croagunk", 4, False,
    "", ("Poison", "Fighting"),
    48, 61, 40, 50,
    ((1, mv.MUD_SLAP), (1, mv.POISON_STING), (4, mv.ASTONISH), (8, mv.TAUNT),
     (12, mv.FLATTER), (16, mv.LOW_KICK), (20, mv.VENOSHOCK),
     (24, mv.SUCKER_PUNCH), (28, mv.SWAGGER), (32, mv.POISON_JAB),
     (36, mv.TOXIC), (40, mv.NASTY_PLOT), (44, mv.SLUDGE_BOMB),
     (48, mv.BELCH)),
    TOXICROAK, 37, True, "")

CARNIVINE = Pokemon(
    455, "Carnivine", 4, False,
    "", ("Grass",),
    74, 95, 72, 46,
    ((1, mv.BIND), (1, mv.GROWTH), (7, mv.BITE), (11, mv.VINE_WHIP),
     (17, mv.SWEET_SCENT), (21, mv.INGRAIN), (27, mv.FEINT_ATTACK),
     (31, mv.LEAF_TORNADO), (37, mv.SPIT_UP), (37, mv.STOCKPILE),
     (37, mv.SWALLOW), (41, mv.CRUNCH), (47, mv.WRING_OUT),
     (50, mv.POWER_WHIP)),
    None, 0, False, "")

LUMINEON = Pokemon(
    457, "Lumineon", 4, False,
    "", ("Water",),
    69, 69, 81, 91,
    ((1, mv.GUST), (1, mv.POUND), (1, mv.SOAK), (1, mv.WATER_GUN),
     (13, mv.RAIN_DANCE), (22, mv.WATER_PULSE), (26, mv.ATTRACT),
     (29, mv.SAFEGUARD), (35, mv.AQUA_RING), (42, mv.WHIRLPOOL),
     (48, mv.U_TURN), (53, mv.BOUNCE), (59, mv.TAILWIND)),
    None, 0, False, "")

FINNEON = Pokemon(
    456, "Finneon", 4, False,
    "", ("Water",),
    49, 49, 58, 66,
    ((1, mv.POUND), (6, mv.WATER_GUN), (13, mv.RAIN_DANCE), (17, mv.GUST),
     (22, mv.WATER_PULSE), (26, mv.ATTRACT), (29, mv.SAFEGUARD),
     (33, mv.AQUA_RING), (38, mv.WHIRLPOOL), (42, mv.U_TURN), (45, mv.BOUNCE),
     (49, mv.TAILWIND), (54, mv.SOAK)),
    LUMINEON, 31, True, "")

MANTYKE = Pokemon(
    458, "Mantyke", 4, False,
    "", ("Water", "Flying"),
    45, 40, 85, 50,
    ((1, mv.TACKLE), (1, mv.WATER_GUN), (4, mv.SUPERSONIC),
     (8, mv.WING_ATTACK), (12, mv.WATER_PULSE), (16, mv.WIDE_GUARD),
     (20, mv.AGILITY), (24, mv.BUBBLE_BEAM), (28, mv.HEADBUTT),
     (32, mv.AIR_SLASH), (36, mv.AQUA_RING), (40, mv.BOUNCE),
     (44, mv.TAKE_DOWN), (48, mv.HYDRO_PUMP)),
    MANTINE, 0, True, "level-up")

ABOMASNOW = Pokemon(
    460, "Abomasnow", 4, False,
    "", ("Grass", "Ice"),
    90, 92, 80, 60,
    ((0, mv.ICE_PUNCH), (1, mv.AURORA_VEIL), (1, mv.LEAFAGE), (1, mv.LEER),
     (1, mv.MIST), (1, mv.POWDER_SNOW), (15, mv.ICE_SHARD),
     (20, mv.RAZOR_LEAF), (25, mv.ICY_WIND), (30, mv.SWAGGER),
     (35, mv.INGRAIN), (43, mv.WOOD_HAMMER), (49, mv.BLIZZARD),
     (56, mv.SHEER_COLD)),
    None, 0, False, "")

SNOVER = Pokemon(
    459, "Snover", 4, False,
    "", ("Grass", "Ice"),
    60, 62, 55, 40,
    ((1, mv.LEER), (1, mv.POWDER_SNOW), (5, mv.LEAFAGE), (10, mv.MIST),
     (15, mv.ICE_SHARD), (20, mv.RAZOR_LEAF), (25, mv.ICY_WIND),
     (30, mv.SWAGGER), (35, mv.INGRAIN), (41, mv.WOOD_HAMMER),
     (45, mv.BLIZZARD), (50, mv.SHEER_COLD)),
    ABOMASNOW, 40, True, "")

LEAFEON = Pokemon(
    470, "Leafeon", 4, False,
    "", ("Grass",),
    65, 85, 97, 95,
    ((0, mv.RAZOR_LEAF), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.LEECH_SEED), (25, mv.MAGICAL_LEAF),
     (30, mv.SYNTHESIS), (35, mv.SUNNY_DAY), (40, mv.GIGA_DRAIN),
     (45, mv.SWORDS_DANCE), (50, mv.LEAF_BLADE), (55, mv.LAST_RESORT)),
    None, 0, False, "")

GLACEON = Pokemon(
    471, "Glaceon", 4, False,
    "", ("Ice",),
    65, 95, 102, 65,
    ((0, mv.ICY_WIND), (1, mv.BATON_PASS), (1, mv.CHARM), (1, mv.COPYCAT),
     (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL), (1, mv.HELPING_HAND),
     (1, mv.SWIFT), (1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.TAKE_DOWN),
     (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK), (15, mv.BABY_DOLL_EYES),
     (20, mv.ICE_SHARD), (25, mv.BITE), (30, mv.ICE_FANG), (35, mv.SNOWSCAPE),
     (40, mv.FREEZE_DRY), (45, mv.MIRROR_COAT), (50, mv.BLIZZARD),
     (55, mv.LAST_RESORT)),
    None, 0, False, "")

ROTOM = Pokemon(
    479, "Rotom", 4, False,
    "", ("Electric", "Ghost"),
    50, 72, 77, 91,
    ((1, mv.ASTONISH), (1, mv.DOUBLE_TEAM), (5, mv.THUNDER_SHOCK),
     (10, mv.CONFUSE_RAY), (15, mv.CHARGE), (20, mv.ELECTRO_BALL),
     (25, mv.THUNDER_WAVE), (30, mv.SHOCK_WAVE), (35, mv.HEX),
     (40, mv.SUBSTITUTE), (45, mv.TRICK), (50, mv.DISCHARGE), (55, mv.UPROAR)),
    None, 0, False, "")

UXIE = Pokemon(
    480, "Uxie", 4, False,
    "", ("Psychic",),
    75, 75, 130, 95,
    ((1, mv.CONFUSION), (1, mv.REST), (7, mv.SWIFT), (14, mv.ENDURE),
     (21, mv.PSYBEAM), (28, mv.IMPRISON), (35, mv.EXTRASENSORY),
     (42, mv.AMNESIA), (49, mv.PSYCHIC), (56, mv.YAWN), (63, mv.FUTURE_SIGHT),
     (70, mv.FLAIL), (77, mv.MEMENTO), (84, mv.MYSTICAL_POWER)),
    None, 0, False, "")

MESPRIT = Pokemon(
    481, "Mesprit", 4, False,
    "", ("Psychic",),
    80, 105, 105, 80,
    ((1, mv.CONFUSION), (1, mv.REST), (7, mv.SWIFT), (14, mv.PROTECT),
     (21, mv.PSYBEAM), (28, mv.IMPRISON), (35, mv.EXTRASENSORY),
     (42, mv.CHARM), (49, mv.PSYCHIC), (56, mv.FLATTER), (63, mv.FUTURE_SIGHT),
     (70, mv.COPYCAT), (77, mv.HEALING_WISH), (84, mv.MYSTICAL_POWER)),
    None, 0, False, "")

AZELF = Pokemon(
    482, "Azelf", 4, False,
    "", ("Psychic",),
    75, 125, 70, 115,
    ((1, mv.CONFUSION), (1, mv.REST), (7, mv.SWIFT), (14, mv.DETECT),
     (21, mv.PSYBEAM), (28, mv.IMPRISON), (35, mv.EXTRASENSORY),
     (42, mv.NASTY_PLOT), (49, mv.PSYCHIC), (56, mv.UPROAR),
     (63, mv.FUTURE_SIGHT), (70, mv.LAST_RESORT), (77, mv.EXPLOSION),
     (84, mv.MYSTICAL_POWER)),
    None, 0, False, "")

DIALGA = Pokemon(
    483, "Dialga", 4, False,
    "", ("Steel", "Dragon"),
    100, 135, 110, 90,
    ((1, mv.METAL_CLAW), (1, mv.SCARY_FACE), (8, mv.DRAGON_BREATH),
     (16, mv.ANCIENT_POWER), (24, mv.SLASH), (32, mv.FLASH_CANNON),
     (40, mv.DRAGON_CLAW), (48, mv.AURA_SPHERE), (56, mv.POWER_GEM),
     (64, mv.METAL_BURST), (72, mv.EARTH_POWER), (80, mv.IRON_TAIL),
     (88, mv.ROAR_OF_TIME)),
    None, 0, False, "")

PALKIA = Pokemon(
    484, "Palkia", 4, False,
    "", ("Water", "Dragon"),
    90, 135, 110, 100,
    ((1, mv.SCARY_FACE), (1, mv.WATER_PULSE), (8, mv.DRAGON_BREATH),
     (16, mv.ANCIENT_POWER), (24, mv.SLASH), (32, mv.AQUA_RING),
     (48, mv.AURA_SPHERE), (56, mv.POWER_GEM), (64, mv.AQUA_TAIL),
     (72, mv.EARTH_POWER), (80, mv.SPACIAL_REND), (88, mv.HYDRO_PUMP)),
    None, 0, False, "")

HEATRAN = Pokemon(
    485, "Heatran", 4, False,
    "", ("Fire", "Steel"),
    91, 110, 106, 77,
    ((1, mv.FIRE_SPIN), (1, mv.LEER), (6, mv.METAL_CLAW),
     (12, mv.ANCIENT_POWER), (18, mv.FIRE_FANG), (24, mv.SCARY_FACE),
     (30, mv.IRON_HEAD), (36, mv.CRUNCH), (42, mv.LAVA_PLUME),
     (48, mv.METAL_SOUND), (54, mv.EARTH_POWER), (60, mv.HEAT_WAVE),
     (66, mv.STONE_EDGE), (72, mv.MAGMA_STORM)),
    None, 0, False, "")

REGIGIGAS = Pokemon(
    486, "Regigigas", 4, False,
    "", ("Normal",),
    110, 120, 110, 100,
    ((1, mv.CONFUSE_RAY), (1, mv.POUND), (6, mv.PAYBACK), (12, mv.FACADE),
     (18, mv.STOMP), (24, mv.PROTECT), (30, mv.KNOCK_OFF), (36, mv.MEGA_PUNCH),
     (42, mv.BODY_PRESS), (48, mv.WIDE_GUARD), (54, mv.ZEN_HEADBUTT),
     (60, mv.HEAVY_SLAM), (66, mv.HAMMER_ARM), (72, mv.GIGA_IMPACT),
     (78, mv.CRUSH_GRIP)),
    None, 0, False, "")

GIRATINA = Pokemon(
    487, "Giratina", 4, False,
    "", ("Ghost", "Dragon"),
    150, 100, 120, 90,
    ((1, mv.DEFOG), (1, mv.SHADOW_SNEAK), (7, mv.DRAGON_BREATH),
     (14, mv.ANCIENT_POWER), (21, mv.HEX), (28, mv.SLASH), (35, mv.SCARY_FACE),
     (42, mv.SHADOW_CLAW), (49, mv.PAIN_SPLIT), (56, mv.AURA_SPHERE),
     (63, mv.DRAGON_CLAW), (70, mv.EARTH_POWER), (77, mv.SHADOW_FORCE),
     (84, mv.DESTINY_BOND)),
    None, 0, False, "")

CRESSELIA = Pokemon(
    488, "Cresselia", 4, False,
    "", ("Psychic",),
    120, 72, 125, 85,
    ((1, mv.CONFUSION), (1, mv.DOUBLE_TEAM), (6, mv.MIST),
     (12, mv.AURORA_BEAM), (18, mv.PSYBEAM), (24, mv.ALLY_SWITCH),
     (30, mv.SLASH), (36, mv.PSYCHO_CUT), (42, mv.MOONLIGHT),
     (48, mv.SAFEGUARD), (54, mv.PSYCHIC), (60, mv.MOONBLAST),
     (66, mv.FUTURE_SIGHT), (72, mv.LUNAR_BLESSING), (72, mv.LUNAR_DANCE)),
    None, 0, False, "")

MANAPHY = Pokemon(
    490, "Manaphy", 4, False,
    "", ("Water",),
    100, 100, 100, 100,
    ((1, mv.HEART_SWAP), (1, mv.TAIL_GLOW), (1, mv.WATER_GUN), (9, mv.CHARM),
     (16, mv.SUPERSONIC), (24, mv.BUBBLE_BEAM), (31, mv.ACID_ARMOR),
     (39, mv.WHIRLPOOL), (46, mv.WATER_PULSE), (54, mv.AQUA_RING),
     (61, mv.DIVE), (69, mv.RAIN_DANCE), (76, mv.TAKE_HEART)),
    None, 0, False, "")

PHIONE = Pokemon(
    489, "Phione", 4, False,
    "", ("Water",),
    80, 80, 80, 80,
    ((1, mv.WATER_GUN), (9, mv.CHARM), (16, mv.SUPERSONIC),
     (24, mv.BUBBLE_BEAM), (31, mv.ACID_ARMOR), (39, mv.WHIRLPOOL),
     (46, mv.WATER_PULSE), (54, mv.AQUA_RING), (61, mv.DIVE),
     (69, mv.RAIN_DANCE), (75, mv.TAKE_HEART)),
    MANAPHY, 0, True, "Breed with Ditto")

DARKRAI = Pokemon(
    491, "Darkrai", 4, False,
    "", ("Dark",),
    70, 112, 90, 125,
    ((1, mv.DISABLE), (11, mv.QUICK_ATTACK), (20, mv.HYPNOSIS),
     (29, mv.SUCKER_PUNCH), (38, mv.NIGHT_SHADE), (47, mv.DOUBLE_TEAM),
     (57, mv.HAZE), (66, mv.DARK_VOID), (75, mv.NASTY_PLOT),
     (84, mv.DREAM_EATER), (93, mv.DARK_PULSE)),
    None, 0, False, "")

SHAYMIN = Pokemon(
    492, "Shaymin", 4, False,
    "", ("Grass",),
    100, 100, 100, 100,
    ((1, mv.GROWTH), (10, mv.MAGICAL_LEAF), (19, mv.LEECH_SEED),
     (28, mv.SYNTHESIS), (37, mv.SWEET_SCENT), (46, mv.PLAY_ROUGH),
     (55, mv.WORRY_SEED), (64, mv.GRASSY_TERRAIN), (73, mv.ENERGY_BALL),
     (82, mv.SWEET_KISS), (91, mv.HEALING_WISH), (100, mv.SEED_FLARE)),
    None, 0, False, "")

ARCEUS = Pokemon(
    493, "Arceus", 4, False,
    "", ("Normal",),
    120, 120, 120, 120,
    ((1, mv.COSMIC_POWER), (1, mv.SEISMIC_TOSS), (10, mv.GRAVITY),
     (20, mv.EARTH_POWER), (30, mv.HYPER_VOICE), (40, mv.EXTREME_SPEED),
     (50, mv.HEALING_WISH), (60, mv.FUTURE_SIGHT), (70, mv.RECOVER),
     (80, mv.HYPER_BEAM), (90, mv.PERISH_SONG), (100, mv.JUDGMENT)),
    None, 0, False, "")


# --- generation 5 ---

VICTINI = Pokemon(
    494, "Victini", 5, False,
    "", ("Psychic", "Fire"),
    100, 100, 100, 100,
    ((1, mv.CONFUSION), (1, mv.FLAME_CHARGE), (1, mv.FOCUS_ENERGY),
     (1, mv.QUICK_ATTACK), (1, mv.V_CREATE), (7, mv.WORK_UP),
     (14, mv.INCINERATE), (21, mv.STORED_POWER), (28, mv.HEADBUTT),
     (35, mv.ENDURE), (42, mv.ZEN_HEADBUTT), (49, mv.INFERNO),
     (56, mv.REVERSAL), (63, mv.SEARING_SHOT), (70, mv.DOUBLE_EDGE),
     (77, mv.FLARE_BLITZ), (84, mv.OVERHEAT), (91, mv.FINAL_GAMBIT)),
    None, 0, False, "")

SERPERIOR = Pokemon(
    497, "Serperior", 5, True,
    "Flora", ("Grass",),
    75, 75, 95, 113,
    ((1, mv.LEER), (1, mv.TACKLE), (1, mv.VINE_WHIP), (1, mv.WRAP),
     (13, mv.GROWTH), (16, mv.MAGICAL_LEAF), (20, mv.LEECH_SEED),
     (24, mv.MEGA_DRAIN), (28, mv.SLAM), (32, mv.LEAF_BLADE), (38, mv.COIL),
     (44, mv.GIGA_DRAIN), (50, mv.GASTRO_ACID), (56, mv.LEAF_STORM)),
    None, 0, False, "")

SERVINE = Pokemon(
    496, "Servine", 5, True,
    "Flora", ("Grass",),
    60, 60, 75, 83,
    ((1, mv.LEER), (1, mv.TACKLE), (1, mv.VINE_WHIP), (1, mv.WRAP),
     (13, mv.GROWTH), (16, mv.MAGICAL_LEAF), (20, mv.LEECH_SEED),
     (24, mv.MEGA_DRAIN), (28, mv.SLAM), (32, mv.LEAF_BLADE), (36, mv.COIL),
     (40, mv.GIGA_DRAIN), (44, mv.GASTRO_ACID), (48, mv.LEAF_STORM)),
    SERPERIOR, 36, True, "")

SNIVY = Pokemon(
    495, "Snivy", 5, True,
    "Flora", ("Grass",),
    45, 45, 55, 63,
    ((1, mv.TACKLE), (4, mv.LEER), (7, mv.VINE_WHIP), (10, mv.WRAP),
     (13, mv.GROWTH), (16, mv.MAGICAL_LEAF), (19, mv.LEECH_SEED),
     (22, mv.MEGA_DRAIN), (25, mv.SLAM), (28, mv.LEAF_BLADE), (31, mv.COIL),
     (34, mv.GIGA_DRAIN), (37, mv.GASTRO_ACID), (40, mv.LEAF_STORM)),
    SERVINE, 17, True, "")

EMBOAR = Pokemon(
    500, "Emboar", 5, True,
    "Flame", ("Fire", "Fighting"),
    110, 111, 65, 65,
    ((1, mv.ARM_THRUST), (1, mv.EMBER), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (13, mv.DEFENSE_CURL), (15, mv.FLAME_CHARGE), (20, mv.SMOG),
     (23, mv.ROLLOUT), (28, mv.TAKE_DOWN), (31, mv.HEAT_CRASH),
     (38, mv.ASSURANCE), (43, mv.FLAMETHROWER), (50, mv.HEAD_SMASH),
     (55, mv.ROAR), (62, mv.FLARE_BLITZ)),
    None, 0, False, "")

PIGNITE = Pokemon(
    499, "Pignite", 5, True,
    "Flame", ("Fire", "Fighting"),
    90, 81, 55, 55,
    ((0, mv.ARM_THRUST), (1, mv.EMBER), (1, mv.ENDURE), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (13, mv.DEFENSE_CURL), (15, mv.FLAME_CHARGE),
     (20, mv.SMOG), (23, mv.ROLLOUT), (28, mv.TAKE_DOWN), (31, mv.HEAT_CRASH),
     (36, mv.ASSURANCE), (39, mv.FLAMETHROWER), (44, mv.HEAD_SMASH),
     (47, mv.ROAR), (52, mv.FLARE_BLITZ)),
    EMBOAR, 36, True, "")

TEPIG = Pokemon(
    498, "Tepig", 5, True,
    "Flame", ("Fire",),
    65, 54, 45, 45,
    ((1, mv.TACKLE), (3, mv.TAIL_WHIP), (7, mv.EMBER), (9, mv.ENDURE),
     (13, mv.DEFENSE_CURL), (15, mv.FLAME_CHARGE), (19, mv.SMOG),
     (21, mv.ROLLOUT), (25, mv.TAKE_DOWN), (27, mv.HEAT_CRASH),
     (31, mv.ASSURANCE), (33, mv.FLAMETHROWER), (37, mv.HEAD_SMASH),
     (39, mv.ROAR), (43, mv.FLARE_BLITZ)),
    PIGNITE, 17, True, "")

SAMUROTT = Pokemon(
    503, "Samurott", 5, True,
    "Aqua", ("Water",),
    95, 104, 77, 70,
    ((0, mv.SLASH), (1, mv.MEGAHORN), (1, mv.SOAK), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (13, mv.FOCUS_ENERGY),
     (18, mv.RAZOR_SHELL), (21, mv.FURY_CUTTER), (25, mv.WATER_PULSE),
     (29, mv.AERIAL_ACE), (34, mv.AQUA_JET), (39, mv.ENCORE),
     (46, mv.AQUA_TAIL), (51, mv.RETALIATE), (58, mv.SWORDS_DANCE),
     (63, mv.HYDRO_PUMP)),
    None, 0, False, "")

DEWOTT = Pokemon(
    502, "Dewott", 5, True,
    "Aqua", ("Water",),
    75, 79, 60, 60,
    ((1, mv.SOAK), (1, mv.TACKLE), (1, mv.TAIL_WHIP), (1, mv.WATER_GUN),
     (13, mv.FOCUS_ENERGY), (18, mv.RAZOR_SHELL), (21, mv.FURY_CUTTER),
     (26, mv.WATER_PULSE), (29, mv.AERIAL_ACE), (34, mv.AQUA_JET),
     (37, mv.ENCORE), (42, mv.AQUA_TAIL), (45, mv.RETALIATE),
     (50, mv.SWORDS_DANCE), (53, mv.HYDRO_PUMP)),
    SAMUROTT, 36, True, "")

OSHAWOTT = Pokemon(
    501, "Oshawott", 5, True,
    "Aqua", ("Water",),
    55, 59, 45, 45,
    ((1, mv.TACKLE), (5, mv.TAIL_WHIP), (7, mv.WATER_GUN), (11, mv.SOAK),
     (13, mv.FOCUS_ENERGY), (17, mv.RAZOR_SHELL), (19, mv.FURY_CUTTER),
     (23, mv.WATER_PULSE), (25, mv.AERIAL_ACE), (29, mv.AQUA_JET),
     (31, mv.ENCORE), (35, mv.AQUA_TAIL), (37, mv.RETALIATE),
     (41, mv.SWORDS_DANCE), (43, mv.HYDRO_PUMP)),
    DEWOTT, 17, True, "")

WATCHOG = Pokemon(
    505, "Watchog", 5, False,
    "", ("Normal",),
    60, 72, 69, 77,
    ((1, mv.CONFUSE_RAY), (1, mv.LEER), (1, mv.LOW_KICK), (1, mv.ROTOTILLER),
     (1, mv.TACKLE), (6, mv.BITE), (8, mv.BIDE), (11, mv.DETECT),
     (13, mv.SAND_ATTACK), (16, mv.CRUNCH), (18, mv.HYPNOSIS),
     (22, mv.SUPER_FANG), (25, mv.AFTER_YOU), (29, mv.FOCUS_ENERGY),
     (32, mv.PSYCH_UP), (36, mv.HYPER_FANG), (39, mv.NASTY_PLOT),
     (43, mv.MEAN_LOOK), (46, mv.BATON_PASS), (50, mv.SLAM)),
    None, 0, False, "")

PATRAT = Pokemon(
    504, "Patrat", 5, False,
    "", ("Normal",),
    45, 45, 39, 42,
    ((1, mv.TACKLE), (3, mv.LEER), (6, mv.BITE), (8, mv.BIDE), (11, mv.DETECT),
     (13, mv.SAND_ATTACK), (16, mv.CRUNCH), (18, mv.HYPNOSIS),
     (21, mv.SUPER_FANG), (23, mv.AFTER_YOU), (26, mv.FOCUS_ENERGY),
     (28, mv.WORK_UP), (31, mv.HYPER_FANG), (33, mv.NASTY_PLOT),
     (36, mv.MEAN_LOOK), (38, mv.BATON_PASS), (41, mv.SLAM)),
    WATCHOG, 20, True, "")

STOUTLAND = Pokemon(
    508, "Stoutland", 5, False,
    "", ("Normal",),
    85, 77, 90, 80,
    ((1, mv.BITE), (1, mv.FIRE_FANG), (1, mv.ICE_FANG), (1, mv.LEER),
     (1, mv.TACKLE), (1, mv.THUNDER_FANG), (1, mv.WORK_UP), (12, mv.RETALIATE),
     (19, mv.BABY_DOLL_EYES), (24, mv.PLAY_ROUGH), (30, mv.CRUNCH),
     (38, mv.TAKE_DOWN), (46, mv.HELPING_HAND), (54, mv.REVERSAL),
     (62, mv.ROAR), (70, mv.LAST_RESORT), (78, mv.GIGA_IMPACT)),
    None, 0, False, "")

HERDIER = Pokemon(
    507, "Herdier", 5, False,
    "", ("Normal",),
    65, 57, 65, 60,
    ((1, mv.BITE), (1, mv.LEER), (1, mv.TACKLE), (1, mv.WORK_UP),
     (12, mv.RETALIATE), (19, mv.BABY_DOLL_EYES), (24, mv.PLAY_ROUGH),
     (30, mv.CRUNCH), (36, mv.TAKE_DOWN), (42, mv.HELPING_HAND),
     (48, mv.REVERSAL), (54, mv.ROAR), (60, mv.LAST_RESORT),
     (66, mv.GIGA_IMPACT)),
    STOUTLAND, 32, True, "")

LILLIPUP = Pokemon(
    506, "Lillipup", 5, False,
    "", ("Normal",),
    45, 42, 45, 55,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.WORK_UP), (8, mv.BITE),
     (12, mv.RETALIATE), (17, mv.BABY_DOLL_EYES), (20, mv.PLAY_ROUGH),
     (24, mv.CRUNCH), (28, mv.TAKE_DOWN), (32, mv.HELPING_HAND),
     (36, mv.REVERSAL), (40, mv.ROAR), (44, mv.LAST_RESORT),
     (48, mv.GIGA_IMPACT)),
    HERDIER, 16, True, "")

LIEPARD = Pokemon(
    510, "Liepard", 5, False,
    "", ("Dark",),
    64, 88, 50, 106,
    ((1, mv.FAKE_OUT), (1, mv.GROWL), (1, mv.SAND_ATTACK), (1, mv.SCRATCH),
     (12, mv.FURY_SWIPES), (16, mv.TORMENT), (23, mv.ASSURANCE),
     (28, mv.HONE_CLAWS), (34, mv.SUCKER_PUNCH), (40, mv.NASTY_PLOT),
     (46, mv.NIGHT_SLASH), (52, mv.PLAY_ROUGH)),
    None, 0, False, "")

PURRLOIN = Pokemon(
    509, "Purrloin", 5, False,
    "", ("Dark",),
    41, 50, 37, 66,
    ((1, mv.GROWL), (1, mv.SCRATCH), (4, mv.SAND_ATTACK), (5, mv.FAKE_OUT),
     (12, mv.FURY_SWIPES), (16, mv.TORMENT), (21, mv.ASSURANCE),
     (24, mv.HONE_CLAWS), (28, mv.SUCKER_PUNCH), (32, mv.NASTY_PLOT),
     (36, mv.NIGHT_SLASH), (40, mv.PLAY_ROUGH)),
    LIEPARD, 20, True, "")

SIMISAGE = Pokemon(
    512, "Simisage", 5, False,
    "", ("Grass",),
    75, 98, 63, 101,
    ((1, mv.FURY_SWIPES), (1, mv.LEER), (1, mv.LICK), (1, mv.SEED_BOMB)),
    None, 0, False, "")

PANSAGE = Pokemon(
    511, "Pansage", 5, False,
    "", ("Grass",),
    50, 53, 48, 64,
    ((1, mv.PLAY_NICE), (1, mv.SCRATCH), (4, mv.LEER), (7, mv.LICK),
     (10, mv.VINE_WHIP), (13, mv.FURY_SWIPES), (16, mv.LEECH_SEED),
     (19, mv.BITE), (22, mv.SEED_BOMB), (25, mv.TORMENT), (28, mv.FLING),
     (31, mv.ACROBATICS), (34, mv.GRASS_KNOT), (37, mv.RECYCLE),
     (40, mv.NATURAL_GIFT), (43, mv.CRUNCH)),
    SIMISAGE, 0, True, "item:leaf-stone")

SIMISEAR = Pokemon(
    514, "Simisear", 5, False,
    "", ("Fire",),
    75, 98, 63, 101,
    ((1, mv.FLAME_BURST), (1, mv.FURY_SWIPES), (1, mv.LEER), (1, mv.LICK)),
    None, 0, False, "")

PANSEAR = Pokemon(
    513, "Pansear", 5, False,
    "", ("Fire",),
    50, 53, 48, 64,
    ((1, mv.PLAY_NICE), (1, mv.SCRATCH), (4, mv.LEER), (7, mv.LICK),
     (10, mv.INCINERATE), (13, mv.FURY_SWIPES), (16, mv.YAWN), (19, mv.BITE),
     (22, mv.FLAME_BURST), (25, mv.AMNESIA), (28, mv.FLING),
     (31, mv.ACROBATICS), (34, mv.FIRE_BLAST), (37, mv.RECYCLE),
     (40, mv.NATURAL_GIFT), (43, mv.CRUNCH)),
    SIMISEAR, 0, True, "item:fire-stone")

SIMIPOUR = Pokemon(
    516, "Simipour", 5, False,
    "", ("Water",),
    75, 98, 63, 101,
    ((1, mv.FURY_SWIPES), (1, mv.LEER), (1, mv.LICK), (1, mv.SCALD)),
    None, 0, False, "")

PANPOUR = Pokemon(
    515, "Panpour", 5, False,
    "", ("Water",),
    50, 53, 48, 64,
    ((1, mv.PLAY_NICE), (1, mv.SCRATCH), (4, mv.LEER), (7, mv.LICK),
     (10, mv.WATER_GUN), (13, mv.FURY_SWIPES), (16, mv.WATER_SPORT),
     (19, mv.BITE), (22, mv.SCALD), (25, mv.TAUNT), (28, mv.FLING),
     (31, mv.ACROBATICS), (34, mv.BRINE), (37, mv.RECYCLE),
     (40, mv.NATURAL_GIFT), (43, mv.CRUNCH)),
    SIMIPOUR, 0, True, "item:water-stone")

MUSHARNA = Pokemon(
    518, "Musharna", 5, False,
    "", ("Psychic",),
    116, 81, 90, 29,
    ((1, mv.CALM_MIND), (1, mv.DEFENSE_CURL), (1, mv.DREAM_EATER),
     (1, mv.FUTURE_SIGHT), (1, mv.HYPNOSIS), (1, mv.IMPRISON),
     (1, mv.MAGIC_COAT), (1, mv.MOONBLAST), (1, mv.MOONLIGHT), (1, mv.PSYBEAM),
     (1, mv.PSYCHIC), (1, mv.PSYCHIC_TERRAIN), (1, mv.STORED_POWER),
     (1, mv.WONDER_ROOM), (1, mv.YAWN), (1, mv.ZEN_HEADBUTT)),
    None, 0, False, "")

MUNNA = Pokemon(
    517, "Munna", 5, False,
    "", ("Psychic",),
    76, 46, 50, 24,
    ((1, mv.DEFENSE_CURL), (1, mv.STORED_POWER), (4, mv.HYPNOSIS),
     (8, mv.PSYBEAM), (12, mv.IMPRISON), (16, mv.MOONLIGHT),
     (20, mv.MAGIC_COAT), (24, mv.ZEN_HEADBUTT), (28, mv.CALM_MIND),
     (32, mv.YAWN), (36, mv.PSYCHIC), (40, mv.MOONBLAST), (44, mv.DREAM_EATER),
     (48, mv.FUTURE_SIGHT), (52, mv.WONDER_ROOM)),
    MUSHARNA, 0, True, "item:moon-stone")

UNFEZANT = Pokemon(
    521, "Unfezant", 5, False,
    "", ("Normal", "Flying"),
    80, 90, 67, 93,
    ((1, mv.GROWL), (1, mv.GUST), (1, mv.LEER), (1, mv.QUICK_ATTACK),
     (12, mv.TAUNT), (16, mv.AIR_CUTTER), (20, mv.SWAGGER),
     (26, mv.FEATHER_DANCE), (36, mv.DETECT), (42, mv.AIR_SLASH),
     (50, mv.ROOST), (58, mv.TAILWIND), (66, mv.SKY_ATTACK)),
    None, 0, False, "")

TRANQUILL = Pokemon(
    520, "Tranquill", 5, False,
    "", ("Normal", "Flying"),
    62, 63, 52, 65,
    ((1, mv.GROWL), (1, mv.GUST), (1, mv.LEER), (1, mv.QUICK_ATTACK),
     (12, mv.TAUNT), (16, mv.AIR_CUTTER), (20, mv.SWAGGER),
     (26, mv.FEATHER_DANCE), (34, mv.DETECT), (38, mv.AIR_SLASH),
     (44, mv.ROOST), (50, mv.TAILWIND), (56, mv.SKY_ATTACK)),
    UNFEZANT, 32, True, "")

PIDOVE = Pokemon(
    519, "Pidove", 5, False,
    "", ("Normal", "Flying"),
    50, 45, 40, 43,
    ((1, mv.GROWL), (1, mv.GUST), (4, mv.LEER), (8, mv.QUICK_ATTACK),
     (12, mv.TAUNT), (16, mv.AIR_CUTTER), (20, mv.SWAGGER),
     (24, mv.FEATHER_DANCE), (28, mv.DETECT), (32, mv.AIR_SLASH),
     (36, mv.ROOST), (40, mv.TAILWIND), (44, mv.SKY_ATTACK)),
    TRANQUILL, 21, True, "")

ZEBSTRIKA = Pokemon(
    523, "Zebstrika", 5, False,
    "", ("Electric",),
    75, 90, 63, 116,
    ((1, mv.CHARGE), (1, mv.QUICK_ATTACK), (1, mv.TAIL_WHIP),
     (1, mv.THUNDER_WAVE), (11, mv.SHOCK_WAVE), (18, mv.FLAME_CHARGE),
     (25, mv.SPARK), (31, mv.STOMP), (36, mv.DISCHARGE), (42, mv.AGILITY),
     (47, mv.WILD_CHARGE), (53, mv.THRASH)),
    None, 0, False, "")

BLITZLE = Pokemon(
    522, "Blitzle", 5, False,
    "", ("Electric",),
    45, 55, 32, 76,
    ((1, mv.QUICK_ATTACK), (4, mv.TAIL_WHIP), (8, mv.CHARGE),
     (11, mv.SHOCK_WAVE), (15, mv.THUNDER_WAVE), (18, mv.FLAME_CHARGE),
     (22, mv.SPARK), (25, mv.STOMP), (29, mv.DISCHARGE), (33, mv.AGILITY),
     (35, mv.WILD_CHARGE), (40, mv.THRASH)),
    ZEBSTRIKA, 27, True, "")

GIGALITH = Pokemon(
    526, "Gigalith", 5, False,
    "", ("Rock",),
    85, 97, 105, 25,
    ((1, mv.HARDEN), (1, mv.POWER_GEM), (1, mv.SAND_ATTACK),
     (1, mv.STEALTH_ROCK), (1, mv.TACKLE), (12, mv.MUD_SLAP),
     (16, mv.SMACK_DOWN), (20, mv.IRON_DEFENSE), (24, mv.HEADBUTT),
     (30, mv.ROCK_SLIDE), (36, mv.ROCK_BLAST), (42, mv.SANDSTORM),
     (48, mv.STONE_EDGE), (54, mv.EXPLOSION)),
    None, 0, False, "")

BOLDORE = Pokemon(
    525, "Boldore", 5, False,
    "", ("Rock",),
    70, 77, 72, 20,
    ((0, mv.POWER_GEM), (1, mv.HARDEN), (1, mv.SAND_ATTACK),
     (1, mv.STEALTH_ROCK), (1, mv.TACKLE), (12, mv.MUD_SLAP),
     (16, mv.SMACK_DOWN), (20, mv.IRON_DEFENSE), (24, mv.HEADBUTT),
     (30, mv.ROCK_SLIDE), (36, mv.ROCK_BLAST), (42, mv.SANDSTORM),
     (48, mv.STONE_EDGE), (54, mv.EXPLOSION)),
    GIGALITH, 0, True, "trade")

ROGGENROLA = Pokemon(
    524, "Roggenrola", 5, False,
    "", ("Rock",),
    55, 50, 55, 15,
    ((1, mv.SAND_ATTACK), (1, mv.TACKLE), (4, mv.HARDEN), (8, mv.STEALTH_ROCK),
     (12, mv.MUD_SLAP), (16, mv.SMACK_DOWN), (20, mv.IRON_DEFENSE),
     (24, mv.HEADBUTT), (28, mv.ROCK_SLIDE), (32, mv.ROCK_BLAST),
     (36, mv.SANDSTORM), (40, mv.STONE_EDGE), (44, mv.EXPLOSION)),
    BOLDORE, 25, True, "")

SWOOBAT = Pokemon(
    528, "Swoobat", 5, False,
    "", ("Psychic", "Flying"),
    67, 67, 55, 114,
    ((1, mv.ATTRACT), (1, mv.CONFUSION), (1, mv.ENDEAVOR), (1, mv.GUST),
     (15, mv.AIR_CUTTER), (20, mv.IMPRISON), (25, mv.ASSURANCE),
     (30, mv.AMNESIA), (35, mv.AIR_SLASH), (40, mv.PSYCHIC),
     (45, mv.CALM_MIND), (50, mv.FUTURE_SIGHT), (55, mv.SIMPLE_BEAM)),
    None, 0, False, "")

WOOBAT = Pokemon(
    527, "Woobat", 5, False,
    "", ("Psychic", "Flying"),
    65, 50, 43, 72,
    ((1, mv.ATTRACT), (1, mv.GUST), (5, mv.CONFUSION), (10, mv.ENDEAVOR),
     (15, mv.AIR_CUTTER), (20, mv.IMPRISON), (25, mv.ASSURANCE),
     (30, mv.AMNESIA), (35, mv.AIR_SLASH), (40, mv.PSYCHIC),
     (45, mv.CALM_MIND), (50, mv.FUTURE_SIGHT), (55, mv.SIMPLE_BEAM)),
    SWOOBAT, 0, True, "happiness")

EXCADRILL = Pokemon(
    530, "Excadrill", 5, False,
    "", ("Ground", "Steel"),
    110, 92, 62, 88,
    ((0, mv.HORN_DRILL), (1, mv.HONE_CLAWS), (1, mv.MUD_SLAP),
     (1, mv.RAPID_SPIN), (1, mv.SCRATCH), (12, mv.FURY_SWIPES),
     (16, mv.METAL_CLAW), (20, mv.SANDSTORM), (24, mv.CRUSH_CLAW),
     (28, mv.ROCK_SLIDE), (34, mv.DIG), (40, mv.SWORDS_DANCE),
     (46, mv.DRILL_RUN), (52, mv.EARTHQUAKE), (58, mv.FISSURE)),
    None, 0, False, "")

DRILBUR = Pokemon(
    529, "Drilbur", 5, False,
    "", ("Ground",),
    60, 57, 42, 68,
    ((1, mv.MUD_SLAP), (1, mv.RAPID_SPIN), (4, mv.SCRATCH), (8, mv.HONE_CLAWS),
     (12, mv.FURY_SWIPES), (16, mv.METAL_CLAW), (20, mv.SANDSTORM),
     (24, mv.CRUSH_CLAW), (28, mv.ROCK_SLIDE), (32, mv.DIG),
     (36, mv.SWORDS_DANCE), (40, mv.DRILL_RUN), (44, mv.EARTHQUAKE),
     (48, mv.FISSURE)),
    EXCADRILL, 31, True, "")

AUDINO = Pokemon(
    531, "Audino", 5, False,
    "", ("Normal",),
    103, 60, 86, 50,
    ((1, mv.PLAY_NICE), (1, mv.POUND), (4, mv.DISARMING_VOICE),
     (9, mv.BABY_DOLL_EYES), (12, mv.HELPING_HAND), (16, mv.GROWL),
     (20, mv.ZEN_HEADBUTT), (24, mv.LIFE_DEW), (28, mv.AFTER_YOU),
     (32, mv.TAKE_DOWN), (36, mv.SIMPLE_BEAM), (40, mv.HYPER_VOICE),
     (44, mv.HEAL_PULSE), (48, mv.DOUBLE_EDGE), (52, mv.ENTRAINMENT),
     (56, mv.MISTY_TERRAIN), (60, mv.LAST_RESORT)),
    None, 0, False, "")

CONKELDURR = Pokemon(
    534, "Conkeldurr", 5, False,
    "", ("Fighting",),
    105, 97, 80, 45,
    ((1, mv.LEER), (1, mv.LOW_KICK), (1, mv.POUND), (1, mv.ROCK_THROW),
     (12, mv.FOCUS_ENERGY), (16, mv.BULK_UP), (20, mv.ROCK_SLIDE),
     (24, mv.SLAM), (30, mv.SCARY_FACE), (36, mv.DYNAMIC_PUNCH),
     (42, mv.HAMMER_ARM), (48, mv.STONE_EDGE), (54, mv.SUPERPOWER),
     (60, mv.FOCUS_PUNCH)),
    None, 0, False, "")

GURDURR = Pokemon(
    533, "Gurdurr", 5, False,
    "", ("Fighting",),
    85, 72, 67, 40,
    ((1, mv.LEER), (1, mv.LOW_KICK), (1, mv.POUND), (1, mv.ROCK_THROW),
     (12, mv.FOCUS_ENERGY), (16, mv.BULK_UP), (20, mv.ROCK_SLIDE),
     (24, mv.SLAM), (30, mv.SCARY_FACE), (36, mv.DYNAMIC_PUNCH),
     (42, mv.HAMMER_ARM), (48, mv.STONE_EDGE), (54, mv.SUPERPOWER),
     (60, mv.FOCUS_PUNCH)),
    CONKELDURR, 0, True, "trade")

TIMBURR = Pokemon(
    532, "Timburr", 5, False,
    "", ("Fighting",),
    75, 52, 45, 35,
    ((1, mv.LEER), (1, mv.POUND), (4, mv.LOW_KICK), (8, mv.ROCK_THROW),
     (12, mv.FOCUS_ENERGY), (16, mv.BULK_UP), (20, mv.ROCK_SLIDE),
     (24, mv.SLAM), (28, mv.SCARY_FACE), (32, mv.DYNAMIC_PUNCH),
     (36, mv.HAMMER_ARM), (40, mv.STONE_EDGE), (44, mv.SUPERPOWER),
     (48, mv.FOCUS_PUNCH)),
    GURDURR, 25, True, "")

SEISMITOAD = Pokemon(
    537, "Seismitoad", 5, False,
    "", ("Water", "Ground"),
    105, 90, 75, 74,
    ((1, mv.ACID), (1, mv.DRAIN_PUNCH), (1, mv.ECHOED_VOICE),
     (1, mv.GASTRO_ACID), (1, mv.GROWL), (1, mv.SUPERSONIC), (12, mv.MUD_SHOT),
     (16, mv.ROUND), (20, mv.BUBBLE_BEAM), (24, mv.FLAIL), (30, mv.UPROAR),
     (39, mv.AQUA_RING), (46, mv.HYPER_VOICE), (54, mv.MUDDY_WATER),
     (62, mv.RAIN_DANCE), (70, mv.HYDRO_PUMP)),
    None, 0, False, "")

PALPITOAD = Pokemon(
    536, "Palpitoad", 5, False,
    "", ("Water", "Ground"),
    75, 65, 55, 69,
    ((1, mv.ACID), (1, mv.ECHOED_VOICE), (1, mv.GROWL), (1, mv.SUPERSONIC),
     (12, mv.MUD_SHOT), (16, mv.ROUND), (20, mv.BUBBLE_BEAM), (24, mv.FLAIL),
     (30, mv.UPROAR), (37, mv.AQUA_RING), (42, mv.HYPER_VOICE),
     (48, mv.MUDDY_WATER), (54, mv.RAIN_DANCE), (60, mv.HYDRO_PUMP)),
    SEISMITOAD, 36, True, "")

TYMPOLE = Pokemon(
    535, "Tympole", 5, False,
    "", ("Water",),
    50, 50, 40, 64,
    ((1, mv.ECHOED_VOICE), (1, mv.GROWL), (4, mv.ACID), (8, mv.SUPERSONIC),
     (12, mv.MUD_SHOT), (16, mv.ROUND), (20, mv.BUBBLE_BEAM), (24, mv.FLAIL),
     (28, mv.UPROAR), (32, mv.AQUA_RING), (36, mv.HYPER_VOICE),
     (40, mv.MUDDY_WATER), (44, mv.RAIN_DANCE), (48, mv.HYDRO_PUMP)),
    PALPITOAD, 25, True, "")

THROH = Pokemon(
    538, "Throh", 5, False,
    "", ("Fighting",),
    120, 65, 85, 45,
    ((1, mv.BIND), (1, mv.LEER), (5, mv.FOCUS_ENERGY), (10, mv.CIRCLE_THROW),
     (15, mv.WIDE_GUARD), (20, mv.REVENGE), (25, mv.BULK_UP),
     (30, mv.STORM_THROW), (35, mv.VITAL_THROW), (40, mv.SEISMIC_TOSS),
     (45, mv.ENDURE), (50, mv.REVERSAL), (55, mv.SUPERPOWER)),
    None, 0, False, "")

SAWK = Pokemon(
    539, "Sawk", 5, False,
    "", ("Fighting",),
    75, 77, 75, 85,
    ((1, mv.LEER), (1, mv.ROCK_SMASH), (5, mv.FOCUS_ENERGY),
     (10, mv.DOUBLE_KICK), (15, mv.QUICK_GUARD), (20, mv.LOW_SWEEP),
     (25, mv.BULK_UP), (30, mv.RETALIATE), (35, mv.BRICK_BREAK),
     (40, mv.COUNTER), (45, mv.ENDURE), (50, mv.REVERSAL),
     (55, mv.CLOSE_COMBAT)),
    None, 0, False, "")

LEAVANNY = Pokemon(
    542, "Leavanny", 5, False,
    "", ("Bug", "Grass"),
    75, 86, 80, 92,
    ((0, mv.SLASH), (1, mv.FALSE_SWIPE), (1, mv.RAZOR_LEAF),
     (1, mv.STRING_SHOT), (1, mv.TACKLE), (22, mv.STRUGGLE_BUG),
     (29, mv.FELL_STINGER), (32, mv.HELPING_HAND), (36, mv.LEAF_BLADE),
     (39, mv.X_SCISSOR), (43, mv.ENTRAINMENT), (46, mv.SWORDS_DANCE),
     (50, mv.LEAF_STORM)),
    None, 0, False, "")

SWADLOON = Pokemon(
    541, "Swadloon", 5, False,
    "", ("Bug", "Grass"),
    55, 56, 85, 42,
    ((0, mv.PROTECT), (1, mv.BUG_BITE), (1, mv.RAZOR_LEAF),
     (1, mv.STRING_SHOT), (1, mv.TACKLE), (22, mv.STRUGGLE_BUG),
     (29, mv.ENDURE), (31, mv.STICKY_WEB), (36, mv.BUG_BUZZ), (43, mv.FLAIL)),
    LEAVANNY, 0, True, "happiness")

SEWADDLE = Pokemon(
    540, "Sewaddle", 5, False,
    "", ("Bug", "Grass"),
    45, 46, 65, 42,
    ((1, mv.STRING_SHOT), (1, mv.TACKLE), (8, mv.BUG_BITE),
     (15, mv.RAZOR_LEAF), (22, mv.STRUGGLE_BUG), (29, mv.ENDURE),
     (31, mv.STICKY_WEB), (36, mv.BUG_BUZZ), (43, mv.FLAIL)),
    SWADLOON, 20, True, "")

SCOLIPEDE = Pokemon(
    545, "Scolipede", 5, False,
    "", ("Bug", "Poison"),
    60, 77, 79, 112,
    ((1, mv.BATON_PASS), (1, mv.DEFENSE_CURL), (1, mv.IRON_DEFENSE),
     (1, mv.POISON_STING), (1, mv.PROTECT), (1, mv.ROLLOUT),
     (12, mv.POISON_TAIL), (16, mv.SCREECH), (20, mv.BUG_BITE),
     (26, mv.VENOSHOCK), (34, mv.TAKE_DOWN), (42, mv.AGILITY), (50, mv.TOXIC),
     (58, mv.VENOM_DRENCH), (66, mv.DOUBLE_EDGE), (74, mv.MEGAHORN)),
    None, 0, False, "")

WHIRLIPEDE = Pokemon(
    544, "Whirlipede", 5, False,
    "", ("Bug", "Poison"),
    40, 47, 89, 47,
    ((1, mv.DEFENSE_CURL), (1, mv.IRON_DEFENSE), (1, mv.POISON_STING),
     (1, mv.PROTECT), (1, mv.ROLLOUT), (12, mv.POISON_TAIL), (16, mv.SCREECH),
     (20, mv.BUG_BITE), (26, mv.VENOSHOCK), (32, mv.TAKE_DOWN),
     (38, mv.AGILITY), (44, mv.TOXIC), (50, mv.VENOM_DRENCH),
     (56, mv.DOUBLE_EDGE)),
    SCOLIPEDE, 30, True, "")

VENIPEDE = Pokemon(
    543, "Venipede", 5, False,
    "", ("Bug", "Poison"),
    30, 37, 49, 57,
    ((1, mv.DEFENSE_CURL), (1, mv.POISON_STING), (4, mv.ROLLOUT),
     (8, mv.PROTECT), (12, mv.POISON_TAIL), (16, mv.SCREECH),
     (20, mv.BUG_BITE), (24, mv.VENOSHOCK), (28, mv.TAKE_DOWN),
     (32, mv.AGILITY), (36, mv.TOXIC), (40, mv.VENOM_DRENCH),
     (44, mv.DOUBLE_EDGE)),
    WHIRLIPEDE, 22, True, "")

WHIMSICOTT = Pokemon(
    547, "Whimsicott", 5, False,
    "", ("Grass", "Fairy"),
    60, 72, 80, 116,
    ((1, mv.ABSORB), (1, mv.CHARM), (1, mv.COTTON_GUARD), (1, mv.COTTON_SPORE),
     (1, mv.ENDEAVOR), (1, mv.ENERGY_BALL), (1, mv.FAIRY_WIND),
     (1, mv.GIGA_DRAIN), (1, mv.GROWTH), (1, mv.GUST), (1, mv.HELPING_HAND),
     (1, mv.HURRICANE), (1, mv.LEECH_SEED), (1, mv.MEGA_DRAIN),
     (1, mv.MEMENTO), (1, mv.MOONBLAST), (1, mv.POISON_POWDER),
     (1, mv.RAZOR_LEAF), (1, mv.SOLAR_BEAM), (1, mv.STUN_SPORE),
     (1, mv.SUNNY_DAY), (1, mv.TAILWIND)),
    None, 0, False, "")

COTTONEE = Pokemon(
    546, "Cottonee", 5, False,
    "", ("Grass", "Fairy"),
    40, 32, 55, 66,
    ((1, mv.ABSORB), (1, mv.HELPING_HAND), (3, mv.FAIRY_WIND),
     (6, mv.STUN_SPORE), (12, mv.MEGA_DRAIN), (15, mv.RAZOR_LEAF),
     (18, mv.GROWTH), (21, mv.POISON_POWDER), (24, mv.GIGA_DRAIN),
     (27, mv.CHARM), (30, mv.LEECH_SEED), (33, mv.COTTON_SPORE),
     (36, mv.ENERGY_BALL), (39, mv.SUNNY_DAY), (42, mv.ENDEAVOR),
     (45, mv.COTTON_GUARD), (48, mv.SOLAR_BEAM)),
    WHIMSICOTT, 0, True, "item:sun-stone")

LILLIGANT = Pokemon(
    549, "Lilligant", 5, False,
    "", ("Grass",),
    70, 85, 75, 90,
    ((0, mv.PETAL_DANCE), (1, mv.ABSORB), (1, mv.AFTER_YOU), (1, mv.CHARM),
     (1, mv.ENERGY_BALL), (1, mv.ENTRAINMENT), (1, mv.GIGA_DRAIN),
     (1, mv.GROWTH), (1, mv.HELPING_HAND), (1, mv.LEAF_STORM),
     (1, mv.LEECH_SEED), (1, mv.MEGA_DRAIN), (1, mv.PETAL_BLIZZARD),
     (1, mv.QUIVER_DANCE), (1, mv.SLEEP_POWDER), (1, mv.STUN_SPORE),
     (1, mv.SUNNY_DAY), (1, mv.SYNTHESIS), (1, mv.TEETER_DANCE),
     (5, mv.MAGICAL_LEAF)),
    None, 0, False, "")

PETILIL = Pokemon(
    548, "Petilil", 5, False,
    "", ("Grass",),
    45, 52, 50, 30,
    ((1, mv.ABSORB), (1, mv.GROWTH), (3, mv.HELPING_HAND), (6, mv.STUN_SPORE),
     (9, mv.MEGA_DRAIN), (12, mv.CHARM), (15, mv.MAGICAL_LEAF),
     (18, mv.SLEEP_POWDER), (21, mv.GIGA_DRAIN), (24, mv.LEECH_SEED),
     (27, mv.AFTER_YOU), (30, mv.ENERGY_BALL), (33, mv.SYNTHESIS),
     (36, mv.SUNNY_DAY), (39, mv.ENTRAINMENT), (42, mv.LEAF_STORM)),
    LILLIGANT, 0, True, "item:sun-stone")


# --- generation 8 ---

BASCULEGION = Pokemon(
    902, "Basculegion", 8, False,
    "", ("Water", "Ghost"),
    120, 96, 70, 78,
    ((1, mv.PHANTOM_FORCE), (1, mv.SHADOW_BALL), (1, mv.TAIL_WHIP),
     (1, mv.WATER_GUN), (4, mv.TACKLE), (8, mv.FLAIL), (12, mv.AQUA_JET),
     (16, mv.BITE), (20, mv.SCARY_FACE), (24, mv.HEADBUTT), (28, mv.SOAK),
     (32, mv.CRUNCH), (36, mv.TAKE_DOWN), (40, mv.UPROAR), (44, mv.WAVE_CRASH),
     (48, mv.THRASH), (52, mv.DOUBLE_EDGE), (56, mv.HEAD_SMASH)),
    None, 0, False, "")


# --- generation 5 ---

BASCULIN = Pokemon(
    550, "Basculin", 5, False,
    "", ("Water",),
    70, 86, 60, 98,
    ((1, mv.TAIL_WHIP), (1, mv.WATER_GUN), (4, mv.TACKLE), (8, mv.FLAIL),
     (12, mv.AQUA_JET), (16, mv.BITE), (20, mv.SCARY_FACE), (24, mv.HEADBUTT),
     (28, mv.SOAK), (32, mv.CRUNCH), (36, mv.TAKE_DOWN), (40, mv.FINAL_GAMBIT),
     (44, mv.WAVE_CRASH), (48, mv.THRASH), (52, mv.DOUBLE_EDGE),
     (56, mv.HEAD_SMASH)),
    BASCULEGION, 0, True, "recoil-damage")

KROOKODILE = Pokemon(
    553, "Krookodile", 5, False,
    "", ("Ground", "Dark"),
    95, 91, 75, 92,
    ((1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.POWER_TRIP), (1, mv.SAND_ATTACK),
     (9, mv.SAND_TOMB), (12, mv.SCARY_FACE), (15, mv.BITE), (18, mv.TORMENT),
     (21, mv.DIG), (24, mv.SWAGGER), (27, mv.CRUNCH), (32, mv.SANDSTORM),
     (35, mv.FOUL_PLAY), (44, mv.EARTHQUAKE), (51, mv.THRASH),
     (58, mv.OUTRAGE)),
    None, 0, False, "")

KROKOROK = Pokemon(
    552, "Krokorok", 5, False,
    "", ("Ground", "Dark"),
    60, 63, 45, 74,
    ((1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.POWER_TRIP), (1, mv.SAND_ATTACK),
     (9, mv.SAND_TOMB), (12, mv.SCARY_FACE), (15, mv.BITE), (18, mv.TORMENT),
     (21, mv.DIG), (24, mv.SWAGGER), (27, mv.CRUNCH), (32, mv.SANDSTORM),
     (35, mv.FOUL_PLAY), (42, mv.EARTHQUAKE), (47, mv.THRASH)),
    KROOKODILE, 40, True, "")

SANDILE = Pokemon(
    551, "Sandile", 5, False,
    "", ("Ground", "Dark"),
    50, 53, 35, 65,
    ((1, mv.LEER), (1, mv.POWER_TRIP), (3, mv.SAND_ATTACK), (6, mv.HONE_CLAWS),
     (9, mv.SAND_TOMB), (12, mv.SCARY_FACE), (15, mv.BITE), (18, mv.TORMENT),
     (21, mv.DIG), (24, mv.SWAGGER), (27, mv.CRUNCH), (30, mv.SANDSTORM),
     (33, mv.FOUL_PLAY), (36, mv.EARTHQUAKE), (39, mv.THRASH)),
    KROKOROK, 29, True, "")

DARMANITAN = Pokemon(
    555, "Darmanitan", 5, False,
    "", ("Fire",),
    105, 85, 55, 95,
    ((0, mv.HAMMER_ARM), (1, mv.BITE), (1, mv.EMBER), (1, mv.TACKLE),
     (1, mv.TAUNT), (12, mv.INCINERATE), (16, mv.WORK_UP), (20, mv.FIRE_FANG),
     (24, mv.HEADBUTT), (28, mv.FIRE_PUNCH), (32, mv.UPROAR),
     (38, mv.BELLY_DRUM), (44, mv.FLARE_BLITZ), (50, mv.THRASH),
     (56, mv.SUPERPOWER)),
    None, 0, False, "")

DARUMAKA = Pokemon(
    554, "Darumaka", 5, False,
    "", ("Fire",),
    70, 52, 45, 50,
    ((1, mv.EMBER), (1, mv.TACKLE), (4, mv.TAUNT), (8, mv.BITE),
     (12, mv.INCINERATE), (16, mv.WORK_UP), (20, mv.FIRE_FANG),
     (24, mv.HEADBUTT), (28, mv.FIRE_PUNCH), (32, mv.UPROAR),
     (36, mv.BELLY_DRUM), (40, mv.FLARE_BLITZ), (44, mv.THRASH),
     (48, mv.SUPERPOWER)),
    DARMANITAN, 35, True, "")

MARACTUS = Pokemon(
    556, "Maractus", 5, False,
    "", ("Grass",),
    75, 96, 67, 60,
    ((1, mv.ABSORB), (1, mv.AFTER_YOU), (1, mv.INGRAIN), (1, mv.PECK),
     (1, mv.SPIKY_SHIELD), (4, mv.GROWTH), (8, mv.MEGA_DRAIN),
     (12, mv.LEECH_SEED), (16, mv.SUCKER_PUNCH), (20, mv.PIN_MISSILE),
     (24, mv.GIGA_DRAIN), (28, mv.SWEET_SCENT), (32, mv.SYNTHESIS),
     (36, mv.PETAL_BLIZZARD), (40, mv.COTTON_SPORE), (44, mv.SUNNY_DAY),
     (48, mv.SOLAR_BEAM), (52, mv.ACUPRESSURE), (56, mv.PETAL_DANCE),
     (60, mv.COTTON_GUARD)),
    None, 0, False, "")

CRUSTLE = Pokemon(
    558, "Crustle", 5, False,
    "", ("Bug", "Rock"),
    70, 85, 100, 45,
    ((1, mv.FURY_CUTTER), (1, mv.SAND_ATTACK), (1, mv.SMACK_DOWN),
     (1, mv.WITHDRAW), (12, mv.BUG_BITE), (16, mv.FLAIL), (20, mv.SLASH),
     (24, mv.ROCK_SLIDE), (28, mv.STEALTH_ROCK), (32, mv.ROCK_BLAST),
     (38, mv.X_SCISSOR), (44, mv.ROCK_POLISH), (50, mv.SHELL_SMASH),
     (56, mv.ROCK_WRECKER)),
    None, 0, False, "")

DWEBBLE = Pokemon(
    557, "Dwebble", 5, False,
    "", ("Bug", "Rock"),
    50, 50, 60, 55,
    ((1, mv.FURY_CUTTER), (1, mv.SAND_ATTACK), (4, mv.WITHDRAW),
     (8, mv.SMACK_DOWN), (12, mv.BUG_BITE), (16, mv.FLAIL), (20, mv.SLASH),
     (24, mv.ROCK_SLIDE), (28, mv.STEALTH_ROCK), (32, mv.ROCK_BLAST),
     (36, mv.X_SCISSOR), (40, mv.ROCK_POLISH), (44, mv.SHELL_SMASH),
     (48, mv.ROCK_WRECKER)),
    CRUSTLE, 34, True, "")

SCRAFTY = Pokemon(
    560, "Scrafty", 5, False,
    "", ("Dark", "Fighting"),
    65, 67, 115, 58,
    ((1, mv.HEADBUTT), (1, mv.LEER), (1, mv.LOW_KICK), (1, mv.PAYBACK),
     (12, mv.SAND_ATTACK), (16, mv.FACADE), (20, mv.TORMENT), (24, mv.BEAT_UP),
     (28, mv.SCARY_FACE), (32, mv.BRICK_BREAK), (36, mv.SWAGGER),
     (42, mv.CRUNCH), (48, mv.HIGH_JUMP_KICK), (54, mv.FOCUS_PUNCH),
     (60, mv.HEAD_SMASH)),
    None, 0, False, "")

SCRAGGY = Pokemon(
    559, "Scraggy", 5, False,
    "", ("Dark", "Fighting"),
    50, 55, 70, 48,
    ((1, mv.LEER), (1, mv.LOW_KICK), (4, mv.PAYBACK), (8, mv.HEADBUTT),
     (12, mv.SAND_ATTACK), (16, mv.FACADE), (20, mv.TORMENT), (24, mv.BEAT_UP),
     (28, mv.SCARY_FACE), (32, mv.BRICK_BREAK), (36, mv.SWAGGER),
     (40, mv.CRUNCH), (44, mv.HIGH_JUMP_KICK), (48, mv.FOCUS_PUNCH),
     (52, mv.HEAD_SMASH)),
    SCRAFTY, 39, True, "")

SIGILYPH = Pokemon(
    561, "Sigilyph", 5, False,
    "", ("Psychic", "Flying"),
    72, 80, 80, 97,
    ((1, mv.CONFUSION), (1, mv.GUST), (5, mv.GRAVITY), (10, mv.HYPNOSIS),
     (15, mv.AIR_CUTTER), (20, mv.PSYBEAM), (25, mv.WHIRLWIND),
     (30, mv.COSMIC_POWER), (35, mv.AIR_SLASH), (40, mv.PSYCHIC),
     (45, mv.TAILWIND), (50, mv.LIGHT_SCREEN), (50, mv.REFLECT),
     (55, mv.SKY_ATTACK), (60, mv.SKILL_SWAP)),
    None, 0, False, "")

COFAGRIGUS = Pokemon(
    563, "Cofagrigus", 5, False,
    "", ("Ghost",),
    58, 72, 125, 30,
    ((0, mv.SHADOW_CLAW), (1, mv.ASTONISH), (1, mv.HAZE), (1, mv.NIGHT_SHADE),
     (1, mv.PROTECT), (1, mv.SCARY_FACE), (12, mv.DISABLE),
     (16, mv.WILL_O_WISP), (20, mv.CRAFTY_SHIELD), (24, mv.HEX),
     (28, mv.MEAN_LOOK), (32, mv.GRUDGE), (38, mv.CURSE), (44, mv.SHADOW_BALL),
     (50, mv.DARK_PULSE), (56, mv.GUARD_SPLIT), (56, mv.POWER_SPLIT),
     (62, mv.DESTINY_BOND)),
    None, 0, False, "")

YAMASK = Pokemon(
    562, "Yamask", 5, False,
    "", ("Ghost",),
    38, 42, 75, 30,
    ((1, mv.ASTONISH), (1, mv.PROTECT), (4, mv.HAZE), (8, mv.NIGHT_SHADE),
     (12, mv.DISABLE), (16, mv.WILL_O_WISP), (20, mv.CRAFTY_SHIELD),
     (24, mv.HEX), (28, mv.MEAN_LOOK), (32, mv.GRUDGE), (36, mv.CURSE),
     (40, mv.SHADOW_BALL), (44, mv.DARK_PULSE), (48, mv.GUARD_SPLIT),
     (48, mv.POWER_SPLIT), (52, mv.DESTINY_BOND)),
    COFAGRIGUS, 0, True, "take-damage")

CARRACOSTA = Pokemon(
    565, "Carracosta", 5, False,
    "", ("Water", "Rock"),
    74, 95, 99, 32,
    ((1, mv.AQUA_JET), (1, mv.PROTECT), (1, mv.WATER_GUN), (1, mv.WITHDRAW),
     (9, mv.SMACK_DOWN), (12, mv.ANCIENT_POWER), (15, mv.BITE),
     (18, mv.WIDE_GUARD), (21, mv.BRINE), (24, mv.ROCK_SLIDE), (27, mv.CRUNCH),
     (30, mv.CURSE), (33, mv.IRON_DEFENSE), (36, mv.AQUA_TAIL),
     (41, mv.RAIN_DANCE), (46, mv.HYDRO_PUMP), (51, mv.SHELL_SMASH)),
    None, 0, False, "")

TIRTOUGA = Pokemon(
    564, "Tirtouga", 5, False,
    "", ("Water", "Rock"),
    54, 65, 74, 22,
    ((1, mv.WATER_GUN), (1, mv.WITHDRAW), (3, mv.PROTECT), (6, mv.AQUA_JET),
     (9, mv.SMACK_DOWN), (12, mv.ANCIENT_POWER), (15, mv.BITE),
     (18, mv.WIDE_GUARD), (21, mv.BRINE), (24, mv.ROCK_SLIDE), (27, mv.CRUNCH),
     (30, mv.CURSE), (33, mv.IRON_DEFENSE), (36, mv.AQUA_TAIL),
     (39, mv.RAIN_DANCE), (42, mv.HYDRO_PUMP), (45, mv.SHELL_SMASH)),
    CARRACOSTA, 37, True, "")

ARCHEOPS = Pokemon(
    567, "Archeops", 5, False,
    "", ("Rock", "Flying"),
    75, 126, 65, 110,
    ((1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.ROCK_THROW),
     (1, mv.WING_ATTACK), (9, mv.DRAGON_BREATH), (12, mv.ANCIENT_POWER),
     (15, mv.PLUCK), (18, mv.QUICK_GUARD), (21, mv.U_TURN),
     (24, mv.ROCK_SLIDE), (27, mv.SCARY_FACE), (30, mv.CRUNCH),
     (33, mv.AGILITY), (36, mv.TAILWIND), (41, mv.DRAGON_CLAW),
     (46, mv.THRASH), (51, mv.ENDEAVOR)),
    None, 0, False, "")

ARCHEN = Pokemon(
    566, "Archen", 5, False,
    "", ("Rock", "Flying"),
    55, 93, 45, 70,
    ((1, mv.LEER), (1, mv.QUICK_ATTACK), (3, mv.ROCK_THROW),
     (6, mv.WING_ATTACK), (9, mv.DRAGON_BREATH), (12, mv.ANCIENT_POWER),
     (15, mv.PLUCK), (18, mv.QUICK_GUARD), (21, mv.U_TURN),
     (24, mv.ROCK_SLIDE), (27, mv.SCARY_FACE), (30, mv.CRUNCH),
     (33, mv.AGILITY), (36, mv.TAILWIND), (39, mv.DRAGON_CLAW),
     (42, mv.THRASH), (45, mv.ENDEAVOR)),
    ARCHEOPS, 37, True, "")

GARBODOR = Pokemon(
    569, "Garbodor", 5, False,
    "", ("Poison",),
    80, 77, 82, 75,
    ((1, mv.ACID_SPRAY), (1, mv.METAL_CLAW), (1, mv.POISON_GAS), (1, mv.POUND),
     (1, mv.RECYCLE), (1, mv.TAKE_DOWN), (9, mv.AMNESIA), (12, mv.CLEAR_SMOG),
     (15, mv.TOXIC_SPIKES), (18, mv.SLUDGE), (21, mv.STOCKPILE),
     (21, mv.SWALLOW), (24, mv.BODY_SLAM), (27, mv.SLUDGE_BOMB),
     (30, mv.TOXIC), (33, mv.BELCH), (39, mv.PAIN_SPLIT), (43, mv.GUNK_SHOT),
     (48, mv.EXPLOSION)),
    None, 0, False, "")

TRUBBISH = Pokemon(
    568, "Trubbish", 5, False,
    "", ("Poison",),
    50, 45, 62, 65,
    ((1, mv.POISON_GAS), (1, mv.POUND), (3, mv.RECYCLE), (6, mv.ACID_SPRAY),
     (9, mv.AMNESIA), (12, mv.CLEAR_SMOG), (15, mv.TOXIC_SPIKES),
     (18, mv.SLUDGE), (21, mv.STOCKPILE), (21, mv.SWALLOW), (24, mv.TAKE_DOWN),
     (27, mv.SLUDGE_BOMB), (30, mv.TOXIC), (33, mv.BELCH), (37, mv.PAIN_SPLIT),
     (39, mv.GUNK_SHOT), (42, mv.EXPLOSION)),
    GARBODOR, 36, True, "")

ZOROARK = Pokemon(
    571, "Zoroark", 5, False,
    "", ("Dark",),
    60, 112, 60, 105,
    ((0, mv.NIGHT_SLASH), (1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.SCRATCH),
     (1, mv.TORMENT), (1, mv.U_TURN), (12, mv.FURY_SWIPES), (20, mv.TAUNT),
     (24, mv.KNOCK_OFF), (28, mv.FAKE_TEARS), (34, mv.AGILITY),
     (40, mv.IMPRISON), (46, mv.NIGHT_DAZE), (52, mv.NASTY_PLOT),
     (58, mv.FOUL_PLAY)),
    None, 0, False, "")

ZORUA = Pokemon(
    570, "Zorua", 5, False,
    "", ("Dark",),
    40, 72, 40, 65,
    ((1, mv.LEER), (1, mv.SCRATCH), (4, mv.TORMENT), (8, mv.HONE_CLAWS),
     (12, mv.FURY_SWIPES), (16, mv.SCARY_FACE), (20, mv.TAUNT),
     (24, mv.KNOCK_OFF), (28, mv.FAKE_TEARS), (32, mv.AGILITY),
     (36, mv.IMPRISON), (40, mv.NIGHT_DAZE), (44, mv.NASTY_PLOT),
     (48, mv.FOUL_PLAY)),
    ZOROARK, 30, True, "")

CINCCINO = Pokemon(
    573, "Cinccino", 5, False,
    "", ("Normal",),
    75, 80, 60, 115,
    ((0, mv.TAIL_SLAP), (1, mv.BULLET_SEED), (1, mv.CHARM), (1, mv.POUND),
     (1, mv.SING)),
    None, 0, False, "")

MINCCINO = Pokemon(
    572, "Minccino", 5, False,
    "", ("Normal",),
    55, 45, 40, 75,
    ((1, mv.BABY_DOLL_EYES), (1, mv.POUND), (4, mv.HELPING_HAND),
     (8, mv.ECHOED_VOICE), (12, mv.SING), (16, mv.CHARM), (20, mv.SWIFT),
     (24, mv.ENCORE), (28, mv.AFTER_YOU), (32, mv.TAIL_SLAP), (36, mv.TICKLE),
     (40, mv.SLAM), (44, mv.HYPER_VOICE), (48, mv.LAST_RESORT)),
    CINCCINO, 0, True, "item:shiny-stone")

GOTHITELLE = Pokemon(
    576, "Gothitelle", 5, False,
    "", ("Psychic",),
    70, 75, 102, 65,
    ((1, mv.CONFUSION), (1, mv.PLAY_NICE), (1, mv.POUND), (1, mv.TICKLE),
     (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK), (24, mv.HYPNOSIS),
     (28, mv.FAKE_TEARS), (35, mv.PSYCH_UP), (40, mv.PSYCHIC),
     (48, mv.FLATTER), (56, mv.FUTURE_SIGHT), (64, mv.MAGIC_ROOM)),
    None, 0, False, "")

GOTHORITA = Pokemon(
    575, "Gothorita", 5, False,
    "", ("Psychic",),
    60, 60, 77, 55,
    ((1, mv.CONFUSION), (1, mv.PLAY_NICE), (1, mv.POUND), (1, mv.TICKLE),
     (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK), (24, mv.HYPNOSIS),
     (28, mv.FAKE_TEARS), (35, mv.PSYCH_UP), (46, mv.FLATTER),
     (52, mv.FUTURE_SIGHT), (58, mv.MAGIC_ROOM)),
    GOTHITELLE, 41, True, "")

GOTHITA = Pokemon(
    574, "Gothita", 5, False,
    "", ("Psychic",),
    45, 42, 57, 45,
    ((1, mv.CONFUSION), (1, mv.POUND), (4, mv.PLAY_NICE), (8, mv.TICKLE),
     (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK), (24, mv.HYPNOSIS),
     (28, mv.FAKE_TEARS), (33, mv.PSYCH_UP), (36, mv.PSYCHIC),
     (40, mv.FLATTER), (44, mv.FUTURE_SIGHT), (48, mv.MAGIC_ROOM)),
    GOTHORITA, 32, True, "")

REUNICLUS = Pokemon(
    579, "Reuniclus", 5, False,
    "", ("Psychic",),
    110, 95, 80, 30,
    ((0, mv.HAMMER_ARM), (1, mv.CONFUSION), (1, mv.ENDEAVOR), (1, mv.PROTECT),
     (1, mv.RECOVER), (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK),
     (24, mv.LIGHT_SCREEN), (24, mv.REFLECT), (28, mv.ALLY_SWITCH),
     (35, mv.PAIN_SPLIT), (40, mv.PSYCHIC), (48, mv.SKILL_SWAP),
     (56, mv.FUTURE_SIGHT), (64, mv.WONDER_ROOM)),
    None, 0, False, "")

DUOSION = Pokemon(
    578, "Duosion", 5, False,
    "", ("Psychic",),
    65, 82, 55, 30,
    ((1, mv.CONFUSION), (1, mv.ENDEAVOR), (1, mv.PROTECT), (1, mv.RECOVER),
     (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK),
     (24, mv.LIGHT_SCREEN), (24, mv.REFLECT), (28, mv.ALLY_SWITCH),
     (35, mv.PAIN_SPLIT), (40, mv.PSYCHIC), (46, mv.SKILL_SWAP),
     (52, mv.FUTURE_SIGHT), (58, mv.WONDER_ROOM)),
    REUNICLUS, 41, True, "")

SOLOSIS = Pokemon(
    577, "Solosis", 5, False,
    "", ("Psychic",),
    45, 67, 45, 20,
    ((1, mv.CONFUSION), (1, mv.PROTECT), (4, mv.RECOVER), (8, mv.ENDEAVOR),
     (12, mv.PSYBEAM), (16, mv.CHARM), (20, mv.PSYSHOCK),
     (24, mv.LIGHT_SCREEN), (24, mv.REFLECT), (28, mv.ALLY_SWITCH),
     (33, mv.PAIN_SPLIT), (36, mv.PSYCHIC), (40, mv.SKILL_SWAP),
     (44, mv.FUTURE_SIGHT), (48, mv.WONDER_ROOM)),
    DUOSION, 32, True, "")

SWANNA = Pokemon(
    581, "Swanna", 5, False,
    "", ("Water", "Flying"),
    75, 87, 63, 98,
    ((1, mv.DEFOG), (1, mv.WATER_GUN), (1, mv.WING_ATTACK),
     (13, mv.WATER_PULSE), (15, mv.AERIAL_ACE), (19, mv.BUBBLE_BEAM),
     (21, mv.FEATHER_DANCE), (24, mv.AQUA_RING), (27, mv.AIR_SLASH),
     (30, mv.ROOST), (34, mv.RAIN_DANCE), (40, mv.TAILWIND),
     (47, mv.BRAVE_BIRD), (55, mv.HURRICANE)),
    None, 0, False, "")

DUCKLETT = Pokemon(
    580, "Ducklett", 5, False,
    "", ("Water", "Flying"),
    62, 44, 50, 55,
    ((1, mv.WATER_GUN), (6, mv.DEFOG), (9, mv.WING_ATTACK),
     (13, mv.WATER_PULSE), (15, mv.AERIAL_ACE), (19, mv.BUBBLE_BEAM),
     (21, mv.FEATHER_DANCE), (24, mv.AQUA_RING), (27, mv.AIR_SLASH),
     (30, mv.ROOST), (34, mv.RAIN_DANCE), (37, mv.TAILWIND),
     (41, mv.BRAVE_BIRD), (46, mv.HURRICANE)),
    SWANNA, 35, True, "")

VANILLUXE = Pokemon(
    584, "Vanilluxe", 5, False,
    "", ("Ice",),
    71, 102, 90, 79,
    ((1, mv.ASTONISH), (1, mv.FREEZE_DRY), (1, mv.HARDEN),
     (1, mv.ICICLE_CRASH), (1, mv.MIST), (1, mv.TAUNT), (1, mv.WEATHER_BALL),
     (12, mv.ICY_WIND), (16, mv.AVALANCHE), (20, mv.HAIL),
     (24, mv.ICICLE_SPEAR), (28, mv.UPROAR), (32, mv.ACID_ARMOR),
     (38, mv.MIRROR_COAT), (44, mv.ICE_BEAM), (52, mv.BLIZZARD),
     (60, mv.SHEER_COLD)),
    None, 0, False, "")

VANILLISH = Pokemon(
    583, "Vanillish", 5, False,
    "", ("Ice",),
    51, 72, 70, 59,
    ((1, mv.ASTONISH), (1, mv.HARDEN), (1, mv.MIST), (1, mv.TAUNT),
     (12, mv.ICY_WIND), (16, mv.AVALANCHE), (20, mv.HAIL),
     (24, mv.ICICLE_SPEAR), (28, mv.UPROAR), (32, mv.ACID_ARMOR),
     (38, mv.MIRROR_COAT), (44, mv.ICE_BEAM), (50, mv.BLIZZARD),
     (56, mv.SHEER_COLD)),
    VANILLUXE, 47, True, "")

VANILLITE = Pokemon(
    582, "Vanillite", 5, False,
    "", ("Ice",),
    36, 57, 55, 44,
    ((1, mv.ASTONISH), (1, mv.HARDEN), (4, mv.TAUNT), (8, mv.MIST),
     (12, mv.ICY_WIND), (16, mv.AVALANCHE), (20, mv.HAIL),
     (24, mv.ICICLE_SPEAR), (28, mv.UPROAR), (32, mv.ACID_ARMOR),
     (36, mv.MIRROR_COAT), (40, mv.ICE_BEAM), (44, mv.BLIZZARD),
     (48, mv.SHEER_COLD)),
    VANILLISH, 35, True, "")

SAWSBUCK = Pokemon(
    586, "Sawsbuck", 5, False,
    "", ("Normal", "Grass"),
    80, 80, 70, 95,
    ((0, mv.HORN_LEECH), (1, mv.GROWL), (1, mv.MEGAHORN), (1, mv.SAND_ATTACK),
     (1, mv.TACKLE), (10, mv.DOUBLE_KICK), (13, mv.LEECH_SEED),
     (16, mv.BULLET_SEED), (20, mv.TAKE_DOWN), (24, mv.ZEN_HEADBUTT),
     (28, mv.ENERGY_BALL), (36, mv.CHARM), (44, mv.DOUBLE_EDGE),
     (52, mv.SOLAR_BEAM)),
    None, 0, False, "")

DEERLING = Pokemon(
    585, "Deerling", 5, False,
    "", ("Normal", "Grass"),
    60, 50, 50, 75,
    ((1, mv.TACKLE), (4, mv.GROWL), (7, mv.SAND_ATTACK), (10, mv.DOUBLE_KICK),
     (13, mv.LEECH_SEED), (16, mv.BULLET_SEED), (20, mv.TAKE_DOWN),
     (24, mv.ZEN_HEADBUTT), (28, mv.ENERGY_BALL), (32, mv.CHARM),
     (37, mv.DOUBLE_EDGE), (42, mv.SOLAR_BEAM)),
    SAWSBUCK, 34, True, "")

EMOLGA = Pokemon(
    587, "Emolga", 5, False,
    "", ("Electric", "Flying"),
    55, 75, 60, 103,
    ((1, mv.NUZZLE), (1, mv.TAIL_WHIP), (5, mv.DOUBLE_TEAM),
     (10, mv.QUICK_ATTACK), (15, mv.THUNDER_SHOCK), (20, mv.CHARGE),
     (25, mv.ACROBATICS), (30, mv.SPARK), (35, mv.ENCORE),
     (40, mv.VOLT_SWITCH), (45, mv.LIGHT_SCREEN), (50, mv.DISCHARGE),
     (55, mv.AGILITY)),
    None, 0, False, "")

ESCAVALIER = Pokemon(
    589, "Escavalier", 5, False,
    "", ("Bug", "Steel"),
    70, 97, 105, 20,
    ((1, mv.DOUBLE_EDGE), (1, mv.ENDURE), (1, mv.FELL_STINGER), (1, mv.FLAIL),
     (1, mv.FURY_CUTTER), (1, mv.LEER), (1, mv.PECK), (1, mv.QUICK_GUARD),
     (1, mv.SCARY_FACE), (1, mv.TAKE_DOWN), (12, mv.FALSE_SWIPE),
     (16, mv.ACID_SPRAY), (20, mv.HEADBUTT), (24, mv.REVERSAL),
     (28, mv.IRON_DEFENSE), (32, mv.X_SCISSOR), (36, mv.SWORDS_DANCE),
     (40, mv.IRON_HEAD), (44, mv.BUG_BUZZ), (48, mv.GIGA_IMPACT),
     (52, mv.METAL_BURST)),
    None, 0, False, "")

KARRABLAST = Pokemon(
    588, "Karrablast", 5, False,
    "", ("Bug",),
    50, 57, 45, 60,
    ((1, mv.LEER), (1, mv.PECK), (4, mv.FURY_CUTTER), (8, mv.ENDURE),
     (12, mv.FALSE_SWIPE), (16, mv.ACID_SPRAY), (20, mv.HEADBUTT),
     (24, mv.FLAIL), (28, mv.SCARY_FACE), (32, mv.X_SCISSOR),
     (36, mv.SWORDS_DANCE), (40, mv.TAKE_DOWN), (44, mv.BUG_BUZZ),
     (48, mv.DOUBLE_EDGE)),
    ESCAVALIER, 0, True, "trade")

AMOONGUSS = Pokemon(
    591, "Amoonguss", 5, False,
    "", ("Grass", "Poison"),
    114, 85, 75, 30,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.GROWTH), (1, mv.STUN_SPORE),
     (12, mv.MEGA_DRAIN), (16, mv.SYNTHESIS), (20, mv.CLEAR_SMOG),
     (24, mv.SWEET_SCENT), (28, mv.GIGA_DRAIN), (32, mv.INGRAIN),
     (36, mv.TOXIC), (42, mv.RAGE_POWDER), (48, mv.SOLAR_BEAM),
     (54, mv.SPORE)),
    None, 0, False, "")

FOONGUS = Pokemon(
    590, "Foongus", 5, False,
    "", ("Grass", "Poison"),
    69, 55, 50, 15,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (4, mv.GROWTH), (8, mv.STUN_SPORE),
     (12, mv.MEGA_DRAIN), (16, mv.SYNTHESIS), (20, mv.CLEAR_SMOG),
     (24, mv.SWEET_SCENT), (28, mv.GIGA_DRAIN), (32, mv.INGRAIN),
     (36, mv.TOXIC), (40, mv.RAGE_POWDER), (44, mv.SOLAR_BEAM),
     (48, mv.SPORE)),
    AMOONGUSS, 39, True, "")

JELLICENT = Pokemon(
    593, "Jellicent", 5, False,
    "", ("Water", "Ghost"),
    100, 72, 87, 60,
    ((1, mv.ABSORB), (1, mv.ACID_ARMOR), (1, mv.NIGHT_SHADE),
     (1, mv.POISON_STING), (1, mv.WATER_GUN), (12, mv.WATER_PULSE),
     (16, mv.RAIN_DANCE), (20, mv.HEX), (24, mv.BRINE), (28, mv.RECOVER),
     (32, mv.SHADOW_BALL), (36, mv.WHIRLPOOL), (43, mv.HYDRO_PUMP),
     (48, mv.DESTINY_BOND), (54, mv.WATER_SPOUT)),
    None, 0, False, "")

FRILLISH = Pokemon(
    592, "Frillish", 5, False,
    "", ("Water", "Ghost"),
    55, 52, 67, 40,
    ((1, mv.ABSORB), (1, mv.WATER_GUN), (4, mv.POISON_STING),
     (8, mv.NIGHT_SHADE), (12, mv.WATER_PULSE), (16, mv.RAIN_DANCE),
     (20, mv.HEX), (24, mv.BRINE), (28, mv.RECOVER), (32, mv.SHADOW_BALL),
     (36, mv.WHIRLPOOL), (41, mv.HYDRO_PUMP), (44, mv.DESTINY_BOND),
     (48, mv.WATER_SPOUT)),
    JELLICENT, 40, True, "")

ALOMOMOLA = Pokemon(
    594, "Alomomola", 5, False,
    "", ("Water",),
    165, 57, 62, 65,
    ((1, mv.PLAY_NICE), (1, mv.POUND), (5, mv.AQUA_RING), (9, mv.AQUA_JET),
     (13, mv.HELPING_HAND), (13, mv.WIDE_GUARD), (21, mv.PROTECT),
     (25, mv.WATER_PULSE), (29, mv.HEALING_WISH), (33, mv.SOAK), (37, mv.WISH),
     (41, mv.BRINE), (45, mv.SAFEGUARD), (49, mv.WHIRLPOOL),
     (55, mv.HYDRO_PUMP)),
    None, 0, False, "")

GALVANTULA = Pokemon(
    596, "Galvantula", 5, False,
    "", ("Bug", "Electric"),
    70, 87, 60, 108,
    ((0, mv.STICKY_WEB), (1, mv.ABSORB), (1, mv.BUG_BITE), (1, mv.ELECTROWEB),
     (1, mv.FURY_CUTTER), (12, mv.STRING_SHOT), (16, mv.THUNDER_WAVE),
     (20, mv.ELECTRO_BALL), (24, mv.AGILITY), (28, mv.SUCKER_PUNCH),
     (32, mv.SLASH), (39, mv.DISCHARGE), (44, mv.SCREECH),
     (50, mv.GASTRO_ACID), (56, mv.BUG_BUZZ)),
    None, 0, False, "")

JOLTIK = Pokemon(
    595, "Joltik", 5, False,
    "", ("Bug", "Electric"),
    50, 52, 50, 65,
    ((1, mv.ABSORB), (1, mv.FURY_CUTTER), (4, mv.ELECTROWEB), (8, mv.BUG_BITE),
     (12, mv.STRING_SHOT), (16, mv.THUNDER_WAVE), (20, mv.ELECTRO_BALL),
     (24, mv.AGILITY), (28, mv.SUCKER_PUNCH), (32, mv.SLASH),
     (37, mv.DISCHARGE), (40, mv.SCREECH), (44, mv.GASTRO_ACID),
     (48, mv.BUG_BUZZ)),
    GALVANTULA, 36, True, "")

FERROTHORN = Pokemon(
    598, "Ferrothorn", 5, False,
    "", ("Grass", "Steel"),
    74, 74, 123, 20,
    ((0, mv.POWER_WHIP), (1, mv.HARDEN), (1, mv.METAL_CLAW),
     (1, mv.PIN_MISSILE), (1, mv.TACKLE), (15, mv.INGRAIN),
     (20, mv.FLASH_CANNON), (25, mv.IRON_HEAD), (30, mv.SELF_DESTRUCT),
     (35, mv.IRON_DEFENSE), (43, mv.CURSE), (49, mv.GYRO_BALL),
     (56, mv.EXPLOSION)),
    None, 0, False, "")

FERROSEED = Pokemon(
    597, "Ferroseed", 5, False,
    "", ("Grass", "Steel"),
    44, 37, 88, 10,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.METAL_CLAW), (10, mv.PIN_MISSILE),
     (15, mv.INGRAIN), (20, mv.FLASH_CANNON), (25, mv.IRON_HEAD),
     (30, mv.SELF_DESTRUCT), (35, mv.IRON_DEFENSE), (41, mv.CURSE),
     (45, mv.GYRO_BALL), (50, mv.EXPLOSION)),
    FERROTHORN, 40, True, "")

KLINKLANG = Pokemon(
    601, "Klinklang", 5, False,
    "", ("Steel",),
    60, 85, 100, 90,
    ((1, mv.BIND), (1, mv.CHARGE), (1, mv.GEAR_UP), (1, mv.MAGNETIC_FLUX),
     (1, mv.THUNDER_SHOCK), (1, mv.VISE_GRIP), (12, mv.CHARGE_BEAM),
     (16, mv.METAL_SOUND), (20, mv.AUTOTOMIZE), (24, mv.DISCHARGE),
     (28, mv.SCREECH), (32, mv.GEAR_GRIND), (36, mv.LOCK_ON),
     (42, mv.SHIFT_GEAR), (48, mv.ZAP_CANNON), (56, mv.HYPER_BEAM),
     (64, mv.ELECTRIC_TERRAIN)),
    None, 0, False, "")

KLANG = Pokemon(
    600, "Klang", 5, False,
    "", ("Steel",),
    60, 75, 90, 50,
    ((1, mv.BIND), (1, mv.CHARGE), (1, mv.THUNDER_SHOCK), (1, mv.VISE_GRIP),
     (12, mv.CHARGE_BEAM), (16, mv.METAL_SOUND), (20, mv.AUTOTOMIZE),
     (24, mv.DISCHARGE), (28, mv.SCREECH), (32, mv.GEAR_GRIND),
     (36, mv.LOCK_ON), (42, mv.SHIFT_GEAR), (48, mv.ZAP_CANNON),
     (54, mv.HYPER_BEAM)),
    KLINKLANG, 49, True, "")

KLINK = Pokemon(
    599, "Klink", 5, False,
    "", ("Steel",),
    40, 50, 65, 30,
    ((1, mv.THUNDER_SHOCK), (1, mv.VISE_GRIP), (4, mv.BIND), (8, mv.CHARGE),
     (12, mv.CHARGE_BEAM), (16, mv.METAL_SOUND), (20, mv.AUTOTOMIZE),
     (24, mv.DISCHARGE), (28, mv.SCREECH), (32, mv.GEAR_GRIND),
     (36, mv.LOCK_ON), (40, mv.SHIFT_GEAR), (44, mv.ZAP_CANNON),
     (48, mv.HYPER_BEAM)),
    KLANG, 38, True, "")

EELEKTROSS = Pokemon(
    604, "Eelektross", 5, False,
    "", ("Electric",),
    85, 110, 80, 50,
    ((1, mv.ACID), (1, mv.COIL), (1, mv.CRUNCH), (1, mv.CRUSH_CLAW),
     (1, mv.DISCHARGE), (1, mv.GASTRO_ACID), (1, mv.HEADBUTT), (1, mv.THRASH),
     (1, mv.ZAP_CANNON), (5, mv.WILD_CHARGE)),
    None, 0, False, "")

EELEKTRIK = Pokemon(
    603, "Eelektrik", 5, False,
    "", ("Electric",),
    65, 80, 70, 40,
    ((0, mv.CRUNCH), (1, mv.CHARGE_BEAM), (1, mv.HEADBUTT), (1, mv.SPARK),
     (1, mv.THUNDER_WAVE), (9, mv.BIND), (19, mv.ACID), (29, mv.DISCHARGE),
     (44, mv.THUNDERBOLT), (49, mv.ACID_SPRAY), (54, mv.COIL),
     (59, mv.WILD_CHARGE), (64, mv.GASTRO_ACID), (69, mv.ZAP_CANNON),
     (74, mv.THRASH)),
    EELEKTROSS, 0, True, "item:thunder-stone")

TYNAMO = Pokemon(
    602, "Tynamo", 5, False,
    "", ("Electric",),
    35, 50, 40, 60,
    ((1, mv.CHARGE_BEAM), (1, mv.SPARK), (1, mv.TACKLE), (1, mv.THUNDER_WAVE)),
    EELEKTRIK, 39, True, "")

BEHEEYEM = Pokemon(
    606, "Beheeyem", 5, False,
    "", ("Psychic",),
    75, 100, 85, 40,
    ((1, mv.CONFUSION), (1, mv.GROWL), (1, mv.IMPRISON),
     (1, mv.PSYCHIC_TERRAIN), (1, mv.TELEPORT), (18, mv.PSYBEAM),
     (24, mv.GUARD_SPLIT), (24, mv.POWER_SPLIT), (30, mv.HEADBUTT),
     (36, mv.ZEN_HEADBUTT), (45, mv.RECOVER), (52, mv.CALM_MIND),
     (60, mv.WONDER_ROOM), (68, mv.PSYCHIC)),
    None, 0, False, "")

ELGYEM = Pokemon(
    605, "Elgyem", 5, False,
    "", ("Psychic",),
    55, 70, 55, 30,
    ((1, mv.CONFUSION), (1, mv.GROWL), (6, mv.IMPRISON), (12, mv.TELEPORT),
     (18, mv.PSYBEAM), (24, mv.GUARD_SPLIT), (24, mv.POWER_SPLIT),
     (30, mv.HEADBUTT), (36, mv.ZEN_HEADBUTT), (43, mv.RECOVER),
     (48, mv.CALM_MIND), (54, mv.WONDER_ROOM), (60, mv.PSYCHIC)),
    BEHEEYEM, 42, True, "")

CHANDELURE = Pokemon(
    609, "Chandelure", 5, False,
    "", ("Ghost", "Fire"),
    60, 100, 90, 80,
    ((1, mv.ASTONISH), (1, mv.CONFUSE_RAY), (1, mv.CURSE), (1, mv.EMBER),
     (1, mv.FIRE_SPIN), (1, mv.HEX), (1, mv.IMPRISON), (1, mv.INFERNO),
     (1, mv.MEMENTO), (1, mv.MINIMIZE), (1, mv.NIGHT_SHADE), (1, mv.OVERHEAT),
     (1, mv.PAIN_SPLIT), (1, mv.SHADOW_BALL), (1, mv.SMOG),
     (1, mv.WILL_O_WISP)),
    None, 0, False, "")

LAMPENT = Pokemon(
    608, "Lampent", 5, False,
    "", ("Ghost", "Fire"),
    60, 67, 60, 55,
    ((1, mv.ASTONISH), (1, mv.EMBER), (1, mv.MINIMIZE), (1, mv.SMOG),
     (12, mv.CONFUSE_RAY), (16, mv.HEX), (20, mv.WILL_O_WISP),
     (24, mv.FIRE_SPIN), (28, mv.NIGHT_SHADE), (32, mv.CURSE),
     (36, mv.SHADOW_BALL), (40, mv.INFERNO), (46, mv.IMPRISON),
     (52, mv.PAIN_SPLIT), (58, mv.OVERHEAT), (64, mv.MEMENTO)),
    CHANDELURE, 0, True, "item:dusk-stone")

LITWICK = Pokemon(
    607, "Litwick", 5, False,
    "", ("Ghost", "Fire"),
    50, 47, 55, 20,
    ((1, mv.ASTONISH), (1, mv.SMOG), (4, mv.EMBER), (8, mv.MINIMIZE),
     (12, mv.CONFUSE_RAY), (16, mv.HEX), (20, mv.WILL_O_WISP),
     (24, mv.FIRE_SPIN), (28, mv.NIGHT_SHADE), (32, mv.CURSE),
     (36, mv.SHADOW_BALL), (40, mv.INFERNO), (44, mv.IMPRISON),
     (48, mv.PAIN_SPLIT), (52, mv.OVERHEAT), (56, mv.MEMENTO)),
    LAMPENT, 41, True, "")

HAXORUS = Pokemon(
    612, "Haxorus", 5, False,
    "", ("Dragon",),
    76, 103, 80, 97,
    ((1, mv.BITE), (1, mv.FALSE_SWIPE), (1, mv.LEER), (1, mv.SCRATCH),
     (9, mv.ASSURANCE), (12, mv.TAUNT), (15, mv.SLASH), (18, mv.DRAGON_CLAW),
     (21, mv.SCARY_FACE), (24, mv.CRUNCH), (27, mv.DRAGON_DANCE),
     (30, mv.BREAKING_SWIPE), (33, mv.FOCUS_ENERGY), (36, mv.DRAGON_PULSE),
     (41, mv.SWORDS_DANCE), (46, mv.OUTRAGE), (53, mv.GUILLOTINE),
     (60, mv.GIGA_IMPACT)),
    None, 0, False, "")

FRAXURE = Pokemon(
    611, "Fraxure", 5, False,
    "", ("Dragon",),
    66, 78, 60, 67,
    ((1, mv.BITE), (1, mv.FALSE_SWIPE), (1, mv.LEER), (1, mv.SCRATCH),
     (9, mv.ASSURANCE), (12, mv.TAUNT), (15, mv.SLASH), (18, mv.DRAGON_CLAW),
     (21, mv.SCARY_FACE), (24, mv.CRUNCH), (27, mv.DRAGON_DANCE),
     (30, mv.BREAKING_SWIPE), (33, mv.FOCUS_ENERGY), (36, mv.DRAGON_PULSE),
     (41, mv.SWORDS_DANCE), (46, mv.OUTRAGE), (51, mv.GUILLOTINE),
     (56, mv.GIGA_IMPACT)),
    HAXORUS, 48, True, "")

AXEW = Pokemon(
    610, "Axew", 5, False,
    "", ("Dragon",),
    46, 58, 50, 57,
    ((1, mv.LEER), (1, mv.SCRATCH), (3, mv.BITE), (6, mv.FALSE_SWIPE),
     (9, mv.ASSURANCE), (12, mv.TAUNT), (15, mv.SLASH), (18, mv.DRAGON_CLAW),
     (21, mv.SCARY_FACE), (24, mv.CRUNCH), (27, mv.DRAGON_DANCE),
     (30, mv.BREAKING_SWIPE), (33, mv.FOCUS_ENERGY), (36, mv.DRAGON_PULSE),
     (39, mv.SWORDS_DANCE), (42, mv.OUTRAGE), (45, mv.GUILLOTINE),
     (48, mv.GIGA_IMPACT)),
    FRAXURE, 38, True, "")

BEARTIC = Pokemon(
    614, "Beartic", 5, False,
    "", ("Ice",),
    95, 100, 80, 50,
    ((0, mv.ICICLE_CRASH), (1, mv.AQUA_JET), (1, mv.CHARM), (1, mv.ENDURE),
     (1, mv.FURY_SWIPES), (1, mv.GROWL), (1, mv.POWDER_SNOW), (9, mv.ICY_WIND),
     (12, mv.PLAY_NICE), (15, mv.BRINE), (18, mv.FROST_BREATH), (21, mv.SLASH),
     (24, mv.FLAIL), (27, mv.SWAGGER), (30, mv.SNOWSCAPE), (33, mv.THRASH),
     (36, mv.REST), (41, mv.BLIZZARD), (46, mv.SHEER_COLD),
     (51, mv.SUPERPOWER)),
    None, 0, False, "")

CUBCHOO = Pokemon(
    613, "Cubchoo", 5, False,
    "", ("Ice",),
    55, 65, 40, 40,
    ((1, mv.GROWL), (1, mv.POWDER_SNOW), (3, mv.ENDURE), (6, mv.FURY_SWIPES),
     (9, mv.ICY_WIND), (12, mv.PLAY_NICE), (15, mv.BRINE),
     (18, mv.FROST_BREATH), (21, mv.SLASH), (24, mv.FLAIL), (27, mv.CHARM),
     (30, mv.SNOWSCAPE), (33, mv.THRASH), (36, mv.REST), (39, mv.BLIZZARD),
     (42, mv.SHEER_COLD)),
    BEARTIC, 37, True, "")

CRYOGONAL = Pokemon(
    615, "Cryogonal", 5, False,
    "", ("Ice",),
    80, 72, 92, 105,
    ((1, mv.BIND), (1, mv.ICE_SHARD), (4, mv.CONFUSE_RAY), (8, mv.RAPID_SPIN),
     (12, mv.ICY_WIND), (16, mv.HAZE), (16, mv.MIST), (20, mv.ANCIENT_POWER),
     (24, mv.AURORA_BEAM), (28, mv.SLASH), (32, mv.NIGHT_SLASH),
     (36, mv.FREEZE_DRY), (40, mv.LIGHT_SCREEN), (40, mv.REFLECT),
     (44, mv.RECOVER), (48, mv.ICE_BEAM), (52, mv.ACID_ARMOR),
     (56, mv.SOLAR_BEAM), (60, mv.SHEER_COLD)),
    None, 0, False, "")

ACCELGOR = Pokemon(
    617, "Accelgor", 5, False,
    "", ("Bug",),
    80, 85, 50, 145,
    ((1, mv.ABSORB), (1, mv.ACID), (1, mv.ACID_ARMOR), (1, mv.ACID_SPRAY),
     (1, mv.BODY_SLAM), (1, mv.CURSE), (1, mv.DOUBLE_TEAM), (1, mv.GUARD_SWAP),
     (1, mv.QUICK_ATTACK), (1, mv.WATER_SHURIKEN), (1, mv.YAWN),
     (12, mv.MEGA_DRAIN), (16, mv.STRUGGLE_BUG), (20, mv.SWIFT),
     (24, mv.AGILITY), (28, mv.GIGA_DRAIN), (32, mv.POWER_SWAP),
     (36, mv.U_TURN), (40, mv.RECOVER), (44, mv.BUG_BUZZ),
     (48, mv.FINAL_GAMBIT), (52, mv.TOXIC)),
    None, 0, False, "")

SHELMET = Pokemon(
    616, "Shelmet", 5, False,
    "", ("Bug",),
    50, 40, 75, 25,
    ((1, mv.ABSORB), (1, mv.PROTECT), (4, mv.ACID), (8, mv.CURSE),
     (12, mv.MEGA_DRAIN), (16, mv.STRUGGLE_BUG), (20, mv.YAWN),
     (24, mv.ACID_ARMOR), (28, mv.GIGA_DRAIN), (32, mv.GUARD_SWAP),
     (36, mv.BODY_SLAM), (40, mv.RECOVER), (44, mv.BUG_BUZZ),
     (48, mv.FINAL_GAMBIT)),
    ACCELGOR, 0, True, "trade")

STUNFISK = Pokemon(
    618, "Stunfisk", 5, False,
    "", ("Ground", "Electric"),
    109, 73, 91, 32,
    ((1, mv.MUD_SLAP), (1, mv.TACKLE), (1, mv.THUNDER_SHOCK),
     (1, mv.WATER_GUN), (5, mv.ENDURE), (10, mv.MUD_SHOT), (15, mv.REVENGE),
     (20, mv.CHARGE), (25, mv.SUCKER_PUNCH), (30, mv.ELECTRIC_TERRAIN),
     (35, mv.BOUNCE), (40, mv.MUDDY_WATER), (45, mv.DISCHARGE), (50, mv.FLAIL),
     (55, mv.FISSURE)),
    None, 0, False, "")

MIENSHAO = Pokemon(
    620, "Mienshao", 5, False,
    "", ("Fighting",),
    65, 110, 60, 105,
    ((1, mv.DETECT), (1, mv.FAKE_OUT), (1, mv.POUND), (1, mv.QUICK_GUARD),
     (1, mv.REVERSAL), (15, mv.FURY_SWIPES), (20, mv.WIDE_GUARD),
     (25, mv.FORCE_PALM), (30, mv.U_TURN), (35, mv.DRAIN_PUNCH),
     (40, mv.HONE_CLAWS), (45, mv.AURA_SPHERE), (53, mv.BOUNCE),
     (59, mv.CALM_MIND), (66, mv.HIGH_JUMP_KICK)),
    None, 0, False, "")

MIENFOO = Pokemon(
    619, "Mienfoo", 5, False,
    "", ("Fighting",),
    45, 70, 50, 65,
    ((1, mv.DETECT), (1, mv.POUND), (5, mv.FAKE_OUT), (10, mv.REVERSAL),
     (15, mv.FURY_SWIPES), (20, mv.QUICK_GUARD), (25, mv.FORCE_PALM),
     (30, mv.U_TURN), (35, mv.DRAIN_PUNCH), (40, mv.HONE_CLAWS),
     (45, mv.AURA_SPHERE), (51, mv.BOUNCE), (55, mv.CALM_MIND),
     (60, mv.HIGH_JUMP_KICK)),
    MIENSHAO, 50, True, "")

DRUDDIGON = Pokemon(
    621, "Druddigon", 5, False,
    "", ("Dragon",),
    77, 90, 90, 48,
    ((1, mv.LEER), (1, mv.SCRATCH), (5, mv.BITE), (10, mv.DRAGON_TAIL),
     (15, mv.METAL_CLAW), (20, mv.SCARY_FACE), (25, mv.SLASH),
     (30, mv.DRAGON_CLAW), (35, mv.HONE_CLAWS), (40, mv.CRUNCH),
     (45, mv.IRON_HEAD), (50, mv.OUTRAGE), (55, mv.SUPERPOWER)),
    None, 0, False, "")

GOLURK = Pokemon(
    623, "Golurk", 5, False,
    "", ("Ground", "Ghost"),
    89, 89, 80, 55,
    ((1, mv.ASTONISH), (1, mv.DEFENSE_CURL), (1, mv.HIGH_HORSEPOWER),
     (1, mv.POUND), (12, mv.SHADOW_PUNCH), (16, mv.CURSE),
     (20, mv.NIGHT_SHADE), (24, mv.STOMPING_TANTRUM), (28, mv.IRON_DEFENSE),
     (32, mv.MEGA_PUNCH), (36, mv.SHADOW_BALL), (40, mv.HEAVY_SLAM),
     (46, mv.PHANTOM_FORCE), (52, mv.HAMMER_ARM), (58, mv.EARTHQUAKE),
     (64, mv.DYNAMIC_PUNCH)),
    None, 0, False, "")

GOLETT = Pokemon(
    622, "Golett", 5, False,
    "", ("Ground", "Ghost"),
    59, 54, 50, 35,
    ((1, mv.ASTONISH), (1, mv.MUD_SLAP), (4, mv.DEFENSE_CURL), (8, mv.POUND),
     (12, mv.SHADOW_PUNCH), (16, mv.CURSE), (20, mv.NIGHT_SHADE),
     (24, mv.STOMPING_TANTRUM), (28, mv.IRON_DEFENSE), (32, mv.MEGA_PUNCH),
     (36, mv.SHADOW_BALL), (40, mv.HEAVY_SLAM), (44, mv.PHANTOM_FORCE),
     (48, mv.HAMMER_ARM), (52, mv.EARTHQUAKE), (56, mv.DYNAMIC_PUNCH)),
    GOLURK, 43, True, "")


# --- generation 9 ---

KINGAMBIT = Pokemon(
    983, "Kingambit", 9, False,
    "", ("Dark", "Steel"),
    100, 97, 102, 50,
    ((0, mv.KOWTOW_CLEAVE), (1, mv.FURY_CUTTER), (1, mv.LEER),
     (1, mv.METAL_BURST), (1, mv.METAL_CLAW), (1, mv.SCRATCH),
     (15, mv.TORMENT), (20, mv.SCARY_FACE), (25, mv.ASSURANCE),
     (30, mv.METAL_SOUND), (35, mv.SLASH), (40, mv.NIGHT_SLASH),
     (45, mv.IRON_DEFENSE), (50, mv.RETALIATE), (57, mv.IRON_HEAD),
     (64, mv.SWORDS_DANCE), (71, mv.GUILLOTINE)),
    None, 0, False, "")


# --- generation 5 ---

BISHARP = Pokemon(
    625, "Bisharp", 5, False,
    "", ("Dark", "Steel"),
    65, 92, 85, 70,
    ((1, mv.FURY_CUTTER), (1, mv.LEER), (1, mv.METAL_BURST),
     (1, mv.METAL_CLAW), (1, mv.SCRATCH), (15, mv.TORMENT),
     (20, mv.SCARY_FACE), (25, mv.ASSURANCE), (30, mv.METAL_SOUND),
     (35, mv.SLASH), (40, mv.NIGHT_SLASH), (45, mv.IRON_DEFENSE),
     (50, mv.RETALIATE), (57, mv.IRON_HEAD), (64, mv.SWORDS_DANCE),
     (71, mv.GUILLOTINE)),
    KINGAMBIT, 0, True,
    "Level up after defeating 3 Bisharp holding a Leader's Crest")

PAWNIARD = Pokemon(
    624, "Pawniard", 5, False,
    "", ("Dark", "Steel"),
    45, 62, 55, 60,
    ((1, mv.LEER), (1, mv.SCRATCH), (5, mv.FURY_CUTTER), (10, mv.METAL_CLAW),
     (15, mv.TORMENT), (20, mv.SCARY_FACE), (25, mv.ASSURANCE),
     (30, mv.METAL_SOUND), (35, mv.SLASH), (40, mv.NIGHT_SLASH),
     (45, mv.IRON_DEFENSE), (50, mv.RETALIATE), (55, mv.IRON_HEAD),
     (60, mv.SWORDS_DANCE), (65, mv.GUILLOTINE)),
    BISHARP, 52, True, "")

BOUFFALANT = Pokemon(
    626, "Bouffalant", 5, False,
    "", ("Normal",),
    95, 75, 95, 55,
    ((1, mv.LEER), (1, mv.TACKLE), (5, mv.FOCUS_ENERGY), (10, mv.FURY_ATTACK),
     (15, mv.REVENGE), (20, mv.SCARY_FACE), (25, mv.HORN_ATTACK),
     (30, mv.REVERSAL), (35, mv.THROAT_CHOP), (40, mv.HEAD_CHARGE),
     (45, mv.SWORDS_DANCE), (50, mv.MEGAHORN), (55, mv.GIGA_IMPACT)),
    None, 0, False, "")

BRAVIARY = Pokemon(
    628, "Braviary", 5, False,
    "", ("Normal", "Flying"),
    100, 90, 75, 80,
    ((0, mv.SUPERPOWER), (1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.PECK),
     (1, mv.SKY_ATTACK), (1, mv.WING_ATTACK), (18, mv.TAILWIND),
     (24, mv.SCARY_FACE), (30, mv.AERIAL_ACE), (36, mv.SLASH),
     (42, mv.WHIRLWIND), (48, mv.CRUSH_CLAW), (57, mv.AIR_SLASH),
     (64, mv.DEFOG), (72, mv.THRASH)),
    None, 0, False, "")

RUFFLET = Pokemon(
    627, "Rufflet", 5, False,
    "", ("Normal", "Flying"),
    70, 60, 50, 60,
    ((1, mv.LEER), (1, mv.PECK), (6, mv.HONE_CLAWS), (12, mv.WING_ATTACK),
     (18, mv.TAILWIND), (24, mv.SCARY_FACE), (30, mv.AERIAL_ACE),
     (36, mv.SLASH), (42, mv.WHIRLWIND), (48, mv.CRUSH_CLAW),
     (55, mv.AIR_SLASH), (60, mv.DEFOG), (66, mv.THRASH), (72, mv.BRAVE_BIRD)),
    BRAVIARY, 54, True, "")

MANDIBUZZ = Pokemon(
    630, "Mandibuzz", 5, False,
    "", ("Dark", "Flying"),
    110, 60, 100, 80,
    ((0, mv.BONE_RUSH), (1, mv.FLATTER), (1, mv.GUST), (1, mv.LEER),
     (1, mv.PLUCK), (1, mv.SKY_ATTACK), (1, mv.TOXIC), (18, mv.TAILWIND),
     (24, mv.KNOCK_OFF), (30, mv.IRON_DEFENSE), (36, mv.WHIRLWIND),
     (42, mv.AIR_SLASH), (48, mv.DARK_PULSE), (57, mv.NASTY_PLOT),
     (64, mv.DEFOG), (72, mv.ATTRACT), (80, mv.BRAVE_BIRD)),
    None, 0, False, "")

VULLABY = Pokemon(
    629, "Vullaby", 5, False,
    "", ("Dark", "Flying"),
    70, 50, 70, 60,
    ((1, mv.GUST), (1, mv.LEER), (6, mv.FLATTER), (12, mv.PLUCK),
     (18, mv.TAILWIND), (24, mv.KNOCK_OFF), (30, mv.IRON_DEFENSE),
     (36, mv.WHIRLWIND), (42, mv.AIR_SLASH), (48, mv.DARK_PULSE),
     (54, mv.NASTY_PLOT), (60, mv.DEFOG), (66, mv.ATTRACT),
     (72, mv.BRAVE_BIRD)),
    MANDIBUZZ, 54, True, "")

HEATMOR = Pokemon(
    631, "Heatmor", 5, False,
    "", ("Fire",),
    85, 101, 66, 65,
    ((1, mv.LICK), (1, mv.TACKLE), (5, mv.FURY_SWIPES), (10, mv.INCINERATE),
     (15, mv.BUG_BITE), (20, mv.SPIT_UP), (20, mv.STOCKPILE), (20, mv.SWALLOW),
     (25, mv.SLASH), (30, mv.BIND), (35, mv.FIRE_LASH), (40, mv.HONE_CLAWS),
     (45, mv.AMNESIA), (50, mv.FIRE_SPIN), (55, mv.INFERNO),
     (60, mv.FLARE_BLITZ)),
    None, 0, False, "")

DURANT = Pokemon(
    632, "Durant", 5, False,
    "", ("Bug", "Steel"),
    58, 78, 80, 109,
    ((1, mv.FURY_CUTTER), (1, mv.SAND_ATTACK), (4, mv.VISE_GRIP),
     (8, mv.METAL_CLAW), (12, mv.BEAT_UP), (16, mv.BUG_BITE), (20, mv.BITE),
     (24, mv.AGILITY), (28, mv.DIG), (32, mv.X_SCISSOR), (36, mv.CRUNCH),
     (40, mv.METAL_SOUND), (44, mv.IRON_HEAD), (48, mv.ENTRAINMENT),
     (52, mv.IRON_DEFENSE), (56, mv.GUILLOTINE)),
    None, 0, False, "")

HYDREIGON = Pokemon(
    635, "Hydreigon", 5, False,
    "", ("Dark", "Dragon"),
    92, 115, 90, 98,
    ((1, mv.BITE), (1, mv.DOUBLE_HIT), (1, mv.DRAGON_BREATH),
     (1, mv.FOCUS_ENERGY), (1, mv.TACKLE), (1, mv.TRI_ATTACK), (12, mv.ROAR),
     (16, mv.ASSURANCE), (20, mv.HEADBUTT), (24, mv.WORK_UP), (28, mv.SLAM),
     (32, mv.CRUNCH), (36, mv.SCARY_FACE), (40, mv.DRAGON_PULSE),
     (44, mv.BODY_SLAM), (48, mv.HYPER_VOICE), (54, mv.DRAGON_RUSH),
     (60, mv.NASTY_PLOT), (68, mv.OUTRAGE), (76, mv.HYPER_BEAM)),
    None, 0, False, "")

ZWEILOUS = Pokemon(
    634, "Zweilous", 5, False,
    "", ("Dark", "Dragon"),
    72, 75, 70, 58,
    ((1, mv.BITE), (1, mv.DOUBLE_HIT), (1, mv.DRAGON_BREATH),
     (1, mv.FOCUS_ENERGY), (1, mv.TACKLE), (12, mv.ROAR), (16, mv.ASSURANCE),
     (20, mv.HEADBUTT), (24, mv.WORK_UP), (28, mv.SLAM), (32, mv.CRUNCH),
     (36, mv.SCARY_FACE), (40, mv.DRAGON_PULSE), (44, mv.BODY_SLAM),
     (48, mv.HYPER_VOICE), (54, mv.DRAGON_RUSH), (60, mv.NASTY_PLOT),
     (66, mv.OUTRAGE)),
    HYDREIGON, 64, True, "")

DEINO = Pokemon(
    633, "Deino", 5, False,
    "", ("Dark", "Dragon"),
    52, 55, 50, 38,
    ((1, mv.FOCUS_ENERGY), (1, mv.TACKLE), (4, mv.DRAGON_BREATH), (8, mv.BITE),
     (12, mv.ROAR), (16, mv.ASSURANCE), (20, mv.HEADBUTT), (24, mv.WORK_UP),
     (28, mv.SLAM), (32, mv.CRUNCH), (36, mv.SCARY_FACE),
     (40, mv.DRAGON_PULSE), (44, mv.BODY_SLAM), (48, mv.HYPER_VOICE),
     (52, mv.DRAGON_RUSH), (56, mv.NASTY_PLOT), (60, mv.OUTRAGE)),
    ZWEILOUS, 50, True, "")

VOLCARONA = Pokemon(
    637, "Volcarona", 5, False,
    "", ("Bug", "Fire"),
    85, 97, 85, 100,
    ((0, mv.QUIVER_DANCE), (1, mv.DOUBLE_EDGE), (1, mv.EMBER),
     (1, mv.FIERY_DANCE), (1, mv.FIRE_SPIN), (1, mv.FLAME_CHARGE),
     (1, mv.FLARE_BLITZ), (1, mv.GUST), (1, mv.STRING_SHOT),
     (1, mv.STRUGGLE_BUG), (1, mv.TAKE_DOWN), (1, mv.WHIRLWIND),
     (18, mv.FLAME_WHEEL), (24, mv.BUG_BITE), (30, mv.SCREECH),
     (36, mv.LEECH_LIFE), (42, mv.BUG_BUZZ), (48, mv.HEAT_WAVE),
     (54, mv.AMNESIA), (62, mv.HURRICANE), (70, mv.FIRE_BLAST),
     (78, mv.RAGE_POWDER)),
    None, 0, False, "")

LARVESTA = Pokemon(
    636, "Larvesta", 5, False,
    "", ("Bug", "Fire"),
    55, 67, 55, 60,
    ((1, mv.EMBER), (1, mv.STRING_SHOT), (6, mv.FLAME_CHARGE),
     (12, mv.STRUGGLE_BUG), (18, mv.FLAME_WHEEL), (24, mv.BUG_BITE),
     (30, mv.SCREECH), (36, mv.LEECH_LIFE), (42, mv.BUG_BUZZ),
     (48, mv.TAKE_DOWN), (54, mv.AMNESIA), (60, mv.DOUBLE_EDGE),
     (66, mv.FLARE_BLITZ)),
    VOLCARONA, 59, True, "")

COBALION = Pokemon(
    638, "Cobalion", 5, False,
    "", ("Steel", "Fighting"),
    91, 90, 100, 108,
    ((1, mv.HELPING_HAND), (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.WORK_UP),
     (7, mv.METAL_CLAW), (14, mv.QUICK_GUARD), (21, mv.DOUBLE_KICK),
     (28, mv.RETALIATE), (35, mv.METAL_BURST), (42, mv.TAKE_DOWN),
     (49, mv.SACRED_SWORD), (56, mv.SWORDS_DANCE), (63, mv.IRON_HEAD),
     (70, mv.CLOSE_COMBAT)),
    None, 0, False, "")

TERRAKION = Pokemon(
    639, "Terrakion", 5, False,
    "", ("Rock", "Fighting"),
    91, 100, 90, 108,
    ((1, mv.HELPING_HAND), (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.WORK_UP),
     (7, mv.SMACK_DOWN), (14, mv.QUICK_GUARD), (21, mv.DOUBLE_KICK),
     (28, mv.RETALIATE), (35, mv.ROCK_SLIDE), (42, mv.TAKE_DOWN),
     (49, mv.SACRED_SWORD), (56, mv.SWORDS_DANCE), (63, mv.STONE_EDGE),
     (70, mv.CLOSE_COMBAT)),
    None, 0, False, "")

VIRIZION = Pokemon(
    640, "Virizion", 5, False,
    "", ("Grass", "Fighting"),
    91, 90, 100, 108,
    ((1, mv.HELPING_HAND), (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.WORK_UP),
     (7, mv.MAGICAL_LEAF), (14, mv.QUICK_GUARD), (21, mv.DOUBLE_KICK),
     (28, mv.RETALIATE), (35, mv.GIGA_DRAIN), (42, mv.SYNTHESIS),
     (49, mv.SACRED_SWORD), (56, mv.SWORDS_DANCE), (63, mv.LEAF_BLADE),
     (70, mv.CLOSE_COMBAT)),
    None, 0, False, "")

TORNADUS = Pokemon(
    641, "Tornadus", 5, False,
    "", ("Flying",),
    79, 120, 75, 111,
    ((1, mv.ASTONISH), (1, mv.GUST), (5, mv.LEER), (10, mv.SWAGGER),
     (15, mv.BITE), (20, mv.AIR_CUTTER), (25, mv.AGILITY), (30, mv.TAILWIND),
     (35, mv.AIR_SLASH), (40, mv.CRUNCH), (45, mv.EXTRASENSORY),
     (50, mv.UPROAR), (55, mv.HAMMER_ARM), (60, mv.RAIN_DANCE),
     (65, mv.HURRICANE), (70, mv.THRASH), (77, mv.BLEAKWIND_STORM)),
    None, 0, False, "")

THUNDURUS = Pokemon(
    642, "Thundurus", 5, False,
    "", ("Electric", "Flying"),
    79, 120, 75, 111,
    ((1, mv.ASTONISH), (1, mv.THUNDER_SHOCK), (5, mv.LEER), (10, mv.SWAGGER),
     (15, mv.BITE), (20, mv.SHOCK_WAVE), (25, mv.AGILITY), (30, mv.CHARGE),
     (35, mv.VOLT_SWITCH), (40, mv.CRUNCH), (45, mv.DISCHARGE),
     (50, mv.UPROAR), (55, mv.HAMMER_ARM), (60, mv.RAIN_DANCE),
     (65, mv.THUNDER), (70, mv.THRASH), (75, mv.WILDBOLT_STORM)),
    None, 0, False, "")

RESHIRAM = Pokemon(
    643, "Reshiram", 5, False,
    "", ("Dragon", "Fire"),
    100, 135, 110, 90,
    ((1, mv.ANCIENT_POWER), (1, mv.DRAGON_BREATH), (1, mv.FIRE_FANG),
     (1, mv.NOBLE_ROAR), (8, mv.SLASH), (16, mv.CRUNCH), (24, mv.EXTRASENSORY),
     (32, mv.DRAGON_PULSE), (40, mv.FLAMETHROWER), (48, mv.FUSION_FLARE),
     (56, mv.HYPER_VOICE), (64, mv.FIRE_BLAST), (72, mv.IMPRISON),
     (80, mv.OUTRAGE), (88, mv.BLUE_FLARE)),
    None, 0, False, "")

ZEKROM = Pokemon(
    644, "Zekrom", 5, False,
    "", ("Dragon", "Electric"),
    100, 135, 110, 90,
    ((1, mv.ANCIENT_POWER), (1, mv.DRAGON_BREATH), (1, mv.NOBLE_ROAR),
     (1, mv.THUNDER_FANG), (8, mv.SLASH), (16, mv.CRUNCH),
     (24, mv.ZEN_HEADBUTT), (32, mv.DRAGON_CLAW), (40, mv.THUNDERBOLT),
     (48, mv.FUSION_BOLT), (56, mv.HYPER_VOICE), (64, mv.THUNDER),
     (72, mv.IMPRISON), (80, mv.OUTRAGE), (88, mv.BOLT_STRIKE)),
    None, 0, False, "")

LANDORUS = Pokemon(
    645, "Landorus", 5, False,
    "", ("Ground", "Flying"),
    89, 120, 85, 101,
    ((1, mv.SAND_TOMB), (1, mv.SMACK_DOWN), (5, mv.LEER), (10, mv.BLOCK),
     (15, mv.BULLDOZE), (20, mv.ROCK_TOMB), (30, mv.IMPRISON),
     (35, mv.ROCK_SLIDE), (40, mv.EARTH_POWER), (45, mv.EXTRASENSORY),
     (50, mv.STONE_EDGE), (55, mv.HAMMER_ARM), (60, mv.SANDSTORM),
     (65, mv.EARTHQUAKE), (70, mv.OUTRAGE), (75, mv.FISSURE),
     (80, mv.SANDSEAR_STORM)),
    None, 0, False, "")

KYUREM = Pokemon(
    646, "Kyurem", 5, False,
    "", ("Dragon", "Ice"),
    125, 130, 90, 95,
    ((1, mv.ANCIENT_POWER), (1, mv.DRAGON_BREATH), (1, mv.FREEZE_DRY),
     (1, mv.NOBLE_ROAR), (8, mv.SLASH), (16, mv.ENDEAVOR),
     (24, mv.DRAGON_PULSE), (32, mv.ICE_BEAM), (40, mv.HYPER_VOICE),
     (48, mv.SCARY_FACE), (56, mv.BLIZZARD), (64, mv.IMPRISON),
     (72, mv.OUTRAGE), (80, mv.GLACIATE), (88, mv.SHEER_COLD)),
    None, 0, False, "")

KELDEO = Pokemon(
    647, "Keldeo", 5, False,
    "", ("Water", "Fighting"),
    91, 100, 90, 108,
    ((1, mv.AQUA_JET), (1, mv.HELPING_HAND), (1, mv.LEER),
     (1, mv.SECRET_SWORD), (1, mv.WORK_UP), (7, mv.BUBBLE_BEAM),
     (14, mv.QUICK_GUARD), (21, mv.DOUBLE_KICK), (28, mv.RETALIATE),
     (35, mv.AQUA_TAIL), (42, mv.TAKE_DOWN), (49, mv.SACRED_SWORD),
     (56, mv.SWORDS_DANCE), (63, mv.HYDRO_PUMP), (70, mv.CLOSE_COMBAT)),
    None, 0, False, "")

MELOETTA = Pokemon(
    648, "Meloetta", 5, False,
    "", ("Normal", "Psychic"),
    100, 102, 102, 90,
    ((1, mv.CONFUSION), (1, mv.QUICK_ATTACK), (1, mv.ROUND), (1, mv.SING),
     (21, mv.TEETER_DANCE), (26, mv.ACROBATICS), (31, mv.PSYBEAM),
     (36, mv.ECHOED_VOICE), (43, mv.U_TURN), (50, mv.RELIC_SONG),
     (57, mv.PSYCHIC), (64, mv.HYPER_VOICE), (71, mv.ROLE_PLAY),
     (78, mv.CLOSE_COMBAT), (85, mv.PERISH_SONG)),
    None, 0, False, "")

GENESECT = Pokemon(
    649, "Genesect", 5, False,
    "", ("Bug", "Steel"),
    71, 120, 95, 99,
    ((1, mv.FURY_CUTTER), (1, mv.QUICK_ATTACK), (7, mv.SCREECH),
     (14, mv.METAL_CLAW), (21, mv.FELL_STINGER), (28, mv.FLAME_CHARGE),
     (35, mv.METAL_SOUND), (42, mv.X_SCISSOR), (49, mv.MAGNET_RISE),
     (56, mv.BUG_BUZZ), (63, mv.SIMPLE_BEAM), (70, mv.ZAP_CANNON),
     (77, mv.LOCK_ON), (84, mv.TECHNO_BLAST), (91, mv.SELF_DESTRUCT)),
    None, 0, False, "")


# --- generation 6 ---

CHESNAUGHT = Pokemon(
    652, "Chesnaught", 6, True,
    "Flora", ("Grass", "Fighting"),
    88, 90, 98, 64,
    ((0, mv.SPIKY_SHIELD), (1, mv.FEINT), (1, mv.GROWL), (1, mv.HAMMER_ARM),
     (1, mv.ROLLOUT), (1, mv.TACKLE), (1, mv.VINE_WHIP), (11, mv.BITE),
     (15, mv.LEECH_SEED), (19, mv.PIN_MISSILE), (29, mv.TAKE_DOWN),
     (35, mv.SEED_BOMB), (41, mv.MUD_SHOT), (48, mv.BULK_UP),
     (54, mv.BODY_SLAM), (60, mv.PAIN_SPLIT), (66, mv.WOOD_HAMMER),
     (78, mv.GIGA_IMPACT)),
    None, 0, False, "")

QUILLADIN = Pokemon(
    651, "Quilladin", 6, True,
    "Flora", ("Grass",),
    61, 67, 76, 57,
    ((1, mv.GROWL), (1, mv.VINE_WHIP), (8, mv.ROLLOUT), (11, mv.BITE),
     (15, mv.LEECH_SEED), (20, mv.SEED_BOMB), (24, mv.PIN_MISSILE),
     (29, mv.TAKE_DOWN), (34, mv.MUD_SHOT), (38, mv.BULK_UP),
     (43, mv.BODY_SLAM), (47, mv.PAIN_SPLIT), (53, mv.WOOD_HAMMER)),
    CHESNAUGHT, 36, True, "")

CHESPIN = Pokemon(
    650, "Chespin", 6, True,
    "Flora", ("Grass",),
    56, 54, 55, 38,
    ((1, mv.GROWL), (1, mv.VINE_WHIP), (8, mv.ROLLOUT), (11, mv.BITE),
     (15, mv.LEECH_SEED), (18, mv.PIN_MISSILE), (27, mv.TAKE_DOWN),
     (32, mv.SEED_BOMB), (35, mv.MUD_SHOT), (42, mv.BODY_SLAM),
     (45, mv.PAIN_SPLIT), (48, mv.WOOD_HAMMER)),
    QUILLADIN, 16, True, "")

DELPHOX = Pokemon(
    655, "Delphox", 6, True,
    "Flame", ("Fire", "Psychic"),
    75, 91, 86, 104,
    ((0, mv.MYSTICAL_FIRE), (1, mv.EMBER), (1, mv.FUTURE_SIGHT), (1, mv.HOWL),
     (1, mv.ROLE_PLAY), (1, mv.SCRATCH), (1, mv.SHADOW_BALL),
     (1, mv.SWITCHEROO), (1, mv.TAIL_WHIP), (14, mv.FLAME_CHARGE),
     (18, mv.PSYBEAM), (22, mv.FIRE_SPIN), (28, mv.LIGHT_SCREEN),
     (38, mv.PSYSHOCK), (45, mv.FLAMETHROWER), (51, mv.WILL_O_WISP),
     (57, mv.PSYCHIC), (62, mv.SUNNY_DAY), (68, mv.MAGIC_ROOM),
     (74, mv.FIRE_BLAST)),
    None, 0, False, "")

BRAIXEN = Pokemon(
    654, "Braixen", 6, True,
    "Flame", ("Fire",),
    59, 74, 64, 73,
    ((1, mv.EMBER), (1, mv.SCRATCH), (1, mv.TAIL_WHIP), (11, mv.HOWL),
     (14, mv.FLAME_CHARGE), (18, mv.PSYBEAM), (22, mv.FIRE_SPIN),
     (28, mv.LIGHT_SCREEN), (36, mv.PSYSHOCK), (41, mv.FLAMETHROWER),
     (45, mv.WILL_O_WISP), (49, mv.PSYCHIC), (52, mv.SUNNY_DAY),
     (56, mv.MAGIC_ROOM), (59, mv.FIRE_BLAST)),
    DELPHOX, 36, True, "")

FENNEKIN = Pokemon(
    653, "Fennekin", 6, True,
    "Flame", ("Fire",),
    40, 53, 50, 60,
    ((1, mv.SCRATCH), (1, mv.TAIL_WHIP), (5, mv.EMBER), (11, mv.HOWL),
     (14, mv.FLAME_CHARGE), (17, mv.PSYBEAM), (20, mv.FIRE_SPIN),
     (25, mv.LIGHT_SCREEN), (31, mv.PSYSHOCK), (35, mv.FLAMETHROWER),
     (38, mv.WILL_O_WISP), (41, mv.PSYCHIC), (43, mv.SUNNY_DAY),
     (48, mv.FIRE_BLAST)),
    BRAIXEN, 16, True, "")

GRENINJA = Pokemon(
    658, "Greninja", 6, True,
    "Aqua", ("Water", "Dark"),
    72, 99, 69, 122,
    ((0, mv.WATER_SHURIKEN), (1, mv.GROWL), (1, mv.HAZE), (1, mv.NIGHT_SLASH),
     (1, mv.POUND), (1, mv.QUICK_ATTACK), (1, mv.ROLE_PLAY), (1, mv.WATER_GUN),
     (10, mv.LICK), (14, mv.WATER_PULSE), (19, mv.SMOKESCREEN),
     (23, mv.SHADOW_SNEAK), (28, mv.SPIKES), (33, mv.AERIAL_ACE),
     (42, mv.SUBSTITUTE), (49, mv.EXTRASENSORY), (56, mv.DOUBLE_TEAM),
     (68, mv.HYDRO_PUMP)),
    None, 0, False, "")

FROGADIER = Pokemon(
    657, "Frogadier", 6, True,
    "Aqua", ("Water",),
    54, 73, 54, 97,
    ((1, mv.GROWL), (1, mv.POUND), (1, mv.WATER_GUN), (8, mv.QUICK_ATTACK),
     (10, mv.LICK), (14, mv.WATER_PULSE), (19, mv.SMOKESCREEN), (23, mv.ROUND),
     (28, mv.FLING), (33, mv.SMACK_DOWN), (40, mv.SUBSTITUTE), (45, mv.BOUNCE),
     (50, mv.DOUBLE_TEAM), (56, mv.HYDRO_PUMP)),
    GRENINJA, 36, True, "")

FROAKIE = Pokemon(
    656, "Froakie", 6, True,
    "Aqua", ("Water",),
    41, 59, 42, 71,
    ((1, mv.GROWL), (1, mv.POUND), (5, mv.WATER_GUN), (8, mv.QUICK_ATTACK),
     (10, mv.LICK), (14, mv.WATER_PULSE), (18, mv.SMOKESCREEN), (21, mv.ROUND),
     (25, mv.FLING), (29, mv.SMACK_DOWN), (35, mv.SUBSTITUTE), (39, mv.BOUNCE),
     (43, mv.DOUBLE_TEAM), (48, mv.HYDRO_PUMP)),
    FROGADIER, 16, True, "")

DIGGERSBY = Pokemon(
    660, "Diggersby", 6, False,
    "", ("Normal", "Ground"),
    85, 53, 77, 78,
    ((1, mv.LASER_FOCUS), (1, mv.LEER), (1, mv.MUD_SLAP), (1, mv.TACKLE),
     (9, mv.QUICK_ATTACK), (12, mv.MUD_SHOT), (15, mv.FLAIL),
     (18, mv.DOUBLE_KICK), (23, mv.BULLDOZE), (28, mv.DIG), (33, mv.BOUNCE),
     (38, mv.TAKE_DOWN), (43, mv.SWORDS_DANCE), (48, mv.EARTHQUAKE),
     (53, mv.SUPER_FANG), (58, mv.HAMMER_ARM)),
    None, 0, False, "")

BUNNELBY = Pokemon(
    659, "Bunnelby", 6, False,
    "", ("Normal",),
    38, 34, 37, 57,
    ((1, mv.LEER), (1, mv.MUD_SLAP), (3, mv.TACKLE), (6, mv.LASER_FOCUS),
     (9, mv.QUICK_ATTACK), (12, mv.MUD_SHOT), (15, mv.FLAIL),
     (18, mv.DOUBLE_KICK), (21, mv.BULLDOZE), (24, mv.DIG), (27, mv.BOUNCE),
     (30, mv.TAKE_DOWN), (33, mv.SWORDS_DANCE), (36, mv.EARTHQUAKE),
     (39, mv.SUPER_FANG)),
    DIGGERSBY, 20, True, "")

TALONFLAME = Pokemon(
    663, "Talonflame", 6, False,
    "", ("Fire", "Flying"),
    78, 77, 70, 126,
    ((1, mv.EMBER), (1, mv.FEINT), (1, mv.FLAME_CHARGE), (1, mv.FLARE_BLITZ),
     (1, mv.GROWL), (1, mv.PECK), (1, mv.QUICK_ATTACK), (15, mv.FLAIL),
     (22, mv.ACROBATICS), (29, mv.AGILITY), (38, mv.AERIAL_ACE),
     (47, mv.TAILWIND), (56, mv.STEEL_WING), (65, mv.ROOST), (74, mv.FLY),
     (83, mv.BRAVE_BIRD)),
    None, 0, False, "")

FLETCHINDER = Pokemon(
    662, "Fletchinder", 6, False,
    "", ("Fire", "Flying"),
    62, 64, 53, 84,
    ((0, mv.FLAME_CHARGE), (1, mv.EMBER), (1, mv.FEINT), (1, mv.GROWL),
     (1, mv.PECK), (1, mv.QUICK_ATTACK), (15, mv.FLAIL), (22, mv.ACROBATICS),
     (29, mv.AGILITY), (36, mv.AERIAL_ACE), (43, mv.TAILWIND),
     (50, mv.STEEL_WING), (57, mv.ROOST), (64, mv.FLY)),
    TALONFLAME, 35, True, "")

FLETCHLING = Pokemon(
    661, "Fletchling", 6, False,
    "", ("Normal", "Flying"),
    45, 45, 40, 62,
    ((1, mv.GROWL), (1, mv.PECK), (5, mv.QUICK_ATTACK), (10, mv.EMBER),
     (15, mv.FLAIL), (20, mv.ACROBATICS), (25, mv.AGILITY),
     (30, mv.AERIAL_ACE), (35, mv.TAILWIND), (40, mv.STEEL_WING),
     (45, mv.ROOST), (50, mv.FLY)),
    FLETCHINDER, 17, True, "")

VIVILLON = Pokemon(
    666, "Vivillon", 6, False,
    "", ("Bug", "Flying"),
    80, 71, 50, 89,
    ((0, mv.GUST), (1, mv.POISON_POWDER), (1, mv.SLEEP_POWDER),
     (1, mv.STRUGGLE_BUG), (1, mv.STUN_SPORE), (12, mv.LIGHT_SCREEN),
     (17, mv.PSYBEAM), (21, mv.SUPERSONIC), (25, mv.DRAINING_KISS),
     (31, mv.SAFEGUARD), (35, mv.BUG_BUZZ), (45, mv.QUIVER_DANCE),
     (50, mv.HURRICANE)),
    None, 0, False, "")

SPEWPA = Pokemon(
    665, "Spewpa", 6, False,
    "", ("Bug",),
    45, 24, 45, 29,
    ((0, mv.PROTECT), (1, mv.HARDEN)),
    VIVILLON, 12, True, "")

SCATTERBUG = Pokemon(
    664, "Scatterbug", 6, False,
    "", ("Bug",),
    38, 31, 32, 35,
    ((1, mv.STRING_SHOT), (1, mv.TACKLE), (6, mv.STUN_SPORE),
     (15, mv.BUG_BITE)),
    SPEWPA, 9, True, "")

PYROAR = Pokemon(
    668, "Pyroar", 6, False,
    "", ("Fire", "Normal"),
    86, 88, 69, 106,
    ((1, mv.EMBER), (1, mv.HYPER_BEAM), (1, mv.LEER), (1, mv.TACKLE),
     (1, mv.WORK_UP), (11, mv.HEADBUTT), (15, mv.NOBLE_ROAR),
     (20, mv.TAKE_DOWN), (23, mv.FIRE_FANG), (28, mv.ENDEAVOR),
     (33, mv.ECHOED_VOICE), (38, mv.FLAMETHROWER), (42, mv.CRUNCH),
     (48, mv.HYPER_VOICE), (51, mv.INCINERATE), (57, mv.OVERHEAT)),
    None, 0, False, "")

LITLEO = Pokemon(
    667, "Litleo", 6, False,
    "", ("Fire", "Normal"),
    62, 61, 56, 72,
    ((1, mv.LEER), (1, mv.TACKLE), (5, mv.EMBER), (8, mv.WORK_UP),
     (11, mv.HEADBUTT), (15, mv.NOBLE_ROAR), (20, mv.TAKE_DOWN),
     (23, mv.FIRE_FANG), (28, mv.ENDEAVOR), (33, mv.ECHOED_VOICE),
     (36, mv.FLAMETHROWER), (39, mv.CRUNCH), (43, mv.HYPER_VOICE),
     (46, mv.INCINERATE), (50, mv.OVERHEAT)),
    PYROAR, 35, True, "")

FLORGES = Pokemon(
    671, "Florges", 6, False,
    "", ("Fairy",),
    78, 88, 111, 75,
    ((1, mv.DISARMING_VOICE), (1, mv.GRASSY_TERRAIN), (1, mv.GRASS_KNOT),
     (1, mv.MAGICAL_LEAF), (1, mv.MISTY_TERRAIN), (1, mv.PETAL_BLIZZARD),
     (1, mv.PETAL_DANCE), (1, mv.SAFEGUARD), (1, mv.SOLAR_BEAM),
     (1, mv.SYNTHESIS), (1, mv.WISH), (5, mv.MOONBLAST)),
    None, 0, False, "")

FLOETTE = Pokemon(
    670, "Floette", 6, False,
    "", ("Fairy",),
    54, 60, 72, 52,
    ((1, mv.FAIRY_WIND), (1, mv.TACKLE), (1, mv.VINE_WHIP), (10, mv.SAFEGUARD),
     (15, mv.RAZOR_LEAF), (20, mv.WISH), (25, mv.MAGICAL_LEAF),
     (27, mv.GRASSY_TERRAIN), (33, mv.PETAL_BLIZZARD), (38, mv.SYNTHESIS),
     (43, mv.MISTY_TERRAIN), (46, mv.MOONBLAST), (51, mv.PETAL_DANCE),
     (58, mv.SOLAR_BEAM)),
    FLORGES, 0, True, "item:shiny-stone")

FLABEBE = Pokemon(
    669, "Flabébé", 6, False,
    "", ("Fairy",),
    44, 49, 59, 42,
    ((1, mv.TACKLE), (1, mv.VINE_WHIP), (6, mv.FAIRY_WIND), (10, mv.SAFEGUARD),
     (15, mv.RAZOR_LEAF), (20, mv.WISH), (22, mv.MAGICAL_LEAF),
     (24, mv.GRASSY_TERRAIN), (28, mv.PETAL_BLIZZARD), (33, mv.SYNTHESIS),
     (37, mv.MISTY_TERRAIN), (41, mv.MOONBLAST), (45, mv.PETAL_DANCE),
     (48, mv.SOLAR_BEAM)),
    FLOETTE, 19, True, "")

GOGOAT = Pokemon(
    673, "Gogoat", 6, False,
    "", ("Grass",),
    123, 98, 71, 68,
    ((0, mv.AERIAL_ACE), (1, mv.EARTHQUAKE), (1, mv.GROWTH), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (1, mv.VINE_WHIP), (12, mv.LEECH_SEED),
     (13, mv.RAZOR_LEAF), (16, mv.WORRY_SEED), (20, mv.SYNTHESIS),
     (22, mv.TAKE_DOWN), (26, mv.BULLDOZE), (30, mv.SEED_BOMB),
     (34, mv.BULK_UP), (40, mv.DOUBLE_EDGE), (47, mv.HORN_LEECH),
     (55, mv.LEAF_BLADE), (58, mv.MILK_DRINK)),
    None, 0, False, "")

SKIDDO = Pokemon(
    672, "Skiddo", 6, False,
    "", ("Grass",),
    66, 63, 52, 52,
    ((1, mv.GROWTH), (1, mv.TACKLE), (7, mv.VINE_WHIP), (9, mv.TAIL_WHIP),
     (12, mv.LEECH_SEED), (13, mv.RAZOR_LEAF), (16, mv.WORRY_SEED),
     (20, mv.SYNTHESIS), (22, mv.TAKE_DOWN), (26, mv.BULLDOZE),
     (30, mv.SEED_BOMB), (34, mv.BULK_UP), (38, mv.DOUBLE_EDGE),
     (42, mv.HORN_LEECH), (45, mv.LEAF_BLADE)),
    GOGOAT, 32, True, "")

PANGORO = Pokemon(
    675, "Pangoro", 6, False,
    "", ("Fighting", "Dark"),
    95, 96, 74, 58,
    ((1, mv.ARM_THRUST), (1, mv.BULLET_PUNCH), (1, mv.LEER),
     (1, mv.NIGHT_SLASH), (1, mv.TACKLE), (1, mv.TAUNT), (12, mv.CIRCLE_THROW),
     (16, mv.LOW_SWEEP), (20, mv.WORK_UP), (24, mv.SLASH),
     (28, mv.VITAL_THROW), (35, mv.CRUNCH), (40, mv.BODY_SLAM),
     (46, mv.PARTING_SHOT), (52, mv.ENTRAINMENT), (58, mv.HAMMER_ARM)),
    None, 0, False, "")

PANCHAM = Pokemon(
    674, "Pancham", 6, False,
    "", ("Fighting",),
    67, 64, 55, 43,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.ARM_THRUST), (8, mv.TAUNT),
     (12, mv.CIRCLE_THROW), (16, mv.LOW_SWEEP), (20, mv.WORK_UP),
     (24, mv.SLASH), (28, mv.VITAL_THROW), (33, mv.CRUNCH), (36, mv.BODY_SLAM),
     (40, mv.PARTING_SHOT), (44, mv.ENTRAINMENT)),
    PANGORO, 32, True, "")

FURFROU = Pokemon(
    676, "Furfrou", 6, False,
    "", ("Normal",),
    75, 72, 75, 102,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.SAND_ATTACK),
     (9, mv.BABY_DOLL_EYES), (12, mv.HEADBUTT), (15, mv.TAIL_WHIP),
     (22, mv.BITE), (27, mv.ODOR_SLEUTH), (33, mv.RETALIATE),
     (35, mv.TAKE_DOWN), (38, mv.CHARM), (42, mv.SUCKER_PUNCH),
     (48, mv.COTTON_GUARD)),
    None, 0, False, "")

MEOWSTIC = Pokemon(
    678, "Meowstic", 6, False,
    "", ("Psychic",),
    74, 65, 78, 104,
    ((1, mv.DISARMING_VOICE), (1, mv.FAKE_OUT), (1, mv.LEER),
     (1, mv.MEAN_LOOK), (1, mv.SCRATCH), (9, mv.CONFUSION),
     (12, mv.HELPING_HAND), (15, mv.CHARM), (18, mv.COVET), (21, mv.PSYBEAM),
     (24, mv.SUCKER_PUNCH), (29, mv.ROLE_PLAY), (34, mv.LIGHT_SCREEN),
     (34, mv.REFLECT), (39, mv.PSYSHOCK), (44, mv.IMPRISON),
     (49, mv.QUICK_GUARD), (54, mv.PSYCHIC), (59, mv.MISTY_TERRAIN)),
    None, 0, False, "")

ESPURR = Pokemon(
    677, "Espurr", 6, False,
    "", ("Psychic",),
    62, 55, 57, 68,
    ((1, mv.LEER), (1, mv.SCRATCH), (3, mv.FAKE_OUT), (6, mv.DISARMING_VOICE),
     (9, mv.CONFUSION), (18, mv.COVET), (21, mv.PSYBEAM),
     (30, mv.LIGHT_SCREEN), (30, mv.REFLECT), (33, mv.PSYSHOCK)),
    MEOWSTIC, 25, True, "")

AEGISLASH = Pokemon(
    681, "Aegislash", 6, False,
    "", ("Steel", "Ghost"),
    60, 50, 140, 60,
    ((1, mv.AERIAL_ACE), (1, mv.AUTOTOMIZE), (1, mv.FURY_CUTTER),
     (1, mv.HEAD_SMASH), (1, mv.IRON_DEFENSE), (1, mv.IRON_HEAD),
     (1, mv.KINGS_SHIELD), (1, mv.METAL_SOUND), (1, mv.NIGHT_SLASH),
     (1, mv.POWER_TRICK), (1, mv.RETALIATE), (1, mv.SACRED_SWORD),
     (1, mv.SHADOW_SNEAK), (1, mv.SLASH), (1, mv.SWORDS_DANCE),
     (1, mv.TACKLE)),
    None, 0, False, "")

DOUBLADE = Pokemon(
    680, "Doublade", 6, False,
    "", ("Steel", "Ghost"),
    59, 77, 99, 35,
    ((1, mv.AUTOTOMIZE), (1, mv.FURY_CUTTER), (1, mv.SHADOW_SNEAK),
     (1, mv.TACKLE), (12, mv.AERIAL_ACE), (16, mv.METAL_SOUND), (20, mv.SLASH),
     (24, mv.NIGHT_SLASH), (28, mv.RETALIATE), (32, mv.IRON_DEFENSE),
     (38, mv.IRON_HEAD), (44, mv.POWER_TRICK), (50, mv.SWORDS_DANCE),
     (56, mv.SACRED_SWORD)),
    AEGISLASH, 0, True, "item:dusk-stone")

HONEDGE = Pokemon(
    679, "Honedge", 6, False,
    "", ("Steel", "Ghost"),
    45, 57, 68, 28,
    ((1, mv.FURY_CUTTER), (1, mv.TACKLE), (4, mv.SHADOW_SNEAK),
     (8, mv.AUTOTOMIZE), (12, mv.AERIAL_ACE), (16, mv.METAL_SOUND),
     (20, mv.SLASH), (24, mv.NIGHT_SLASH), (28, mv.RETALIATE),
     (32, mv.IRON_DEFENSE), (36, mv.IRON_HEAD), (40, mv.POWER_TRICK),
     (44, mv.SWORDS_DANCE), (48, mv.SACRED_SWORD)),
    DOUBLADE, 35, True, "")

AROMATISSE = Pokemon(
    683, "Aromatisse", 6, False,
    "", ("Fairy",),
    101, 85, 80, 29,
    ((1, mv.AROMATIC_MIST), (1, mv.ECHOED_VOICE), (1, mv.FAIRY_WIND),
     (1, mv.HEAL_PULSE), (1, mv.SWEET_KISS), (1, mv.SWEET_SCENT),
     (9, mv.DISARMING_VOICE), (12, mv.AROMATHERAPY), (15, mv.DRAINING_KISS),
     (18, mv.ATTRACT), (21, mv.FLAIL), (24, mv.MISTY_TERRAIN),
     (27, mv.PSYCHIC), (30, mv.CHARM), (33, mv.CALM_MIND), (36, mv.MOONBLAST),
     (39, mv.SKILL_SWAP), (42, mv.PSYCH_UP)),
    None, 0, False, "")

SPRITZEE = Pokemon(
    682, "Spritzee", 6, False,
    "", ("Fairy",),
    78, 57, 62, 23,
    ((1, mv.FAIRY_WIND), (1, mv.SWEET_SCENT), (3, mv.SWEET_KISS),
     (6, mv.ECHOED_VOICE), (9, mv.DRAINING_KISS), (12, mv.AROMATHERAPY),
     (18, mv.ATTRACT), (21, mv.FLAIL), (24, mv.MISTY_TERRAIN),
     (27, mv.PSYCHIC), (30, mv.CHARM), (33, mv.CALM_MIND), (36, mv.MOONBLAST),
     (39, mv.SKILL_SWAP)),
    AROMATISSE, 0, True, "trade")

SLURPUFF = Pokemon(
    685, "Slurpuff", 6, False,
    "", ("Fairy",),
    82, 82, 80, 72,
    ((1, mv.FAIRY_WIND), (1, mv.PLAY_NICE), (1, mv.SWEET_SCENT),
     (1, mv.TACKLE), (9, mv.AROMATHERAPY), (12, mv.DRAINING_KISS),
     (15, mv.FAKE_TEARS), (18, mv.ROUND), (21, mv.STRING_SHOT),
     (24, mv.COTTON_SPORE), (27, mv.ENERGY_BALL), (30, mv.WISH),
     (33, mv.PLAY_ROUGH), (36, mv.COTTON_GUARD), (39, mv.ENDEAVOR),
     (42, mv.STICKY_WEB)),
    None, 0, False, "")

SWIRLIX = Pokemon(
    684, "Swirlix", 6, False,
    "", ("Fairy",),
    62, 53, 61, 49,
    ((1, mv.SWEET_SCENT), (1, mv.TACKLE), (3, mv.PLAY_NICE),
     (6, mv.FAIRY_WIND), (9, mv.AROMATHERAPY), (12, mv.DRAINING_KISS),
     (15, mv.FAKE_TEARS), (18, mv.ROUND), (21, mv.STRING_SHOT),
     (24, mv.COTTON_SPORE), (27, mv.ENERGY_BALL), (30, mv.WISH),
     (33, mv.PLAY_ROUGH), (36, mv.COTTON_GUARD), (39, mv.ENDEAVOR)),
    SLURPUFF, 0, True, "trade")

MALAMAR = Pokemon(
    687, "Malamar", 6, False,
    "", ("Dark", "Psychic"),
    86, 80, 81, 73,
    ((1, mv.HYPNOSIS), (1, mv.PECK), (1, mv.REVERSAL), (1, mv.TACKLE),
     (1, mv.WRAP), (9, mv.PAYBACK), (12, mv.PLUCK), (15, mv.PSYBEAM),
     (18, mv.SWAGGER), (21, mv.SLASH), (24, mv.NIGHT_SLASH),
     (27, mv.PSYCHO_CUT), (33, mv.SWITCHEROO), (37, mv.FOUL_PLAY),
     (42, mv.TOPSY_TURVY), (47, mv.SUPERPOWER)),
    None, 0, False, "")

INKAY = Pokemon(
    686, "Inkay", 6, False,
    "", ("Dark", "Psychic"),
    53, 45, 49, 45,
    ((1, mv.PECK), (1, mv.TACKLE), (3, mv.HYPNOSIS), (6, mv.WRAP),
     (9, mv.PAYBACK), (12, mv.PLUCK), (15, mv.PSYBEAM), (18, mv.SWAGGER),
     (21, mv.SLASH), (24, mv.NIGHT_SLASH), (27, mv.PSYCHO_CUT),
     (31, mv.SWITCHEROO), (33, mv.FOUL_PLAY), (36, mv.TOPSY_TURVY),
     (39, mv.SUPERPOWER)),
    MALAMAR, 0, True,
    "Level 30 while holding Nintendo Switch upside-down (Handheld mode only)")

BARBARACLE = Pokemon(
    689, "Barbaracle", 6, False,
    "", ("Rock", "Water"),
    72, 79, 100, 68,
    ((1, mv.MUD_SLAP), (1, mv.SCRATCH), (1, mv.SKULL_BASH), (1, mv.WATER_GUN),
     (1, mv.WITHDRAW), (12, mv.FURY_CUTTER), (16, mv.FURY_SWIPES),
     (20, mv.ANCIENT_POWER), (24, mv.ROCK_POLISH), (28, mv.SLASH),
     (32, mv.HONE_CLAWS), (36, mv.RAZOR_SHELL), (42, mv.SHELL_SMASH),
     (48, mv.CROSS_CHOP), (54, mv.STONE_EDGE)),
    None, 0, False, "")

BINACLE = Pokemon(
    688, "Binacle", 6, False,
    "", ("Rock", "Water"),
    42, 45, 61, 50,
    ((1, mv.MUD_SLAP), (1, mv.SCRATCH), (4, mv.WITHDRAW), (8, mv.WATER_GUN),
     (12, mv.FURY_CUTTER), (16, mv.FURY_SWIPES), (20, mv.ANCIENT_POWER),
     (24, mv.ROCK_POLISH), (28, mv.SLASH), (32, mv.HONE_CLAWS),
     (36, mv.RAZOR_SHELL), (40, mv.SHELL_SMASH), (44, mv.CROSS_CHOP)),
    BARBARACLE, 39, True, "")

DRAGALGE = Pokemon(
    691, "Dragalge", 6, False,
    "", ("Poison", "Dragon"),
    65, 86, 106, 44,
    ((1, mv.ACID), (1, mv.SMOKESCREEN), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (15, mv.TAIL_WHIP), (20, mv.DOUBLE_TEAM), (25, mv.POISON_TAIL),
     (30, mv.WATER_PULSE), (35, mv.TOXIC), (40, mv.DRAGON_PULSE),
     (45, mv.AQUA_TAIL), (52, mv.SLUDGE_BOMB), (59, mv.HYDRO_PUMP),
     (66, mv.OUTRAGE)),
    None, 0, False, "")

SKRELP = Pokemon(
    690, "Skrelp", 6, False,
    "", ("Poison", "Water"),
    50, 60, 60, 30,
    ((1, mv.SMOKESCREEN), (1, mv.TACKLE), (5, mv.ACID), (10, mv.WATER_GUN),
     (15, mv.TAIL_WHIP), (20, mv.DOUBLE_TEAM), (25, mv.POISON_TAIL),
     (30, mv.WATER_PULSE), (35, mv.TOXIC), (40, mv.DRAGON_PULSE),
     (45, mv.AQUA_TAIL), (50, mv.SLUDGE_BOMB), (55, mv.HYDRO_PUMP)),
    DRAGALGE, 48, True, "")

CLAWITZER = Pokemon(
    693, "Clawitzer", 6, False,
    "", ("Water",),
    71, 96, 88, 59,
    ((1, mv.DARK_PULSE), (1, mv.DRAGON_PULSE), (1, mv.FLAIL),
     (1, mv.HEAL_PULSE), (1, mv.SPLASH), (1, mv.WATER_GUN), (15, mv.AQUA_JET),
     (20, mv.SMACK_DOWN), (25, mv.HONE_CLAWS), (30, mv.WATER_PULSE),
     (35, mv.SWORDS_DANCE), (42, mv.AURA_SPHERE), (49, mv.BOUNCE),
     (56, mv.MUDDY_WATER), (63, mv.CRABHAMMER)),
    None, 0, False, "")

CLAUNCHER = Pokemon(
    692, "Clauncher", 6, False,
    "", ("Water",),
    50, 55, 62, 44,
    ((1, mv.SPLASH), (1, mv.WATER_GUN), (10, mv.FLAIL), (15, mv.AQUA_JET),
     (20, mv.SMACK_DOWN), (25, mv.HONE_CLAWS), (30, mv.WATER_PULSE),
     (35, mv.SWORDS_DANCE), (40, mv.AURA_SPHERE), (45, mv.BOUNCE),
     (50, mv.MUDDY_WATER), (55, mv.CRABHAMMER)),
    CLAWITZER, 37, True, "")

HELIOLISK = Pokemon(
    695, "Heliolisk", 6, False,
    "", ("Electric", "Normal"),
    62, 82, 73, 109,
    ((1, mv.BULLDOZE), (1, mv.CHARGE), (1, mv.DISCHARGE),
     (1, mv.EERIE_IMPULSE), (1, mv.ELECTRIFY), (1, mv.MUD_SLAP),
     (1, mv.PARABOLIC_CHARGE), (1, mv.POUND), (1, mv.QUICK_ATTACK),
     (1, mv.TAIL_WHIP), (1, mv.THUNDER), (1, mv.THUNDERBOLT),
     (1, mv.THUNDER_SHOCK), (1, mv.THUNDER_WAVE), (1, mv.VOLT_SWITCH)),
    None, 0, False, "")

HELIOPTILE = Pokemon(
    694, "Helioptile", 6, False,
    "", ("Electric", "Normal"),
    44, 49, 38, 70,
    ((1, mv.MUD_SLAP), (1, mv.TAIL_WHIP), (4, mv.POUND), (8, mv.THUNDER_SHOCK),
     (12, mv.QUICK_ATTACK), (16, mv.CHARGE), (20, mv.BULLDOZE),
     (24, mv.VOLT_SWITCH), (28, mv.PARABOLIC_CHARGE), (32, mv.THUNDER_WAVE),
     (36, mv.THUNDERBOLT), (40, mv.ELECTRIFY), (44, mv.THUNDER)),
    HELIOLISK, 0, True, "item:sun-stone")

TYRANTRUM = Pokemon(
    697, "Tyrantrum", 6, False,
    "", ("Rock", "Dragon"),
    82, 95, 89, 71,
    ((1, mv.ANCIENT_POWER), (1, mv.ROAR), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (12, mv.CHARM), (16, mv.BITE), (20, mv.DRAGON_TAIL), (24, mv.STOMP),
     (28, mv.ROCK_SLIDE), (32, mv.CRUNCH), (36, mv.DRAGON_CLAW),
     (42, mv.THRASH), (48, mv.EARTHQUAKE), (54, mv.HORN_DRILL),
     (60, mv.GIGA_IMPACT), (66, mv.HEAD_SMASH)),
    None, 0, False, "")

TYRUNT = Pokemon(
    696, "Tyrunt", 6, False,
    "", ("Rock", "Dragon"),
    58, 67, 61, 48,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (4, mv.ROAR), (8, mv.ANCIENT_POWER),
     (12, mv.CHARM), (16, mv.BITE), (20, mv.DRAGON_TAIL), (24, mv.STOMP),
     (28, mv.ROCK_SLIDE), (32, mv.CRUNCH), (36, mv.DRAGON_CLAW),
     (40, mv.THRASH), (44, mv.EARTHQUAKE), (48, mv.HORN_DRILL)),
    TYRANTRUM, 39, True, "")

AURORUS = Pokemon(
    699, "Aurorus", 6, False,
    "", ("Rock", "Ice"),
    123, 88, 82, 58,
    ((1, mv.ANCIENT_POWER), (1, mv.ENCORE), (1, mv.GROWL), (1, mv.POWDER_SNOW),
     (12, mv.ICY_WIND), (16, mv.ROUND), (20, mv.MIST), (24, mv.AURORA_BEAM),
     (28, mv.THUNDER_WAVE), (32, mv.NATURE_POWER), (36, mv.FREEZE_DRY),
     (42, mv.ICE_BEAM), (48, mv.LIGHT_SCREEN), (54, mv.HAIL),
     (60, mv.BLIZZARD), (66, mv.HYPER_BEAM)),
    None, 0, False, "")

AMAURA = Pokemon(
    698, "Amaura", 6, False,
    "", ("Rock", "Ice"),
    77, 63, 56, 46,
    ((1, mv.GROWL), (1, mv.POWDER_SNOW), (4, mv.ENCORE), (8, mv.ANCIENT_POWER),
     (12, mv.ICY_WIND), (16, mv.ROUND), (20, mv.MIST), (24, mv.AURORA_BEAM),
     (28, mv.THUNDER_WAVE), (32, mv.NATURE_POWER), (36, mv.FREEZE_DRY),
     (40, mv.ICE_BEAM), (44, mv.LIGHT_SCREEN), (48, mv.HAIL),
     (52, mv.BLIZZARD), (56, mv.HYPER_BEAM)),
    AURORUS, 39, True, "")

SYLVEON = Pokemon(
    700, "Sylveon", 6, False,
    "", ("Fairy",),
    95, 87, 97, 60,
    ((0, mv.DISARMING_VOICE), (1, mv.BATON_PASS), (1, mv.BITE), (1, mv.CHARM),
     (1, mv.COPYCAT), (1, mv.COVET), (1, mv.DOUBLE_EDGE), (1, mv.GROWL),
     (1, mv.HELPING_HAND), (1, mv.TACKLE), (1, mv.TAIL_WHIP),
     (1, mv.TAKE_DOWN), (5, mv.SAND_ATTACK), (10, mv.QUICK_ATTACK),
     (15, mv.BABY_DOLL_EYES), (20, mv.SWIFT), (25, mv.LIGHT_SCREEN),
     (30, mv.DRAINING_KISS), (35, mv.MISTY_TERRAIN), (40, mv.SKILL_SWAP),
     (45, mv.PSYCH_UP), (50, mv.MOONBLAST), (55, mv.LAST_RESORT)),
    None, 0, False, "")

HAWLUCHA = Pokemon(
    701, "Hawlucha", 6, False,
    "", ("Fighting", "Flying"),
    78, 83, 69, 118,
    ((1, mv.HONE_CLAWS), (1, mv.TACKLE), (4, mv.WING_ATTACK), (8, mv.DETECT),
     (12, mv.AERIAL_ACE), (16, mv.ENCORE), (20, mv.FEATHER_DANCE),
     (24, mv.BRICK_BREAK), (28, mv.BOUNCE), (32, mv.TAUNT), (36, mv.ROOST),
     (40, mv.SWORDS_DANCE), (44, mv.FLYING_PRESS), (48, mv.HIGH_JUMP_KICK),
     (52, mv.ENDEAVOR), (56, mv.SKY_ATTACK)),
    None, 0, False, "")

DEDENNE = Pokemon(
    702, "Dedenne", 6, False,
    "", ("Electric", "Fairy"),
    67, 69, 62, 101,
    ((1, mv.NUZZLE), (1, mv.TAIL_WHIP), (5, mv.TACKLE), (10, mv.CHARGE),
     (15, mv.THUNDER_SHOCK), (20, mv.CHARM), (25, mv.PARABOLIC_CHARGE),
     (30, mv.VOLT_SWITCH), (35, mv.REST), (35, mv.SNORE), (40, mv.DISCHARGE),
     (45, mv.PLAY_ROUGH), (50, mv.SUPER_FANG), (55, mv.ENTRAINMENT),
     (60, mv.THUNDER)),
    None, 0, False, "")

CARBINK = Pokemon(
    703, "Carbink", 6, False,
    "", ("Rock", "Fairy"),
    50, 50, 150, 50,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.GUARD_SPLIT), (10, mv.SMACK_DOWN),
     (15, mv.FLAIL), (20, mv.ANCIENT_POWER), (25, mv.ROCK_POLISH),
     (30, mv.LIGHT_SCREEN), (35, mv.ROCK_SLIDE), (40, mv.SKILL_SWAP),
     (45, mv.POWER_GEM), (50, mv.STEALTH_ROCK), (55, mv.MOONBLAST),
     (60, mv.STONE_EDGE)),
    None, 0, False, "")

GOODRA = Pokemon(
    706, "Goodra", 6, False,
    "", ("Dragon",),
    90, 105, 110, 80,
    ((0, mv.AQUA_TAIL), (1, mv.ABSORB), (1, mv.ACID_SPRAY),
     (1, mv.DRAGON_BREATH), (1, mv.FEINT), (1, mv.POISON_TAIL), (1, mv.TACKLE),
     (1, mv.TEARFUL_LOOK), (1, mv.WATER_GUN), (15, mv.PROTECT), (20, mv.FLAIL),
     (25, mv.WATER_PULSE), (30, mv.RAIN_DANCE), (43, mv.CURSE),
     (49, mv.BODY_SLAM), (58, mv.MUDDY_WATER), (67, mv.POWER_WHIP)),
    None, 0, False, "")

SLIGGOO = Pokemon(
    705, "Sliggoo", 6, False,
    "", ("Dragon",),
    68, 79, 83, 60,
    ((0, mv.ACID_SPRAY), (1, mv.ABSORB), (1, mv.ACID_ARMOR),
     (1, mv.DRAGON_BREATH), (1, mv.TACKLE), (1, mv.WATER_GUN),
     (15, mv.PROTECT), (20, mv.FLAIL), (25, mv.WATER_PULSE),
     (30, mv.RAIN_DANCE), (35, mv.DRAGON_PULSE), (43, mv.CURSE),
     (49, mv.BODY_SLAM), (56, mv.MUDDY_WATER)),
    GOODRA, 50, True, "")

GOOMY = Pokemon(
    704, "Goomy", 6, False,
    "", ("Dragon",),
    45, 52, 55, 40,
    ((1, mv.ABSORB), (1, mv.TACKLE), (5, mv.WATER_GUN), (10, mv.DRAGON_BREATH),
     (15, mv.PROTECT), (20, mv.FLAIL), (25, mv.WATER_PULSE),
     (30, mv.RAIN_DANCE), (35, mv.DRAGON_PULSE), (41, mv.CURSE),
     (45, mv.BODY_SLAM), (50, mv.MUDDY_WATER)),
    SLIGGOO, 40, True, "")

KLEFKI = Pokemon(
    707, "Klefki", 6, False,
    "", ("Steel", "Fairy"),
    57, 80, 89, 75,
    ((1, mv.ASTONISH), (4, mv.TACKLE), (8, mv.FAIRY_WIND), (12, mv.TORMENT),
     (16, mv.FAIRY_LOCK), (20, mv.METAL_SOUND), (24, mv.DRAINING_KISS),
     (28, mv.RECYCLE), (32, mv.IMPRISON), (36, mv.FLASH_CANNON),
     (40, mv.PLAY_ROUGH), (44, mv.MAGIC_ROOM), (48, mv.FOUL_PLAY),
     (52, mv.LAST_RESORT)),
    None, 0, False, "")

TREVENANT = Pokemon(
    709, "Trevenant", 6, False,
    "", ("Ghost", "Grass"),
    85, 87, 79, 56,
    ((0, mv.SHADOW_CLAW), (1, mv.ASTONISH), (1, mv.BRANCH_POKE),
     (1, mv.LEECH_SEED), (1, mv.TACKLE), (12, mv.CONFUSE_RAY),
     (16, mv.WILL_O_WISP), (20, mv.HEX), (24, mv.GROWTH), (28, mv.HORN_LEECH),
     (32, mv.CURSE), (36, mv.PHANTOM_FORCE), (40, mv.INGRAIN),
     (44, mv.WOOD_HAMMER), (48, mv.DESTINY_BOND), (52, mv.FORESTS_CURSE)),
    None, 0, False, "")

PHANTUMP = Pokemon(
    708, "Phantump", 6, False,
    "", ("Ghost", "Grass"),
    43, 60, 54, 38,
    ((1, mv.ASTONISH), (1, mv.TACKLE), (4, mv.BRANCH_POKE), (8, mv.LEECH_SEED),
     (12, mv.CONFUSE_RAY), (16, mv.WILL_O_WISP), (20, mv.HEX), (24, mv.GROWTH),
     (28, mv.HORN_LEECH), (32, mv.CURSE), (36, mv.PHANTOM_FORCE),
     (40, mv.INGRAIN), (44, mv.WOOD_HAMMER), (48, mv.DESTINY_BOND),
     (52, mv.FORESTS_CURSE)),
    TREVENANT, 0, True, "trade")

GOURGEIST = Pokemon(
    711, "Gourgeist", 6, False,
    "", ("Ghost", "Grass"),
    65, 74, 98, 84,
    ((1, mv.ASTONISH), (1, mv.CONFUSE_RAY), (1, mv.EXPLOSION),
     (1, mv.MOONBLAST), (1, mv.SHADOW_SNEAK), (12, mv.RAZOR_LEAF),
     (12, mv.TRICK_OR_TREAT), (16, mv.LEECH_SEED), (20, mv.BULLET_SEED),
     (24, mv.SCARY_FACE), (28, mv.WORRY_SEED), (32, mv.SEED_BOMB),
     (36, mv.SHADOW_BALL), (40, mv.TRICK), (44, mv.PAIN_SPLIT),
     (48, mv.PHANTOM_FORCE)),
    None, 0, False, "")

PUMPKABOO = Pokemon(
    710, "Pumpkaboo", 6, False,
    "", ("Ghost", "Grass"),
    49, 55, 62, 51,
    ((1, mv.ASTONISH), (4, mv.SHADOW_SNEAK), (8, mv.CONFUSE_RAY),
     (12, mv.RAZOR_LEAF), (16, mv.LEECH_SEED), (20, mv.BULLET_SEED),
     (24, mv.SCARY_FACE), (24, mv.TRICK_OR_TREAT), (28, mv.WORRY_SEED),
     (32, mv.SEED_BOMB), (36, mv.SHADOW_BALL), (40, mv.TRICK),
     (44, mv.PAIN_SPLIT)),
    GOURGEIST, 0, True, "trade")

AVALUGG = Pokemon(
    713, "Avalugg", 6, False,
    "", ("Ice",),
    95, 80, 115, 28,
    ((0, mv.BODY_SLAM), (1, mv.HARDEN), (1, mv.POWDER_SNOW),
     (1, mv.RAPID_SPIN), (1, mv.TACKLE), (1, mv.WIDE_GUARD), (9, mv.CURSE),
     (12, mv.ICY_WIND), (15, mv.PROTECT), (18, mv.AVALANCHE), (21, mv.BITE),
     (24, mv.ICE_FANG), (27, mv.IRON_DEFENSE), (30, mv.RECOVER),
     (33, mv.CRUNCH), (36, mv.TAKE_DOWN), (41, mv.BLIZZARD),
     (46, mv.DOUBLE_EDGE), (51, mv.ICICLE_CRASH)),
    None, 0, False, "")

BERGMITE = Pokemon(
    712, "Bergmite", 6, False,
    "", ("Ice",),
    55, 50, 60, 28,
    ((1, mv.HARDEN), (1, mv.RAPID_SPIN), (3, mv.TACKLE), (6, mv.POWDER_SNOW),
     (9, mv.CURSE), (12, mv.ICY_WIND), (15, mv.PROTECT), (18, mv.AVALANCHE),
     (21, mv.BITE), (24, mv.ICE_FANG), (27, mv.IRON_DEFENSE), (30, mv.RECOVER),
     (33, mv.CRUNCH), (36, mv.TAKE_DOWN), (39, mv.BLIZZARD),
     (42, mv.DOUBLE_EDGE)),
    AVALUGG, 37, True, "")

NOIVERN = Pokemon(
    715, "Noivern", 6, False,
    "", ("Flying", "Dragon"),
    85, 83, 80, 123,
    ((0, mv.DRAGON_PULSE), (1, mv.ABSORB), (1, mv.GUST), (1, mv.MOONLIGHT),
     (1, mv.SUPERSONIC), (1, mv.TACKLE), (12, mv.DOUBLE_TEAM),
     (16, mv.WING_ATTACK), (20, mv.BITE), (24, mv.AIR_CUTTER),
     (28, mv.WHIRLWIND), (32, mv.SUPER_FANG), (36, mv.AIR_SLASH),
     (40, mv.SCREECH), (44, mv.ROOST), (51, mv.TAILWIND), (56, mv.HURRICANE),
     (62, mv.BOOMBURST)),
    None, 0, False, "")

NOIBAT = Pokemon(
    714, "Noibat", 6, False,
    "", ("Flying", "Dragon"),
    40, 37, 37, 55,
    ((1, mv.ABSORB), (1, mv.TACKLE), (4, mv.GUST), (8, mv.SUPERSONIC),
     (12, mv.DOUBLE_TEAM), (16, mv.WING_ATTACK), (20, mv.BITE),
     (24, mv.AIR_CUTTER), (28, mv.WHIRLWIND), (32, mv.SUPER_FANG),
     (36, mv.AIR_SLASH), (40, mv.SCREECH), (44, mv.ROOST), (49, mv.TAILWIND),
     (52, mv.HURRICANE)),
    NOIVERN, 48, True, "")

XERNEAS = Pokemon(
    716, "Xerneas", 6, False,
    "", ("Fairy",),
    126, 131, 96, 99,
    ((1, mv.GRAVITY), (1, mv.TACKLE), (5, mv.LIGHT_SCREEN),
     (10, mv.AURORA_BEAM), (15, mv.NATURE_POWER), (20, mv.NIGHT_SLASH),
     (25, mv.AROMATHERAPY), (30, mv.PSYCH_UP), (35, mv.HORN_LEECH),
     (40, mv.MISTY_TERRAIN), (45, mv.INGRAIN), (50, mv.TAKE_DOWN),
     (55, mv.GEOMANCY), (60, mv.MOONBLAST), (65, mv.HEAL_PULSE),
     (70, mv.MEGAHORN), (75, mv.CLOSE_COMBAT), (80, mv.OUTRAGE),
     (85, mv.GIGA_IMPACT)),
    None, 0, False, "")

YVELTAL = Pokemon(
    717, "Yveltal", 6, False,
    "", ("Dark", "Flying"),
    126, 131, 96, 99,
    ((1, mv.DOUBLE_TEAM), (1, mv.GUST), (5, mv.TAUNT), (10, mv.SNARL),
     (15, mv.DISABLE), (20, mv.SUCKER_PUNCH), (25, mv.TAILWIND),
     (30, mv.ROOST), (35, mv.AIR_SLASH), (40, mv.DARK_PULSE), (45, mv.PSYCHIC),
     (50, mv.OBLIVION_WING), (55, mv.PHANTOM_FORCE), (60, mv.FOUL_PLAY),
     (65, mv.DRAGON_RUSH), (70, mv.HURRICANE), (75, mv.FOCUS_BLAST),
     (80, mv.SKY_ATTACK), (85, mv.HYPER_BEAM)),
    None, 0, False, "")

ZYGARDE = Pokemon(
    718, "Zygarde", 6, False,
    "", ("Dragon", "Ground"),
    108, 90, 108, 95,
    ((1, mv.BIND), (1, mv.BITE), (1, mv.BULLDOZE), (1, mv.CORE_ENFORCER),
     (1, mv.DRAGON_BREATH), (1, mv.THOUSAND_ARROWS), (1, mv.THOUSAND_WAVES),
     (8, mv.HAZE), (16, mv.DIG), (24, mv.SAFEGUARD), (32, mv.CRUNCH),
     (40, mv.DRAGON_PULSE), (48, mv.LANDS_WRATH), (56, mv.GLARE),
     (64, mv.SANDSTORM), (72, mv.COIL), (80, mv.EARTHQUAKE), (88, mv.OUTRAGE)),
    None, 0, False, "")

DIANCIE = Pokemon(
    719, "Diancie", 6, False,
    "", ("Rock", "Fairy"),
    50, 100, 150, 50,
    ((1, mv.DIAMOND_STORM), (1, mv.HARDEN), (1, mv.TACKLE),
     (7, mv.GUARD_SPLIT), (14, mv.SMACK_DOWN), (21, mv.FLAIL),
     (28, mv.ANCIENT_POWER), (35, mv.ROCK_POLISH), (42, mv.LIGHT_SCREEN),
     (49, mv.ROCK_SLIDE), (56, mv.SKILL_SWAP), (63, mv.POWER_GEM),
     (70, mv.STEALTH_ROCK), (77, mv.MOONBLAST), (84, mv.STONE_EDGE)),
    None, 0, False, "")

HOOPA = Pokemon(
    720, "Hoopa", 6, False,
    "", ("Psychic", "Ghost"),
    80, 130, 95, 70,
    ((1, mv.ALLY_SWITCH), (1, mv.CONFUSION), (1, mv.DESTINY_BOND),
     (6, mv.ASTONISH), (10, mv.TRICK), (15, mv.LIGHT_SCREEN), (19, mv.PSYBEAM),
     (25, mv.SKILL_SWAP), (29, mv.GUARD_SPLIT), (29, mv.POWER_SPLIT),
     (35, mv.PHANTOM_FORCE), (46, mv.ZEN_HEADBUTT), (50, mv.TRICK_ROOM),
     (50, mv.WONDER_ROOM), (55, mv.SHADOW_BALL), (68, mv.NASTY_PLOT),
     (75, mv.PSYCHIC), (85, mv.HYPERSPACE_HOLE)),
    None, 0, False, "")

VOLCANION = Pokemon(
    721, "Volcanion", 6, False,
    "", ("Fire", "Water"),
    80, 120, 105, 70,
    ((1, mv.FIRE_SPIN), (1, mv.STEAM_ERUPTION), (1, mv.WATER_GUN),
     (6, mv.LEER), (12, mv.WEATHER_BALL), (18, mv.FLAME_CHARGE),
     (24, mv.WATER_PULSE), (30, mv.SCARY_FACE), (36, mv.INCINERATE),
     (42, mv.STOMP), (48, mv.SCALD), (54, mv.TAKE_DOWN), (60, mv.HAZE),
     (60, mv.MIST), (66, mv.HYDRO_PUMP), (78, mv.FLARE_BLITZ),
     (84, mv.OVERHEAT), (90, mv.EXPLOSION)),
    None, 0, False, "")


# --- generation 7 ---

DECIDUEYE = Pokemon(
    724, "Decidueye", 7, True,
    "Flora", ("Grass", "Ghost"),
    78, 103, 87, 70,
    ((0, mv.SPIRIT_SHACKLE), (1, mv.ASTONISH), (1, mv.GROWL), (1, mv.LEAFAGE),
     (1, mv.LEAF_STORM), (1, mv.PHANTOM_FORCE), (1, mv.SPITE), (1, mv.TACKLE),
     (1, mv.U_TURN), (9, mv.PECK), (12, mv.SHADOW_SNEAK), (15, mv.RAZOR_LEAF),
     (20, mv.SYNTHESIS), (25, mv.PLUCK), (30, mv.NASTY_PLOT),
     (37, mv.SUCKER_PUNCH), (44, mv.LEAF_BLADE), (51, mv.FEATHER_DANCE),
     (58, mv.BRAVE_BIRD)),
    None, 0, False, "")

DARTRIX = Pokemon(
    723, "Dartrix", 7, True,
    "Flora", ("Grass", "Flying"),
    78, 72, 72, 52,
    ((1, mv.ASTONISH), (1, mv.GROWL), (1, mv.LEAFAGE), (1, mv.TACKLE),
     (9, mv.PECK), (12, mv.SHADOW_SNEAK), (15, mv.RAZOR_LEAF),
     (20, mv.SYNTHESIS), (25, mv.PLUCK), (30, mv.NASTY_PLOT),
     (35, mv.SUCKER_PUNCH), (40, mv.LEAF_BLADE), (45, mv.FEATHER_DANCE),
     (50, mv.BRAVE_BIRD)),
    DECIDUEYE, 36, True, "")

ROWLET = Pokemon(
    722, "Rowlet", 7, True,
    "Flora", ("Grass", "Flying"),
    68, 52, 52, 42,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.LEAFAGE), (6, mv.ASTONISH),
     (9, mv.PECK), (12, mv.SHADOW_SNEAK), (15, mv.RAZOR_LEAF),
     (18, mv.SYNTHESIS), (21, mv.PLUCK), (24, mv.NASTY_PLOT),
     (27, mv.SUCKER_PUNCH), (30, mv.LEAF_BLADE), (33, mv.FEATHER_DANCE),
     (36, mv.BRAVE_BIRD)),
    DARTRIX, 17, True, "")

INCINEROAR = Pokemon(
    727, "Incineroar", 7, True,
    "Flame", ("Fire", "Dark"),
    95, 97, 90, 60,
    ((0, mv.DARKEST_LARIAT), (1, mv.BULK_UP), (1, mv.CROSS_CHOP),
     (1, mv.EMBER), (1, mv.LICK), (9, mv.ROAR), (12, mv.FURY_SWIPES),
     (15, mv.BITE), (20, mv.DOUBLE_KICK), (25, mv.FIRE_FANG),
     (30, mv.SCARY_FACE), (32, mv.SWAGGER), (44, mv.FLAMETHROWER),
     (51, mv.THRASH), (58, mv.FLARE_BLITZ)),
    None, 0, False, "")

TORRACAT = Pokemon(
    726, "Torracat", 7, True,
    "Flame", ("Fire",),
    65, 82, 50, 90,
    ((1, mv.EMBER), (1, mv.GROWL), (1, mv.LICK), (1, mv.SCRATCH), (9, mv.ROAR),
     (12, mv.FURY_SWIPES), (15, mv.BITE), (20, mv.DOUBLE_KICK),
     (25, mv.FIRE_FANG), (30, mv.SCARY_FACE), (35, mv.SWAGGER),
     (40, mv.FLAMETHROWER), (45, mv.THRASH), (50, mv.FLARE_BLITZ)),
    INCINEROAR, 34, True, "")

LITTEN = Pokemon(
    725, "Litten", 7, True,
    "Flame", ("Fire",),
    45, 62, 40, 70,
    ((1, mv.GROWL), (1, mv.SCRATCH), (3, mv.EMBER), (6, mv.LICK), (9, mv.ROAR),
     (12, mv.FURY_SWIPES), (15, mv.BITE), (18, mv.DOUBLE_KICK),
     (21, mv.FIRE_FANG), (24, mv.SCARY_FACE), (27, mv.SWAGGER),
     (30, mv.FLAMETHROWER), (33, mv.THRASH), (36, mv.FLARE_BLITZ)),
    TORRACAT, 17, True, "")

PRIMARINA = Pokemon(
    730, "Primarina", 7, True,
    "Aqua", ("Water", "Fairy"),
    80, 100, 95, 60,
    ((0, mv.SPARKLING_ARIA), (1, mv.DISARMING_VOICE), (1, mv.GROWL),
     (1, mv.POUND), (1, mv.WATER_GUN), (9, mv.AQUA_JET),
     (12, mv.BABY_DOLL_EYES), (15, mv.ICY_WIND), (20, mv.SING),
     (25, mv.BUBBLE_BEAM), (30, mv.ENCORE), (37, mv.MISTY_TERRAIN),
     (44, mv.HYPER_VOICE), (51, mv.MOONBLAST), (58, mv.HYDRO_PUMP)),
    None, 0, False, "")

BRIONNE = Pokemon(
    729, "Brionne", 7, True,
    "Aqua", ("Water",),
    60, 80, 75, 50,
    ((1, mv.DISARMING_VOICE), (1, mv.GROWL), (1, mv.POUND), (1, mv.WATER_GUN),
     (9, mv.AQUA_JET), (12, mv.BABY_DOLL_EYES), (15, mv.ICY_WIND),
     (20, mv.SING), (25, mv.BUBBLE_BEAM), (30, mv.ENCORE),
     (35, mv.MISTY_TERRAIN), (40, mv.HYPER_VOICE), (45, mv.MOONBLAST),
     (50, mv.HYDRO_PUMP)),
    PRIMARINA, 34, True, "")

POPPLIO = Pokemon(
    728, "Popplio", 7, True,
    "Aqua", ("Water",),
    50, 60, 55, 40,
    ((1, mv.GROWL), (1, mv.POUND), (3, mv.WATER_GUN), (6, mv.DISARMING_VOICE),
     (9, mv.AQUA_JET), (12, mv.BABY_DOLL_EYES), (15, mv.ICY_WIND),
     (18, mv.SING), (21, mv.BUBBLE_BEAM), (24, mv.ENCORE),
     (27, mv.MISTY_TERRAIN), (30, mv.HYPER_VOICE), (33, mv.MOONBLAST),
     (36, mv.HYDRO_PUMP)),
    BRIONNE, 17, True, "")

TOUCANNON = Pokemon(
    733, "Toucannon", 7, False,
    "", ("Normal", "Flying"),
    80, 97, 75, 60,
    ((0, mv.BEAK_BLAST), (1, mv.ECHOED_VOICE), (1, mv.GROWL), (1, mv.PECK),
     (1, mv.ROCK_BLAST), (1, mv.ROCK_SMASH), (13, mv.SUPERSONIC),
     (16, mv.PLUCK), (21, mv.ROOST), (24, mv.FURY_ATTACK), (30, mv.SCREECH),
     (34, mv.DRILL_PECK), (40, mv.BULLET_SEED), (44, mv.FEATHER_DANCE),
     (50, mv.HYPER_VOICE)),
    None, 0, False, "")

TRUMBEAK = Pokemon(
    732, "Trumbeak", 7, False,
    "", ("Normal", "Flying"),
    55, 62, 50, 75,
    ((1, mv.GROWL), (1, mv.PECK), (1, mv.ROCK_BLAST), (1, mv.ROCK_SMASH),
     (13, mv.SUPERSONIC), (16, mv.PLUCK), (21, mv.ROOST), (24, mv.FURY_ATTACK),
     (29, mv.SCREECH), (32, mv.DRILL_PECK), (37, mv.BULLET_SEED),
     (40, mv.FEATHER_DANCE), (45, mv.HYPER_VOICE)),
    TOUCANNON, 28, True, "")

PIKIPEK = Pokemon(
    731, "Pikipek", 7, False,
    "", ("Normal", "Flying"),
    35, 52, 30, 65,
    ((1, mv.PECK), (3, mv.GROWL), (7, mv.ECHOED_VOICE), (9, mv.ROCK_SMASH),
     (13, mv.SUPERSONIC), (15, mv.PLUCK), (19, mv.ROOST), (21, mv.FURY_ATTACK),
     (25, mv.SCREECH), (27, mv.DRILL_PECK), (31, mv.BULLET_SEED),
     (33, mv.FEATHER_DANCE), (37, mv.HYPER_VOICE)),
    TRUMBEAK, 14, True, "")

GUMSHOOS = Pokemon(
    735, "Gumshoos", 7, False,
    "", ("Normal",),
    88, 82, 60, 45,
    ((1, mv.LEER), (1, mv.PAYBACK), (1, mv.SAND_ATTACK), (1, mv.TACKLE),
     (13, mv.WORK_UP), (19, mv.BITE), (23, mv.MUD_SLAP), (27, mv.SUPER_FANG),
     (31, mv.TAKE_DOWN), (35, mv.SCARY_FACE), (39, mv.CRUNCH), (43, mv.YAWN),
     (47, mv.THRASH), (52, mv.REST)),
    None, 0, False, "")

YUNGOOS = Pokemon(
    734, "Yungoos", 7, False,
    "", ("Normal",),
    48, 50, 30, 45,
    ((1, mv.TACKLE), (3, mv.LEER), (7, mv.PAYBACK), (10, mv.SAND_ATTACK),
     (13, mv.WORK_UP), (19, mv.BITE), (22, mv.MUD_SLAP), (25, mv.SUPER_FANG),
     (28, mv.TAKE_DOWN), (31, mv.SCARY_FACE), (34, mv.CRUNCH), (37, mv.YAWN),
     (40, mv.THRASH), (43, mv.REST)),
    GUMSHOOS, 20, True, "")

VIKAVOLT = Pokemon(
    738, "Vikavolt", 7, False,
    "", ("Bug", "Electric"),
    77, 107, 82, 43,
    ((0, mv.THUNDERBOLT), (1, mv.CHARGE), (1, mv.CRUNCH), (1, mv.DISCHARGE),
     (1, mv.STRING_SHOT), (15, mv.BITE), (23, mv.SPARK), (29, mv.STICKY_WEB),
     (36, mv.BUG_BUZZ), (43, mv.GUILLOTINE), (50, mv.FLY), (57, mv.AGILITY),
     (64, mv.ZAP_CANNON)),
    None, 0, False, "")

CHARJABUG = Pokemon(
    737, "Charjabug", 7, False,
    "", ("Bug", "Electric"),
    57, 68, 85, 36,
    ((0, mv.CHARGE), (1, mv.BUG_BITE), (1, mv.MUD_SLAP), (1, mv.STRING_SHOT),
     (1, mv.VISE_GRIP), (15, mv.BITE), (23, mv.SPARK), (29, mv.STICKY_WEB),
     (36, mv.X_SCISSOR), (43, mv.CRUNCH), (50, mv.DIG), (57, mv.IRON_DEFENSE),
     (64, mv.DISCHARGE)),
    VIKAVOLT, 0, True, "item:thunder-stone")

GRUBBIN = Pokemon(
    736, "Grubbin", 7, False,
    "", ("Bug",),
    47, 58, 45, 46,
    ((1, mv.MUD_SLAP), (1, mv.VISE_GRIP), (5, mv.STRING_SHOT),
     (10, mv.BUG_BITE), (15, mv.BITE), (21, mv.SPARK), (25, mv.STICKY_WEB),
     (30, mv.X_SCISSOR), (35, mv.CRUNCH), (40, mv.DIG)),
    CHARJABUG, 20, True, "")

CRABOMINABLE = Pokemon(
    740, "Crabominable", 7, False,
    "", ("Fighting", "Ice"),
    97, 97, 72, 43,
    ((0, mv.ICE_PUNCH), (1, mv.LEER), (1, mv.PROTECT), (1, mv.ROCK_SMASH),
     (17, mv.BUBBLE_BEAM), (22, mv.BRICK_BREAK), (25, mv.SLAM),
     (29, mv.AVALANCHE), (33, mv.REVERSAL), (37, mv.ICE_HAMMER),
     (42, mv.IRON_DEFENSE), (45, mv.DYNAMIC_PUNCH), (49, mv.CLOSE_COMBAT)),
    None, 0, False, "")

CRABRAWLER = Pokemon(
    739, "Crabrawler", 7, False,
    "", ("Fighting",),
    47, 62, 52, 63,
    ((5, mv.ROCK_SMASH), (9, mv.LEER), (13, mv.BUBBLE_BEAM), (17, mv.PROTECT),
     (22, mv.BRICK_BREAK), (25, mv.SLAM), (29, mv.PAYBACK), (33, mv.REVERSAL),
     (37, mv.CRABHAMMER), (42, mv.IRON_DEFENSE), (45, mv.DYNAMIC_PUNCH),
     (49, mv.CLOSE_COMBAT)),
    CRABOMINABLE, 0, True, "item:ice-stone")

ORICORIO = Pokemon(
    741, "Oricorio", 7, False,
    "", ("Fire", "Flying"),
    75, 84, 70, 93,
    ((1, mv.POUND), (4, mv.GROWL), (6, mv.PECK), (10, mv.HELPING_HAND),
     (13, mv.AIR_CUTTER), (16, mv.BATON_PASS), (20, mv.FEATHER_DANCE),
     (23, mv.ACROBATICS), (26, mv.TEETER_DANCE), (30, mv.ROOST),
     (33, mv.FLATTER), (36, mv.AIR_SLASH), (40, mv.REVELATION_DANCE),
     (43, mv.AGILITY), (47, mv.HURRICANE)),
    None, 0, False, "")

RIBOMBEE = Pokemon(
    743, "Ribombee", 7, False,
    "", ("Bug", "Fairy"),
    60, 75, 65, 124,
    ((0, mv.POLLEN_PUFF), (1, mv.ABSORB), (1, mv.FAIRY_WIND),
     (1, mv.STUN_SPORE), (1, mv.SWEET_SCENT), (18, mv.DRAINING_KISS),
     (24, mv.STRUGGLE_BUG), (32, mv.COVET), (40, mv.SWITCHEROO),
     (48, mv.DAZZLING_GLEAM), (56, mv.BUG_BUZZ), (64, mv.QUIVER_DANCE)),
    None, 0, False, "")

CUTIEFLY = Pokemon(
    742, "Cutiefly", 7, False,
    "", ("Bug", "Fairy"),
    40, 50, 40, 84,
    ((1, mv.ABSORB), (1, mv.FAIRY_WIND), (6, mv.STUN_SPORE),
     (12, mv.SWEET_SCENT), (18, mv.DRAINING_KISS), (24, mv.STRUGGLE_BUG),
     (30, mv.COVET), (36, mv.SWITCHEROO), (42, mv.DAZZLING_GLEAM),
     (48, mv.BUG_BUZZ), (54, mv.QUIVER_DANCE)),
    RIBOMBEE, 25, True, "")

LYCANROC = Pokemon(
    745, "Lycanroc", 7, False,
    "", ("Rock",),
    75, 85, 65, 112,
    ((0, mv.SUCKER_PUNCH), (1, mv.ACCELEROCK), (1, mv.DOUBLE_TEAM),
     (1, mv.LEER), (1, mv.QUICK_ATTACK), (1, mv.QUICK_GUARD),
     (1, mv.SAND_ATTACK), (1, mv.TACKLE), (12, mv.ROCK_THROW), (16, mv.HOWL),
     (20, mv.BITE), (24, mv.ROCK_TOMB), (30, mv.ROAR), (36, mv.ROCK_SLIDE),
     (42, mv.CRUNCH), (48, mv.SCARY_FACE), (54, mv.STEALTH_ROCK),
     (60, mv.STONE_EDGE)),
    None, 0, False, "")

ROCKRUFF = Pokemon(
    744, "Rockruff", 7, False,
    "", ("Rock",),
    45, 47, 40, 60,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.SAND_ATTACK), (8, mv.DOUBLE_TEAM),
     (12, mv.ROCK_THROW), (16, mv.HOWL), (20, mv.BITE), (24, mv.ROCK_TOMB),
     (28, mv.ROAR), (32, mv.ROCK_SLIDE), (36, mv.CRUNCH), (40, mv.SCARY_FACE),
     (44, mv.STEALTH_ROCK), (48, mv.STONE_EDGE)),
    LYCANROC, 25, True, "")

WISHIWASHI = Pokemon(
    746, "Wishiwashi", 7, False,
    "", ("Water",),
    45, 22, 22, 40,
    ((1, mv.GROWL), (1, mv.WATER_GUN), (4, mv.HELPING_HAND), (8, mv.BEAT_UP),
     (12, mv.BRINE), (16, mv.TEARFUL_LOOK), (20, mv.DIVE), (24, mv.SOAK),
     (28, mv.UPROAR), (32, mv.AQUA_TAIL), (36, mv.AQUA_RING),
     (40, mv.ENDEAVOR), (44, mv.HYDRO_PUMP), (48, mv.DOUBLE_EDGE)),
    None, 0, False, "")

TOXAPEX = Pokemon(
    748, "Toxapex", 7, False,
    "", ("Poison", "Water"),
    50, 58, 147, 35,
    ((0, mv.BANEFUL_BUNKER), (1, mv.BITE), (1, mv.PECK), (1, mv.POISON_STING),
     (1, mv.WIDE_GUARD), (15, mv.VENOSHOCK), (20, mv.RECOVER),
     (25, mv.PIN_MISSILE), (30, mv.TOXIC_SPIKES), (35, mv.LIQUIDATION),
     (42, mv.ACID_SPRAY), (49, mv.POISON_JAB), (56, mv.TOXIC)),
    None, 0, False, "")

MAREANIE = Pokemon(
    747, "Mareanie", 7, False,
    "", ("Poison", "Water"),
    50, 48, 57, 45,
    ((1, mv.PECK), (1, mv.POISON_STING), (5, mv.WIDE_GUARD), (10, mv.BITE),
     (15, mv.VENOSHOCK), (20, mv.RECOVER), (25, mv.PIN_MISSILE),
     (30, mv.TOXIC_SPIKES), (35, mv.LIQUIDATION), (40, mv.ACID_SPRAY),
     (45, mv.POISON_JAB), (50, mv.TOXIC)),
    TOXAPEX, 38, True, "")

MUDSDALE = Pokemon(
    750, "Mudsdale", 7, False,
    "", ("Ground",),
    100, 90, 92, 35,
    ((1, mv.DOUBLE_KICK), (1, mv.IRON_DEFENSE), (1, mv.MUD_SLAP),
     (1, mv.ROCK_SMASH), (12, mv.BULLDOZE), (16, mv.STOMP), (20, mv.STRENGTH),
     (24, mv.COUNTER), (28, mv.HIGH_HORSEPOWER), (34, mv.HEAVY_SLAM),
     (40, mv.EARTHQUAKE), (46, mv.MEGA_KICK), (52, mv.SUPERPOWER)),
    None, 0, False, "")

MUDBRAY = Pokemon(
    749, "Mudbray", 7, False,
    "", ("Ground",),
    70, 72, 62, 45,
    ((1, mv.MUD_SLAP), (1, mv.ROCK_SMASH), (4, mv.IRON_DEFENSE),
     (8, mv.DOUBLE_KICK), (12, mv.BULLDOZE), (16, mv.STOMP), (20, mv.STRENGTH),
     (24, mv.COUNTER), (28, mv.HIGH_HORSEPOWER), (32, mv.HEAVY_SLAM),
     (36, mv.EARTHQUAKE), (40, mv.MEGA_KICK), (44, mv.SUPERPOWER)),
    MUDSDALE, 30, True, "")

ARAQUANID = Pokemon(
    752, "Araquanid", 7, False,
    "", ("Water", "Bug"),
    68, 60, 112, 42,
    ((1, mv.BITE), (1, mv.BUG_BITE), (1, mv.INFESTATION), (1, mv.WATER_GUN),
     (1, mv.WIDE_GUARD), (12, mv.BUBBLE_BEAM), (16, mv.AQUA_RING),
     (20, mv.HEADBUTT), (26, mv.CRUNCH), (32, mv.SOAK), (38, mv.ENTRAINMENT),
     (44, mv.LUNGE), (50, mv.LIQUIDATION), (56, mv.LEECH_LIFE),
     (62, mv.MIRROR_COAT)),
    None, 0, False, "")

DEWPIDER = Pokemon(
    751, "Dewpider", 7, False,
    "", ("Water", "Bug"),
    38, 40, 62, 27,
    ((1, mv.INFESTATION), (1, mv.WATER_GUN), (4, mv.BUG_BITE), (8, mv.BITE),
     (12, mv.BUBBLE_BEAM), (16, mv.AQUA_RING), (20, mv.HEADBUTT),
     (24, mv.CRUNCH), (28, mv.SOAK), (32, mv.ENTRAINMENT), (36, mv.LUNGE),
     (40, mv.LIQUIDATION), (44, mv.LEECH_LIFE), (48, mv.MIRROR_COAT)),
    ARAQUANID, 22, True, "")

LURANTIS = Pokemon(
    754, "Lurantis", 7, False,
    "", ("Grass",),
    70, 92, 90, 45,
    ((0, mv.PETAL_BLIZZARD), (1, mv.FURY_CUTTER), (1, mv.GROWTH),
     (1, mv.INGRAIN), (1, mv.LEAFAGE), (1, mv.NIGHT_SLASH), (1, mv.SOLAR_BEAM),
     (15, mv.RAZOR_LEAF), (20, mv.SWEET_SCENT), (25, mv.SLASH),
     (30, mv.X_SCISSOR), (37, mv.SYNTHESIS), (44, mv.LEAF_BLADE),
     (51, mv.SUNNY_DAY), (63, mv.SOLAR_BLADE)),
    None, 0, False, "")

FOMANTIS = Pokemon(
    753, "Fomantis", 7, False,
    "", ("Grass",),
    40, 52, 35, 35,
    ((1, mv.FURY_CUTTER), (1, mv.LEAFAGE), (5, mv.GROWTH), (10, mv.INGRAIN),
     (15, mv.RAZOR_LEAF), (20, mv.SWEET_SCENT), (25, mv.SLASH),
     (30, mv.X_SCISSOR), (35, mv.SYNTHESIS), (40, mv.LEAF_BLADE),
     (45, mv.SUNNY_DAY), (50, mv.SOLAR_BEAM)),
    LURANTIS, 34, True, "")

SHIINOTIC = Pokemon(
    756, "Shiinotic", 7, False,
    "", ("Grass", "Fairy"),
    60, 67, 90, 30,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.CONFUSE_RAY), (1, mv.INGRAIN),
     (12, mv.MEGA_DRAIN), (16, mv.SLEEP_POWDER), (20, mv.MOONLIGHT),
     (27, mv.STRENGTH_SAP), (32, mv.GIGA_DRAIN), (38, mv.DAZZLING_GLEAM),
     (44, mv.SPORE), (50, mv.MOONBLAST), (56, mv.DREAM_EATER)),
    None, 0, False, "")

MORELULL = Pokemon(
    755, "Morelull", 7, False,
    "", ("Grass", "Fairy"),
    40, 50, 65, 15,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (4, mv.CONFUSE_RAY), (8, mv.INGRAIN),
     (12, mv.MEGA_DRAIN), (16, mv.SLEEP_POWDER), (20, mv.MOONLIGHT),
     (25, mv.STRENGTH_SAP), (28, mv.GIGA_DRAIN), (32, mv.DAZZLING_GLEAM),
     (36, mv.SPORE), (40, mv.MOONBLAST), (44, mv.DREAM_EATER)),
    SHIINOTIC, 24, True, "")

SALAZZLE = Pokemon(
    758, "Salazzle", 7, False,
    "", ("Poison", "Fire"),
    68, 87, 60, 117,
    ((0, mv.FIRE_LASH), (1, mv.DISABLE), (1, mv.EMBER), (1, mv.ENCORE),
     (1, mv.ENDEAVOR), (1, mv.KNOCK_OFF), (1, mv.POISON_GAS), (1, mv.POUND),
     (1, mv.SCRATCH), (1, mv.SMOG), (1, mv.SWAGGER), (1, mv.TORMENT),
     (15, mv.POISON_FANG), (20, mv.SWEET_SCENT), (25, mv.NASTY_PLOT),
     (30, mv.INCINERATE), (37, mv.VENOSHOCK), (44, mv.DRAGON_PULSE),
     (51, mv.FLAMETHROWER), (58, mv.TOXIC)),
    None, 0, False, "")

SALANDIT = Pokemon(
    757, "Salandit", 7, False,
    "", ("Poison", "Fire"),
    48, 57, 40, 77,
    ((1, mv.POISON_GAS), (1, mv.SCRATCH), (5, mv.SMOG), (10, mv.EMBER),
     (15, mv.POISON_FANG), (20, mv.SWEET_SCENT), (25, mv.NASTY_PLOT),
     (30, mv.INCINERATE), (35, mv.VENOSHOCK), (40, mv.DRAGON_PULSE),
     (45, mv.FLAMETHROWER), (50, mv.TOXIC), (55, mv.ENDEAVOR)),
    SALAZZLE, 33, True, "")

BEWEAR = Pokemon(
    760, "Bewear", 7, False,
    "", ("Normal", "Fighting"),
    120, 90, 70, 60,
    ((1, mv.BABY_DOLL_EYES), (1, mv.BIND), (1, mv.LEER), (1, mv.PAYBACK),
     (1, mv.TACKLE), (12, mv.BRUTAL_SWING), (16, mv.ENDURE), (20, mv.STRENGTH),
     (24, mv.TAKE_DOWN), (30, mv.FLAIL), (36, mv.HAMMER_ARM), (42, mv.THRASH),
     (48, mv.PAIN_SPLIT), (54, mv.DOUBLE_EDGE), (60, mv.SUPERPOWER)),
    None, 0, False, "")

STUFFUL = Pokemon(
    759, "Stufful", 7, False,
    "", ("Normal", "Fighting"),
    70, 60, 50, 50,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.BABY_DOLL_EYES), (8, mv.PAYBACK),
     (12, mv.BRUTAL_SWING), (16, mv.ENDURE), (20, mv.STRENGTH),
     (24, mv.TAKE_DOWN), (28, mv.FLAIL), (32, mv.HAMMER_ARM), (36, mv.THRASH),
     (40, mv.PAIN_SPLIT), (44, mv.DOUBLE_EDGE), (48, mv.SUPERPOWER)),
    BEWEAR, 27, True, "")

TSAREENA = Pokemon(
    763, "Tsareena", 7, False,
    "", ("Grass",),
    72, 85, 98, 72,
    ((0, mv.TROP_KICK), (1, mv.FLAIL), (1, mv.PLAY_NICE), (1, mv.POWER_WHIP),
     (1, mv.RAPID_SPIN), (1, mv.RAZOR_LEAF), (1, mv.SPLASH), (1, mv.SWAGGER),
     (16, mv.SWEET_SCENT), (22, mv.MAGICAL_LEAF), (28, mv.STOMP),
     (34, mv.TEETER_DANCE), (40, mv.AROMATIC_MIST), (46, mv.LEAF_STORM),
     (58, mv.HIGH_JUMP_KICK)),
    None, 0, False, "")

STEENEE = Pokemon(
    762, "Steenee", 7, False,
    "", ("Grass",),
    52, 40, 48, 62,
    ((1, mv.FLAIL), (1, mv.PLAY_NICE), (1, mv.RAPID_SPIN), (1, mv.RAZOR_LEAF),
     (1, mv.SPLASH), (16, mv.SWEET_SCENT), (22, mv.MAGICAL_LEAF),
     (28, mv.STOMP), (34, mv.TEETER_DANCE), (40, mv.AROMATIC_MIST),
     (46, mv.LEAF_STORM)),
    TSAREENA, 0, True, "level-up")

BOUNSWEET = Pokemon(
    761, "Bounsweet", 7, False,
    "", ("Grass",),
    42, 30, 38, 32,
    ((1, mv.SPLASH), (4, mv.PLAY_NICE), (8, mv.RAPID_SPIN),
     (12, mv.RAZOR_LEAF), (16, mv.SWEET_SCENT), (20, mv.MAGICAL_LEAF),
     (24, mv.FLAIL), (28, mv.TEETER_DANCE), (32, mv.AROMATIC_MIST)),
    STEENEE, 18, True, "")

COMFEY = Pokemon(
    764, "Comfey", 7, False,
    "", ("Fairy",),
    51, 67, 100, 100,
    ((1, mv.GROWTH), (1, mv.WRAP), (3, mv.VINE_WHIP), (6, mv.HELPING_HAND),
     (9, mv.DRAINING_KISS), (12, mv.CHARM), (15, mv.MAGICAL_LEAF),
     (18, mv.SYNTHESIS), (21, mv.LEECH_SEED), (24, mv.GRASS_KNOT),
     (27, mv.SWEET_KISS), (30, mv.FLORAL_HEALING), (33, mv.PETAL_BLIZZARD),
     (36, mv.BIND), (39, mv.PLAY_ROUGH), (42, mv.SWEET_SCENT),
     (45, mv.PETAL_DANCE), (48, mv.GRASSY_TERRAIN)),
    None, 0, False, "")

ORANGURU = Pokemon(
    765, "Oranguru", 7, False,
    "", ("Normal", "Psychic"),
    90, 75, 95, 60,
    ((1, mv.CONFUSION), (1, mv.TAUNT), (5, mv.AFTER_YOU), (10, mv.CALM_MIND),
     (15, mv.STORED_POWER), (20, mv.PSYCH_UP), (25, mv.QUASH),
     (30, mv.NASTY_PLOT), (35, mv.ZEN_HEADBUTT), (40, mv.TRICK_ROOM),
     (45, mv.PSYCHIC), (50, mv.INSTRUCT), (55, mv.FOUL_PLAY),
     (60, mv.FUTURE_SIGHT)),
    None, 0, False, "")

PASSIMIAN = Pokemon(
    766, "Passimian", 7, False,
    "", ("Fighting",),
    100, 80, 75, 80,
    ((1, mv.LEER), (1, mv.TACKLE), (5, mv.ROCK_SMASH), (10, mv.FOCUS_ENERGY),
     (15, mv.BEAT_UP), (20, mv.SCARY_FACE), (25, mv.TAKE_DOWN), (30, mv.FLING),
     (35, mv.BULK_UP), (40, mv.THRASH), (45, mv.DOUBLE_EDGE),
     (50, mv.CLOSE_COMBAT), (55, mv.REVERSAL), (60, mv.GIGA_IMPACT)),
    None, 0, False, "")

GOLISOPOD = Pokemon(
    768, "Golisopod", 7, False,
    "", ("Bug", "Water"),
    75, 92, 115, 40,
    ((1, mv.DEFENSE_CURL), (1, mv.FIRST_IMPRESSION), (1, mv.SAND_ATTACK),
     (1, mv.SPITE), (1, mv.STRUGGLE_BUG), (4, mv.ROCK_SMASH),
     (8, mv.FURY_CUTTER), (12, mv.MUD_SHOT), (16, mv.BUG_BITE),
     (20, mv.IRON_DEFENSE), (24, mv.SUCKER_PUNCH), (28, mv.SLASH),
     (32, mv.RAZOR_SHELL), (36, mv.PIN_MISSILE), (40, mv.SWORDS_DANCE),
     (44, mv.LIQUIDATION)),
    None, 0, False, "")

WIMPOD = Pokemon(
    767, "Wimpod", 7, False,
    "", ("Bug", "Water"),
    25, 27, 35, 80,
    ((1, mv.DEFENSE_CURL), (1, mv.SAND_ATTACK), (1, mv.STRUGGLE_BUG)),
    GOLISOPOD, 30, True, "")

PALOSSAND = Pokemon(
    770, "Palossand", 7, False,
    "", ("Ghost", "Ground"),
    85, 87, 92, 35,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.HARDEN), (1, mv.SAND_TOMB),
     (15, mv.MEGA_DRAIN), (20, mv.SAND_ATTACK), (25, mv.BULLDOZE),
     (30, mv.HYPNOSIS), (35, mv.GIGA_DRAIN), (40, mv.IRON_DEFENSE),
     (47, mv.SHADOW_BALL), (54, mv.EARTH_POWER), (61, mv.SHORE_UP),
     (68, mv.SANDSTORM)),
    None, 0, False, "")

SANDYGAST = Pokemon(
    769, "Sandygast", 7, False,
    "", ("Ghost", "Ground"),
    55, 62, 62, 15,
    ((1, mv.ABSORB), (1, mv.HARDEN), (5, mv.ASTONISH), (10, mv.SAND_TOMB),
     (15, mv.MEGA_DRAIN), (20, mv.SAND_ATTACK), (25, mv.BULLDOZE),
     (30, mv.HYPNOSIS), (35, mv.GIGA_DRAIN), (40, mv.IRON_DEFENSE),
     (45, mv.SHADOW_BALL), (50, mv.EARTH_POWER), (55, mv.SHORE_UP),
     (60, mv.SANDSTORM)),
    PALOSSAND, 42, True, "")

PYUKUMUKU = Pokemon(
    771, "Pyukumuku", 7, False,
    "", ("Water",),
    55, 45, 130, 5,
    ((1, mv.BATON_PASS), (1, mv.HARDEN), (5, mv.HELPING_HAND), (10, mv.TAUNT),
     (15, mv.SAFEGUARD), (20, mv.COUNTER), (25, mv.PURIFY), (30, mv.CURSE),
     (35, mv.GASTRO_ACID), (40, mv.PAIN_SPLIT), (45, mv.RECOVER),
     (50, mv.SOAK), (55, mv.TOXIC), (60, mv.MEMENTO)),
    None, 0, False, "")

SILVALLY = Pokemon(
    773, "Silvally", 7, False,
    "", ("Normal",),
    95, 95, 95, 95,
    ((0, mv.MULTI_ATTACK), (1, mv.AERIAL_ACE), (1, mv.BITE), (1, mv.EXPLOSION),
     (1, mv.FIRE_FANG), (1, mv.ICE_FANG), (1, mv.IMPRISON), (1, mv.IRON_HEAD),
     (1, mv.POISON_FANG), (1, mv.SCARY_FACE), (1, mv.TACKLE),
     (1, mv.THUNDER_FANG), (15, mv.DOUBLE_HIT), (20, mv.METAL_SOUND),
     (25, mv.CRUSH_CLAW), (30, mv.AIR_SLASH), (35, mv.TRI_ATTACK),
     (40, mv.X_SCISSOR), (45, mv.CRUNCH), (50, mv.TAKE_DOWN),
     (55, mv.DOUBLE_EDGE), (60, mv.PARTING_SHOT)),
    None, 0, False, "")

TYPE_NULL = Pokemon(
    772, "Type: Null", 7, False,
    "", ("Normal",),
    95, 95, 95, 59,
    ((1, mv.IMPRISON), (1, mv.TACKLE), (5, mv.AERIAL_ACE), (10, mv.SCARY_FACE),
     (15, mv.DOUBLE_HIT), (20, mv.METAL_SOUND), (25, mv.CRUSH_CLAW),
     (30, mv.AIR_SLASH), (35, mv.TRI_ATTACK), (40, mv.X_SCISSOR),
     (45, mv.IRON_HEAD), (50, mv.TAKE_DOWN), (55, mv.DOUBLE_EDGE)),
    SILVALLY, 0, True, "happiness")

MINIOR = Pokemon(
    774, "Minior", 7, False,
    "", ("Rock", "Flying"),
    60, 60, 100, 60,
    ((1, mv.TACKLE), (3, mv.DEFENSE_CURL), (8, mv.ROLLOUT),
     (10, mv.CONFUSE_RAY), (15, mv.SWIFT), (17, mv.ANCIENT_POWER),
     (22, mv.SELF_DESTRUCT), (24, mv.STEALTH_ROCK), (29, mv.TAKE_DOWN),
     (31, mv.ROCK_POLISH), (36, mv.COSMIC_POWER), (38, mv.POWER_GEM),
     (43, mv.DOUBLE_EDGE), (45, mv.SHELL_SMASH), (50, mv.EXPLOSION)),
    None, 0, False, "")

KOMALA = Pokemon(
    775, "Komala", 7, False,
    "", ("Normal",),
    65, 95, 80, 65,
    ((1, mv.DEFENSE_CURL), (1, mv.ROLLOUT), (6, mv.SPIT_UP), (6, mv.STOCKPILE),
     (6, mv.SWALLOW), (11, mv.RAPID_SPIN), (16, mv.YAWN), (21, mv.SLAM),
     (26, mv.FLAIL), (31, mv.SUCKER_PUNCH), (36, mv.PSYCH_UP),
     (41, mv.WOOD_HAMMER), (46, mv.THRASH)),
    None, 0, False, "")

TURTONATOR = Pokemon(
    776, "Turtonator", 7, False,
    "", ("Fire", "Dragon"),
    60, 84, 110, 36,
    ((1, mv.SMOG), (1, mv.TACKLE), (4, mv.EMBER), (8, mv.PROTECT),
     (12, mv.ENDURE), (16, mv.FLAIL), (20, mv.INCINERATE),
     (24, mv.IRON_DEFENSE), (28, mv.DRAGON_PULSE), (32, mv.BODY_SLAM),
     (36, mv.FLAMETHROWER), (40, mv.SHELL_TRAP), (44, mv.SHELL_SMASH),
     (48, mv.OVERHEAT), (52, mv.EXPLOSION)),
    None, 0, False, "")

TOGEDEMARU = Pokemon(
    777, "Togedemaru", 7, False,
    "", ("Electric", "Steel"),
    65, 69, 68, 96,
    ((1, mv.NUZZLE), (1, mv.TACKLE), (5, mv.DEFENSE_CURL), (10, mv.CHARGE),
     (15, mv.THUNDER_SHOCK), (20, mv.FELL_STINGER), (25, mv.SPARK),
     (30, mv.PIN_MISSILE), (35, mv.MAGNET_RISE), (40, mv.ZING_ZAP),
     (45, mv.DISCHARGE), (50, mv.ELECTRIC_TERRAIN), (55, mv.WILD_CHARGE),
     (60, mv.SPIKY_SHIELD)),
    None, 0, False, "")

MIMIKYU = Pokemon(
    778, "Mimikyu", 7, False,
    "", ("Ghost", "Fairy"),
    55, 70, 92, 96,
    ((1, mv.ASTONISH), (1, mv.COPYCAT), (1, mv.SCRATCH), (1, mv.SPLASH),
     (1, mv.WOOD_HAMMER), (6, mv.SHADOW_SNEAK), (12, mv.DOUBLE_TEAM),
     (18, mv.BABY_DOLL_EYES), (24, mv.MIMIC), (30, mv.HONE_CLAWS),
     (36, mv.SLASH), (42, mv.SHADOW_CLAW), (48, mv.CHARM), (54, mv.PLAY_ROUGH),
     (60, mv.PAIN_SPLIT)),
    None, 0, False, "")

BRUXISH = Pokemon(
    779, "Bruxish", 7, False,
    "", ("Water", "Psychic"),
    68, 87, 70, 92,
    ((1, mv.WATER_GUN), (4, mv.ASTONISH), (9, mv.CONFUSION), (12, mv.BITE),
     (17, mv.AQUA_JET), (20, mv.DISABLE), (25, mv.PSYSHOCK), (28, mv.CRUNCH),
     (33, mv.AQUA_TAIL), (36, mv.SCREECH), (41, mv.PSYCHIC_FANGS),
     (44, mv.WAVE_CRASH)),
    None, 0, False, "")

DRAMPA = Pokemon(
    780, "Drampa", 7, False,
    "", ("Normal", "Dragon"),
    78, 97, 88, 36,
    ((1, mv.ECHOED_VOICE), (1, mv.PLAY_NICE), (5, mv.TWISTER),
     (10, mv.PROTECT), (15, mv.GLARE), (20, mv.SAFEGUARD),
     (25, mv.DRAGON_BREATH), (30, mv.EXTRASENSORY), (35, mv.DRAGON_PULSE),
     (40, mv.LIGHT_SCREEN), (45, mv.FLY), (50, mv.HYPER_VOICE),
     (55, mv.OUTRAGE)),
    None, 0, False, "")

DHELMISE = Pokemon(
    781, "Dhelmise", 7, False,
    "", ("Ghost", "Grass"),
    70, 108, 95, 40,
    ((1, mv.ABSORB), (1, mv.RAPID_SPIN), (4, mv.ASTONISH), (8, mv.WRAP),
     (12, mv.MEGA_DRAIN), (16, mv.GROWTH), (20, mv.GYRO_BALL),
     (24, mv.SWITCHEROO), (28, mv.GIGA_DRAIN), (32, mv.WHIRLPOOL),
     (36, mv.HEAVY_SLAM), (40, mv.SLAM), (44, mv.SHADOW_BALL),
     (48, mv.METAL_SOUND), (52, mv.ANCHOR_SHOT), (56, mv.ENERGY_BALL),
     (60, mv.PHANTOM_FORCE), (64, mv.POWER_WHIP)),
    None, 0, False, "")

KOMMO_O = Pokemon(
    784, "Kommo-o", 7, False,
    "", ("Dragon", "Fighting"),
    75, 105, 115, 85,
    ((0, mv.CLANGING_SCALES), (1, mv.DRAGON_TAIL), (1, mv.LEER),
     (1, mv.PROTECT), (1, mv.TACKLE), (12, mv.SCARY_FACE), (16, mv.HEADBUTT),
     (20, mv.WORK_UP), (24, mv.SCREECH), (28, mv.IRON_DEFENSE),
     (32, mv.DRAGON_CLAW), (38, mv.NOBLE_ROAR), (44, mv.DRAGON_DANCE),
     (52, mv.OUTRAGE), (60, mv.CLOSE_COMBAT), (68, mv.CLANGOROUS_SOUL),
     (76, mv.BOOMBURST)),
    None, 0, False, "")

HAKAMO_O = Pokemon(
    783, "Hakamo-o", 7, False,
    "", ("Dragon", "Fighting"),
    55, 70, 80, 65,
    ((1, mv.DRAGON_TAIL), (1, mv.LEER), (1, mv.PROTECT), (1, mv.TACKLE),
     (12, mv.SCARY_FACE), (16, mv.HEADBUTT), (20, mv.WORK_UP),
     (24, mv.SCREECH), (28, mv.IRON_DEFENSE), (32, mv.DRAGON_CLAW),
     (38, mv.NOBLE_ROAR), (44, mv.DRAGON_DANCE), (50, mv.OUTRAGE),
     (56, mv.CLOSE_COMBAT)),
    KOMMO_O, 45, True, "")

JANGMO_O = Pokemon(
    782, "Jangmo-o", 7, False,
    "", ("Dragon",),
    45, 50, 55, 45,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.PROTECT), (8, mv.DRAGON_TAIL),
     (12, mv.SCARY_FACE), (16, mv.HEADBUTT), (20, mv.WORK_UP),
     (24, mv.SCREECH), (28, mv.IRON_DEFENSE), (32, mv.DRAGON_CLAW),
     (36, mv.NOBLE_ROAR), (40, mv.DRAGON_DANCE), (44, mv.OUTRAGE)),
    HAKAMO_O, 35, True, "")

TAPU_KOKO = Pokemon(
    785, "Tapu Koko", 7, False,
    "", ("Electric", "Fairy"),
    70, 105, 80, 130,
    ((1, mv.QUICK_ATTACK), (1, mv.THUNDER_SHOCK), (5, mv.WITHDRAW),
     (10, mv.FAIRY_WIND), (15, mv.FALSE_SWIPE), (20, mv.SPARK),
     (25, mv.SHOCK_WAVE), (30, mv.CHARGE), (35, mv.AGILITY), (40, mv.SCREECH),
     (45, mv.DISCHARGE), (50, mv.MEAN_LOOK), (55, mv.NATURES_MADNESS),
     (60, mv.WILD_CHARGE), (65, mv.BRAVE_BIRD), (70, mv.POWER_SWAP),
     (75, mv.ELECTRIC_TERRAIN)),
    None, 0, False, "")

TAPU_LELE = Pokemon(
    786, "Tapu Lele", 7, False,
    "", ("Psychic", "Fairy"),
    70, 107, 95, 95,
    ((1, mv.ASTONISH), (1, mv.CONFUSION), (5, mv.WITHDRAW),
     (10, mv.AROMATHERAPY), (15, mv.DRAINING_KISS), (20, mv.PSYBEAM),
     (25, mv.FLATTER), (30, mv.AROMATIC_MIST), (35, mv.SWEET_SCENT),
     (40, mv.EXTRASENSORY), (45, mv.PSYSHOCK), (50, mv.MEAN_LOOK),
     (55, mv.NATURES_MADNESS), (60, mv.MOONBLAST), (65, mv.TICKLE),
     (70, mv.SKILL_SWAP), (75, mv.PSYCHIC_TERRAIN)),
    None, 0, False, "")

TAPU_BULU = Pokemon(
    787, "Tapu Bulu", 7, False,
    "", ("Grass", "Fairy"),
    70, 107, 105, 75,
    ((1, mv.LEAFAGE), (1, mv.ROCK_SMASH), (5, mv.WITHDRAW), (10, mv.DISABLE),
     (15, mv.LEECH_SEED), (20, mv.MEGA_DRAIN), (25, mv.WHIRLWIND),
     (30, mv.HORN_ATTACK), (35, mv.SCARY_FACE), (40, mv.HORN_LEECH),
     (45, mv.ZEN_HEADBUTT), (50, mv.MEAN_LOOK), (55, mv.NATURES_MADNESS),
     (60, mv.WOOD_HAMMER), (65, mv.MEGAHORN), (70, mv.SKULL_BASH),
     (75, mv.GRASSY_TERRAIN)),
    None, 0, False, "")

TAPU_FINI = Pokemon(
    788, "Tapu Fini", 7, False,
    "", ("Water", "Fairy"),
    70, 85, 122, 85,
    ((1, mv.DISARMING_VOICE), (1, mv.WATER_GUN), (5, mv.WITHDRAW),
     (10, mv.HAZE), (10, mv.MIST), (15, mv.AQUA_RING), (20, mv.WATER_PULSE),
     (25, mv.BRINE), (30, mv.DEFOG), (35, mv.HEAL_PULSE), (40, mv.SURF),
     (45, mv.MUDDY_WATER), (50, mv.MEAN_LOOK), (55, mv.NATURES_MADNESS),
     (60, mv.MOONBLAST), (65, mv.HYDRO_PUMP), (70, mv.SOAK),
     (75, mv.MISTY_TERRAIN)),
    None, 0, False, "")

LUNALA = Pokemon(
    792, "Lunala", 7, False,
    "", ("Psychic", "Ghost"),
    137, 125, 98, 97,
    ((0, mv.MOONGEIST_BEAM), (1, mv.CONFUSION), (1, mv.COSMIC_POWER),
     (1, mv.HYPNOSIS), (1, mv.TELEPORT), (7, mv.NIGHT_SHADE),
     (14, mv.CONFUSE_RAY), (21, mv.AIR_SLASH), (28, mv.SHADOW_BALL),
     (35, mv.MOONLIGHT), (42, mv.NIGHT_DAZE), (49, mv.PSYCHIC),
     (56, mv.MOONBLAST), (63, mv.PHANTOM_FORCE), (70, mv.DREAM_EATER),
     (77, mv.WIDE_GUARD)),
    None, 0, False, "")

SOLGALEO = Pokemon(
    791, "Solgaleo", 7, False,
    "", ("Psychic", "Steel"),
    137, 125, 98, 97,
    ((0, mv.SUNSTEEL_STRIKE), (1, mv.COSMIC_POWER), (1, mv.METAL_CLAW),
     (1, mv.NOBLE_ROAR), (1, mv.TELEPORT), (7, mv.IRON_HEAD),
     (14, mv.METAL_SOUND), (21, mv.ZEN_HEADBUTT), (28, mv.FLASH_CANNON),
     (35, mv.MORNING_SUN), (42, mv.CRUNCH), (49, mv.METAL_BURST),
     (56, mv.WILD_CHARGE), (63, mv.SOLAR_BEAM), (70, mv.FLARE_BLITZ),
     (77, mv.WIDE_GUARD), (84, mv.GIGA_IMPACT)),
    LUNALA, 0, True, "Level 53 in Specific Game")

COSMOEM = Pokemon(
    790, "Cosmoem", 7, False,
    "", ("Psychic",),
    43, 29, 131, 37,
    ((0, mv.COSMIC_POWER), (1, mv.TELEPORT)),
    SOLGALEO, 53, True, "")

COSMOG = Pokemon(
    789, "Cosmog", 7, False,
    "", ("Psychic",),
    43, 29, 31, 37,
    ((1, mv.SPLASH), (1, mv.TELEPORT)),
    COSMOEM, 43, True, "")

NIHILEGO = Pokemon(
    793, "Nihilego", 7, False,
    "", ("Rock", "Poison"),
    109, 90, 89, 103,
    ((1, mv.POUND), (1, mv.WRAP), (5, mv.ACID), (10, mv.TICKLE),
     (15, mv.ACID_SPRAY), (20, mv.CLEAR_SMOG), (25, mv.GUARD_SPLIT),
     (25, mv.POWER_SPLIT), (30, mv.VENOSHOCK), (35, mv.HEADBUTT),
     (40, mv.TOXIC_SPIKES), (45, mv.VENOM_DRENCH), (50, mv.POWER_GEM),
     (55, mv.STEALTH_ROCK), (60, mv.MIRROR_COAT), (65, mv.WONDER_ROOM),
     (70, mv.HEAD_SMASH)),
    None, 0, False, "")

BUZZWOLE = Pokemon(
    794, "Buzzwole", 7, False,
    "", ("Bug", "Fighting"),
    107, 96, 96, 79,
    ((1, mv.HARDEN), (1, mv.POWER_UP_PUNCH), (5, mv.TAUNT),
     (10, mv.FELL_STINGER), (15, mv.VITAL_THROW), (20, mv.BULK_UP),
     (25, mv.ENDURE), (30, mv.REVERSAL), (35, mv.MEGA_PUNCH), (40, mv.LUNGE),
     (45, mv.FOCUS_ENERGY), (50, mv.DYNAMIC_PUNCH), (55, mv.COUNTER),
     (60, mv.HAMMER_ARM), (65, mv.SUPERPOWER), (70, mv.FOCUS_PUNCH)),
    None, 0, False, "")

PHEROMOSA = Pokemon(
    795, "Pheromosa", 7, False,
    "", ("Bug", "Fighting"),
    71, 137, 37, 151,
    ((1, mv.FEINT), (1, mv.RAPID_SPIN), (5, mv.LEER), (10, mv.QUICK_GUARD),
     (15, mv.BUG_BITE), (20, mv.LOW_KICK), (25, mv.DOUBLE_KICK),
     (30, mv.TRIPLE_KICK), (35, mv.STOMP), (40, mv.AGILITY), (45, mv.LUNGE),
     (50, mv.BOUNCE), (55, mv.SPEED_SWAP), (60, mv.BUG_BUZZ),
     (65, mv.QUIVER_DANCE), (70, mv.HIGH_JUMP_KICK)),
    None, 0, False, "")

XURKITREE = Pokemon(
    796, "Xurkitree", 7, False,
    "", ("Electric",),
    83, 131, 71, 83,
    ((1, mv.THUNDER_SHOCK), (1, mv.WRAP), (5, mv.CHARGE),
     (10, mv.THUNDER_WAVE), (15, mv.INGRAIN), (20, mv.SPARK),
     (25, mv.SHOCK_WAVE), (30, mv.HYPNOSIS), (35, mv.EERIE_IMPULSE),
     (40, mv.THUNDER_PUNCH), (45, mv.DISCHARGE), (50, mv.MAGNET_RISE),
     (55, mv.THUNDERBOLT), (60, mv.ELECTRIC_TERRAIN), (65, mv.POWER_WHIP),
     (70, mv.ZAP_CANNON)),
    None, 0, False, "")

CELESTEELA = Pokemon(
    797, "Celesteela", 7, False,
    "", ("Steel", "Flying"),
    97, 104, 102, 61,
    ((1, mv.ABSORB), (1, mv.TACKLE), (5, mv.HARDEN), (10, mv.WIDE_GUARD),
     (15, mv.MEGA_DRAIN), (20, mv.SMACK_DOWN), (25, mv.INGRAIN),
     (30, mv.AUTOTOMIZE), (35, mv.GIGA_DRAIN), (40, mv.FLASH_CANNON),
     (45, mv.METAL_SOUND), (50, mv.IRON_DEFENSE), (55, mv.LEECH_SEED),
     (60, mv.HEAVY_SLAM), (65, mv.DOUBLE_EDGE), (70, mv.SKULL_BASH)),
    None, 0, False, "")

KARTANA = Pokemon(
    798, "Kartana", 7, False,
    "", ("Grass", "Steel"),
    59, 120, 81, 109,
    ((1, mv.FURY_CUTTER), (1, mv.VACUUM_WAVE), (5, mv.RAZOR_LEAF),
     (10, mv.FALSE_SWIPE), (15, mv.CUT), (20, mv.AIR_CUTTER),
     (25, mv.AERIAL_ACE), (30, mv.DETECT), (35, mv.NIGHT_SLASH),
     (40, mv.SYNTHESIS), (45, mv.LASER_FOCUS), (50, mv.DEFOG),
     (55, mv.LEAF_BLADE), (60, mv.SACRED_SWORD), (65, mv.SWORDS_DANCE),
     (70, mv.GUILLOTINE)),
    None, 0, False, "")

GUZZLORD = Pokemon(
    799, "Guzzlord", 7, False,
    "", ("Dark", "Dragon"),
    223, 99, 53, 43,
    ((1, mv.BITE), (1, mv.DRAGON_TAIL), (5, mv.STOCKPILE), (5, mv.SWALLOW),
     (10, mv.KNOCK_OFF), (15, mv.STOMP), (20, mv.STOMPING_TANTRUM),
     (25, mv.WIDE_GUARD), (30, mv.CRUNCH), (35, mv.BODY_SLAM),
     (40, mv.GASTRO_ACID), (45, mv.HAMMER_ARM), (50, mv.HEAVY_SLAM),
     (55, mv.DRAGON_RUSH), (60, mv.BELCH), (65, mv.THRASH),
     (70, mv.GIGA_IMPACT)),
    None, 0, False, "")

NECROZMA = Pokemon(
    800, "Necrozma", 7, False,
    "", ("Psychic",),
    97, 117, 95, 79,
    ((1, mv.CHARGE_BEAM), (1, mv.CONFUSION), (1, mv.METAL_CLAW),
     (1, mv.MOONLIGHT), (1, mv.MORNING_SUN), (8, mv.STEALTH_ROCK),
     (16, mv.SLASH), (24, mv.NIGHT_SLASH), (32, mv.PSYCHO_CUT),
     (40, mv.STORED_POWER), (48, mv.ROCK_BLAST), (56, mv.IRON_DEFENSE),
     (64, mv.POWER_GEM), (72, mv.PHOTON_GEYSER), (80, mv.GRAVITY),
     (88, mv.PRISMATIC_LASER)),
    None, 0, False, "")

MAGEARNA = Pokemon(
    801, "Magearna", 7, False,
    "", ("Steel", "Fairy"),
    80, 112, 115, 65,
    ((1, mv.GYRO_BALL), (1, mv.HELPING_HAND), (6, mv.DEFENSE_CURL),
     (12, mv.ROLLOUT), (18, mv.IRON_DEFENSE), (24, mv.MAGNETIC_FLUX),
     (30, mv.PSYBEAM), (36, mv.AURORA_BEAM), (42, mv.LOCK_ON),
     (48, mv.SHIFT_GEAR), (54, mv.TRICK), (60, mv.IRON_HEAD),
     (66, mv.AURA_SPHERE), (72, mv.FLASH_CANNON), (78, mv.PAIN_SPLIT),
     (84, mv.ZAP_CANNON), (90, mv.FLEUR_CANNON)),
    None, 0, False, "")

MARSHADOW = Pokemon(
    802, "Marshadow", 7, False,
    "", ("Fighting", "Ghost"),
    90, 107, 85, 125,
    ((1, mv.COPYCAT), (1, mv.COUNTER), (1, mv.FEINT), (1, mv.FIRE_PUNCH),
     (1, mv.ICE_PUNCH), (1, mv.SHADOW_SNEAK), (1, mv.THUNDER_PUNCH),
     (9, mv.ROLE_PLAY), (18, mv.SHADOW_PUNCH), (27, mv.FORCE_PALM),
     (36, mv.ASSURANCE), (45, mv.SUCKER_PUNCH), (54, mv.DRAIN_PUNCH),
     (63, mv.PSYCH_UP), (72, mv.SPECTRAL_THIEF), (81, mv.LASER_FOCUS),
     (90, mv.ENDEAVOR), (99, mv.CLOSE_COMBAT)),
    None, 0, False, "")

NAGANADEL = Pokemon(
    804, "Naganadel", 7, False,
    "", ("Poison", "Dragon"),
    73, 100, 73, 121,
    ((1, mv.ACID), (1, mv.AIR_CUTTER), (1, mv.AIR_SLASH), (1, mv.DRAGON_PULSE),
     (1, mv.GROWL), (1, mv.HELPING_HAND), (1, mv.PECK), (7, mv.FURY_ATTACK),
     (14, mv.FELL_STINGER), (21, mv.CHARM), (28, mv.VENOSHOCK),
     (35, mv.VENOM_DRENCH), (42, mv.NASTY_PLOT), (49, mv.POISON_JAB),
     (56, mv.GASTRO_ACID), (63, mv.TOXIC), (70, mv.DRAGON_RUSH)),
    None, 0, False, "")

POIPOLE = Pokemon(
    803, "Poipole", 7, False,
    "", ("Poison",),
    67, 73, 67, 73,
    ((1, mv.ACID), (1, mv.DRAGON_PULSE), (1, mv.GROWL), (1, mv.HELPING_HAND),
     (1, mv.PECK), (7, mv.FURY_ATTACK), (14, mv.FELL_STINGER), (21, mv.CHARM),
     (28, mv.VENOSHOCK), (35, mv.VENOM_DRENCH), (42, mv.NASTY_PLOT),
     (49, mv.POISON_JAB), (56, mv.GASTRO_ACID), (63, mv.TOXIC)),
    NAGANADEL, 0, True, "level-up")

STAKATAKA = Pokemon(
    805, "Stakataka", 7, False,
    "", ("Rock", "Steel"),
    61, 92, 156, 13,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.ROCK_THROW), (10, mv.PROTECT),
     (15, mv.STOMP), (20, mv.BLOCK), (25, mv.ROCK_SLIDE), (30, mv.WIDE_GUARD),
     (35, mv.AUTOTOMIZE), (40, mv.ROCK_BLAST), (45, mv.MAGNET_RISE),
     (50, mv.IRON_DEFENSE), (55, mv.IRON_HEAD), (60, mv.TAKE_DOWN),
     (65, mv.STEALTH_ROCK), (70, mv.DOUBLE_EDGE)),
    None, 0, False, "")

BLACEPHALON = Pokemon(
    806, "Blacephalon", 7, False,
    "", ("Fire", "Ghost"),
    53, 139, 66, 107,
    ((1, mv.ASTONISH), (1, mv.FIRE_SPIN), (5, mv.LIGHT_SCREEN), (10, mv.EMBER),
     (15, mv.NIGHT_SHADE), (20, mv.CONFUSE_RAY), (25, mv.MAGIC_COAT),
     (30, mv.INCINERATE), (35, mv.HYPNOSIS), (40, mv.MYSTICAL_FIRE),
     (45, mv.SHADOW_BALL), (50, mv.CALM_MIND), (55, mv.WILL_O_WISP),
     (60, mv.TRICK), (65, mv.FIRE_BLAST), (70, mv.MIND_BLOWN)),
    None, 0, False, "")

ZERAORA = Pokemon(
    807, "Zeraora", 7, False,
    "", ("Electric",),
    88, 107, 77, 143,
    ((1, mv.FAKE_OUT), (1, mv.POWER_UP_PUNCH), (1, mv.QUICK_ATTACK),
     (1, mv.SCRATCH), (1, mv.SNARL), (1, mv.SPARK), (8, mv.FURY_SWIPES),
     (16, mv.QUICK_GUARD), (24, mv.SLASH), (32, mv.VOLT_SWITCH),
     (40, mv.CHARGE), (48, mv.THUNDER_PUNCH), (56, mv.HONE_CLAWS),
     (64, mv.DISCHARGE), (72, mv.WILD_CHARGE), (80, mv.AGILITY),
     (88, mv.PLASMA_FISTS), (96, mv.CLOSE_COMBAT)),
    None, 0, False, "")

MELMETAL = Pokemon(
    809, "Melmetal", 7, False,
    "", ("Steel",),
    135, 111, 104, 34,
    ((1, mv.HARDEN), (1, mv.HEADBUTT), (1, mv.TAIL_WHIP),
     (1, mv.THUNDER_PUNCH), (1, mv.THUNDER_SHOCK), (24, mv.THUNDER_WAVE),
     (32, mv.ACID_ARMOR), (40, mv.FLASH_CANNON), (48, mv.MEGA_PUNCH),
     (56, mv.PROTECT), (64, mv.DISCHARGE), (72, mv.DYNAMIC_PUNCH),
     (80, mv.SUPERPOWER), (88, mv.DOUBLE_IRON_BASH), (96, mv.HYPER_BEAM)),
    None, 0, False, "")

MELTAN = Pokemon(
    808, "Meltan", 7, False,
    "", ("Steel",),
    46, 60, 50, 34,
    ((1, mv.HARDEN), (1, mv.THUNDER_SHOCK), (8, mv.TAIL_WHIP),
     (16, mv.HEADBUTT), (24, mv.THUNDER_WAVE), (32, mv.ACID_ARMOR),
     (40, mv.FLASH_CANNON)),
    MELMETAL, 0, True, "400 Candy in Pokémon GO")


# --- generation 8 ---

RILLABOOM = Pokemon(
    812, "Rillaboom", 8, True,
    "Flora", ("Grass",),
    100, 92, 80, 85,
    ((0, mv.DRUM_BEATING), (1, mv.BRANCH_POKE), (1, mv.DOUBLE_HIT),
     (1, mv.GRASSY_TERRAIN), (1, mv.GROWL), (1, mv.NOBLE_ROAR),
     (1, mv.SCRATCH), (1, mv.TAUNT), (12, mv.RAZOR_LEAF), (19, mv.SCREECH),
     (24, mv.KNOCK_OFF), (30, mv.SLAM), (38, mv.UPROAR), (46, mv.WOOD_HAMMER),
     (54, mv.ENDEAVOR), (62, mv.BOOMBURST)),
    None, 0, False, "")

THWACKEY = Pokemon(
    811, "Thwackey", 8, True,
    "Flora", ("Grass",),
    70, 70, 65, 80,
    ((0, mv.DOUBLE_HIT), (1, mv.BRANCH_POKE), (1, mv.GROWL), (1, mv.SCRATCH),
     (1, mv.TAUNT), (12, mv.RAZOR_LEAF), (19, mv.SCREECH), (24, mv.KNOCK_OFF),
     (30, mv.SLAM), (36, mv.UPROAR), (42, mv.WOOD_HAMMER), (48, mv.ENDEAVOR)),
    RILLABOOM, 35, True, "")

GROOKEY = Pokemon(
    810, "Grookey", 8, True,
    "Flora", ("Grass",),
    50, 52, 45, 65,
    ((1, mv.GROWL), (1, mv.SCRATCH), (6, mv.BRANCH_POKE), (8, mv.TAUNT),
     (12, mv.RAZOR_LEAF), (17, mv.SCREECH), (20, mv.KNOCK_OFF), (24, mv.SLAM),
     (28, mv.UPROAR), (32, mv.WOOD_HAMMER), (36, mv.ENDEAVOR)),
    THWACKEY, 16, True, "")

CINDERACE = Pokemon(
    815, "Cinderace", 8, True,
    "Flame", ("Fire",),
    80, 90, 75, 119,
    ((0, mv.PYRO_BALL), (1, mv.EMBER), (1, mv.FEINT), (1, mv.GROWL),
     (1, mv.QUICK_ATTACK), (1, mv.TACKLE), (12, mv.DOUBLE_KICK),
     (19, mv.FLAME_CHARGE), (24, mv.AGILITY), (30, mv.HEADBUTT),
     (38, mv.COUNTER), (46, mv.BOUNCE), (54, mv.DOUBLE_EDGE),
     (62, mv.COURT_CHANGE)),
    None, 0, False, "")

RABOOT = Pokemon(
    814, "Raboot", 8, True,
    "Flame", ("Fire",),
    65, 70, 60, 94,
    ((1, mv.EMBER), (1, mv.GROWL), (1, mv.QUICK_ATTACK), (1, mv.TACKLE),
     (12, mv.DOUBLE_KICK), (19, mv.FLAME_CHARGE), (24, mv.AGILITY),
     (30, mv.HEADBUTT), (36, mv.COUNTER), (42, mv.BOUNCE),
     (48, mv.DOUBLE_EDGE)),
    CINDERACE, 35, True, "")

SCORBUNNY = Pokemon(
    813, "Scorbunny", 8, True,
    "Flame", ("Fire",),
    50, 55, 40, 69,
    ((1, mv.GROWL), (1, mv.TACKLE), (6, mv.EMBER), (8, mv.QUICK_ATTACK),
     (12, mv.DOUBLE_KICK), (17, mv.FLAME_CHARGE), (20, mv.AGILITY),
     (24, mv.HEADBUTT), (28, mv.COUNTER), (32, mv.BOUNCE),
     (36, mv.DOUBLE_EDGE)),
    RABOOT, 16, True, "")

INTELEON = Pokemon(
    818, "Inteleon", 8, True,
    "Aqua", ("Water",),
    70, 105, 65, 120,
    ((0, mv.SNIPE_SHOT), (1, mv.ACROBATICS), (1, mv.BIND), (1, mv.GROWL),
     (1, mv.POUND), (1, mv.WATER_GUN), (12, mv.WATER_PULSE),
     (19, mv.TEARFUL_LOOK), (24, mv.SUCKER_PUNCH), (30, mv.U_TURN),
     (38, mv.LIQUIDATION), (46, mv.SOAK), (54, mv.RAIN_DANCE),
     (62, mv.HYDRO_PUMP)),
    None, 0, False, "")

DRIZZILE = Pokemon(
    817, "Drizzile", 8, True,
    "Aqua", ("Water",),
    65, 77, 55, 90,
    ((1, mv.BIND), (1, mv.GROWL), (1, mv.POUND), (1, mv.WATER_GUN),
     (12, mv.WATER_PULSE), (19, mv.TEARFUL_LOOK), (24, mv.SUCKER_PUNCH),
     (30, mv.U_TURN), (36, mv.LIQUIDATION), (42, mv.SOAK),
     (48, mv.RAIN_DANCE)),
    INTELEON, 35, True, "")

SOBBLE = Pokemon(
    816, "Sobble", 8, True,
    "Aqua", ("Water",),
    50, 55, 40, 70,
    ((1, mv.GROWL), (1, mv.POUND), (6, mv.WATER_GUN), (8, mv.BIND),
     (12, mv.WATER_PULSE), (17, mv.TEARFUL_LOOK), (20, mv.SUCKER_PUNCH),
     (24, mv.U_TURN), (28, mv.LIQUIDATION), (32, mv.SOAK),
     (36, mv.RAIN_DANCE)),
    DRIZZILE, 16, True, "")

GREEDENT = Pokemon(
    820, "Greedent", 8, False,
    "", ("Normal",),
    120, 75, 85, 20,
    ((0, mv.COVET), (1, mv.BITE), (1, mv.STUFF_CHEEKS), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (15, mv.SPIT_UP), (15, mv.STOCKPILE), (15, mv.SWALLOW),
     (20, mv.BODY_SLAM), (27, mv.REST), (34, mv.COUNTER), (41, mv.BULLET_SEED),
     (48, mv.SUPER_FANG), (55, mv.BELCH)),
    None, 0, False, "")

SKWOVET = Pokemon(
    819, "Skwovet", 8, False,
    "", ("Normal",),
    70, 45, 45, 25,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.BITE), (10, mv.STUFF_CHEEKS),
     (15, mv.SPIT_UP), (15, mv.STOCKPILE), (15, mv.SWALLOW),
     (20, mv.BODY_SLAM), (25, mv.REST), (30, mv.COUNTER), (35, mv.BULLET_SEED),
     (40, mv.SUPER_FANG), (45, mv.BELCH)),
    GREEDENT, 24, True, "")

CORVIKNIGHT = Pokemon(
    823, "Corviknight", 8, False,
    "", ("Flying", "Steel"),
    98, 70, 95, 67,
    ((0, mv.STEEL_WING), (1, mv.HONE_CLAWS), (1, mv.IRON_DEFENSE),
     (1, mv.LEER), (1, mv.METAL_SOUND), (1, mv.PECK), (1, mv.POWER_TRIP),
     (1, mv.SCREECH), (12, mv.FURY_ATTACK), (16, mv.PLUCK), (22, mv.TAUNT),
     (28, mv.SCARY_FACE), (34, mv.DRILL_PECK), (42, mv.SWAGGER),
     (50, mv.BRAVE_BIRD)),
    None, 0, False, "")

CORVISQUIRE = Pokemon(
    822, "Corvisquire", 8, False,
    "", ("Flying",),
    68, 55, 55, 77,
    ((1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.PECK), (1, mv.POWER_TRIP),
     (12, mv.FURY_ATTACK), (16, mv.PLUCK), (22, mv.TAUNT), (28, mv.SCARY_FACE),
     (34, mv.DRILL_PECK), (40, mv.SWAGGER), (46, mv.BRAVE_BIRD)),
    CORVIKNIGHT, 38, True, "")

ROOKIDEE = Pokemon(
    821, "Rookidee", 8, False,
    "", ("Flying",),
    38, 40, 35, 57,
    ((1, mv.LEER), (1, mv.PECK), (4, mv.POWER_TRIP), (8, mv.HONE_CLAWS),
     (12, mv.FURY_ATTACK), (16, mv.PLUCK), (20, mv.TAUNT), (24, mv.SCARY_FACE),
     (28, mv.DRILL_PECK), (32, mv.SWAGGER), (36, mv.BRAVE_BIRD)),
    CORVISQUIRE, 18, True, "")

ORBEETLE = Pokemon(
    826, "Orbeetle", 8, False,
    "", ("Bug", "Psychic"),
    60, 62, 115, 90,
    ((1, mv.CONFUSION), (1, mv.LIGHT_SCREEN), (1, mv.REFLECT),
     (1, mv.STRUGGLE_BUG), (4, mv.CONFUSE_RAY), (8, mv.MAGIC_COAT),
     (12, mv.AGILITY), (16, mv.PSYBEAM), (20, mv.HYPNOSIS),
     (24, mv.ALLY_SWITCH), (28, mv.BUG_BUZZ), (32, mv.MIRROR_COAT),
     (36, mv.PSYCHIC), (40, mv.AFTER_YOU), (44, mv.CALM_MIND),
     (48, mv.PSYCHIC_TERRAIN)),
    None, 0, False, "")

DOTTLER = Pokemon(
    825, "Dottler", 8, False,
    "", ("Bug", "Psychic"),
    50, 42, 85, 30,
    ((0, mv.CONFUSION), (0, mv.LIGHT_SCREEN), (1, mv.REFLECT),
     (1, mv.STRUGGLE_BUG)),
    ORBEETLE, 30, True, "")

BLIPBUG = Pokemon(
    824, "Blipbug", 8, False,
    "", ("Bug",),
    25, 22, 32, 45,
    ((1, mv.STRUGGLE_BUG),),
    DOTTLER, 10, True, "")

THIEVUL = Pokemon(
    828, "Thievul", 8, False,
    "", ("Dark",),
    70, 72, 75, 90,
    ((0, mv.THIEF), (1, mv.BEAT_UP), (1, mv.HONE_CLAWS), (1, mv.QUICK_ATTACK),
     (1, mv.TAIL_WHIP), (12, mv.SNARL), (16, mv.ASSURANCE),
     (22, mv.NASTY_PLOT), (28, mv.SUCKER_PUNCH), (34, mv.NIGHT_SLASH),
     (40, mv.TAIL_SLAP), (46, mv.FOUL_PLAY), (52, mv.PARTING_SHOT)),
    None, 0, False, "")

NICKIT = Pokemon(
    827, "Nickit", 8, False,
    "", ("Dark",),
    40, 37, 40, 50,
    ((1, mv.QUICK_ATTACK), (1, mv.TAIL_WHIP), (4, mv.BEAT_UP),
     (8, mv.HONE_CLAWS), (12, mv.SNARL), (16, mv.ASSURANCE),
     (20, mv.NASTY_PLOT), (24, mv.SUCKER_PUNCH), (28, mv.NIGHT_SLASH),
     (32, mv.TAIL_SLAP), (36, mv.FOUL_PLAY)),
    THIEVUL, 18, True, "")

ELDEGOSS = Pokemon(
    830, "Eldegoss", 8, False,
    "", ("Grass",),
    60, 65, 105, 60,
    ((0, mv.COTTON_SPORE), (1, mv.LEAFAGE), (1, mv.RAPID_SPIN), (1, mv.SING),
     (1, mv.SWEET_SCENT), (12, mv.RAZOR_LEAF), (16, mv.ROUND),
     (23, mv.LEAF_TORNADO), (28, mv.SYNTHESIS), (34, mv.HYPER_VOICE),
     (40, mv.AROMATHERAPY), (46, mv.LEAF_STORM), (52, mv.COTTON_GUARD)),
    None, 0, False, "")

GOSSIFLEUR = Pokemon(
    829, "Gossifleur", 8, False,
    "", ("Grass",),
    40, 40, 60, 10,
    ((1, mv.LEAFAGE), (1, mv.SING), (4, mv.RAPID_SPIN), (8, mv.SWEET_SCENT),
     (12, mv.RAZOR_LEAF), (16, mv.ROUND), (21, mv.LEAF_TORNADO),
     (24, mv.SYNTHESIS), (28, mv.HYPER_VOICE), (32, mv.AROMATHERAPY),
     (36, mv.LEAF_STORM)),
    ELDEGOSS, 20, True, "")

DUBWOOL = Pokemon(
    832, "Dubwool", 8, False,
    "", ("Normal",),
    72, 70, 95, 88,
    ((1, mv.COPYCAT), (1, mv.DEFENSE_CURL), (1, mv.GROWL), (1, mv.TACKLE),
     (12, mv.GUARD_SPLIT), (16, mv.DOUBLE_KICK), (21, mv.HEADBUTT),
     (27, mv.TAKE_DOWN), (32, mv.GUARD_SWAP), (38, mv.REVERSAL),
     (44, mv.COTTON_GUARD), (50, mv.DOUBLE_EDGE), (56, mv.LAST_RESORT)),
    None, 0, False, "")

WOOLOO = Pokemon(
    831, "Wooloo", 8, False,
    "", ("Normal",),
    42, 40, 50, 48,
    ((1, mv.GROWL), (1, mv.TACKLE), (4, mv.DEFENSE_CURL), (8, mv.COPYCAT),
     (12, mv.GUARD_SPLIT), (16, mv.DOUBLE_KICK), (21, mv.HEADBUTT),
     (25, mv.TAKE_DOWN), (28, mv.GUARD_SWAP), (32, mv.REVERSAL),
     (36, mv.COTTON_GUARD), (40, mv.DOUBLE_EDGE)),
    DUBWOOL, 24, True, "")

DREDNAW = Pokemon(
    834, "Drednaw", 8, False,
    "", ("Water", "Rock"),
    90, 81, 79, 74,
    ((0, mv.ROCK_TOMB), (1, mv.BITE), (1, mv.CRUNCH), (1, mv.PROTECT),
     (1, mv.RAZOR_SHELL), (1, mv.ROCK_POLISH), (1, mv.TACKLE),
     (1, mv.WATER_GUN), (21, mv.HEADBUTT), (30, mv.COUNTER), (39, mv.JAW_LOCK),
     (48, mv.LIQUIDATION), (57, mv.BODY_SLAM), (66, mv.HEAD_SMASH)),
    None, 0, False, "")

CHEWTLE = Pokemon(
    833, "Chewtle", 8, False,
    "", ("Water",),
    50, 51, 44, 44,
    ((1, mv.TACKLE), (1, mv.WATER_GUN), (7, mv.BITE), (14, mv.PROTECT),
     (21, mv.HEADBUTT), (28, mv.COUNTER), (35, mv.JAW_LOCK),
     (42, mv.LIQUIDATION), (49, mv.BODY_SLAM)),
    DREDNAW, 22, True, "")

BOLTUND = Pokemon(
    836, "Boltund", 8, False,
    "", ("Electric",),
    69, 90, 60, 121,
    ((1, mv.BITE), (1, mv.ELECTRIFY), (1, mv.NUZZLE), (1, mv.TACKLE),
     (1, mv.TAIL_WHIP), (15, mv.ROAR), (20, mv.SPARK), (28, mv.CHARM),
     (34, mv.CRUNCH), (41, mv.CHARGE), (48, mv.WILD_CHARGE),
     (55, mv.PLAY_ROUGH), (62, mv.ELECTRIC_TERRAIN)),
    None, 0, False, "")

YAMPER = Pokemon(
    835, "Yamper", 8, False,
    "", ("Electric",),
    59, 42, 50, 26,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.NUZZLE), (10, mv.BITE),
     (15, mv.ROAR), (20, mv.SPARK), (26, mv.CHARM), (30, mv.CRUNCH),
     (35, mv.CHARGE), (40, mv.WILD_CHARGE), (45, mv.PLAY_ROUGH)),
    BOLTUND, 25, True, "")

COALOSSAL = Pokemon(
    839, "Coalossal", 8, False,
    "", ("Rock", "Fire"),
    110, 80, 105, 30,
    ((0, mv.TAR_SHOT), (1, mv.FLAME_CHARGE), (1, mv.RAPID_SPIN),
     (1, mv.SMACK_DOWN), (1, mv.SMOKESCREEN), (1, mv.TACKLE),
     (15, mv.ROCK_POLISH), (20, mv.ANCIENT_POWER), (27, mv.INCINERATE),
     (37, mv.STEALTH_ROCK), (45, mv.HEAT_CRASH), (54, mv.ROCK_BLAST),
     (63, mv.STONE_EDGE)),
    None, 0, False, "")

CARKOL = Pokemon(
    838, "Carkol", 8, False,
    "", ("Rock", "Fire"),
    80, 60, 80, 50,
    ((0, mv.FLAME_CHARGE), (1, mv.RAPID_SPIN), (1, mv.SMACK_DOWN),
     (1, mv.SMOKESCREEN), (1, mv.TACKLE), (15, mv.ROCK_POLISH),
     (20, mv.ANCIENT_POWER), (27, mv.INCINERATE), (35, mv.STEALTH_ROCK),
     (41, mv.HEAT_CRASH), (48, mv.ROCK_BLAST), (55, mv.STONE_EDGE)),
    COALOSSAL, 34, True, "")

ROLYCOLY = Pokemon(
    837, "Rolycoly", 8, False,
    "", ("Rock",),
    30, 40, 50, 30,
    ((1, mv.SMOKESCREEN), (1, mv.TACKLE), (5, mv.RAPID_SPIN),
     (10, mv.SMACK_DOWN), (15, mv.ROCK_POLISH), (20, mv.ANCIENT_POWER),
     (25, mv.INCINERATE), (30, mv.STEALTH_ROCK), (35, mv.HEAT_CRASH),
     (40, mv.ROCK_BLAST)),
    CARKOL, 18, True, "")


# --- generation 9 ---

HYDRAPPLE = Pokemon(
    1019, "Hydrapple", 9, False,
    "", ("Grass", "Dragon"),
    106, 100, 95, 44,
    ((0, mv.FICKLE_BEAM), (1, mv.ASTONISH), (1, mv.RECYCLE),
     (1, mv.SWEET_SCENT), (1, mv.WITHDRAW), (4, mv.DRAGON_TAIL),
     (8, mv.GROWTH), (12, mv.DRAGON_BREATH), (16, mv.PROTECT),
     (20, mv.BULLET_SEED), (28, mv.SYRUP_BOMB), (32, mv.DRAGON_PULSE),
     (36, mv.RECOVER), (40, mv.ENERGY_BALL), (44, mv.SUBSTITUTE),
     (54, mv.POWER_WHIP)),
    None, 0, False, "")

DIPPLIN = Pokemon(
    1011, "Dipplin", 9, False,
    "", ("Grass", "Dragon"),
    80, 87, 95, 40,
    ((0, mv.DOUBLE_HIT), (1, mv.ASTONISH), (1, mv.RECYCLE),
     (1, mv.SWEET_SCENT), (1, mv.WITHDRAW), (4, mv.DRAGON_TAIL),
     (8, mv.GROWTH), (12, mv.DRAGON_BREATH), (16, mv.PROTECT),
     (20, mv.BULLET_SEED), (28, mv.SYRUP_BOMB), (32, mv.DRAGON_PULSE),
     (36, mv.RECOVER), (40, mv.ENERGY_BALL), (44, mv.SUBSTITUTE)),
    HYDRAPPLE, 0, True, "level-up")


# --- generation 8 ---

APPLETUN = Pokemon(
    842, "Appletun", 8, False,
    "", ("Grass", "Dragon"),
    110, 92, 80, 30,
    ((0, mv.HEADBUTT), (1, mv.ASTONISH), (1, mv.GROWTH), (1, mv.RECYCLE),
     (1, mv.SWEET_SCENT), (1, mv.WITHDRAW), (4, mv.CURSE), (8, mv.STOMP),
     (12, mv.LEECH_SEED), (16, mv.PROTECT), (20, mv.BULLET_SEED),
     (24, mv.RECOVER), (28, mv.APPLE_ACID), (32, mv.BODY_SLAM),
     (36, mv.IRON_DEFENSE), (40, mv.DRAGON_PULSE), (44, mv.ENERGY_BALL)),
    DIPPLIN, 0, True, "Use Syrupy Apple")

FLAPPLE = Pokemon(
    841, "Flapple", 8, False,
    "", ("Grass", "Dragon"),
    70, 102, 70, 70,
    ((0, mv.WING_ATTACK), (1, mv.ASTONISH), (1, mv.GROWTH), (1, mv.RECYCLE),
     (1, mv.TWISTER), (1, mv.WITHDRAW), (4, mv.ACID_SPRAY), (8, mv.ACROBATICS),
     (12, mv.LEECH_SEED), (16, mv.PROTECT), (20, mv.DRAGON_BREATH),
     (24, mv.DRAGON_DANCE), (28, mv.DRAGON_PULSE), (32, mv.GRAV_APPLE),
     (36, mv.IRON_DEFENSE), (40, mv.FLY), (44, mv.DRAGON_RUSH)),
    APPLETUN, 0, True, "Use Sweet Apple")

APPLIN = Pokemon(
    840, "Applin", 8, False,
    "", ("Grass", "Dragon"),
    40, 40, 60, 20,
    ((1, mv.ASTONISH), (1, mv.WITHDRAW)),
    FLAPPLE, 0, True, "item:syrupy-apple")

SANDACONDA = Pokemon(
    844, "Sandaconda", 8, False,
    "", ("Ground",),
    72, 86, 97, 71,
    ((1, mv.BRUTAL_SWING), (1, mv.MINIMIZE), (1, mv.SAND_ATTACK), (1, mv.WRAP),
     (15, mv.BULLDOZE), (20, mv.HEADBUTT), (25, mv.GLARE), (30, mv.DIG),
     (35, mv.SANDSTORM), (42, mv.SLAM), (49, mv.COIL), (51, mv.SAND_TOMB)),
    None, 0, False, "")

SILICOBRA = Pokemon(
    843, "Silicobra", 8, False,
    "", ("Ground",),
    52, 46, 62, 46,
    ((1, mv.SAND_ATTACK), (1, mv.WRAP), (5, mv.MINIMIZE),
     (10, mv.BRUTAL_SWING), (15, mv.BULLDOZE), (20, mv.HEADBUTT),
     (25, mv.GLARE), (30, mv.DIG), (35, mv.SANDSTORM), (40, mv.SLAM),
     (45, mv.COIL), (50, mv.SAND_TOMB)),
    SANDACONDA, 36, True, "")

CRAMORANT = Pokemon(
    845, "Cramorant", 8, False,
    "", ("Flying", "Water"),
    70, 85, 75, 85,
    ((1, mv.PECK), (1, mv.SPIT_UP), (1, mv.STOCKPILE), (1, mv.SWALLOW),
     (7, mv.WATER_GUN), (14, mv.FURY_ATTACK), (21, mv.PLUCK), (28, mv.DIVE),
     (35, mv.DRILL_PECK), (42, mv.AMNESIA), (49, mv.THRASH),
     (56, mv.HYDRO_PUMP)),
    None, 0, False, "")

BARRASKEWDA = Pokemon(
    847, "Barraskewda", 8, False,
    "", ("Water",),
    61, 91, 55, 136,
    ((1, mv.AQUA_JET), (1, mv.BITE), (1, mv.FURY_ATTACK), (1, mv.PECK),
     (1, mv.THROAT_CHOP), (18, mv.AGILITY), (24, mv.DIVE),
     (32, mv.FOCUS_ENERGY), (40, mv.CRUNCH), (48, mv.LIQUIDATION),
     (56, mv.DOUBLE_EDGE)),
    None, 0, False, "")

ARROKUDA = Pokemon(
    846, "Arrokuda", 8, False,
    "", ("Water",),
    41, 51, 35, 66,
    ((1, mv.AQUA_JET), (1, mv.PECK), (6, mv.FURY_ATTACK), (12, mv.BITE),
     (18, mv.AGILITY), (24, mv.DIVE), (30, mv.FOCUS_ENERGY), (36, mv.CRUNCH),
     (42, mv.LIQUIDATION), (48, mv.DOUBLE_EDGE)),
    BARRASKEWDA, 26, True, "")

TOXTRICITY = Pokemon(
    849, "Toxtricity", 8, False,
    "", ("Electric", "Poison"),
    75, 106, 70, 75,
    ((0, mv.SPARK), (1, mv.ACID), (1, mv.ACID_SPRAY), (1, mv.BELCH),
     (1, mv.FLAIL), (1, mv.GROWL), (1, mv.LEER), (1, mv.NOBLE_ROAR),
     (1, mv.NUZZLE), (1, mv.TEARFUL_LOOK), (1, mv.THUNDER_SHOCK),
     (4, mv.CHARGE), (8, mv.SHOCK_WAVE), (12, mv.SCARY_FACE), (16, mv.TAUNT),
     (24, mv.SCREECH), (28, mv.SWAGGER), (32, mv.TOXIC), (36, mv.DISCHARGE),
     (40, mv.POISON_JAB), (44, mv.OVERDRIVE), (48, mv.BOOMBURST),
     (52, mv.SHIFT_GEAR)),
    None, 0, False, "")

TOXEL = Pokemon(
    848, "Toxel", 8, False,
    "", ("Electric", "Poison"),
    40, 46, 35, 40,
    ((1, mv.ACID), (1, mv.BELCH), (1, mv.FLAIL), (1, mv.GROWL), (1, mv.NUZZLE),
     (1, mv.TEARFUL_LOOK)),
    TOXTRICITY, 0, True,
    "Level 30")

CENTISKORCH = Pokemon(
    851, "Centiskorch", 8, False,
    "", ("Fire", "Bug"),
    100, 102, 77, 65,
    ((1, mv.BITE), (1, mv.EMBER), (1, mv.INFERNO), (1, mv.SMOKESCREEN),
     (1, mv.WRAP), (15, mv.FLAME_WHEEL), (20, mv.BUG_BITE), (25, mv.COIL),
     (32, mv.SLAM), (39, mv.FIRE_SPIN), (46, mv.CRUNCH), (53, mv.FIRE_LASH),
     (60, mv.LUNGE), (67, mv.BURN_UP)),
    None, 0, False, "")

SIZZLIPEDE = Pokemon(
    850, "Sizzlipede", 8, False,
    "", ("Fire", "Bug"),
    50, 57, 47, 45,
    ((1, mv.EMBER), (1, mv.SMOKESCREEN), (5, mv.WRAP), (10, mv.BITE),
     (15, mv.FLAME_WHEEL), (20, mv.BUG_BITE), (25, mv.COIL), (30, mv.SLAM),
     (35, mv.FIRE_SPIN), (40, mv.CRUNCH), (45, mv.FIRE_LASH), (50, mv.LUNGE),
     (55, mv.BURN_UP)),
    CENTISKORCH, 28, True, "")

GRAPPLOCT = Pokemon(
    853, "Grapploct", 8, False,
    "", ("Fighting",),
    80, 94, 85, 42,
    ((1, mv.BIND), (1, mv.FEINT), (1, mv.LEER), (1, mv.OCTAZOOKA),
     (1, mv.OCTOLOCK), (1, mv.ROCK_SMASH), (15, mv.DETECT),
     (20, mv.BRICK_BREAK), (25, mv.BULK_UP), (30, mv.SUBMISSION),
     (35, mv.TAUNT), (40, mv.REVERSAL), (45, mv.SUPERPOWER),
     (50, mv.TOPSY_TURVY)),
    None, 0, False, "")

CLOBBOPUS = Pokemon(
    852, "Clobbopus", 8, False,
    "", ("Fighting",),
    50, 59, 55, 32,
    ((1, mv.LEER), (1, mv.ROCK_SMASH), (5, mv.FEINT), (10, mv.BIND),
     (15, mv.DETECT), (20, mv.BRICK_BREAK), (25, mv.BULK_UP),
     (30, mv.SUBMISSION), (35, mv.TAUNT), (40, mv.REVERSAL),
     (45, mv.SUPERPOWER)),
    GRAPPLOCT, 0, True, "level-up")

POLTEAGEIST = Pokemon(
    855, "Polteageist", 8, False,
    "", ("Ghost",),
    60, 99, 89, 70,
    ((0, mv.TEATIME), (1, mv.AROMATIC_MIST), (1, mv.ASTONISH),
     (1, mv.MEGA_DRAIN), (1, mv.STRENGTH_SAP), (1, mv.WITHDRAW),
     (18, mv.PROTECT), (24, mv.SUCKER_PUNCH), (30, mv.SWEET_SCENT),
     (36, mv.GIGA_DRAIN), (42, mv.NASTY_PLOT), (48, mv.SHADOW_BALL),
     (54, mv.MEMENTO), (60, mv.SHELL_SMASH), (66, mv.CURSE)),
    None, 0, False, "")

SINISTEA = Pokemon(
    854, "Sinistea", 8, False,
    "", ("Ghost",),
    40, 59, 49, 50,
    ((1, mv.ASTONISH), (1, mv.WITHDRAW), (6, mv.AROMATIC_MIST),
     (12, mv.MEGA_DRAIN), (24, mv.SUCKER_PUNCH), (30, mv.SWEET_SCENT),
     (36, mv.GIGA_DRAIN), (42, mv.NASTY_PLOT), (48, mv.SHADOW_BALL),
     (54, mv.MEMENTO), (60, mv.SHELL_SMASH)),
    POLTEAGEIST, 0, True, "item:chipped-pot")

HATTERENE = Pokemon(
    858, "Hatterene", 8, False,
    "", ("Psychic", "Fairy"),
    57, 113, 99, 29,
    ((0, mv.PSYCHO_CUT), (1, mv.BRUTAL_SWING), (1, mv.CONFUSION),
     (1, mv.DISARMING_VOICE), (1, mv.LIFE_DEW), (1, mv.PLAY_NICE),
     (15, mv.AROMATIC_MIST), (20, mv.PSYBEAM), (25, mv.HEAL_PULSE),
     (30, mv.DAZZLING_GLEAM), (37, mv.CALM_MIND), (46, mv.PSYCHIC),
     (55, mv.HEALING_WISH), (64, mv.MAGIC_POWDER)),
    None, 0, False, "")

HATTREM = Pokemon(
    857, "Hattrem", 8, False,
    "", ("Psychic",),
    57, 63, 69, 49,
    ((0, mv.BRUTAL_SWING), (1, mv.CONFUSION), (1, mv.DISARMING_VOICE),
     (1, mv.LIFE_DEW), (1, mv.PLAY_NICE), (15, mv.AROMATIC_MIST),
     (20, mv.PSYBEAM), (25, mv.HEAL_PULSE), (30, mv.DAZZLING_GLEAM),
     (37, mv.CALM_MIND), (44, mv.PSYCHIC), (51, mv.HEALING_WISH)),
    HATTERENE, 42, True, "")

HATENNA = Pokemon(
    856, "Hatenna", 8, False,
    "", ("Psychic",),
    42, 43, 49, 39,
    ((1, mv.CONFUSION), (1, mv.PLAY_NICE), (5, mv.LIFE_DEW),
     (10, mv.DISARMING_VOICE), (15, mv.AROMATIC_MIST), (20, mv.PSYBEAM),
     (25, mv.HEAL_PULSE), (30, mv.DAZZLING_GLEAM), (35, mv.CALM_MIND),
     (40, mv.PSYCHIC), (45, mv.HEALING_WISH)),
    HATTREM, 32, True, "")

GRIMMSNARL = Pokemon(
    861, "Grimmsnarl", 8, False,
    "", ("Dark", "Fairy"),
    95, 107, 70, 60,
    ((0, mv.SPIRIT_BREAK), (1, mv.BITE), (1, mv.BULK_UP), (1, mv.CONFIDE),
     (1, mv.FAKE_OUT), (1, mv.FALSE_SURRENDER), (1, mv.FLATTER),
     (12, mv.FAKE_TEARS), (16, mv.ASSURANCE), (20, mv.SWAGGER),
     (24, mv.SUCKER_PUNCH), (28, mv.TORMENT), (35, mv.DARK_PULSE),
     (40, mv.NASTY_PLOT), (48, mv.PLAY_ROUGH), (56, mv.FOUL_PLAY),
     (64, mv.HAMMER_ARM)),
    None, 0, False, "")

MORGREM = Pokemon(
    860, "Morgrem", 8, False,
    "", ("Dark", "Fairy"),
    65, 67, 50, 70,
    ((0, mv.FALSE_SURRENDER), (1, mv.BITE), (1, mv.CONFIDE), (1, mv.FAKE_OUT),
     (1, mv.FLATTER), (12, mv.FAKE_TEARS), (16, mv.ASSURANCE),
     (20, mv.SWAGGER), (24, mv.SUCKER_PUNCH), (28, mv.TORMENT),
     (35, mv.DARK_PULSE), (40, mv.NASTY_PLOT), (46, mv.PLAY_ROUGH),
     (52, mv.FOUL_PLAY)),
    GRIMMSNARL, 42, True, "")

IMPIDIMP = Pokemon(
    859, "Impidimp", 8, False,
    "", ("Dark", "Fairy"),
    45, 50, 35, 50,
    ((1, mv.CONFIDE), (1, mv.FAKE_OUT), (4, mv.BITE), (8, mv.FLATTER),
     (12, mv.FAKE_TEARS), (16, mv.ASSURANCE), (20, mv.SWAGGER),
     (24, mv.SUCKER_PUNCH), (28, mv.TORMENT), (33, mv.DARK_PULSE),
     (36, mv.NASTY_PLOT), (40, mv.PLAY_ROUGH), (44, mv.FOUL_PLAY)),
    MORGREM, 32, True, "")

PERRSERKER = Pokemon(
    863, "Perrserker", 8, False,
    "", ("Steel",),
    70, 80, 80, 50,
    ((0, mv.IRON_HEAD), (1, mv.FAKE_OUT), (1, mv.GROWL), (1, mv.HONE_CLAWS),
     (1, mv.IRON_DEFENSE), (1, mv.METAL_BURST), (1, mv.SCRATCH),
     (12, mv.PAY_DAY), (16, mv.METAL_CLAW), (20, mv.TAUNT), (24, mv.SWAGGER),
     (31, mv.FURY_SWIPES), (36, mv.SCREECH), (42, mv.SLASH),
     (48, mv.METAL_SOUND), (54, mv.THRASH)),
    None, 0, False, "")

RUNERIGUS = Pokemon(
    867, "Runerigus", 8, False,
    "", ("Ground", "Ghost"),
    58, 72, 125, 30,
    ((1, mv.ASTONISH), (1, mv.HAZE), (1, mv.NIGHT_SHADE), (1, mv.PROTECT),
     (1, mv.SCARY_FACE), (1, mv.SHADOW_CLAW), (12, mv.DISABLE),
     (16, mv.BRUTAL_SWING), (20, mv.CRAFTY_SHIELD), (24, mv.HEX),
     (28, mv.MEAN_LOOK), (32, mv.SLAM), (38, mv.CURSE), (44, mv.SHADOW_BALL),
     (50, mv.EARTHQUAKE), (56, mv.GUARD_SPLIT), (56, mv.POWER_SPLIT),
     (62, mv.DESTINY_BOND)),
    None, 0, False, "")

ALCREMIE = Pokemon(
    869, "Alcremie", 8, False,
    "", ("Fairy",),
    65, 85, 98, 64,
    ((0, mv.DECORATE), (1, mv.AROMATIC_MIST), (1, mv.SWEET_KISS),
     (1, mv.SWEET_SCENT), (1, mv.TACKLE), (15, mv.DRAINING_KISS),
     (20, mv.CHARM), (25, mv.ATTRACT), (30, mv.ACID_ARMOR),
     (35, mv.DAZZLING_GLEAM), (40, mv.RECOVER), (45, mv.MISTY_TERRAIN),
     (50, mv.ENTRAINMENT)),
    None, 0, False, "")

MILCERY = Pokemon(
    868, "Milcery", 8, False,
    "", ("Fairy",),
    45, 45, 50, 34,
    ((1, mv.AROMATIC_MIST), (1, mv.TACKLE), (5, mv.SWEET_KISS),
     (10, mv.SWEET_SCENT), (15, mv.DRAINING_KISS), (20, mv.CHARM),
     (25, mv.ATTRACT), (30, mv.ACID_ARMOR), (35, mv.DAZZLING_GLEAM),
     (40, mv.RECOVER), (45, mv.MISTY_TERRAIN), (50, mv.ENTRAINMENT)),
    ALCREMIE, 0, True, "spin")

FALINKS = Pokemon(
    870, "Falinks", 8, False,
    "", ("Fighting",),
    65, 85, 80, 75,
    ((1, mv.PROTECT), (1, mv.TACKLE), (5, mv.ROCK_SMASH),
     (10, mv.FOCUS_ENERGY), (15, mv.HEADBUTT), (20, mv.BULK_UP),
     (25, mv.ENDURE), (30, mv.REVERSAL), (35, mv.FIRST_IMPRESSION),
     (40, mv.NO_RETREAT), (45, mv.IRON_DEFENSE), (50, mv.CLOSE_COMBAT),
     (55, mv.MEGAHORN), (60, mv.COUNTER)),
    None, 0, False, "")

PINCURCHIN = Pokemon(
    871, "Pincurchin", 8, False,
    "", ("Electric",),
    48, 96, 90, 15,
    ((1, mv.PECK), (1, mv.THUNDER_SHOCK), (5, mv.WATER_GUN), (10, mv.CHARGE),
     (15, mv.FURY_ATTACK), (20, mv.SPARK), (25, mv.BUBBLE_BEAM),
     (30, mv.RECOVER), (35, mv.CURSE), (40, mv.ELECTRIC_TERRAIN),
     (45, mv.POISON_JAB), (50, mv.ZING_ZAP), (55, mv.ACUPRESSURE),
     (60, mv.DISCHARGE)),
    None, 0, False, "")

FROSMOTH = Pokemon(
    873, "Frosmoth", 8, False,
    "", ("Ice", "Bug"),
    70, 95, 75, 65,
    ((0, mv.ICY_WIND), (1, mv.ATTRACT), (1, mv.HELPING_HAND),
     (1, mv.POWDER_SNOW), (1, mv.STRUGGLE_BUG), (4, mv.STUN_SPORE),
     (8, mv.INFESTATION), (12, mv.MIST), (16, mv.DEFOG),
     (21, mv.FEATHER_DANCE), (24, mv.AURORA_BEAM), (28, mv.SNOWSCAPE),
     (32, mv.BUG_BUZZ), (36, mv.AURORA_VEIL), (40, mv.BLIZZARD),
     (44, mv.TAILWIND), (48, mv.WIDE_GUARD), (52, mv.QUIVER_DANCE)),
    None, 0, False, "")

SNOM = Pokemon(
    872, "Snom", 8, False,
    "", ("Ice", "Bug"),
    30, 35, 32, 20,
    ((1, mv.POWDER_SNOW), (1, mv.STRUGGLE_BUG)),
    FROSMOTH, 0, True, "happiness")

STONJOURNER = Pokemon(
    874, "Stonjourner", 8, False,
    "", ("Rock",),
    100, 72, 77, 70,
    ((1, mv.BLOCK), (1, mv.ROCK_THROW), (6, mv.ROCK_POLISH),
     (12, mv.ROCK_TOMB), (18, mv.GRAVITY), (24, mv.STOMP),
     (30, mv.STEALTH_ROCK), (36, mv.ROCK_SLIDE), (42, mv.BODY_SLAM),
     (48, mv.WIDE_GUARD), (54, mv.HEAVY_SLAM), (60, mv.STONE_EDGE),
     (66, mv.MEGA_KICK)),
    None, 0, False, "")

EISCUE = Pokemon(
    875, "Eiscue", 8, False,
    "", ("Ice",),
    75, 72, 100, 50,
    ((1, mv.POWDER_SNOW), (1, mv.TACKLE), (6, mv.MIST), (12, mv.WEATHER_BALL),
     (18, mv.ICY_WIND), (24, mv.HEADBUTT), (30, mv.AMNESIA),
     (36, mv.FREEZE_DRY), (42, mv.SNOWSCAPE), (48, mv.AURORA_VEIL),
     (54, mv.SURF), (60, mv.BLIZZARD)),
    None, 0, False, "")

INDEEDEE = Pokemon(
    876, "Indeedee", 8, False,
    "", ("Psychic", "Normal"),
    60, 85, 75, 95,
    ((1, mv.PLAY_NICE), (1, mv.STORED_POWER), (5, mv.ENCORE),
     (10, mv.DISARMING_VOICE), (15, mv.PSYBEAM), (20, mv.HELPING_HAND),
     (25, mv.AFTER_YOU), (30, mv.HEALING_WISH), (35, mv.PSYCHIC),
     (40, mv.CALM_MIND), (45, mv.POWER_SPLIT), (50, mv.PSYCHIC_TERRAIN),
     (55, mv.LAST_RESORT)),
    None, 0, False, "")

MORPEKO = Pokemon(
    877, "Morpeko", 8, False,
    "", ("Electric", "Dark"),
    58, 82, 58, 97,
    ((1, mv.TAIL_WHIP), (1, mv.THUNDER_SHOCK), (5, mv.LEER),
     (10, mv.POWER_TRIP), (15, mv.QUICK_ATTACK), (20, mv.FLATTER),
     (25, mv.BITE), (30, mv.SPARK), (35, mv.TORMENT), (40, mv.AGILITY),
     (45, mv.BULLET_SEED), (50, mv.CRUNCH), (55, mv.AURA_WHEEL),
     (60, mv.THRASH)),
    None, 0, False, "")

COPPERAJAH = Pokemon(
    879, "Copperajah", 8, False,
    "", ("Steel",),
    122, 105, 69, 30,
    ((0, mv.HEAVY_SLAM), (1, mv.GROWL), (1, mv.ROCK_SMASH), (1, mv.ROLLOUT),
     (1, mv.TACKLE), (15, mv.BULLDOZE), (20, mv.STOMP), (25, mv.IRON_DEFENSE),
     (30, mv.DIG), (37, mv.STRENGTH), (44, mv.IRON_HEAD), (51, mv.PLAY_ROUGH),
     (58, mv.HIGH_HORSEPOWER), (65, mv.SUPERPOWER)),
    None, 0, False, "")

CUFANT = Pokemon(
    878, "Cufant", 8, False,
    "", ("Steel",),
    72, 60, 49, 40,
    ((1, mv.GROWL), (1, mv.TACKLE), (5, mv.ROLLOUT), (10, mv.ROCK_SMASH),
     (15, mv.BULLDOZE), (20, mv.STOMP), (25, mv.IRON_DEFENSE), (30, mv.DIG),
     (35, mv.STRENGTH), (40, mv.IRON_HEAD), (45, mv.PLAY_ROUGH),
     (50, mv.HIGH_HORSEPOWER), (55, mv.SUPERPOWER)),
    COPPERAJAH, 34, True, "")

DRACOZOLT = Pokemon(
    880, "Dracozolt", 8, False,
    "", ("Electric", "Dragon"),
    90, 90, 80, 75,
    ((1, mv.TACKLE), (1, mv.THUNDER_SHOCK), (7, mv.CHARGE),
     (14, mv.AERIAL_ACE), (21, mv.ANCIENT_POWER), (28, mv.PLUCK),
     (35, mv.DRAGON_TAIL), (42, mv.STOMP), (49, mv.SLAM), (56, mv.DISCHARGE),
     (63, mv.BOLT_BEAK), (70, mv.DRAGON_PULSE), (77, mv.DRAGON_RUSH)),
    None, 0, False, "")

ARCTOZOLT = Pokemon(
    881, "Arctozolt", 8, False,
    "", ("Electric", "Ice"),
    90, 95, 85, 55,
    ((1, mv.POWDER_SNOW), (1, mv.THUNDER_SHOCK), (7, mv.CHARGE),
     (14, mv.ECHOED_VOICE), (21, mv.ANCIENT_POWER), (28, mv.PLUCK),
     (35, mv.AVALANCHE), (42, mv.FREEZE_DRY), (49, mv.SLAM),
     (56, mv.DISCHARGE), (63, mv.BOLT_BEAK), (70, mv.ICICLE_CRASH),
     (77, mv.BLIZZARD)),
    None, 0, False, "")

DRACOVISH = Pokemon(
    882, "Dracovish", 8, False,
    "", ("Water", "Dragon"),
    90, 80, 90, 75,
    ((1, mv.TACKLE), (1, mv.WATER_GUN), (7, mv.PROTECT), (14, mv.BRUTAL_SWING),
     (21, mv.ANCIENT_POWER), (28, mv.BITE), (35, mv.DRAGON_BREATH),
     (42, mv.STOMP), (49, mv.SUPER_FANG), (56, mv.CRUNCH),
     (63, mv.FISHIOUS_REND), (70, mv.DRAGON_PULSE), (77, mv.DRAGON_RUSH)),
    None, 0, False, "")

ARCTOVISH = Pokemon(
    883, "Arctovish", 8, False,
    "", ("Water", "Ice"),
    90, 85, 95, 55,
    ((1, mv.POWDER_SNOW), (1, mv.WATER_GUN), (7, mv.PROTECT),
     (14, mv.ICY_WIND), (21, mv.ANCIENT_POWER), (28, mv.BITE),
     (35, mv.AURORA_VEIL), (42, mv.FREEZE_DRY), (49, mv.SUPER_FANG),
     (56, mv.CRUNCH), (63, mv.FISHIOUS_REND), (70, mv.ICICLE_CRASH),
     (77, mv.BLIZZARD)),
    None, 0, False, "")


# --- generation 9 ---

ARCHALUDON = Pokemon(
    1018, "Archaludon", 9, False,
    "", ("Steel", "Dragon"),
    90, 115, 97, 85,
    ((0, mv.ELECTRO_SHOT), (1, mv.LEER), (1, mv.METAL_CLAW),
     (6, mv.ROCK_SMASH), (12, mv.HONE_CLAWS), (18, mv.METAL_SOUND),
     (24, mv.BREAKING_SWIPE), (30, mv.DRAGON_TAIL), (36, mv.IRON_DEFENSE),
     (42, mv.FOCUS_ENERGY), (48, mv.DRAGON_CLAW), (54, mv.FLASH_CANNON),
     (60, mv.METAL_BURST), (66, mv.HYPER_BEAM)),
    None, 0, False, "")


# --- generation 8 ---

DURALUDON = Pokemon(
    884, "Duraludon", 8, False,
    "", ("Steel", "Dragon"),
    70, 107, 82, 85,
    ((1, mv.LEER), (1, mv.METAL_CLAW), (6, mv.ROCK_SMASH), (12, mv.HONE_CLAWS),
     (18, mv.METAL_SOUND), (24, mv.BREAKING_SWIPE), (30, mv.DRAGON_TAIL),
     (36, mv.IRON_DEFENSE), (42, mv.FOCUS_ENERGY), (48, mv.DRAGON_CLAW),
     (54, mv.FLASH_CANNON), (60, mv.METAL_BURST), (66, mv.HYPER_BEAM)),
    ARCHALUDON, 0, True, "item:metal-alloy")

DRAGAPULT = Pokemon(
    887, "Dragapult", 8, False,
    "", ("Dragon", "Ghost"),
    88, 110, 75, 142,
    ((0, mv.DRAGON_DARTS), (1, mv.ASTONISH), (1, mv.BITE),
     (1, mv.DRAGON_BREATH), (1, mv.INFESTATION), (1, mv.QUICK_ATTACK),
     (6, mv.LOCK_ON), (12, mv.ASSURANCE), (18, mv.HEX), (24, mv.AGILITY),
     (30, mv.DOUBLE_HIT), (36, mv.U_TURN), (42, mv.DRAGON_DANCE),
     (48, mv.PHANTOM_FORCE), (54, mv.TAKE_DOWN), (63, mv.DRAGON_RUSH),
     (70, mv.DOUBLE_EDGE), (78, mv.LAST_RESORT)),
    None, 0, False, "")

DRAKLOAK = Pokemon(
    886, "Drakloak", 8, False,
    "", ("Dragon", "Ghost"),
    68, 70, 50, 102,
    ((0, mv.DRAGON_PULSE), (1, mv.ASTONISH), (1, mv.BITE), (1, mv.INFESTATION),
     (1, mv.QUICK_ATTACK), (6, mv.LOCK_ON), (12, mv.ASSURANCE), (18, mv.HEX),
     (24, mv.AGILITY), (30, mv.DOUBLE_HIT), (36, mv.U_TURN),
     (42, mv.DRAGON_DANCE), (48, mv.PHANTOM_FORCE), (54, mv.TAKE_DOWN),
     (61, mv.DRAGON_RUSH), (66, mv.DOUBLE_EDGE), (72, mv.LAST_RESORT)),
    DRAGAPULT, 60, True, "")

DREEPY = Pokemon(
    885, "Dreepy", 8, False,
    "", ("Dragon", "Ghost"),
    28, 50, 30, 82,
    ((1, mv.ASTONISH), (1, mv.BITE), (1, mv.INFESTATION),
     (1, mv.QUICK_ATTACK)),
    DRAKLOAK, 50, True, "")

ZACIAN = Pokemon(
    888, "Zacian", 8, False,
    "", ("Fairy",),
    92, 105, 115, 138,
    ((1, mv.BITE), (1, mv.HOWL), (1, mv.METAL_CLAW), (1, mv.QUICK_ATTACK),
     (1, mv.QUICK_GUARD), (1, mv.SACRED_SWORD), (11, mv.SLASH),
     (22, mv.SWORDS_DANCE), (33, mv.IRON_HEAD), (44, mv.NOBLE_ROAR),
     (55, mv.CRUNCH), (66, mv.MOONBLAST), (77, mv.CLOSE_COMBAT),
     (88, mv.GIGA_IMPACT)),
    None, 0, False, "")

ZAMAZENTA = Pokemon(
    889, "Zamazenta", 8, False,
    "", ("Fighting",),
    92, 105, 115, 138,
    ((1, mv.BITE), (1, mv.HOWL), (1, mv.METAL_CLAW), (1, mv.QUICK_ATTACK),
     (1, mv.WIDE_GUARD), (11, mv.SLASH), (22, mv.IRON_DEFENSE),
     (33, mv.IRON_HEAD), (44, mv.METAL_BURST), (55, mv.CRUNCH),
     (66, mv.MOONBLAST), (77, mv.CLOSE_COMBAT), (88, mv.GIGA_IMPACT)),
    None, 0, False, "")

ETERNATUS = Pokemon(
    890, "Eternatus", 8, False,
    "", ("Poison", "Dragon"),
    140, 115, 95, 130,
    ((1, mv.AGILITY), (1, mv.CONFUSE_RAY), (1, mv.DRAGON_TAIL),
     (1, mv.POISON_TAIL), (8, mv.TOXIC), (16, mv.VENOSHOCK),
     (24, mv.DRAGON_DANCE), (32, mv.CROSS_POISON), (40, mv.DRAGON_PULSE),
     (48, mv.FLAMETHROWER), (56, mv.DYNAMAX_CANNON), (64, mv.COSMIC_POWER),
     (72, mv.RECOVER), (80, mv.HYPER_BEAM), (88, mv.OUTRAGE)),
    None, 0, False, "")

URSHIFU = Pokemon(
    892, "Urshifu", 8, False,
    "", ("Fighting", "Dark"),
    100, 96, 80, 97,
    ((0, mv.WICKED_BLOW), (1, mv.ENDURE), (1, mv.FOCUS_ENERGY), (1, mv.LEER),
     (1, mv.ROCK_SMASH), (1, mv.SUCKER_PUNCH), (12, mv.AERIAL_ACE),
     (16, mv.SCARY_FACE), (20, mv.HEADBUTT), (24, mv.BRICK_BREAK),
     (28, mv.DETECT), (32, mv.BULK_UP), (36, mv.IRON_HEAD),
     (40, mv.DYNAMIC_PUNCH), (44, mv.COUNTER), (48, mv.CLOSE_COMBAT),
     (52, mv.FOCUS_PUNCH)),
    None, 0, False, "")

KUBFU = Pokemon(
    891, "Kubfu", 8, False,
    "", ("Fighting",),
    60, 71, 55, 72,
    ((1, mv.LEER), (1, mv.ROCK_SMASH), (4, mv.ENDURE), (8, mv.FOCUS_ENERGY),
     (12, mv.AERIAL_ACE), (16, mv.SCARY_FACE), (20, mv.HEADBUTT),
     (24, mv.BRICK_BREAK), (28, mv.DETECT), (32, mv.BULK_UP),
     (36, mv.IRON_HEAD), (40, mv.DYNAMIC_PUNCH), (44, mv.COUNTER),
     (48, mv.CLOSE_COMBAT), (52, mv.FOCUS_PUNCH)),
    URSHIFU, 0, True, "item:scroll-of-waters")

ZARUDE = Pokemon(
    893, "Zarude", 8, False,
    "", ("Dark", "Grass"),
    105, 95, 100, 105,
    ((1, mv.BIND), (1, mv.SCRATCH), (6, mv.LEER), (12, mv.VINE_WHIP),
     (18, mv.GROWTH), (24, mv.FURY_SWIPES), (30, mv.SCARY_FACE),
     (36, mv.GRASS_KNOT), (42, mv.BITE), (48, mv.U_TURN), (54, mv.SWAGGER),
     (60, mv.ENERGY_BALL), (66, mv.SYNTHESIS), (72, mv.HAMMER_ARM),
     (78, mv.THRASH), (84, mv.POWER_WHIP), (90, mv.JUNGLE_HEALING)),
    None, 0, False, "")

REGIELEKI = Pokemon(
    894, "Regieleki", 8, False,
    "", ("Electric",),
    80, 100, 50, 200,
    ((1, mv.RAPID_SPIN), (1, mv.THUNDER_SHOCK), (6, mv.ELECTROWEB),
     (12, mv.ANCIENT_POWER), (18, mv.SHOCK_WAVE), (24, mv.THUNDER_WAVE),
     (30, mv.EXTREME_SPEED), (36, mv.THUNDER_CAGE), (42, mv.THUNDERBOLT),
     (48, mv.MAGNET_RISE), (54, mv.THRASH), (60, mv.LOCK_ON),
     (66, mv.ZAP_CANNON), (72, mv.HYPER_BEAM), (78, mv.EXPLOSION)),
    None, 0, False, "")

REGIDRAGO = Pokemon(
    895, "Regidrago", 8, False,
    "", ("Dragon",),
    200, 100, 50, 80,
    ((1, mv.TWISTER), (6, mv.BITE), (12, mv.ANCIENT_POWER),
     (18, mv.DRAGON_BREATH), (30, mv.CRUNCH), (36, mv.DRAGON_CLAW),
     (42, mv.HAMMER_ARM), (48, mv.DRAGON_DANCE), (54, mv.THRASH),
     (60, mv.FOCUS_ENERGY), (66, mv.DRAGON_ENERGY), (72, mv.HYPER_BEAM),
     (78, mv.EXPLOSION)),
    None, 0, False, "")

GLASTRIER = Pokemon(
    896, "Glastrier", 8, False,
    "", ("Ice",),
    100, 105, 120, 30,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (6, mv.DOUBLE_KICK),
     (12, mv.AVALANCHE), (18, mv.STOMP), (24, mv.TORMENT), (30, mv.MIST),
     (36, mv.ICICLE_CRASH), (42, mv.TAKE_DOWN), (48, mv.IRON_DEFENSE),
     (54, mv.THRASH), (60, mv.TAUNT), (66, mv.DOUBLE_EDGE),
     (72, mv.SWORDS_DANCE)),
    None, 0, False, "")

SPECTRIER = Pokemon(
    897, "Spectrier", 8, False,
    "", ("Ghost",),
    100, 105, 70, 130,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (6, mv.DOUBLE_KICK), (12, mv.HEX),
     (18, mv.STOMP), (24, mv.CONFUSE_RAY), (30, mv.HAZE), (36, mv.SHADOW_BALL),
     (42, mv.TAKE_DOWN), (48, mv.AGILITY), (54, mv.THRASH), (60, mv.DISABLE),
     (66, mv.DOUBLE_EDGE), (72, mv.NASTY_PLOT)),
    None, 0, False, "")

CALYREX = Pokemon(
    898, "Calyrex", 8, False,
    "", ("Psychic", "Grass"),
    100, 80, 80, 80,
    ((1, mv.CONFUSION), (1, mv.GROWTH), (1, mv.MEGA_DRAIN), (1, mv.POUND),
     (8, mv.LIFE_DEW), (16, mv.GIGA_DRAIN), (24, mv.PSYSHOCK),
     (32, mv.HELPING_HAND), (40, mv.GRASSY_TERRAIN), (40, mv.PSYCHIC_TERRAIN),
     (48, mv.ENERGY_BALL), (56, mv.PSYCHIC), (64, mv.LEECH_SEED),
     (72, mv.HEAL_PULSE), (80, mv.SOLAR_BEAM), (88, mv.FUTURE_SIGHT)),
    None, 0, False, "")

ENAMORUS = Pokemon(
    905, "Enamorus", 8, False,
    "", ("Fairy", "Flying"),
    74, 125, 75, 106,
    ((1, mv.ASTONISH), (1, mv.FAIRY_WIND), (5, mv.TORMENT), (10, mv.FLATTER),
     (15, mv.TWISTER), (20, mv.DRAINING_KISS), (25, mv.IRON_DEFENSE),
     (30, mv.IMPRISON), (35, mv.MYSTICAL_FIRE), (40, mv.DAZZLING_GLEAM),
     (45, mv.EXTRASENSORY), (50, mv.UPROAR), (55, mv.SUPERPOWER),
     (60, mv.HEALING_WISH), (65, mv.MOONBLAST), (70, mv.OUTRAGE),
     (75, mv.SPRINGTIDE_STORM)),
    None, 0, False, "")


# --- generation 9 ---

MEOWSCARADA = Pokemon(
    908, "Meowscarada", 9, True,
    "Flora", ("Grass", "Dark"),
    76, 95, 70, 123,
    ((0, mv.FLOWER_TRICK), (1, mv.LEAFAGE), (1, mv.SCRATCH), (1, mv.TAIL_WHIP),
     (7, mv.BITE), (10, mv.HONE_CLAWS), (13, mv.MAGICAL_LEAF),
     (15, mv.QUICK_ATTACK), (20, mv.SEED_BOMB), (24, mv.U_TURN),
     (29, mv.WORRY_SEED), (33, mv.SLASH), (38, mv.NIGHT_SLASH),
     (42, mv.ENERGY_BALL), (47, mv.PLAY_ROUGH), (52, mv.KNOCK_OFF),
     (58, mv.GRASSY_TERRAIN), (64, mv.LEAF_STORM)),
    None, 0, False, "")

FLORAGATO = Pokemon(
    907, "Floragato", 9, True,
    "Flora", ("Grass",),
    61, 70, 63, 83,
    ((1, mv.LEAFAGE), (1, mv.SCRATCH), (1, mv.TAIL_WHIP), (7, mv.BITE),
     (10, mv.HONE_CLAWS), (13, mv.MAGICAL_LEAF), (15, mv.QUICK_ATTACK),
     (20, mv.SEED_BOMB), (24, mv.U_TURN), (28, mv.WORRY_SEED), (33, mv.SLASH),
     (38, mv.ENERGY_BALL), (42, mv.PLAY_ROUGH), (46, mv.LEAF_STORM)),
    MEOWSCARADA, 36, True, "")

SPRIGATITO = Pokemon(
    906, "Sprigatito", 9, True,
    "Flora", ("Grass",),
    40, 53, 49, 65,
    ((1, mv.LEAFAGE), (1, mv.SCRATCH), (1, mv.TAIL_WHIP), (7, mv.BITE),
     (10, mv.HONE_CLAWS), (13, mv.MAGICAL_LEAF), (15, mv.QUICK_ATTACK),
     (17, mv.SEED_BOMB), (21, mv.U_TURN), (25, mv.WORRY_SEED), (28, mv.SLASH),
     (32, mv.ENERGY_BALL), (36, mv.PLAY_ROUGH)),
    FLORAGATO, 16, True, "")

SKELEDIRGE = Pokemon(
    911, "Skeledirge", 9, True,
    "Flame", ("Fire", "Ghost"),
    104, 92, 87, 66,
    ((0, mv.TORCH_SONG), (1, mv.EMBER), (1, mv.LEER), (1, mv.TACKLE),
     (7, mv.LICK), (10, mv.ROUND), (12, mv.SCARY_FACE), (15, mv.BITE),
     (17, mv.INCINERATE), (24, mv.SNARL), (28, mv.ROAR), (32, mv.FLAMETHROWER),
     (38, mv.SHADOW_BALL), (42, mv.HYPER_VOICE), (47, mv.HEX),
     (47, mv.WILL_O_WISP), (58, mv.FIRE_BLAST), (64, mv.OVERHEAT)),
    None, 0, False, "")

CROCALOR = Pokemon(
    910, "Crocalor", 9, True,
    "Flame", ("Fire",),
    81, 72, 68, 49,
    ((1, mv.EMBER), (1, mv.LEER), (1, mv.TACKLE), (7, mv.LICK), (10, mv.ROUND),
     (12, mv.BITE), (15, mv.YAWN), (17, mv.INCINERATE), (24, mv.SNARL),
     (28, mv.ROAR), (32, mv.FLAMETHROWER), (38, mv.HYPER_VOICE),
     (42, mv.WILL_O_WISP), (47, mv.FIRE_BLAST)),
    SKELEDIRGE, 36, True, "")

FUECOCO = Pokemon(
    909, "Fuecoco", 9, True,
    "Flame", ("Fire",),
    67, 54, 49, 36,
    ((1, mv.EMBER), (1, mv.LEER), (1, mv.TACKLE), (7, mv.ROUND), (12, mv.BITE),
     (15, mv.INCINERATE), (17, mv.YAWN), (21, mv.SNARL), (25, mv.ROAR),
     (28, mv.FLAMETHROWER), (32, mv.HYPER_VOICE), (36, mv.FIRE_BLAST)),
    CROCALOR, 16, True, "")

QUAQUAVAL = Pokemon(
    914, "Quaquaval", 9, True,
    "Aqua", ("Water", "Fighting"),
    85, 102, 77, 85,
    ((0, mv.AQUA_STEP), (1, mv.DOUBLE_HIT), (1, mv.GROWL), (1, mv.POUND),
     (1, mv.WATER_GUN), (7, mv.WORK_UP), (10, mv.WING_ATTACK),
     (13, mv.AQUA_JET), (17, mv.LOW_SWEEP), (17, mv.WATER_PULSE),
     (21, mv.AQUA_CUTTER), (27, mv.AIR_SLASH), (32, mv.FOCUS_ENERGY),
     (38, mv.MEGA_KICK), (43, mv.ACROBATICS), (47, mv.LIQUIDATION),
     (52, mv.FEATHER_DANCE), (58, mv.CLOSE_COMBAT), (64, mv.WAVE_CRASH)),
    None, 0, False, "")

QUAXWELL = Pokemon(
    913, "Quaxwell", 9, True,
    "Aqua", ("Water",),
    70, 75, 62, 65,
    ((1, mv.DOUBLE_HIT), (1, mv.GROWL), (1, mv.POUND), (1, mv.WATER_GUN),
     (7, mv.WORK_UP), (10, mv.WING_ATTACK), (13, mv.AQUA_JET),
     (17, mv.WATER_PULSE), (19, mv.LOW_SWEEP), (23, mv.AQUA_CUTTER),
     (27, mv.AIR_SLASH), (32, mv.FOCUS_ENERGY), (38, mv.ACROBATICS),
     (43, mv.LIQUIDATION), (48, mv.FEATHER_DANCE)),
    QUAQUAVAL, 36, True, "")

QUAXLY = Pokemon(
    912, "Quaxly", 9, True,
    "Aqua", ("Water",),
    55, 57, 45, 50,
    ((1, mv.GROWL), (1, mv.POUND), (1, mv.WATER_GUN), (7, mv.WORK_UP),
     (10, mv.WING_ATTACK), (13, mv.AQUA_JET), (17, mv.DOUBLE_HIT),
     (21, mv.AQUA_CUTTER), (24, mv.AIR_SLASH), (28, mv.FOCUS_ENERGY),
     (31, mv.ACROBATICS), (35, mv.LIQUIDATION)),
    QUAXWELL, 16, True, "")

OINKOLOGNE = Pokemon(
    916, "Oinkologne", 9, False,
    "", ("Normal",),
    110, 79, 77, 65,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.DISARMING_VOICE),
     (8, mv.ECHOED_VOICE), (12, mv.MUD_SHOT), (15, mv.COVET), (17, mv.DIG),
     (23, mv.HEADBUTT), (26, mv.TAKE_DOWN), (27, mv.YAWN), (34, mv.WORK_UP),
     (38, mv.UPROAR), (42, mv.DOUBLE_EDGE), (48, mv.EARTH_POWER),
     (54, mv.BELCH)),
    None, 0, False, "")

LECHONK = Pokemon(
    915, "Lechonk", 9, False,
    "", ("Normal",),
    54, 40, 42, 35,
    ((1, mv.TACKLE), (1, mv.TAIL_WHIP), (5, mv.DISARMING_VOICE),
     (8, mv.ECHOED_VOICE), (12, mv.MUD_SHOT), (15, mv.COVET), (17, mv.DIG),
     (21, mv.HEADBUTT), (24, mv.YAWN), (27, mv.TAKE_DOWN), (30, mv.WORK_UP),
     (32, mv.UPROAR), (35, mv.DOUBLE_EDGE)),
    OINKOLOGNE, 18, True, "")

SPIDOPS = Pokemon(
    918, "Spidops", 9, False,
    "", ("Bug",),
    60, 65, 89, 35,
    ((0, mv.SILK_TRAP), (1, mv.STRING_SHOT), (1, mv.TACKLE),
     (5, mv.STRUGGLE_BUG), (8, mv.ASSURANCE), (11, mv.FEINT),
     (14, mv.BUG_BITE), (19, mv.BLOCK), (24, mv.COUNTER), (28, mv.HEADBUTT),
     (33, mv.STICKY_WEB), (37, mv.GASTRO_ACID), (41, mv.CIRCLE_THROW),
     (45, mv.THROAT_CHOP), (49, mv.SKITTER_SMACK)),
    None, 0, False, "")

TAROUNTULA = Pokemon(
    917, "Tarountula", 9, False,
    "", ("Bug",),
    35, 35, 42, 20,
    ((1, mv.STRING_SHOT), (1, mv.TACKLE), (5, mv.STRUGGLE_BUG),
     (8, mv.ASSURANCE), (11, mv.FEINT), (14, mv.BUG_BITE), (18, mv.BLOCK),
     (22, mv.COUNTER), (25, mv.HEADBUTT), (29, mv.STICKY_WEB),
     (33, mv.GASTRO_ACID), (36, mv.CIRCLE_THROW), (40, mv.THROAT_CHOP),
     (44, mv.SKITTER_SMACK)),
    SPIDOPS, 15, True, "")

LOKIX = Pokemon(
    920, "Lokix", 9, False,
    "", ("Bug", "Dark"),
    71, 77, 66, 92,
    ((0, mv.LUNGE), (1, mv.DETECT), (1, mv.LEER), (1, mv.LOW_KICK),
     (1, mv.TACKLE), (4, mv.STRUGGLE_BUG), (6, mv.ASTONISH), (9, mv.ASSURANCE),
     (11, mv.DOUBLE_KICK), (14, mv.SCREECH), (18, mv.ENDURE),
     (22, mv.BUG_BITE), (28, mv.FEINT), (32, mv.AGILITY), (36, mv.THROAT_CHOP),
     (40, mv.SUCKER_PUNCH), (44, mv.FIRST_IMPRESSION), (48, mv.BOUNCE),
     (53, mv.AXE_KICK)),
    None, 0, False, "")

NYMBLE = Pokemon(
    919, "Nymble", 9, False,
    "", ("Bug",),
    33, 33, 32, 45,
    ((1, mv.LEER), (1, mv.TACKLE), (4, mv.STRUGGLE_BUG), (6, mv.ASTONISH),
     (9, mv.ASSURANCE), (11, mv.DOUBLE_KICK), (14, mv.SCREECH),
     (18, mv.ENDURE), (22, mv.BUG_BITE), (26, mv.FEINT), (30, mv.AGILITY),
     (38, mv.SUCKER_PUNCH), (41, mv.FIRST_IMPRESSION)),
    LOKIX, 24, True, "")

PAWMOT = Pokemon(
    923, "Pawmot", 9, False,
    "", ("Electric", "Fighting"),
    70, 92, 65, 105,
    ((0, mv.REVIVAL_BLESSING), (1, mv.GROWL), (1, mv.SCRATCH),
     (1, mv.WILD_CHARGE), (3, mv.THUNDER_SHOCK), (6, mv.QUICK_ATTACK),
     (8, mv.CHARGE), (12, mv.NUZZLE), (15, mv.DIG), (19, mv.BITE),
     (23, mv.SPARK), (25, mv.ARM_THRUST), (29, mv.THUNDER_WAVE), (33, mv.SLAM),
     (39, mv.ENTRAINMENT), (44, mv.CLOSE_COMBAT), (49, mv.DISCHARGE),
     (54, mv.AGILITY), (60, mv.DOUBLE_SHOCK)),
    None, 0, False, "")

PAWMO = Pokemon(
    922, "Pawmo", 9, False,
    "", ("Electric", "Fighting"),
    60, 62, 40, 85,
    ((0, mv.ARM_THRUST), (1, mv.GROWL), (1, mv.SCRATCH), (3, mv.THUNDER_SHOCK),
     (6, mv.QUICK_ATTACK), (8, mv.CHARGE), (12, mv.NUZZLE), (15, mv.DIG),
     (19, mv.BITE), (23, mv.SPARK), (27, mv.THUNDER_WAVE), (32, mv.SLAM),
     (38, mv.ENTRAINMENT), (42, mv.DISCHARGE), (46, mv.AGILITY),
     (52, mv.WILD_CHARGE)),
    PAWMOT, 0, True, "level-up")

PAWMI = Pokemon(
    921, "Pawmi", 9, False,
    "", ("Electric",),
    45, 45, 22, 60,
    ((1, mv.GROWL), (1, mv.SCRATCH), (3, mv.THUNDER_SHOCK),
     (6, mv.QUICK_ATTACK), (8, mv.CHARGE), (12, mv.NUZZLE), (15, mv.DIG),
     (19, mv.BITE), (23, mv.SPARK), (27, mv.THUNDER_WAVE),
     (31, mv.ENTRAINMENT), (35, mv.SLAM), (38, mv.DISCHARGE), (40, mv.AGILITY),
     (44, mv.WILD_CHARGE)),
    PAWMO, 18, True, "")

MAUSHOLD = Pokemon(
    925, "Maushold", 9, False,
    "", ("Normal",),
    74, 70, 72, 111,
    ((1, mv.BABY_DOLL_EYES), (1, mv.FOLLOW_ME), (1, mv.POUND), (1, mv.TIDY_UP),
     (5, mv.ECHOED_VOICE), (8, mv.HELPING_HAND), (11, mv.SUPER_FANG),
     (14, mv.DOUBLE_HIT), (18, mv.BULLET_SEED), (22, mv.ENCORE),
     (29, mv.PLAY_ROUGH), (33, mv.HYPER_VOICE), (37, mv.CHARM),
     (41, mv.BEAT_UP), (46, mv.COPYCAT), (53, mv.POPULATION_BOMB)),
    None, 0, False, "")

TANDEMAUS = Pokemon(
    924, "Tandemaus", 9, False,
    "", ("Normal",),
    50, 45, 45, 75,
    ((1, mv.BABY_DOLL_EYES), (1, mv.POUND), (5, mv.ECHOED_VOICE),
     (8, mv.HELPING_HAND), (11, mv.SUPER_FANG), (14, mv.DOUBLE_HIT),
     (18, mv.BULLET_SEED), (22, mv.ENCORE), (26, mv.PLAY_ROUGH),
     (30, mv.HYPER_VOICE), (33, mv.CHARM), (37, mv.BEAT_UP), (41, mv.COPYCAT),
     (46, mv.POPULATION_BOMB)),
    MAUSHOLD, 25, True, "")

DACHSBUN = Pokemon(
    927, "Dachsbun", 9, False,
    "", ("Fairy",),
    57, 65, 97, 95,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.LICK), (6, mv.TAIL_WHIP),
     (8, mv.COVET), (11, mv.BITE), (15, mv.BABY_DOLL_EYES),
     (18, mv.PLAY_ROUGH), (22, mv.WORK_UP), (29, mv.BATON_PASS), (33, mv.ROAR),
     (38, mv.DOUBLE_EDGE), (42, mv.CHARM), (47, mv.CRUNCH),
     (53, mv.LAST_RESORT)),
    None, 0, False, "")

FIDOUGH = Pokemon(
    926, "Fidough", 9, False,
    "", ("Fairy",),
    37, 42, 62, 65,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.LICK), (6, mv.TAIL_WHIP),
     (8, mv.COVET), (11, mv.BITE), (15, mv.BABY_DOLL_EYES),
     (18, mv.PLAY_ROUGH), (22, mv.WORK_UP), (26, mv.BATON_PASS), (30, mv.ROAR),
     (33, mv.DOUBLE_EDGE), (36, mv.CHARM), (40, mv.CRUNCH),
     (45, mv.LAST_RESORT)),
    DACHSBUN, 26, True, "")

ARBOLIVA = Pokemon(
    930, "Arboliva", 9, False,
    "", ("Grass", "Normal"),
    78, 97, 99, 39,
    ((1, mv.MIRROR_COAT), (1, mv.SAFEGUARD), (1, mv.SWEET_SCENT),
     (1, mv.TACKLE), (5, mv.ABSORB), (7, mv.GROWTH), (10, mv.RAZOR_LEAF),
     (13, mv.HELPING_HAND), (16, mv.FLAIL), (20, mv.MEGA_DRAIN),
     (23, mv.GRASSY_TERRAIN), (29, mv.SEED_BOMB), (34, mv.ENERGY_BALL),
     (39, mv.LEECH_SEED), (46, mv.TERRAIN_PULSE), (52, mv.PETAL_BLIZZARD),
     (58, mv.PETAL_DANCE)),
    None, 0, False, "")

DOLLIV = Pokemon(
    929, "Dolliv", 9, False,
    "", ("Grass", "Normal"),
    52, 65, 69, 33,
    ((1, mv.SWEET_SCENT), (1, mv.TACKLE), (5, mv.ABSORB), (7, mv.GROWTH),
     (10, mv.RAZOR_LEAF), (13, mv.HELPING_HAND), (16, mv.FLAIL),
     (20, mv.MEGA_DRAIN), (23, mv.GRASSY_TERRAIN), (29, mv.SEED_BOMB),
     (34, mv.ENERGY_BALL), (37, mv.LEECH_SEED), (42, mv.TERRAIN_PULSE)),
    ARBOLIVA, 35, True, "")

SMOLIV = Pokemon(
    928, "Smoliv", 9, False,
    "", ("Grass", "Normal"),
    41, 46, 48, 30,
    ((1, mv.SWEET_SCENT), (1, mv.TACKLE), (5, mv.ABSORB), (7, mv.GROWTH),
     (10, mv.RAZOR_LEAF), (13, mv.HELPING_HAND), (16, mv.FLAIL),
     (20, mv.MEGA_DRAIN), (23, mv.GRASSY_TERRAIN), (27, mv.SEED_BOMB),
     (30, mv.ENERGY_BALL), (34, mv.LEECH_SEED), (38, mv.TERRAIN_PULSE)),
    DOLLIV, 25, True, "")

SQUAWKABILLY = Pokemon(
    931, "Squawkabilly", 9, False,
    "", ("Normal", "Flying"),
    82, 70, 51, 92,
    ((1, mv.GROWL), (1, mv.MIMIC), (1, mv.PECK), (6, mv.QUICK_ATTACK),
     (10, mv.TORMENT), (13, mv.AERIAL_ACE), (17, mv.FURY_ATTACK),
     (20, mv.TAUNT), (24, mv.UPROAR), (27, mv.COPYCAT), (30, mv.FLY),
     (34, mv.FACADE), (38, mv.SWAGGER), (42, mv.BRAVE_BIRD), (47, mv.ROOST),
     (52, mv.REVERSAL)),
    None, 0, False, "")

GARGANACL = Pokemon(
    934, "Garganacl", 9, False,
    "", ("Rock",),
    100, 72, 110, 35,
    ((0, mv.HAMMER_ARM), (1, mv.BLOCK), (1, mv.HARDEN), (1, mv.ROCK_BLAST),
     (1, mv.TACKLE), (1, mv.WIDE_GUARD), (5, mv.ROCK_THROW), (7, mv.MUD_SHOT),
     (10, mv.ROCK_TOMB), (13, mv.ROCK_POLISH), (16, mv.HEADBUTT),
     (24, mv.SALT_CURE), (30, mv.RECOVER), (34, mv.ROCK_SLIDE),
     (40, mv.STEALTH_ROCK), (44, mv.HEAVY_SLAM), (49, mv.EARTHQUAKE),
     (54, mv.STONE_EDGE), (60, mv.EXPLOSION)),
    None, 0, False, "")

NACLSTACK = Pokemon(
    933, "Naclstack", 9, False,
    "", ("Rock",),
    60, 47, 82, 35,
    ((0, mv.SALT_CURE), (1, mv.HARDEN), (1, mv.TACKLE), (5, mv.ROCK_THROW),
     (7, mv.MUD_SHOT), (10, mv.SMACK_DOWN), (13, mv.ROCK_POLISH),
     (16, mv.HEADBUTT), (20, mv.IRON_DEFENSE), (30, mv.RECOVER),
     (34, mv.ROCK_SLIDE), (38, mv.STEALTH_ROCK), (41, mv.HEAVY_SLAM),
     (45, mv.EARTHQUAKE), (51, mv.STONE_EDGE)),
    GARGANACL, 38, True, "")

NACLI = Pokemon(
    932, "Nacli", 9, False,
    "", ("Rock",),
    55, 45, 55, 25,
    ((1, mv.HARDEN), (1, mv.TACKLE), (5, mv.ROCK_THROW), (7, mv.MUD_SHOT),
     (10, mv.SMACK_DOWN), (13, mv.ROCK_POLISH), (16, mv.HEADBUTT),
     (20, mv.IRON_DEFENSE), (25, mv.RECOVER), (30, mv.ROCK_SLIDE),
     (33, mv.STEALTH_ROCK), (35, mv.HEAVY_SLAM), (40, mv.EARTHQUAKE),
     (45, mv.STONE_EDGE)),
    NACLSTACK, 24, True, "")

CERULEDGE = Pokemon(
    937, "Ceruledge", 9, False,
    "", ("Fire", "Ghost"),
    75, 92, 90, 85,
    ((0, mv.SHADOW_CLAW), (1, mv.ASTONISH), (1, mv.EMBER), (1, mv.LEER),
     (8, mv.CLEAR_SMOG), (12, mv.FIRE_SPIN), (16, mv.WILL_O_WISP),
     (20, mv.NIGHT_SHADE), (24, mv.FLAME_CHARGE), (28, mv.INCINERATE),
     (32, mv.LAVA_PLUME), (37, mv.SWORDS_DANCE), (42, mv.ALLY_SWITCH),
     (48, mv.BITTER_BLADE), (56, mv.PSYCHO_CUT), (62, mv.FLARE_BLITZ)),
    None, 0, False, "")

ARMAROUGE = Pokemon(
    936, "Armarouge", 9, False,
    "", ("Fire", "Psychic"),
    85, 92, 90, 75,
    ((0, mv.PSYSHOCK), (1, mv.ASTONISH), (1, mv.EMBER), (1, mv.LEER),
     (1, mv.MYSTICAL_FIRE), (1, mv.WIDE_GUARD), (8, mv.CLEAR_SMOG),
     (12, mv.FIRE_SPIN), (16, mv.WILL_O_WISP), (20, mv.NIGHT_SHADE),
     (24, mv.FLAME_CHARGE), (28, mv.INCINERATE), (32, mv.LAVA_PLUME),
     (37, mv.CALM_MIND), (42, mv.ALLY_SWITCH), (48, mv.FLAMETHROWER),
     (56, mv.EXPANDING_FORCE), (62, mv.ARMOR_CANNON)),
    CERULEDGE, 0, True, "Use Malicious Armor")

CHARCADET = Pokemon(
    935, "Charcadet", 9, False,
    "", ("Fire",),
    40, 50, 40, 35,
    ((1, mv.ASTONISH), (1, mv.EMBER), (1, mv.LEER), (8, mv.CLEAR_SMOG),
     (12, mv.FIRE_SPIN), (16, mv.WILL_O_WISP), (20, mv.NIGHT_SHADE),
     (24, mv.FLAME_CHARGE), (28, mv.INCINERATE), (32, mv.LAVA_PLUME)),
    ARMAROUGE, 0, True, "item:malicious-armor")

BELLIBOLT = Pokemon(
    939, "Bellibolt", 9, False,
    "", ("Electric",),
    109, 83, 87, 45,
    ((1, mv.MUD_SLAP), (1, mv.SLACK_OFF), (1, mv.TACKLE),
     (7, mv.THUNDER_SHOCK), (11, mv.WATER_GUN), (17, mv.CHARGE),
     (21, mv.SPARK), (24, mv.MUD_SHOT), (25, mv.FLAIL), (32, mv.DISCHARGE),
     (36, mv.WEATHER_BALL), (40, mv.ELECTRIC_TERRAIN), (45, mv.SUCKER_PUNCH),
     (50, mv.ZAP_CANNON)),
    None, 0, False, "")

TADBULB = Pokemon(
    938, "Tadbulb", 9, False,
    "", ("Electric",),
    61, 45, 38, 45,
    ((1, mv.MUD_SLAP), (1, mv.TACKLE), (7, mv.THUNDER_SHOCK),
     (11, mv.WATER_GUN), (17, mv.CHARGE), (21, mv.SPARK), (24, mv.MUD_SHOT),
     (25, mv.FLAIL), (32, mv.DISCHARGE), (36, mv.WEATHER_BALL),
     (40, mv.ELECTRIC_TERRAIN), (45, mv.SUCKER_PUNCH), (50, mv.ZAP_CANNON)),
    BELLIBOLT, 0, True, "item:thunder-stone")

KILOWATTREL = Pokemon(
    941, "Kilowattrel", 9, False,
    "", ("Electric", "Flying"),
    70, 87, 60, 125,
    ((0, mv.ELECTRO_BALL), (1, mv.GROWL), (1, mv.PECK), (4, mv.THUNDER_SHOCK),
     (7, mv.QUICK_ATTACK), (11, mv.PLUCK), (15, mv.SPARK), (19, mv.UPROAR),
     (24, mv.ROOST), (30, mv.DUAL_WINGBEAT), (36, mv.AGILITY),
     (43, mv.VOLT_SWITCH), (48, mv.DISCHARGE), (55, mv.HURRICANE)),
    None, 0, False, "")

WATTREL = Pokemon(
    940, "Wattrel", 9, False,
    "", ("Electric", "Flying"),
    40, 47, 37, 70,
    ((1, mv.GROWL), (1, mv.PECK), (4, mv.THUNDER_SHOCK), (7, mv.QUICK_ATTACK),
     (11, mv.PLUCK), (15, mv.SPARK), (19, mv.UPROAR), (23, mv.ROOST),
     (27, mv.DUAL_WINGBEAT), (32, mv.AGILITY), (37, mv.VOLT_SWITCH),
     (43, mv.DISCHARGE)),
    KILOWATTREL, 25, True, "")

MABOSSTIFF = Pokemon(
    943, "Mabosstiff", 9, False,
    "", ("Dark",),
    80, 90, 80, 85,
    ((0, mv.COMEUPPANCE), (1, mv.LEER), (1, mv.SCARY_FACE), (1, mv.TACKLE),
     (4, mv.LICK), (7, mv.SNARL), (10, mv.HONE_CLAWS), (14, mv.BITE),
     (18, mv.ROAR), (22, mv.HEADBUTT), (26, mv.PAYBACK), (34, mv.CRUNCH),
     (39, mv.SWAGGER), (43, mv.REVERSAL), (48, mv.JAW_LOCK),
     (55, mv.DOUBLE_EDGE), (60, mv.OUTRAGE)),
    None, 0, False, "")

MASCHIFF = Pokemon(
    942, "Maschiff", 9, False,
    "", ("Dark",),
    60, 59, 55, 51,
    ((1, mv.LEER), (1, mv.SCARY_FACE), (1, mv.TACKLE), (4, mv.LICK),
     (7, mv.SNARL), (10, mv.HONE_CLAWS), (14, mv.BITE), (18, mv.ROAR),
     (22, mv.HEADBUTT), (26, mv.PAYBACK), (31, mv.CRUNCH), (35, mv.SWAGGER),
     (39, mv.REVERSAL), (43, mv.JAW_LOCK), (49, mv.DOUBLE_EDGE)),
    MABOSSTIFF, 30, True, "")

GRAFAIAI = Pokemon(
    945, "Grafaiai", 9, False,
    "", ("Poison", "Normal"),
    63, 87, 68, 110,
    ((0, mv.DOODLE), (1, mv.LEER), (1, mv.SCRATCH), (5, mv.ACID_SPRAY),
     (8, mv.FURY_SWIPES), (11, mv.SWITCHEROO), (14, mv.POISON_FANG),
     (18, mv.FLATTER), (21, mv.SLASH), (25, mv.U_TURN), (33, mv.POISON_JAB),
     (37, mv.TAUNT), (40, mv.SUBSTITUTE), (45, mv.KNOCK_OFF),
     (51, mv.GUNK_SHOT)),
    None, 0, False, "")

SHROODLE = Pokemon(
    944, "Shroodle", 9, False,
    "", ("Poison", "Normal"),
    40, 52, 35, 75,
    ((1, mv.LEER), (1, mv.SCRATCH), (5, mv.ACID_SPRAY), (8, mv.BITE),
     (8, mv.FURY_SWIPES), (11, mv.SWITCHEROO), (14, mv.POISON_FANG),
     (18, mv.FLATTER), (21, mv.SLASH), (25, mv.U_TURN), (29, mv.POISON_JAB),
     (33, mv.TAUNT), (36, mv.SUBSTITUTE), (40, mv.KNOCK_OFF),
     (45, mv.GUNK_SHOT)),
    GRAFAIAI, 28, True, "")

BRAMBLEGHAST = Pokemon(
    947, "Brambleghast", 9, False,
    "", ("Grass", "Ghost"),
    55, 97, 70, 90,
    ((1, mv.ASTONISH), (1, mv.DEFENSE_CURL), (1, mv.ROLLOUT), (5, mv.ABSORB),
     (9, mv.RAPID_SPIN), (13, mv.BULLET_SEED), (17, mv.INFESTATION),
     (21, mv.HEX), (25, mv.MEGA_DRAIN), (29, mv.DISABLE),
     (35, mv.PHANTOM_FORCE), (40, mv.GIGA_DRAIN), (45, mv.CURSE),
     (50, mv.PAIN_SPLIT), (55, mv.POWER_WHIP)),
    None, 0, False, "")

BRAMBLIN = Pokemon(
    946, "Bramblin", 9, False,
    "", ("Grass", "Ghost"),
    40, 55, 32, 60,
    ((1, mv.ASTONISH), (1, mv.DEFENSE_CURL), (1, mv.ROLLOUT), (5, mv.ABSORB),
     (9, mv.RAPID_SPIN), (13, mv.BULLET_SEED), (17, mv.INFESTATION),
     (21, mv.HEX), (25, mv.MEGA_DRAIN), (29, mv.DISABLE),
     (35, mv.PHANTOM_FORCE), (40, mv.GIGA_DRAIN), (45, mv.CURSE),
     (50, mv.PAIN_SPLIT), (55, mv.POWER_WHIP)),
    BRAMBLEGHAST, 0, True,
    "Level up after walking 1,000 steps in Let's Go mode")

TOEDSCRUEL = Pokemon(
    949, "Toedscruel", 9, False,
    "", ("Ground", "Grass"),
    80, 75, 92, 100,
    ((1, mv.MUD_SLAP), (1, mv.REFLECT_TYPE), (1, mv.WRAP), (4, mv.ABSORB),
     (8, mv.POISON_POWDER), (8, mv.STUN_SPORE), (12, mv.SUPERSONIC),
     (15, mv.TACKLE), (16, mv.MEGA_DRAIN), (20, mv.SCREECH), (24, mv.MUD_SHOT),
     (28, mv.HEX), (34, mv.SEED_BOMB), (40, mv.SPORE), (44, mv.GROWTH),
     (48, mv.GIGA_DRAIN), (54, mv.EARTH_POWER), (58, mv.POWER_WHIP)),
    None, 0, False, "")

TOEDSCOOL = Pokemon(
    948, "Toedscool", 9, False,
    "", ("Ground", "Grass"),
    40, 45, 67, 70,
    ((1, mv.MUD_SLAP), (1, mv.WRAP), (4, mv.ABSORB), (8, mv.POISON_POWDER),
     (8, mv.STUN_SPORE), (12, mv.SUPERSONIC), (15, mv.TACKLE),
     (16, mv.MEGA_DRAIN), (20, mv.SCREECH), (24, mv.MUD_SHOT), (28, mv.HEX),
     (32, mv.SEED_BOMB), (36, mv.SPORE), (40, mv.GROWTH), (44, mv.GIGA_DRAIN),
     (48, mv.EARTH_POWER), (52, mv.POWER_WHIP)),
    TOEDSCRUEL, 30, True, "")

KLAWF = Pokemon(
    950, "Klawf", 9, False,
    "", ("Rock",),
    70, 67, 85, 75,
    ((1, mv.ROCK_THROW), (6, mv.HARDEN), (9, mv.ROCK_SMASH),
     (13, mv.ROCK_TOMB), (17, mv.METAL_CLAW), (21, mv.PROTECT),
     (24, mv.ROCK_BLAST), (29, mv.X_SCISSOR), (33, mv.SWORDS_DANCE),
     (37, mv.FLAIL), (42, mv.ROCK_SLIDE), (47, mv.HIGH_HORSEPOWER),
     (51, mv.IRON_DEFENSE), (56, mv.GUILLOTINE)),
    None, 0, False, "")

SCOVILLAIN = Pokemon(
    952, "Scovillain", 9, False,
    "", ("Grass", "Fire"),
    65, 108, 65, 75,
    ((0, mv.FLAMETHROWER), (0, mv.SPICY_EXTRACT), (1, mv.FIRE_FANG),
     (1, mv.LEAFAGE), (1, mv.LEER), (4, mv.BITE), (10, mv.GROWTH),
     (13, mv.RAZOR_LEAF), (17, mv.SUNNY_DAY), (21, mv.BULLET_SEED),
     (24, mv.HEADBUTT), (28, mv.ZEN_HEADBUTT), (33, mv.WORRY_SEED),
     (38, mv.CRUNCH), (44, mv.SEED_BOMB), (48, mv.OVERHEAT),
     (48, mv.SOLAR_BEAM)),
    None, 0, False, "")

CAPSAKID = Pokemon(
    951, "Capsakid", 9, False,
    "", ("Grass",),
    50, 62, 40, 50,
    ((1, mv.LEAFAGE), (1, mv.LEER), (4, mv.BITE), (10, mv.GROWTH),
     (13, mv.RAZOR_LEAF), (17, mv.SUNNY_DAY), (21, mv.BULLET_SEED),
     (24, mv.HEADBUTT), (28, mv.ZEN_HEADBUTT), (38, mv.CRUNCH),
     (44, mv.SEED_BOMB), (48, mv.SOLAR_BEAM)),
    SCOVILLAIN, 0, True, "item:fire-stone")

RABSCA = Pokemon(
    954, "Rabsca", 9, False,
    "", ("Bug", "Psychic"),
    75, 82, 92, 45,
    ((0, mv.REVIVAL_BLESSING), (1, mv.CONFUSION), (1, mv.DEFENSE_CURL),
     (1, mv.TACKLE), (4, mv.SAND_ATTACK), (7, mv.STRUGGLE_BUG),
     (11, mv.ROLLOUT), (15, mv.PSYBEAM), (20, mv.BUG_BITE), (24, mv.TAKE_DOWN),
     (29, mv.EXTRASENSORY), (35, mv.LUNGE), (40, mv.GUARD_SWAP),
     (40, mv.POWER_SWAP), (40, mv.SPEED_SWAP), (45, mv.BUG_BUZZ),
     (50, mv.PSYCHIC)),
    None, 0, False, "")

RELLOR = Pokemon(
    953, "Rellor", 9, False,
    "", ("Bug",),
    41, 40, 59, 30,
    ((1, mv.DEFENSE_CURL), (1, mv.TACKLE), (4, mv.SAND_ATTACK),
     (7, mv.STRUGGLE_BUG), (11, mv.ROLLOUT), (15, mv.MUD_SHOT),
     (20, mv.BUG_BITE), (24, mv.TAKE_DOWN), (29, mv.DIG), (35, mv.LUNGE)),
    RABSCA, 0, True, "level-up")

ESPATHRA = Pokemon(
    956, "Espathra", 9, False,
    "", ("Psychic",),
    95, 80, 60, 105,
    ((0, mv.LUMINA_CRASH), (1, mv.DRILL_PECK), (1, mv.FEATHER_DANCE),
     (1, mv.GROWL), (1, mv.PECK), (5, mv.CONFUSION), (8, mv.BABY_DOLL_EYES),
     (11, mv.DISARMING_VOICE), (15, mv.QUICK_ATTACK), (19, mv.PSYBEAM),
     (24, mv.PLUCK), (29, mv.AGILITY), (34, mv.UPROAR),
     (43, mv.DAZZLING_GLEAM), (49, mv.PSYCHIC), (54, mv.LAST_RESORT)),
    None, 0, False, "")

FLITTLE = Pokemon(
    955, "Flittle", 9, False,
    "", ("Psychic",),
    30, 45, 30, 75,
    ((1, mv.GROWL), (1, mv.PECK), (5, mv.CONFUSION), (8, mv.BABY_DOLL_EYES),
     (11, mv.DISARMING_VOICE), (15, mv.QUICK_ATTACK), (19, mv.PSYBEAM),
     (24, mv.PLUCK), (29, mv.AGILITY), (34, mv.UPROAR)),
    ESPATHRA, 35, True, "")

TINKATON = Pokemon(
    959, "Tinkaton", 9, False,
    "", ("Fairy", "Steel"),
    85, 72, 91, 94,
    ((0, mv.GIGATON_HAMMER), (1, mv.ASTONISH), (1, mv.FAIRY_WIND),
     (5, mv.BABY_DOLL_EYES), (8, mv.METAL_CLAW), (11, mv.COVET),
     (14, mv.ROCK_SMASH), (17, mv.DRAINING_KISS), (21, mv.SWEET_KISS),
     (24, mv.BRUTAL_SWING), (27, mv.SLAM), (31, mv.FLASH_CANNON),
     (35, mv.PLAY_ROUGH), (39, mv.FAKE_OUT), (43, mv.FLATTER),
     (47, mv.SKITTER_SMACK), (52, mv.KNOCK_OFF)),
    None, 0, False, "")

TINKATUFF = Pokemon(
    958, "Tinkatuff", 9, False,
    "", ("Fairy", "Steel"),
    65, 50, 68, 78,
    ((1, mv.ASTONISH), (1, mv.FAIRY_WIND), (5, mv.BABY_DOLL_EYES),
     (8, mv.METAL_CLAW), (11, mv.COVET), (14, mv.ROCK_SMASH),
     (17, mv.DRAINING_KISS), (21, mv.SWEET_KISS), (24, mv.BRUTAL_SWING),
     (27, mv.SLAM), (31, mv.FLASH_CANNON), (35, mv.PLAY_ROUGH),
     (39, mv.FAKE_OUT), (43, mv.FLATTER), (47, mv.SKITTER_SMACK),
     (52, mv.KNOCK_OFF)),
    TINKATON, 38, True, "")

TINKATINK = Pokemon(
    957, "Tinkatink", 9, False,
    "", ("Fairy", "Steel"),
    50, 40, 54, 58,
    ((1, mv.ASTONISH), (1, mv.FAIRY_WIND), (5, mv.BABY_DOLL_EYES),
     (8, mv.METAL_CLAW), (11, mv.COVET), (14, mv.ROCK_SMASH),
     (17, mv.DRAINING_KISS), (21, mv.SWEET_KISS), (24, mv.BRUTAL_SWING),
     (27, mv.SLAM), (31, mv.FLASH_CANNON), (35, mv.PLAY_ROUGH),
     (39, mv.FAKE_OUT), (43, mv.FLATTER), (47, mv.SKITTER_SMACK),
     (52, mv.KNOCK_OFF)),
    TINKATUFF, 24, True, "")

WUGTRIO = Pokemon(
    961, "Wugtrio", 9, False,
    "", ("Water",),
    35, 75, 60, 120,
    ((1, mv.MUD_SLAP), (1, mv.SAND_ATTACK), (1, mv.WATER_GUN), (1, mv.WRAP),
     (12, mv.AQUA_JET), (16, mv.SLAM), (20, mv.WATER_PULSE), (24, mv.HEADBUTT),
     (30, mv.TRIPLE_DIVE), (36, mv.DIG), (42, mv.SUCKER_PUNCH),
     (48, mv.THROAT_CHOP), (54, mv.LIQUIDATION)),
    None, 0, False, "")

WIGLETT = Pokemon(
    960, "Wiglett", 9, False,
    "", ("Water",),
    10, 45, 25, 95,
    ((1, mv.SAND_ATTACK), (1, mv.WATER_GUN), (4, mv.MUD_SLAP), (8, mv.WRAP),
     (12, mv.AQUA_JET), (20, mv.SLAM), (20, mv.WATER_PULSE), (24, mv.HEADBUTT),
     (28, mv.DIG), (32, mv.SUCKER_PUNCH), (36, mv.THROAT_CHOP),
     (40, mv.LIQUIDATION)),
    WUGTRIO, 26, True, "")

BOMBIRDIER = Pokemon(
    962, "Bombirdier", 9, False,
    "", ("Flying", "Dark"),
    70, 81, 85, 82,
    ((1, mv.HONE_CLAWS), (1, mv.LEER), (1, mv.MEMENTO), (1, mv.PECK),
     (1, mv.WING_ATTACK), (7, mv.THIEF), (11, mv.ROCK_THROW),
     (16, mv.WHIRLWIND), (20, mv.PLUCK), (24, mv.TORMENT), (29, mv.ROCK_TOMB),
     (36, mv.PAYBACK), (42, mv.DUAL_WINGBEAT), (47, mv.ROCK_SLIDE),
     (53, mv.KNOCK_OFF), (60, mv.PARTING_SHOT)),
    None, 0, False, "")

PALAFIN = Pokemon(
    964, "Palafin", 9, False,
    "", ("Water",),
    100, 61, 67, 100,
    ((0, mv.FLIP_TURN), (1, mv.JET_PUNCH), (1, mv.SUPERSONIC),
     (1, mv.WATER_GUN), (7, mv.ASTONISH), (10, mv.FOCUS_ENERGY),
     (13, mv.AQUA_JET), (17, mv.DOUBLE_HIT), (21, mv.DIVE), (25, mv.CHARM),
     (29, mv.ACROBATICS), (34, mv.ENCORE), (39, mv.AQUA_TAIL), (44, mv.MIST),
     (50, mv.HYDRO_PUMP), (55, mv.FOCUS_PUNCH), (61, mv.WAVE_CRASH)),
    None, 0, False, "")

FINIZEN = Pokemon(
    963, "Finizen", 9, False,
    "", ("Water",),
    70, 45, 40, 75,
    ((1, mv.SUPERSONIC), (1, mv.WATER_GUN), (7, mv.ASTONISH),
     (10, mv.FOCUS_ENERGY), (13, mv.AQUA_JET), (17, mv.DOUBLE_HIT),
     (21, mv.DIVE), (25, mv.CHARM), (29, mv.ACROBATICS), (34, mv.ENCORE),
     (39, mv.AQUA_TAIL), (44, mv.MIST), (50, mv.HYDRO_PUMP)),
    PALAFIN, 38, True, "")

REVAVROOM = Pokemon(
    966, "Revavroom", 9, False,
    "", ("Steel", "Poison"),
    80, 86, 78, 90,
    ((0, mv.SHIFT_GEAR), (1, mv.LICK), (1, mv.MAGNET_RISE), (1, mv.POISON_GAS),
     (4, mv.SMOG), (7, mv.TAUNT), (10, mv.ASSURANCE), (13, mv.SLUDGE),
     (17, mv.GYRO_BALL), (21, mv.HEADBUTT), (25, mv.SCREECH),
     (28, mv.IRON_HEAD), (32, mv.SWAGGER), (36, mv.POISON_JAB),
     (46, mv.UPROAR), (52, mv.SPIN_OUT), (58, mv.GUNK_SHOT)),
    None, 0, False, "")

VAROOM = Pokemon(
    965, "Varoom", 9, False,
    "", ("Steel", "Poison"),
    45, 50, 54, 47,
    ((1, mv.LICK), (1, mv.POISON_GAS), (4, mv.SMOG), (7, mv.TAUNT),
     (10, mv.ASSURANCE), (13, mv.SLUDGE), (17, mv.GYRO_BALL),
     (21, mv.HEADBUTT), (25, mv.SCREECH), (28, mv.IRON_HEAD), (32, mv.SWAGGER),
     (36, mv.POISON_JAB), (41, mv.UPROAR), (46, mv.SPIN_OUT),
     (50, mv.GUNK_SHOT)),
    REVAVROOM, 40, True, "")

CYCLIZAR = Pokemon(
    967, "Cyclizar", 9, False,
    "", ("Dragon", "Normal"),
    70, 90, 65, 121,
    ((1, mv.GROWL), (1, mv.TACKLE), (7, mv.RAPID_SPIN), (11, mv.TAUNT),
     (14, mv.BREAKING_SWIPE), (18, mv.QUICK_ATTACK), (23, mv.BITE),
     (27, mv.U_TURN), (31, mv.SHED_TAIL), (36, mv.DRAGON_CLAW),
     (40, mv.SHIFT_GEAR), (45, mv.DRAGON_PULSE), (51, mv.DOUBLE_EDGE),
     (57, mv.DRAGON_RUSH)),
    None, 0, False, "")

ORTHWORM = Pokemon(
    968, "Orthworm", 9, False,
    "", ("Steel",),
    70, 72, 100, 65,
    ((1, mv.HARDEN), (1, mv.TACKLE), (1, mv.WRAP), (7, mv.MUD_SLAP),
     (12, mv.SMACK_DOWN), (16, mv.BULLDOZE), (21, mv.IRON_HEAD),
     (26, mv.TAKE_DOWN), (30, mv.DIG), (34, mv.SANDSTORM),
     (38, mv.IRON_DEFENSE), (43, mv.IRON_TAIL), (47, mv.EARTHQUAKE),
     (52, mv.SHED_TAIL)),
    None, 0, False, "")

GLIMMORA = Pokemon(
    970, "Glimmora", 9, False,
    "", ("Rock", "Poison"),
    83, 92, 85, 86,
    ((0, mv.MORTAL_SPIN), (1, mv.HARDEN), (1, mv.ROCK_THROW),
     (1, mv.SMACK_DOWN), (1, mv.SPIKY_SHIELD), (1, mv.TOXIC_SPIKES),
     (7, mv.ACID_SPRAY), (11, mv.ANCIENT_POWER), (15, mv.ROCK_POLISH),
     (18, mv.STEALTH_ROCK), (22, mv.VENOSHOCK), (26, mv.SANDSTORM),
     (29, mv.SELF_DESTRUCT), (33, mv.ROCK_SLIDE), (39, mv.POWER_GEM),
     (44, mv.ACID_ARMOR), (50, mv.SLUDGE_WAVE)),
    None, 0, False, "")

GLIMMET = Pokemon(
    969, "Glimmet", 9, False,
    "", ("Rock", "Poison"),
    48, 70, 51, 60,
    ((1, mv.HARDEN), (1, mv.ROCK_THROW), (1, mv.SMACK_DOWN),
     (7, mv.ACID_SPRAY), (11, mv.ANCIENT_POWER), (15, mv.ROCK_POLISH),
     (18, mv.STEALTH_ROCK), (22, mv.VENOSHOCK), (26, mv.SANDSTORM),
     (29, mv.SELF_DESTRUCT), (33, mv.ROCK_SLIDE), (37, mv.POWER_GEM),
     (41, mv.ACID_ARMOR), (46, mv.SLUDGE_WAVE)),
    GLIMMORA, 35, True, "")

HOUNDSTONE = Pokemon(
    972, "Houndstone", 9, False,
    "", ("Ghost",),
    72, 75, 98, 68,
    ((0, mv.LAST_RESPECTS), (1, mv.GROWL), (1, mv.TACKLE), (3, mv.LICK),
     (6, mv.BITE), (6, mv.TAIL_WHIP), (9, mv.ROAR), (12, mv.HEADBUTT),
     (16, mv.DIG), (24, mv.REST), (28, mv.CRUNCH), (36, mv.PLAY_ROUGH),
     (41, mv.HELPING_HAND), (46, mv.PHANTOM_FORCE), (51, mv.CHARM),
     (58, mv.DOUBLE_EDGE)),
    None, 0, False, "")

GREAVARD = Pokemon(
    971, "Greavard", 9, False,
    "", ("Ghost",),
    50, 45, 57, 34,
    ((1, mv.GROWL), (1, mv.TACKLE), (3, mv.LICK), (6, mv.BITE),
     (6, mv.TAIL_WHIP), (9, mv.ROAR), (12, mv.HEADBUTT), (16, mv.DIG),
     (24, mv.REST), (28, mv.CRUNCH), (32, mv.PLAY_ROUGH),
     (37, mv.HELPING_HAND), (41, mv.PHANTOM_FORCE), (46, mv.CHARM),
     (52, mv.DOUBLE_EDGE)),
    HOUNDSTONE, 30, True, "")

FLAMIGO = Pokemon(
    973, "Flamigo", 9, False,
    "", ("Flying", "Fighting"),
    82, 95, 69, 90,
    ((1, mv.COPYCAT), (1, mv.PECK), (5, mv.DOUBLE_KICK), (9, mv.DETECT),
     (12, mv.WING_ATTACK), (15, mv.FOCUS_ENERGY), (18, mv.LOW_KICK),
     (21, mv.FEINT), (27, mv.PAYBACK), (31, mv.ROOST), (35, mv.AIR_SLASH),
     (39, mv.MEGA_KICK), (44, mv.WIDE_GUARD), (48, mv.THROAT_CHOP),
     (54, mv.BRAVE_BIRD)),
    None, 0, False, "")

CETITAN = Pokemon(
    975, "Cetitan", 9, False,
    "", ("Ice",),
    170, 79, 60, 73,
    ((1, mv.POWDER_SNOW), (1, mv.TACKLE), (6, mv.GROWL), (9, mv.ECHOED_VOICE),
     (12, mv.ICE_SHARD), (15, mv.REST), (19, mv.TAKE_DOWN), (25, mv.FLAIL),
     (27, mv.AVALANCHE), (31, mv.BOUNCE), (36, mv.BODY_SLAM), (40, mv.AMNESIA),
     (44, mv.ICE_SPINNER), (49, mv.DOUBLE_EDGE), (53, mv.BLIZZARD)),
    None, 0, False, "")

CETODDLE = Pokemon(
    974, "Cetoddle", 9, False,
    "", ("Ice",),
    108, 49, 42, 43,
    ((1, mv.POWDER_SNOW), (1, mv.TACKLE), (6, mv.GROWL), (9, mv.ECHOED_VOICE),
     (12, mv.ICE_SHARD), (15, mv.REST), (19, mv.TAKE_DOWN), (25, mv.FLAIL),
     (27, mv.AVALANCHE), (31, mv.BOUNCE), (36, mv.BODY_SLAM), (40, mv.AMNESIA),
     (44, mv.ICE_SPINNER), (49, mv.DOUBLE_EDGE), (53, mv.BLIZZARD)),
    CETITAN, 0, True, "item:ice-stone")

VELUZA = Pokemon(
    976, "Veluza", 9, False,
    "", ("Water", "Psychic"),
    90, 90, 69, 70,
    ((1, mv.AQUA_JET), (1, mv.TACKLE), (7, mv.PLUCK), (11, mv.WATER_PULSE),
     (15, mv.FOCUS_ENERGY), (20, mv.SLASH), (25, mv.AQUA_CUTTER),
     (30, mv.FILLET_AWAY), (35, mv.NIGHT_SLASH), (40, mv.PSYCHO_CUT),
     (45, mv.LIQUIDATION), (50, mv.CRUNCH), (55, mv.FINAL_GAMBIT)),
    None, 0, False, "")

DONDOZO = Pokemon(
    977, "Dondozo", 9, False,
    "", ("Water",),
    150, 82, 90, 35,
    ((1, mv.SUPERSONIC), (1, mv.TACKLE), (1, mv.WATER_GUN), (5, mv.TICKLE),
     (10, mv.FLAIL), (15, mv.REST), (15, mv.SLEEP_TALK), (20, mv.DIVE),
     (25, mv.NOBLE_ROAR), (30, mv.SOAK), (35, mv.BODY_SLAM),
     (40, mv.AQUA_TAIL), (45, mv.RAIN_DANCE), (50, mv.ORDER_UP),
     (55, mv.HEAVY_SLAM), (60, mv.DOUBLE_EDGE), (65, mv.WAVE_CRASH)),
    None, 0, False, "")

TATSUGIRI = Pokemon(
    978, "Tatsugiri", 9, False,
    "", ("Dragon", "Water"),
    68, 85, 77, 82,
    ((1, mv.SPLASH), (1, mv.WATER_GUN), (6, mv.HARDEN), (12, mv.HELPING_HAND),
     (17, mv.WATER_PULSE), (23, mv.SOAK), (28, mv.TAUNT), (34, mv.MEMENTO),
     (39, mv.MUDDY_WATER), (43, mv.NASTY_PLOT), (47, mv.MIRROR_COAT),
     (52, mv.DRAGON_PULSE)),
    None, 0, False, "")

GREAT_TUSK = Pokemon(
    984, "Great Tusk", 9, False,
    "", ("Ground", "Fighting"),
    115, 92, 92, 87,
    ((1, mv.DEFENSE_CURL), (1, mv.HORN_ATTACK), (1, mv.ROLLOUT),
     (1, mv.SUNNY_DAY), (7, mv.BULLDOZE), (14, mv.TAUNT), (21, mv.RAPID_SPIN),
     (28, mv.BRICK_BREAK), (35, mv.STOMPING_TANTRUM), (42, mv.KNOCK_OFF),
     (49, mv.EARTHQUAKE), (56, mv.GIGA_IMPACT), (63, mv.CLOSE_COMBAT),
     (70, mv.ENDEAVOR), (77, mv.MEGAHORN), (84, mv.HEAD_SMASH),
     (91, mv.HEADLONG_RUSH)),
    None, 0, False, "")

SCREAM_TAIL = Pokemon(
    985, "Scream Tail", 9, False,
    "", ("Fairy", "Psychic"),
    115, 65, 107, 111,
    ((1, mv.DISABLE), (1, mv.POUND), (1, mv.SING), (7, mv.HOWL),
     (14, mv.NOBLE_ROAR), (21, mv.BITE), (28, mv.BODY_SLAM), (35, mv.REST),
     (42, mv.PLAY_ROUGH), (49, mv.HYPER_VOICE), (56, mv.PSYCHIC_FANGS),
     (63, mv.CRUNCH), (70, mv.WISH), (77, mv.GYRO_BALL), (84, mv.PERISH_SONG),
     (91, mv.BOOMBURST)),
    None, 0, False, "")

BRUTE_BONNET = Pokemon(
    986, "Brute Bonnet", 9, False,
    "", ("Grass", "Dark"),
    111, 103, 99, 55,
    ((1, mv.ABSORB), (1, mv.ASTONISH), (1, mv.GROWTH), (7, mv.STUN_SPORE),
     (14, mv.MEGA_DRAIN), (21, mv.SYNTHESIS), (28, mv.CLEAR_SMOG),
     (35, mv.PAYBACK), (42, mv.THRASH), (49, mv.GIGA_DRAIN),
     (56, mv.SUCKER_PUNCH), (63, mv.SPORE), (70, mv.INGRAIN),
     (77, mv.RAGE_POWDER), (91, mv.SOLAR_BEAM)),
    None, 0, False, "")

FLUTTER_MANE = Pokemon(
    987, "Flutter Mane", 9, False,
    "", ("Ghost", "Fairy"),
    55, 95, 95, 135,
    ((1, mv.ASTONISH), (1, mv.CONFUSE_RAY), (1, mv.SPITE), (7, mv.PSYBEAM),
     (14, mv.MEAN_LOOK), (21, mv.MEMENTO), (28, mv.WISH),
     (35, mv.DAZZLING_GLEAM), (42, mv.SHADOW_BALL), (49, mv.MYSTICAL_FIRE),
     (56, mv.POWER_GEM), (63, mv.PSYSHOCK), (70, mv.PHANTOM_FORCE),
     (77, mv.PAIN_SPLIT), (84, mv.MOONBLAST), (91, mv.PERISH_SONG)),
    None, 0, False, "")

SLITHER_WING = Pokemon(
    988, "Slither Wing", 9, False,
    "", ("Bug", "Fighting"),
    85, 110, 92, 81,
    ((1, mv.BUG_BITE), (1, mv.EMBER), (1, mv.GUST), (7, mv.POISON_POWDER),
     (7, mv.STUN_SPORE), (14, mv.FLAME_CHARGE), (21, mv.STOMP),
     (28, mv.LOW_SWEEP), (35, mv.MORNING_SUN), (42, mv.LUNGE),
     (49, mv.SUPERPOWER), (56, mv.BULK_UP), (63, mv.DUAL_WINGBEAT),
     (70, mv.FIRST_IMPRESSION), (77, mv.WHIRLWIND), (84, mv.LEECH_LIFE),
     (91, mv.THRASH)),
    None, 0, False, "")

SANDY_SHOCKS = Pokemon(
    989, "Sandy Shocks", 9, False,
    "", ("Electric", "Ground"),
    85, 101, 91, 101,
    ((1, mv.ELECTRIC_TERRAIN), (1, mv.SUPERSONIC), (1, mv.THUNDER_SHOCK),
     (1, mv.THUNDER_WAVE), (7, mv.SPARK), (14, mv.BULLDOZE),
     (21, mv.CHARGE_BEAM), (28, mv.TRI_ATTACK), (35, mv.SCREECH),
     (42, mv.HEAVY_SLAM), (49, mv.METAL_SOUND), (56, mv.DISCHARGE),
     (63, mv.EARTH_POWER), (70, mv.MIRROR_COAT), (77, mv.GRAVITY),
     (84, mv.ZAP_CANNON), (91, mv.MAGNETIC_FLUX)),
    None, 0, False, "")

IRON_TREADS = Pokemon(
    990, "Iron Treads", 9, False,
    "", ("Ground", "Steel"),
    90, 92, 95, 106,
    ((1, mv.DEFENSE_CURL), (1, mv.ELECTRIC_TERRAIN), (1, mv.HORN_ATTACK),
     (1, mv.ROLLOUT), (7, mv.BULLDOZE), (21, mv.RAPID_SPIN),
     (28, mv.IRON_HEAD), (35, mv.STOMPING_TANTRUM), (42, mv.KNOCK_OFF),
     (49, mv.EARTHQUAKE), (56, mv.HEAVY_SLAM), (63, mv.WILD_CHARGE),
     (70, mv.ENDEAVOR), (77, mv.MEGAHORN), (84, mv.GIGA_IMPACT),
     (91, mv.STEEL_ROLLER)),
    None, 0, False, "")

IRON_BUNDLE = Pokemon(
    991, "Iron Bundle", 9, False,
    "", ("Ice", "Water"),
    56, 102, 87, 136,
    ((1, mv.PRESENT), (7, mv.POWDER_SNOW), (14, mv.WHIRLPOOL),
     (21, mv.TAKE_DOWN), (28, mv.DRILL_PECK), (35, mv.HELPING_HAND),
     (42, mv.FREEZE_DRY), (49, mv.FLIP_TURN), (56, mv.ICE_BEAM),
     (63, mv.AGILITY), (70, mv.SNOWSCAPE), (77, mv.HYDRO_PUMP),
     (84, mv.AURORA_VEIL), (91, mv.BLIZZARD)),
    None, 0, False, "")

IRON_HANDS = Pokemon(
    992, "Iron Hands", 9, False,
    "", ("Fighting", "Electric"),
    154, 95, 88, 50,
    ((1, mv.ARM_THRUST), (1, mv.FOCUS_ENERGY), (1, mv.SAND_ATTACK),
     (1, mv.TACKLE), (7, mv.FAKE_OUT), (14, mv.WHIRLWIND),
     (21, mv.THUNDER_PUNCH), (28, mv.SLAM), (35, mv.FORCE_PALM),
     (42, mv.SEISMIC_TOSS), (49, mv.CHARGE), (56, mv.WILD_CHARGE),
     (63, mv.CLOSE_COMBAT), (70, mv.DETECT), (77, mv.HEAVY_SLAM),
     (84, mv.BELLY_DRUM), (91, mv.FOCUS_PUNCH)),
    None, 0, False, "")

IRON_JUGULIS = Pokemon(
    993, "Iron Jugulis", 9, False,
    "", ("Dark", "Flying"),
    94, 101, 83, 108,
    ((1, mv.AIR_CUTTER), (1, mv.ELECTRIC_TERRAIN), (1, mv.FOCUS_ENERGY),
     (1, mv.TRI_ATTACK), (1, mv.WORK_UP), (7, mv.ROAR), (14, mv.ASSURANCE),
     (21, mv.DRAGON_BREATH), (28, mv.SNARL), (35, mv.CRUNCH),
     (42, mv.HYPER_VOICE), (56, mv.AIR_SLASH), (63, mv.KNOCK_OFF),
     (70, mv.DARK_PULSE), (77, mv.OUTRAGE), (84, mv.DRAGON_PULSE),
     (91, mv.HYPER_BEAM)),
    None, 0, False, "")

IRON_MOTH = Pokemon(
    994, "Iron Moth", 9, False,
    "", ("Fire", "Poison"),
    80, 105, 85, 110,
    ((1, mv.ACID_SPRAY), (1, mv.EMBER), (1, mv.GUST), (1, mv.WHIRLWIND),
     (7, mv.STRUGGLE_BUG), (14, mv.FIRE_SPIN), (21, mv.TAKE_DOWN),
     (28, mv.LUNGE), (35, mv.SCREECH), (42, mv.DISCHARGE),
     (49, mv.SLUDGE_WAVE), (56, mv.FIERY_DANCE), (63, mv.METAL_SOUND),
     (70, mv.MORNING_SUN), (77, mv.HURRICANE), (84, mv.BUG_BUZZ),
     (91, mv.OVERHEAT)),
    None, 0, False, "")

IRON_THORNS = Pokemon(
    995, "Iron Thorns", 9, False,
    "", ("Rock", "Electric"),
    100, 102, 97, 72,
    ((1, mv.FIRE_FANG), (1, mv.ICE_FANG), (1, mv.IRON_DEFENSE),
     (1, mv.ROCK_THROW), (1, mv.THUNDER_FANG), (7, mv.SCREECH),
     (21, mv.ROCK_TOMB), (28, mv.BITE), (35, mv.CHARGE), (42, mv.ROCK_SLIDE),
     (49, mv.SANDSTORM), (56, mv.WILD_CHARGE), (63, mv.PIN_MISSILE),
     (70, mv.EARTHQUAKE), (77, mv.STEALTH_ROCK), (84, mv.STONE_EDGE),
     (91, mv.GIGA_IMPACT)),
    None, 0, False, "")

BAXCALIBUR = Pokemon(
    998, "Baxcalibur", 9, False,
    "", ("Dragon", "Ice"),
    115, 110, 89, 87,
    ((0, mv.GLAIVE_RUSH), (1, mv.BREAKING_SWIPE), (1, mv.DRAGON_TAIL),
     (1, mv.ICE_SHARD), (1, mv.LEER), (1, mv.SNOWSCAPE), (1, mv.TACKLE),
     (6, mv.ICY_WIND), (12, mv.DRAGON_BREATH), (18, mv.FOCUS_ENERGY),
     (24, mv.BITE), (29, mv.ICE_FANG), (35, mv.DRAGON_CLAW),
     (42, mv.TAKE_DOWN), (48, mv.ICE_BEAM), (55, mv.CRUNCH),
     (62, mv.ICICLE_CRASH)),
    None, 0, False, "")

ARCTIBAX = Pokemon(
    997, "Arctibax", 9, False,
    "", ("Dragon", "Ice"),
    90, 70, 65, 62,
    ((1, mv.DRAGON_TAIL), (1, mv.LEER), (1, mv.TACKLE), (6, mv.ICY_WIND),
     (12, mv.DRAGON_BREATH), (18, mv.FOCUS_ENERGY), (24, mv.BITE),
     (29, mv.ICE_FANG), (40, mv.TAKE_DOWN), (45, mv.ICE_BEAM), (50, mv.CRUNCH),
     (55, mv.ICICLE_CRASH)),
    BAXCALIBUR, 54, True, "")

FRIGIBAX = Pokemon(
    996, "Frigibax", 9, False,
    "", ("Dragon", "Ice"),
    65, 55, 45, 55,
    ((1, mv.DRAGON_TAIL), (1, mv.LEER), (1, mv.TACKLE), (6, mv.ICY_WIND),
     (12, mv.DRAGON_BREATH), (18, mv.FOCUS_ENERGY), (24, mv.BITE),
     (29, mv.ICE_FANG), (32, mv.DRAGON_CLAW), (36, mv.TAKE_DOWN),
     (40, mv.ICE_BEAM), (44, mv.CRUNCH), (48, mv.ICICLE_CRASH)),
    ARCTIBAX, 35, True, "")

GHOLDENGO = Pokemon(
    1000, "Gholdengo", 9, False,
    "", ("Steel", "Ghost"),
    87, 96, 93, 84,
    ((1, mv.ASTONISH), (1, mv.TACKLE), (7, mv.NIGHT_SHADE),
     (14, mv.CONFUSE_RAY), (21, mv.SUBSTITUTE), (28, mv.METAL_SOUND),
     (35, mv.SHADOW_BALL), (42, mv.RECOVER), (49, mv.POWER_GEM),
     (56, mv.MAKE_IT_RAIN), (63, mv.NASTY_PLOT), (70, mv.MEMENTO)),
    None, 0, False, "")

GIMMIGHOUL = Pokemon(
    999, "Gimmighoul", 9, False,
    "", ("Ghost",),
    45, 52, 70, 10,
    ((1, mv.ASTONISH), (1, mv.TACKLE)),
    GHOLDENGO, 0, True, "gimmighoul-coins")

WO_CHIEN = Pokemon(
    1001, "Wo-Chien", 9, False,
    "", ("Dark", "Grass"),
    85, 90, 117, 70,
    ((1, mv.ABSORB), (1, mv.MEAN_LOOK), (1, mv.SPITE), (5, mv.TICKLE),
     (10, mv.PAYBACK), (15, mv.POISON_POWDER), (15, mv.STUN_SPORE),
     (20, mv.MEGA_DRAIN), (25, mv.LEECH_SEED), (30, mv.GROWTH),
     (35, mv.INGRAIN), (40, mv.DARK_PULSE), (45, mv.GIGA_DRAIN),
     (50, mv.RUINATION), (55, mv.FOUL_PLAY), (60, mv.POWER_WHIP),
     (65, mv.GRASSY_TERRAIN), (70, mv.KNOCK_OFF), (75, mv.LEAF_STORM)),
    None, 0, False, "")

CHIEN_PAO = Pokemon(
    1002, "Chien-Pao", 9, False,
    "", ("Dark", "Ice"),
    80, 105, 72, 135,
    ((1, mv.MEAN_LOOK), (1, mv.POWDER_SNOW), (1, mv.SPITE), (5, mv.ICY_WIND),
     (10, mv.PAYBACK), (15, mv.HAZE), (15, mv.MIST), (20, mv.ICE_SHARD),
     (25, mv.SWORDS_DANCE), (30, mv.SNOWSCAPE), (35, mv.NIGHT_SLASH),
     (40, mv.DARK_PULSE), (45, mv.ICICLE_CRASH), (50, mv.RUINATION),
     (55, mv.SUCKER_PUNCH), (60, mv.SACRED_SWORD), (65, mv.RECOVER),
     (70, mv.THROAT_CHOP), (75, mv.SHEER_COLD)),
    None, 0, False, "")

TING_LU = Pokemon(
    1003, "Ting-Lu", 9, False,
    "", ("Dark", "Ground"),
    155, 82, 102, 45,
    ((1, mv.MEAN_LOOK), (1, mv.SAND_TOMB), (1, mv.SPITE), (5, mv.SPIKES),
     (10, mv.PAYBACK), (15, mv.STOMP), (20, mv.BULLDOZE), (25, mv.WHIRLWIND),
     (30, mv.TAUNT), (35, mv.THRASH), (40, mv.DARK_PULSE),
     (45, mv.STOMPING_TANTRUM), (50, mv.RUINATION), (55, mv.THROAT_CHOP),
     (60, mv.ROCK_SLIDE), (65, mv.MEMENTO), (70, mv.EARTHQUAKE),
     (75, mv.FISSURE)),
    None, 0, False, "")

CHI_YU = Pokemon(
    1004, "Chi-Yu", 9, False,
    "", ("Dark", "Fire"),
    55, 107, 100, 100,
    ((1, mv.EMBER), (1, mv.MEAN_LOOK), (1, mv.SPITE), (5, mv.FLAME_WHEEL),
     (10, mv.PAYBACK), (15, mv.WILL_O_WISP), (20, mv.FLAME_CHARGE),
     (25, mv.INCINERATE), (30, mv.CONFUSE_RAY), (35, mv.NASTY_PLOT),
     (40, mv.DARK_PULSE), (45, mv.LAVA_PLUME), (50, mv.RUINATION),
     (55, mv.BOUNCE), (60, mv.SWAGGER), (65, mv.INFERNO), (70, mv.MEMENTO),
     (75, mv.OVERHEAT)),
    None, 0, False, "")

ROARING_MOON = Pokemon(
    1005, "Roaring Moon", 9, False,
    "", ("Dragon", "Dark"),
    105, 97, 86, 119,
    ((1, mv.BITE), (1, mv.DRAGON_BREATH), (1, mv.FOCUS_ENERGY), (1, mv.LEER),
     (7, mv.INCINERATE), (14, mv.HEADBUTT), (21, mv.SCARY_FACE),
     (28, mv.DRAGON_CLAW), (35, mv.ZEN_HEADBUTT), (42, mv.FLAMETHROWER),
     (49, mv.NIGHT_SLASH), (56, mv.DRAGON_DANCE), (63, mv.DRAGON_RUSH),
     (70, mv.FLY), (77, mv.THROAT_CHOP), (84, mv.ROOST), (91, mv.DOUBLE_EDGE)),
    None, 0, False, "")

IRON_VALIANT = Pokemon(
    1006, "Iron Valiant", 9, False,
    "", ("Fairy", "Fighting"),
    74, 125, 75, 116,
    ((1, mv.DISABLE), (1, mv.DOUBLE_TEAM), (1, mv.FURY_CUTTER),
     (1, mv.SHADOW_SNEAK), (7, mv.HYPNOSIS), (14, mv.FEINT),
     (21, mv.FUTURE_SIGHT), (28, mv.DAZZLING_GLEAM), (35, mv.PSYCHO_CUT),
     (42, mv.NIGHT_SLASH), (49, mv.LEAF_BLADE), (56, mv.MOONBLAST),
     (63, mv.CLOSE_COMBAT), (70, mv.KNOCK_OFF), (77, mv.DESTINY_BOND),
     (84, mv.QUICK_GUARD), (84, mv.WIDE_GUARD), (91, mv.SPIRIT_BREAK)),
    None, 0, False, "")

KORAIDON = Pokemon(
    1007, "Koraidon", 9, False,
    "", ("Fighting", "Dragon"),
    100, 110, 107, 135,
    ((1, mv.BREAKING_SWIPE), (1, mv.SUNNY_DAY), (7, mv.ROCK_SMASH),
     (14, mv.ANCIENT_POWER), (21, mv.DRAIN_PUNCH), (28, mv.BRICK_BREAK),
     (35, mv.AGILITY), (42, mv.DRAGON_CLAW), (49, mv.FLAMETHROWER),
     (56, mv.COLLISION_COURSE), (63, mv.SCREECH), (70, mv.COUNTER),
     (77, mv.OUTRAGE), (84, mv.CLOSE_COMBAT), (91, mv.FLARE_BLITZ),
     (98, mv.GIGA_IMPACT)),
    None, 0, False, "")

MIRAIDON = Pokemon(
    1008, "Miraidon", 9, False,
    "", ("Electric", "Dragon"),
    100, 110, 107, 135,
    ((1, mv.DRAGON_BREATH), (1, mv.ELECTRIC_TERRAIN), (1, mv.THUNDER_SHOCK),
     (7, mv.SHOCK_WAVE), (14, mv.CHARGE), (21, mv.PARABOLIC_CHARGE),
     (28, mv.DISCHARGE), (35, mv.AGILITY), (42, mv.DRAGON_PULSE),
     (56, mv.ELECTRO_DRIFT), (63, mv.METAL_SOUND), (70, mv.MIRROR_COAT),
     (77, mv.OUTRAGE), (84, mv.THUNDER), (91, mv.OVERHEAT),
     (98, mv.HYPER_BEAM)),
    None, 0, False, "")

WALKING_WAKE = Pokemon(
    1009, "Walking Wake", 9, False,
    "", ("Water", "Dragon"),
    99, 104, 87, 109,
    ((0, mv.AQUA_JET), (0, mv.LEER), (0, mv.ROAR), (0, mv.TWISTER),
     (7, mv.BITE), (14, mv.WATER_PULSE), (21, mv.NOBLE_ROAR),
     (28, mv.DRAGON_BREATH), (35, mv.BREAKING_SWIPE), (42, mv.DRAGON_RUSH),
     (56, mv.HYDRO_STEAM), (63, mv.DRAGON_PULSE), (70, mv.OUTRAGE),
     (77, mv.FLAMETHROWER), (84, mv.HYDRO_PUMP)),
    None, 0, False, "")

IRON_LEAVES = Pokemon(
    1010, "Iron Leaves", 9, False,
    "", ("Grass", "Psychic"),
    90, 100, 98, 104,
    ((0, mv.HELPING_HAND), (0, mv.LEER), (0, mv.QUICK_ATTACK), (0, mv.WORK_UP),
     (7, mv.MAGICAL_LEAF), (14, mv.RETALIATE), (21, mv.QUICK_GUARD),
     (28, mv.NIGHT_SLASH), (35, mv.SWORDS_DANCE), (42, mv.SACRED_SWORD),
     (49, mv.LEAF_BLADE), (56, mv.PSYBLADE), (63, mv.CLOSE_COMBAT),
     (70, mv.IMPRISON), (77, mv.MEGAHORN), (84, mv.ALLY_SWITCH),
     (91, mv.SOLAR_BLADE)),
    None, 0, False, "")

SINISTCHA = Pokemon(
    1013, "Sinistcha", 9, False,
    "", ("Grass", "Ghost"),
    71, 90, 93, 70,
    ((0, mv.MATCHA_GOTCHA), (1, mv.ASTONISH), (1, mv.STUN_SPORE),
     (1, mv.WITHDRAW), (6, mv.ABSORB), (12, mv.LIFE_DEW), (18, mv.FOUL_PLAY),
     (24, mv.MEGA_DRAIN), (30, mv.HEX), (36, mv.RAGE_POWDER),
     (42, mv.STRENGTH_SAP), (48, mv.SHADOW_BALL), (54, mv.MEMENTO),
     (60, mv.LEAF_STORM)),
    None, 0, False, "")

POLTCHAGEIST = Pokemon(
    1012, "Poltchageist", 9, False,
    "", ("Grass", "Ghost"),
    40, 59, 49, 50,
    ((1, mv.ASTONISH), (1, mv.STUN_SPORE), (1, mv.WITHDRAW), (6, mv.ABSORB),
     (12, mv.LIFE_DEW), (18, mv.FOUL_PLAY), (24, mv.MEGA_DRAIN), (30, mv.HEX),
     (36, mv.RAGE_POWDER), (42, mv.GIGA_DRAIN), (48, mv.SHADOW_BALL),
     (54, mv.MEMENTO), (60, mv.LEAF_STORM)),
    SINISTCHA, 0, True, "item:masterpiece-teacup")

OKIDOGI = Pokemon(
    1014, "Okidogi", 9, False,
    "", ("Poison", "Fighting"),
    88, 93, 100, 80,
    ((1, mv.BITE), (1, mv.BULK_UP), (1, mv.LOW_KICK), (8, mv.HOWL),
     (16, mv.POISON_FANG), (24, mv.FORCE_PALM), (32, mv.COUNTER),
     (40, mv.POISON_JAB), (48, mv.BRUTAL_SWING), (56, mv.CRUNCH),
     (64, mv.SUPERPOWER), (72, mv.GIGA_IMPACT)),
    None, 0, False, "")

MUNKIDORI = Pokemon(
    1015, "Munkidori", 9, False,
    "", ("Poison", "Psychic"),
    88, 102, 78, 106,
    ((1, mv.CONFUSION), (1, mv.FAKE_OUT), (1, mv.FLATTER), (1, mv.SCRATCH),
     (8, mv.HELPING_HAND), (16, mv.PSYBEAM), (24, mv.CLEAR_SMOG),
     (32, mv.POISON_JAB), (40, mv.PSYCHIC), (48, mv.SLUDGE_WAVE),
     (56, mv.NASTY_PLOT), (64, mv.FUTURE_SIGHT), (72, mv.PARTING_SHOT)),
    None, 0, False, "")

FEZANDIPITI = Pokemon(
    1016, "Fezandipiti", 9, False,
    "", ("Poison", "Fairy"),
    88, 80, 103, 99,
    ((1, mv.DISARMING_VOICE), (1, mv.DOUBLE_KICK), (1, mv.PECK),
     (1, mv.POISON_GAS), (8, mv.QUICK_ATTACK), (16, mv.ATTRACT),
     (24, mv.WING_ATTACK), (32, mv.CROSS_POISON), (40, mv.TAIL_SLAP),
     (48, mv.BEAT_UP), (56, mv.FLATTER), (56, mv.SWAGGER), (64, mv.ROOST),
     (72, mv.MOONBLAST)),
    None, 0, False, "")

OGERPON = Pokemon(
    1017, "Ogerpon", 9, False,
    "", ("Grass",),
    80, 90, 90, 110,
    ((1, mv.FOLLOW_ME), (1, mv.LEECH_SEED), (1, mv.QUICK_ATTACK),
     (1, mv.VINE_WHIP), (6, mv.FOCUS_ENERGY), (12, mv.GROWTH), (18, mv.SLAM),
     (24, mv.LOW_SWEEP), (30, mv.IVY_CUDGEL), (36, mv.THROAT_CHOP),
     (42, mv.SYNTHESIS), (48, mv.SPIKY_SHIELD), (54, mv.POWER_WHIP),
     (60, mv.SUPERPOWER), (66, mv.WOOD_HAMMER)),
    None, 0, False, "")

GOUGING_FIRE = Pokemon(
    1020, "Gouging Fire", 9, False,
    "", ("Fire", "Dragon"),
    105, 90, 107, 91,
    ((1, mv.INCINERATE), (1, mv.LEER), (1, mv.STOMP), (1, mv.SUNNY_DAY),
     (7, mv.FIRE_FANG), (14, mv.HOWL), (21, mv.BITE), (28, mv.DRAGON_CLAW),
     (35, mv.CRUSH_CLAW), (42, mv.MORNING_SUN), (49, mv.BURNING_BULWARK),
     (56, mv.DRAGON_RUSH), (63, mv.FIRE_BLAST), (70, mv.LAVA_PLUME),
     (77, mv.OUTRAGE), (84, mv.FLARE_BLITZ), (91, mv.RAGING_FURY)),
    None, 0, False, "")

RAGING_BOLT = Pokemon(
    1021, "Raging Bolt", 9, False,
    "", ("Electric", "Dragon"),
    125, 105, 90, 75,
    ((1, mv.SHOCK_WAVE), (1, mv.STOMP), (1, mv.SUNNY_DAY), (1, mv.TWISTER),
     (7, mv.CHARGE), (14, mv.DRAGON_BREATH), (21, mv.ELECTRIC_TERRAIN),
     (28, mv.DISCHARGE), (35, mv.DRAGON_TAIL), (42, mv.CALM_MIND),
     (49, mv.THUNDERCLAP), (56, mv.DRAGON_HAMMER), (63, mv.RISING_VOLTAGE),
     (70, mv.DRAGON_PULSE), (77, mv.ZAP_CANNON), (84, mv.BODY_PRESS),
     (91, mv.THUNDER)),
    None, 0, False, "")

IRON_BOULDER = Pokemon(
    1022, "Iron Boulder", 9, False,
    "", ("Rock", "Psychic"),
    90, 94, 94, 124,
    ((1, mv.ELECTRIC_TERRAIN), (1, mv.HORN_ATTACK), (1, mv.LEER),
     (1, mv.ROCK_THROW), (7, mv.QUICK_ATTACK), (14, mv.SLASH),
     (21, mv.AGILITY), (28, mv.PSYCHO_CUT), (35, mv.COUNTER),
     (42, mv.ROCK_TOMB), (49, mv.SACRED_SWORD), (56, mv.MIGHTY_CLEAVE),
     (63, mv.SWORDS_DANCE), (70, mv.MEGAHORN), (77, mv.QUICK_GUARD),
     (84, mv.STONE_EDGE), (91, mv.GIGA_IMPACT)),
    None, 0, False, "")

IRON_CROWN = Pokemon(
    1023, "Iron Crown", 9, False,
    "", ("Steel", "Psychic"),
    90, 97, 104, 98,
    ((1, mv.CONFUSION), (1, mv.ELECTRIC_TERRAIN), (1, mv.LEER),
     (1, mv.METAL_CLAW), (7, mv.SMART_STRIKE), (14, mv.SLASH),
     (21, mv.IRON_DEFENSE), (28, mv.PSYSHOCK), (35, mv.PSYCHO_CUT),
     (42, mv.FLASH_CANNON), (49, mv.SACRED_SWORD), (56, mv.TACHYON_CUTTER),
     (63, mv.FUTURE_SIGHT), (70, mv.VOLT_SWITCH), (77, mv.QUICK_GUARD),
     (84, mv.METAL_BURST), (91, mv.HYPER_BEAM)),
    None, 0, False, "")

TERAPAGOS = Pokemon(
    1024, "Terapagos", 9, False,
    "", ("Normal",),
    90, 65, 85, 60,
    ((1, mv.RAPID_SPIN), (1, mv.TRI_ATTACK), (1, mv.WITHDRAW),
     (10, mv.ANCIENT_POWER), (20, mv.HEADBUTT), (30, mv.PROTECT),
     (40, mv.EARTH_POWER), (50, mv.HEAVY_SLAM), (60, mv.TERA_STARSTORM),
     (70, mv.DOUBLE_EDGE), (80, mv.ROCK_POLISH), (90, mv.GYRO_BALL)),
    None, 0, False, "")

PECHARUNT = Pokemon(
    1025, "Pecharunt", 9, False,
    "", ("Poison", "Ghost"),
    88, 88, 124, 88,
    ((1, mv.ASTONISH), (1, mv.MEMENTO), (1, mv.POISON_GAS), (1, mv.SMOG),
     (8, mv.WITHDRAW), (16, mv.DESTINY_BOND), (24, mv.FAKE_TEARS),
     (32, mv.PARTING_SHOT), (40, mv.SHADOW_BALL), (48, mv.MALIGNANT_CHAIN),
     (56, mv.TOXIC), (64, mv.NASTY_PLOT), (72, mv.RECOVER)),
    None, 0, False, "")
