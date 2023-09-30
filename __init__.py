from BaseClasses import Tutorial
from ..AutoWorld import WebWorld, World


class MLSSWebWorld(WebWorld):
    settings_page = "games/MLSS/info/en"
    theme = 'partyTime'
    tutorials = [
        Tutorial(
            tutorial_name='Setup Guide',
            description='A guide to playing Mario & Luigi: Superstar Saga',
            language='English',
            file_name='setup_en.md',
            link='setup/en',
            authors=['jamesbrq']
        )
    ]


class MLSSWorld(World):
    """
    MLSS funny haha
    """
    game = "Mario & Luigi: Superstar Saga"
    web = MLSS_WebWorld()
    data_version = 1