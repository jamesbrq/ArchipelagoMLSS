from BaseClasses import Tutorial, ItemClassification
from ..AutoWorld import WebWorld, World
from .Locations import all_locations
from .Options import MLSS_Options
from .Regions import create_regions, connect_regions
from .Rules import set_rules
from .Items import MLSSItem, itemList, item_frequencies, item_table


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


class MLSSWorld(World):
    """
    MLSS funny haha
    """
    game = "Mario & Luigi Superstar Saga"
    web = MLSSWebWorld()
    data_version = 1
    option_definitions = MLSS_Options
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}
      
    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player)
        connect_regions(self.multiworld, self.player)
        
    def create_items(self) -> None:
        # First add in all progression and useful items
        required_items = []
        for item in itemList:
            if item.progression != ItemClassification.filler:
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
                print(item.itemName)
                freq = item_frequencies.get(item.itemName)
                if freq is None:
                    freq = 1
                filler_items += [item.itemName for _ in range(freq)]

        remaining = len(all_locations) - len(required_items)
        print(remaining)
        print(len(filler_items))
        for i in range(remaining):
            filler_item_name = self.multiworld.random.choice(filler_items)
            item = self.create_item(filler_item_name)
            self.multiworld.itempool.append(item)
            filler_items.remove(filler_item_name)
    
    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.can_reach("Bowser's Castle", "Region", self.player)
            
    def create_item(self, name: str) -> MLSSItem:
        item = item_table[name]
        return MLSSItem(item.itemName, item.progression, item.code, self.player)
