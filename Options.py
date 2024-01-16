import typing
from Options import Choice, Option, Toggle, StartInventoryPool


class IntroSkip(Toggle):
    """
    Skip the intro sequence. Spawns you in pipe 1 on game start.
    This does not affect any items.
    """
    display_name = "Intro Skip"


class BowsersCastleSkip(Toggle):
    """
    Skip straight from the entrance hall to bowletta in Bowser's Castle.
    All Bowser's Castle items will be removed from the location pool.
    """
    display_name = "Bowser's Castle Skip"


class ExtraPipes(Toggle):
    """
    Gives the player access to pipes 1, 3, 4, and 6 from the start.
    """
    display_name = "Start With Extra Pipes"


class SkipMinecart(Toggle):
    """
    Skip the minecart minigame that leads you through Hoohoo Mountain Base.
    This will remove the 1 item in the minecart cave from the location pool.
    """
    display_name = "Skip Minecart Minigame"


class DisableSurf(Toggle):
    """
    Remove the surf minigame item from the location pool.
    """
    display_name = "Disable Surf Minigame"


class RandomMusic(Toggle):
    """
    Randomize all music in the game, including overworld, battle, and all minigame and menu music.
    Includes unused beta music tracks as well.
    """
    display_name = "Randomize Music"


class DisableMusic(Toggle):
    """
    Disable all music in the game. You will still hear all normal sounds but there will be no music.
    """
    display_name = "Disable Music"


class RandomSounds(Toggle):
    """
    Randomizes every sound in the game, minus a few sounds that can softlock the game* (UNSTABLE OPTION)
    """
    display_name = "Randomize Sounds"


class MarioColor(Choice):
    """
    This changes the color of Mario's hat, as well as some key colors that are red including UI etc.
    """
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
    """
    This changes the color of Luigi's hat, as well as some key colors that are green including UI etc.
    """
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
    """
    This changes the color of Mario's trousers.
    """
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
    """
    This changes the color of Luigi's trousers.
    """
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
    """
    Randomize all normal enemy encounters in the game.
    If Bowser's castle skip is enabled then enemies from Bowser's Castle will not be included.
    """
    display_name = "Randomize Enemies"


class RandomizeBosses(Choice):
    """
    Randomize all boss encounters in the game.
    If Bowser's castle skip is enabled then bosses from Bowser's Castle will not be included.
    Some bosses are not randomized due to flags, and story (Such as the final boss)
    Boss Only: Bosses will only be swapped with another boss.
    Boss Normal: Bosses can be swapped with normal enemy encounters.
    """
    display_name = "Randomize Bosses"
    option_none = 0
    option_bossonly = 1
    option_bossnormal = 2
    default = 0


class ScaleStats(Toggle):
    """
    This scales enemy HP and XP according to the area of the game you are in scaling linearly.
    """
    display_name = "Scale Enemy Stats"


class ScalePow(Toggle):
    """
    This scales enemy POW according to the area of the game you are in scaling linearly.
    """
    display_name = "Scale Enemy POW"


class TattleHp(Toggle):
    """
    This will display the enemies current and max health while in battle.
    """
    display_name = "Tattle HP"


class RandomizeBackgrounds(Toggle):
    """
    This randomizes the background image in battles
    """
    display_name = "Randomize Battle Backgrounds"


class HiddenVisible(Toggle):
    """
    This makes any hidden blocks in the game into regular item blocks.
    """
    display_name = "Hidden Blocks Visible"


class BlocksInvisible(Toggle):
    """
    Turns any item blocks in the game into hidden blocks.
    """
    display_name = "Item Blocks Invisible"


class Coins(Toggle):
    """
    Add all coin blocks in the game to the location pool.
    """
    display_name = "Coin Blocks"


class HarhallsPants(Toggle):
    """
    This will remove the Harhall's Pants check from the pool.
    """
    display_name = "Remove Harhall's Pants"


class DifficultLogic(Toggle):
    """
    This adjusts the logic to be more difficult in a few areas,
    allowing for the logic to account for players getting to certain area's in unintended ways.
    Enable at your own risk, this is not an option made for beginners.
    """
    display_name = "Difficult Logic Toggle"


class ChuckleBeans(Choice):
    """
    Choose how you want chuckle bean digspots to be randomized.
    none: No chuckle bean digspots will be added into the item pool.
    only_visible: Only chuckle bean digspots clearly marked with an X will be added into the item pool.
    all: All chuckle bean digspots will be added into the item pool.
    """
    display_name = "Chuckle Beans"
    option_none = 0
    option_only_visible = 1
    option_all = 2
    default = 2


mlss_options: typing.Dict[str, type(Option)] = {
    "start_inventory_from_pool": StartInventoryPool,
    "coins": Coins,
    "difficult_logic": DifficultLogic,
    "skip_intro": IntroSkip,
    "castle_skip": BowsersCastleSkip,
    "extra_pipes": ExtraPipes,
    "skip_minecart": SkipMinecart,
    "disable_surf": DisableSurf,
    "harhalls_pants": HarhallsPants,
    "hidden_visible": HiddenVisible,
    "blocks_invisible": BlocksInvisible,
    "chuckle_beans": ChuckleBeans,
    "randomize_music": RandomMusic,
    "disable_music": DisableMusic,
    "randomize_sounds": RandomSounds,
    "randomize_enemies": RandomizeEnemies,
    "randomize_bosses": RandomizeBosses,
    "randomize_backgrounds": RandomizeBackgrounds,
    "scale_stats": ScaleStats,
    "scale_pow": ScalePow,
    "tattle_hp": TattleHp,
    "mario_color": MarioColor,
    "luigi_color": LuigiColor,
    "mario_pants": MarioPants,
    "luigi_pants": LuigiPants
}
