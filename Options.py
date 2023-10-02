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


class MarioColor(Choice):
    """Mario Color Option"""
    display_name = "Mario's Color"
    option_red = 0
    option_green = 1
    default = 0


class LuigiColor(Choice):
    """Luigi Color Option"""
    display_name = "Luigi's Color"
    option_green = 0
    option_red = 1
    default = 0


MLSS_Options: typing.Dict[str, type(Option)] = {
    "SkipInto": IntroSkip,
    "CastleSkip": BowsersCastleSkip,
    "CastleStart": CastleStart,
    "SkipMinecart": SkipMinecart,
    "DisableSurf": DisableSurf,
    "MarioColor": MarioColor,
    "LuigiColor": LuigiColor
}
