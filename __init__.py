import typing
import settings
from BaseClasses import Tutorial, ItemClassification
from ..AutoWorld import WebWorld, World
from .Locations import all_locations, location_table, bowsers, bowsersMini
from .Options import mlss_options
from .Regions import create_regions, connect_regions
from .Rules import set_rules
from .Items import MLSSItem, itemList, item_frequencies, item_table
from .Rom import Rom
from .Names.LocationName import LocationName
from .Client import MLSSClient


class MLSSWebWorld(WebWorld):
    settings_page = "games/MLSS/info/en"
    theme = 'partyTime'
    tutorials = [
        Tutorial(
            tutorial_name='Setup Guide',
            description='A guide to playing Mario & Luigi Superstar Saga',
            language='English',
            file_name='setup_en.md',
            link='setup/en',
            authors=['jamesbrq']
        )
    ]


class MLSSSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the MLSS US rom"""
        copy_to = "Mario & Luigi - Superstar Saga (U).gba"
        description = "MLSS ROM File"
        md5s = [Rom.hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True


class MLSSWorld(World):
    """
    MLSS funny haha
    """
    game = "Mario & Luigi Superstar Saga"
    web = MLSSWebWorld()
    data_version = 1
    option_definitions = mlss_options
    settings = typing.ClassVar[MLSSSettings]
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}
    required_client_version = (0, 4, 3)

    excluded_locations = []

    def generate_early(self) -> None:
        if self.multiworld.skip_minecart[self.player]:
            self.excluded_locations += [LocationName.HoohooMountainBaseMinecartCaveDigspot]
        if self.multiworld.disable_surf[self.player]:
            self.excluded_locations += [LocationName.SurfMinigame]

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.excluded_locations)
        connect_regions(self.multiworld, self.player)

    def generate_basic(self) -> None:
        item = self.create_item("Mushroom")
        self.multiworld.get_location(LocationName.ShopStartingFlag1, self.player).place_locked_item(item)
        item = self.create_item("Syrup")
        self.multiworld.get_location(LocationName.ShopStartingFlag2, self.player).place_locked_item(item)
        item = self.create_item("1-UP Mushroom")
        self.multiworld.get_location(LocationName.ShopStartingFlag3, self.player).place_locked_item(item)

    def create_items(self) -> None:
        # First add in all progression and useful items
        required_items = []
        precollected = [item for item in itemList if item in self.multiworld.precollected_items[self.player]]
        for item in itemList:
            if item.progression != ItemClassification.filler and item not in precollected:
                freq = item_frequencies.get(item.itemName, 1)
                if freq is None:
                    freq = 1
                required_items += [item.itemName for _ in range(freq)]

        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        # Then, get a random amount of fillers until we have as many items as we have locations
        filler_items = []
        for item in itemList:
            if item.progression == ItemClassification.filler:
                freq = item_frequencies.get(item.itemName)
                if freq is None:
                    freq = 1
                filler_items += [item.itemName for _ in range(freq)]

        remaining = len(all_locations) - len(required_items) - 3
        if self.multiworld.castle_skip[self.player]:
            remaining -= (len(bowsers) + len(bowsersMini))
        if self.multiworld.skip_minecart[self.player]:
            remaining -= 1
        if self.multiworld.disable_surf[self.player]:
            remaining -= 1
        for i in range(remaining):
            filler_item_name = self.multiworld.random.choice(filler_items)
            item = self.create_item(filler_item_name)
            self.multiworld.itempool.append(item)
            filler_items.remove(filler_item_name)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.excluded_locations)
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.can_reach("PostJokes", "Region", self.player)

    def create_item(self, name: str) -> MLSSItem:
        item = item_table[name]
        return MLSSItem(item.itemName, item.progression, item.code, self.player)

    def generate_output(self, output_directory: str) -> None:
        rom = Rom(self.multiworld, self.player)

        for location_name in location_table.keys():
            if (self.multiworld.skip_minecart[self.player] and "Minecart" in location_name and "After" not in location_name) or (self.multiworld.castle_skip[self.player] and "Bowser" in location_name) or (self.multiworld.disable_surf[self.player] and "Surf Minigame" in location_name):
                continue
            location = self.multiworld.get_location(location_name, self.player)
            item = location.item
            address = [address for address in all_locations if address.name == location.name]
            rom.item_inject(location.address, address[0].itemType, item)
            if "Shop" in location_name and "Coffee" not in location_name and item.player != self.player:
                rom.desc_inject(location, item)
        rom.patch_options()

        rom.close(output_directory)
