import typing
from Options import Choice, Option, Toggle


class IntroSkip(Toggle):
    """Intro Skip option"""
    display_name = "Intro Skip"


class BowsersCastleSkip(Toggle):
    """Bowser's Castle Skip Option"""
    display_name = "Bowser's Castle Skip"


class CastleStart(Toggle):
    """Castle Start option"""
    display_name = "Start in Castle Town"


class SkipMinecart(Toggle):
    """Skip Minecart Minigame Option"""
    display_name = "Skip Minecart Minigame"


class DisableSurf(Toggle):
    """Disable Surf Minigame Option"""
    display_name = "Disable Surf Minigame"


class RandomMusic(Toggle):
    """Randomize Music Option"""
    display_name = "Randomize Music"


class DisableMusic(Toggle):
    """Disable Music Option"""
    display_name = "Disable Music"


class RandomSounds(Toggle):
    """Randomize Sounds Option"""
    display_name = "Randomize Sounds"


class MarioColor(Choice):
    """Mario Color Option"""
    display_name = "Mario's Color"
    option_red = 0
    option_green = 1
    option_blue = 2
    option_cyan = 3
    option_yellow = 4
    option_orange = 5
    option_purple = 6
    option_pink = 7
    option_black = 8
    option_white = 9
    option_silhouette = 10
    option_chaos = 11
    option_truechaos = 12
    default = 0


class LuigiColor(Choice):
    """Luigi Color Option"""
    display_name = "Luigi's Color"
    option_red = 0
    option_green = 1
    option_blue = 2
    option_cyan = 3
    option_yellow = 4
    option_orange = 5
    option_purple = 6
    option_pink = 7
    option_black = 8
    option_white = 9
    option_silhouette = 10
    option_chaos = 11
    option_truechaos = 12
    default = 1


class MarioPants(Choice):
    """Mario Pants Color Option"""
    display_name = "Mario's Pants Color"
    option_vanilla = 0
    option_red = 1
    option_green = 2
    option_blue = 3
    option_cyan = 4
    option_yellow = 5
    option_orange = 6
    option_purple = 7
    option_pink = 8
    option_black = 9
    option_white = 10
    option_chaos = 11
    default = 0


class LuigiPants(Choice):
    """Luigi Pants Color Option"""
    display_name = "Luigi's Pants Color"
    option_vanilla = 0
    option_red = 1
    option_green = 2
    option_blue = 3
    option_cyan = 4
    option_yellow = 5
    option_orange = 6
    option_purple = 7
    option_pink = 8
    option_black = 9
    option_white = 10
    option_chaos = 11
    default = 0


class RandomizeEnemies(Toggle):
    """Randomize Enemies Option"""
    display_name = "Randomize Enemies"


class RandomizeBosses(Choice):
    """Randomize Bosses Option"""
    display_name = "Randomize Bosses"
    option_none = 0
    option_bossonly = 1
    option_bossnormal = 2
    default = 0


class ScaleStats(Toggle):
    """Scale Stats Option"""
    display_name = "Scale Enemy Stats"


class ScalePow(Toggle):
    """Scale POW Option"""
    display_name = "Scale Enemy POW"


class RandomizeBackgrounds(Toggle):
    """Randomize Backgrounds Option"""
    display_name = "Randomize Battle Backgrounds"


mlss_options: typing.Dict[str, type(Option)] = {
    "skip_intro": IntroSkip,
    "castle_skip": BowsersCastleSkip,
    "castle_start": CastleStart,
    "skip_minecart": SkipMinecart,
    "disable_surf": DisableSurf,
    "randomize_music": RandomMusic,
    "disable_music": DisableMusic,
    "randomize_sounds": RandomSounds,
    "randomize_enemies": RandomizeEnemies,
    "randomize_bosses": RandomizeBosses,
    "randomize_backgrounds": RandomizeBackgrounds,
    "scale_stats": ScaleStats,
    "scale_pow": ScalePow,
    "mario_color": MarioColor,
    "luigi_color": LuigiColor,
    "mario_pants": MarioPants,
    "luigi_pants": LuigiPants
}
