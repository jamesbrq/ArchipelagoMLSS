import typing

from BaseClasses import Location


class LocationData:
    name: str = ""
    id: int = 0x00

    flag_byte: int = 0x2000030
    flag_mask: int = 0x01

    def __init__(self, name, id_, flag, mask):
        self.name = name
        self.id = id_
        self.flag_byte = flag
        self.flag_mask = mask


class MLSSLocation(Location):
    game: str = "Mario & Luigi Superstar Saga"


mainArea: typing.List[LocationData] = [
    LocationData("Stardust Fields 1 Block 1", 0x39d65d, 0x02000000, 0x00),
    LocationData("Stardust Fields 1 Block 2", 0x39d665, 0x02000000, 0x00),
    LocationData("Stardust Fields 2 Block", 0x39d678, 0x02000000, 0x00),
    LocationData("Stardust Fields 3 Block", 0x39d6ad, 0x02000000, 0x00),
    LocationData("Stardust Fields 4 Block 1", 0x39d6ca, 0x02000000, 0x00),
    LocationData("Stardust Fields 4 Block 2", 0x39d6c2, 0x02000000, 0x00),
    LocationData("Stardust Fields 4 Block 3", 0x39d6ba, 0x02000000, 0x00),
    LocationData("Stardust Fields 5 Block", 0x39d713, 0x02000000, 0x00),
    LocationData("Hoohoo Village Hammer House Block", 0x39d731, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Below Summit Block 1", 0x39d873, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Below Summit Block 2", 0x39d87b, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Below Summit Block 3", 0x39d883, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain After Hoohooros Block 1", 0x39d890, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain After Hoohooros Block 2", 0x39d8a0, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Hoohooros Room Block 1", 0x39d8ad, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Hoohooros Room Block 2", 0x39d8b5, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Before Hoohooros Block", 0x39d8d2, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Fountain Room Block 1", 0x39d8f2, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Fountain Room Block 2", 0x39d8fa, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Room 1 Block 1", 0x39d91c, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Room 1 Block 2", 0x39d924, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Room 1 Block 3", 0x39d92c, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Room 1 Block", 0x39d939, 0x02000000, 0x00),
    LocationData("Hoohoo Village Right Side Block", 0x39d957, 0x02000000, 0x00),
    LocationData("Hoohoo Village Bridge Room Block 1", 0x39d96f, 0x02000000, 0x00),
    LocationData("Hoohoo Village Bridge Room Block 2", 0x39d97f, 0x02000000, 0x00),
    LocationData("Hoohoo Village Bridge Room Block 3", 0x39d98f, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Bridge Room Block 1", 0x39d99c, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Bridge Room Block 2", 0x39d9a4, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Bridge Room Block 3", 0x39d9ac, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Bridge Room Block 4", 0x39d9b4, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Bridge Room Digspot", 0x39d9bc, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Boostatue Room Block 1", 0x39d9c9, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Boostatue Room Block 2", 0x39d9d1, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 1", 0x39d9d9, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 2", 0x39d9e1, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Grassy Area Block 1", 0x39d9fe, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Grassy Area Block 2", 0x39d9f6, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base After Minecart Minigame Block 1", 0x39da35, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base After Minecart Minigame Block 2", 0x39da2d, 0x02000000, 0x00),
    LocationData("Cave Connecting Stardust Fields and Hoohoo Village Block 1", 0x39da77, 0x02000000, 0x00),
    LocationData("Cave Connecting Stardust Fields and Hoohoo Village Block 2", 0x39da7f, 0x02000000, 0x00),
    LocationData("Hoohoo Village South Cave Block", 0x39dacd, 0x02000000, 0x00),
    LocationData("Hoohoo Village North Cave Room 1 Block", 0x39da98, 0x02000000, 0x00),
    LocationData("Hoohoo Village North Cave Room 2 Block", 0x39dab5, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Surf Beach Block", 0x39dd03, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Star Room Block 1", 0x39e13d, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Star Room Block 2", 0x39e145, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Star Room Block 3", 0x39e14d, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Sun Door Block 1", 0x39e15a, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Sun Door Block 2", 0x39e162, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 1", 0x39e1f0, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 2", 0x39e1f8, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 3", 0x39e200, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Fountain Room 2 Block", 0x39e8f5, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Block", 0x39e912, 0x02000000, 0x00),
    LocationData("Outside Woohoo Hooniversity Block", 0x39e9b5, 0x02000000, 0x00),
    LocationData("Shop Starting Flag 1", 0x3c05f0, 0x02000000, 0x00),
    LocationData("Shop Starting Flag 2", 0x3c05f2, 0x02000000, 0x00),
    LocationData("Shop Starting Flag 3", 0x3c05f4, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Summit Digspot", 0x39d85e, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Below Summit Digspot", 0x39d86b, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain After Hoohooros Digspot", 0x39d898, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Hoohooros Room Digspot 1", 0x39d8bd, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Hoohooros Room Digspot 2", 0x39d8c5, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Before Hoohooros Digspot", 0x39d8e2, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Room 2 Digspot 1", 0x39d907, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Room 2 Digspot 2", 0x39d90f, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Room 1 Digspot", 0x39d941, 0x02000000, 0x00),
    LocationData("Hoohoo Village Right Side Digspot", 0x39d95f, 0x02000000, 0x00),
    LocationData("Hoohoo Village Super Hammer Cave Digspot", 0x39db02, 0x02000000, 0x00),
    LocationData("Hoohoo Village Super Hammer Cave Block", 0x39daea, 0x02000000, 0x00),
    LocationData("Hoohoo Village North Cave Room 2 Digspot", 0x39daad, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Minecart Cave Digspot", 0x39db0f, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Farm Room Digspot 1", 0x39db22, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Farm Room Digspot 2", 0x39db2a, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Farm Room Digspot 3", 0x39db32, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NW Block", 0x39db87, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NW Digspot", 0x39db97, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts W Digspot 1", 0x39dbac, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts W Digspot 2", 0x39dbb4, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts W Digspot 3", 0x39dbbc, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SW Digspot 1", 0x39dbc9, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SW Digspot 2", 0x39dbd9, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SW Digspot 3", 0x39dbe1, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts N Room 1 Digspot", 0x39dbee, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts N Room 2 Digspot", 0x39dbfb, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 1 Digspot 1", 0x39dc08, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 1 Block", 0x39dc20, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 1 Digspot 2", 0x39dc28, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 2 Block 1", 0x39dc4d, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NE Digspot 1", 0x39dc7a, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NE Digspot 2", 0x39dc82, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts E Digspot 1", 0x39dc8f, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts E Digspot 2", 0x39dc97, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts E Digspot 3", 0x39dc9f, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SE Digspot 1", 0x39dcac, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SE Digspot 2", 0x39dcbc, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts SE Digspot 3", 0x39dcc4, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts North Beach Digspot 1", 0x39dcd1, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts North Beach Digspot 2", 0x39dce1, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts North Beach Digspot 3", 0x39dcd9, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts South Beach Digspot", 0x39dcee, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room Digspot 1", 0x39e17f, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room Digspot 2", 0x39e187, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 2 Digspot", 0x39e1d6, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 3 Digspot", 0x39e1e3, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 4 Digspot 1", 0x39e208, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 4 Digspot 2", 0x39e210, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity West of Star Room 5 Digspot", 0x39e21d, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room Digspot 1", 0x39e22a, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room Digspot 2", 0x39e232, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room 2 Digspot", 0x39e23f, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Block", 0x39e24c, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Digspot", 0x39e254, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 1", 0x39e261, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 2", 0x39e269, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 3", 0x39e271, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 4", 0x39e279, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Fountain Room 2 Digspot", 0x39e8fd, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Digspot 1", 0x39e90a, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Digspot 2", 0x39e91a, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Secret Scroll 1", 0x1e9411, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Secret Scroll 2", 0x1e9412, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 1", 0x229345, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 2", 0x22954d, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 3", 0x228a17, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 4", 0x22913a, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 5", 0x22890e, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 6", 0x228775, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Bean Fruit 7", 0x1e9431, 0x02000000, 0x00),
    LocationData("Hoohoo Village Mole Behind Turtle", 0x277ab2, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NE Solo Mario Mole 2", 0x1e9436, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Thunder Hand Mole", 0x2779c8, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Peasley's Rose", 0x1e9430, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Super Hammer Upgrade", 0x1e9404, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Ultra Hammer Upgrade", 0x1e9405, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts NE Solo Mario Mole 1", 0x1e9435, 0x02000000, 0x00),
    LocationData("Hoohoo Village Hammers", 0x1e9403, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Solo Luigi Cave Mole", 0x242888, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Farm Room Mole Reward 1", 0x243844, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Farm Room Mole Reward 2", 0x24387d, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 1", 0x39e990, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 2", 0x39e998, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 3", 0x39e9a0, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Entrance to Hoohoo Mountain Base Digspot 1", 0x39eb5a, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Entrance to Hoohoo Mountain Base Digspot 2", 0x39eb62, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Pipe 2 Room Digspot", 0x39ec40, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Pipe 4 Room Digspot", 0x39ec4d, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Mini Mario Block 1", 0x39d813, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Mini Mario Block 2", 0x39d81b, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Mini Mario Block 3", 0x39d823, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Mini Mario Block 4", 0x39d82b, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Mini Mario Block 5", 0x39d833, 0x02000000, 0x00)
]

baseUltraRocks: typing.List[LocationData] = [
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 1", 0x39da42, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 2", 0x39da4a, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 3", 0x39da52, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 3", 0x39d9e9, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Mole Near Teehee Valley", 0x277a45, 0x02000000, 0x00),
    LocationData("Teehee Valley Entrance To Hoohoo Mountain Digspot", 0x39e5b5, 0x02000000, 0x00),
    LocationData("Teehee Valley Solo Luigi Maze Room 2 Digspot 1", 0x39e5c8, 0x02000000, 0x00),
    LocationData("Teehee Valley Solo Luigi Maze Room 2 Digspot 2", 0x39e5d0, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Guffawha Ruins Entrance Digspot", 0x39da0b, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Teehee Valley Entrance Digspot", 0x39da20, 0x02000000, 0x00),
    LocationData("Hoohoo Mountain Base Teehee Valley Entrance Block", 0x39da18, 0x02000000, 0x00)
]

booStatue: typing.List[LocationData] = [
    LocationData("Beanbean Outskirts Before Harhall Digspot 1", 0x39e951, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Before Harhall Digspot 2", 0x39e959, 0x02000000, 0x00),
    LocationData("Beanstar Piece Harhall", 0x1e9441, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Boo Statue Mole", 0x1e9434, 0x02000000, 0x00),
    LocationData("Harhall's Pants", 0x1e9444, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 2 Digspot 1", 0x39dc65, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 2 Digspot 2", 0x39dc5d, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 2 Block 2", 0x39dc45, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts S Room 2 Digspot 3", 0x39dc35, 0x02000000, 0x00)
]

chucklehuck: typing.List[LocationData] = [
    LocationData("Chateau Room 1 Digspot", 0x39dd20, 0x02000000, 0x00),
    LocationData("Chateau Popple Fight Room Block 1", 0x39dd38, 0x02000000, 0x00),
    LocationData("Chateau Popple Fight Room Block 2", 0x39dd48, 0x02000000, 0x00),
    LocationData("Chateau Popple Fight Room Digspot", 0x39dd50, 0x02000000, 0x00),
    LocationData("Chateau Barrel Room Digspot ", 0x39dd5d, 0x02000000, 0x00),
    LocationData("Chateau Goblet Room Digspot", 0x39dd6d, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Cave Room 1 Block 1", 0x39dd82, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Cave Room 1 Block 2", 0x39dd8a, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Cave Room 2 Block", 0x39dd9f, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Cave Room 3 Block", 0x39ddac, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 2 Block", 0x39ddc1, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 2 Digspot", 0x39ddc9, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Pipe Room Block 1", 0x39ddd6, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Pipe Room Block 2", 0x39ddde, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Pipe Room Digspot 1", 0x39ddee, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Pipe Room Digspot 2", 0x39ddf6, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 4 Block 1", 0x39de06, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 4 Block 2", 0x39de0e, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 4 Block 3", 0x39de16, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 7 Block 1", 0x39de29, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 7 Block 2", 0x39de39, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 7 Digspot 1", 0x39de41, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 7 Digspot 2", 0x39de49, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 8 Digspot", 0x39de56, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods East of Chuckleroot Digspot", 0x39de66, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 1", 0x39de73, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 2", 0x39de7b, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 3", 0x39de83, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 4", 0x39de8b, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 1", 0x39de98, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 2", 0x39dea0, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 3", 0x39dea8, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods West of Chuckleroot Block", 0x39deb5, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Southwest of Chuckleroot Block", 0x39dec2, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Wiggler room Digspot 1", 0x39decf, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Wiggler room Digspot 2", 0x39ded7, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 1", 0x39dee4, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 2", 0x39deec, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 3", 0x39def4, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 4", 0x39defc, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 5", 0x39df04, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods After Chuckleroot Block 6", 0x39df0c, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Koopa Room Block 1", 0x39df4b, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Koopa Room Block 2", 0x39df5b, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Koopa Room Digspot", 0x39df63, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Room 1 Digspot", 0x39e1c9, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Brooch Guards Room Digspot 1", 0x39e966, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Brooch Guards Room Digspot 2", 0x39e96e, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Chateau Entrance Digspot 1", 0x39e97b, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Chateau Entrance Digspot 2", 0x39e983, 0x02000000, 0x00),
    LocationData("Chateau Green Goblet", 0x24e628, 0x02000000, 0x00),
    LocationData("Chateau Red Goblet", 0x1e943e, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Red Chuckola Fruit", 0x250621, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods White Chuckola Fruit", 0x24ff18, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Purple Chuckola Fruit", 0x24ed74, 0x02000000, 0x00)
]

castleTown: typing.List[LocationData] = [
    LocationData("Beanbean Castle Town Left Side House Block 1", 0x39d7a4, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Left Side House Block 2", 0x39d7ac, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Left Side House Block 3", 0x39d7b4, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Left Side House Block 4", 0x39d7bc, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Right Side House Block 1", 0x39d7d8, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Right Side House Block 2", 0x39d7e0, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Right Side House Block 3", 0x39d7e8, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Right Side House Block 4", 0x39d7f0, 0x02000000, 0x00),
    LocationData("Beanbean Castle Peach's Extra Dress", 0x1e9433, 0x02000000, 0x00),
    LocationData("Beanbean Castle Fake Beastar", 0x1e9432, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet 1", 0x251347, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet 2", 0x2513fb, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet 3", 0x2513a1, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet 4", 0x251988, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet 5", 0x25192e, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 1", 0x25117d, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 2", 0x2511d6, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 3", 0x25122f, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 4", 0x251288, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 5", 0x2512e1, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 6", 0x2517c3, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 7", 0x25181f, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 8", 0x25187b, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 9", 0x25170b, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone 10", 0x251767, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 1", 0x253515, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 2", 0x253776, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 3", 0x253c70, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 4", 0x254324, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 5", 0x254718, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 6", 0x254a34, 0x02000000, 0x00),
    LocationData("Coffee Shop Brew Reward 7", 0x254e24, 0x02000000, 0x00),
    LocationData("Coffee Shop Woohoo Blend", 0x252d07, 0x02000000, 0x00),
    LocationData("Coffee Shop Hoohoo Blend", 0x252d28, 0x02000000, 0x00),
    LocationData("Coffee Shop Chuckle Blend", 0x252d49, 0x02000000, 0x00),
    LocationData("Coffee Shop Teehee Blend", 0x252d6a, 0x02000000, 0x00),
    LocationData("Coffee Shop Hoolumbian", 0x252d8b, 0x02000000, 0x00),
    LocationData("Coffee Shop Chuckoccino", 0x252dac, 0x02000000, 0x00),
    LocationData("Coffee Shop Teeheespresso", 0x252dcd, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanstone Reward", 0x251071, 0x02000000, 0x00),
    LocationData("Beanbean Castle Town Beanlet Reward", 0x2515eb, 0x02000000, 0x00)
]

startingFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Starting Flag 1", 0x3c0618, 0x02000000, 0x00),
    LocationData("Badge Shop Starting Flag 2", 0x3c061a, 0x02000000, 0x00),
    LocationData("Pants Shop Starting Flag 1", 0x3c061c, 0x02000000, 0x00),
    LocationData("Pants Shop Starting Flag 2", 0x3c061e, 0x02000000, 0x00),
    LocationData("Pants Shop Starting Flag 3", 0x3c0620, 0x02000000, 0x00)
]

chuckolatorFlag: typing.List[LocationData] = [
    LocationData("Shop Chuckolator Flag", 0x3c05f8, 0x02000000, 0x00),
    LocationData("Pants Shop Chuckolator Flag 1", 0x3c062a, 0x02000000, 0x00),
    LocationData("Pants Shop Chuckolator Flag 2", 0x3c062c, 0x02000000, 0x00),
    LocationData("Pants Shop Chuckolator Flag 3", 0x3c062e, 0x02000000, 0x00),
    LocationData("Badge Shop Chuckolator Flag 1", 0x3c0624, 0x02000000, 0x00),
    LocationData("Badge Shop Chuckolator Flag 2", 0x3c0626, 0x02000000, 0x00),
    LocationData("Badge Shop Chuckolator Flag 3", 0x3c0628, 0x02000000, 0x00)
]

piranhaFlag: typing.List[LocationData] = [
    LocationData("Shop Mom Piranha Flag 1", 0x3c05fc, 0x02000000, 0x00),
    LocationData("Shop Mom Piranha Flag 2", 0x3c05fe, 0x02000000, 0x00),
    LocationData("Shop Mom Piranha Flag 3", 0x3c0600, 0x02000000, 0x00),
    LocationData("Shop Mom Piranha Flag 4", 0x3c0602, 0x02000000, 0x00),
    LocationData("Pants Shop Mom Piranha Flag 1", 0x3c0638, 0x02000000, 0x00),
    LocationData("Pants Shop Mom Piranha Flag 2", 0x3c063a, 0x02000000, 0x00),
    LocationData("Pants Shop Mom Piranha Flag 3", 0x3c063c, 0x02000000, 0x00),
    LocationData("Badge Shop Mom Piranha Flag 1", 0x3c0632, 0x02000000, 0x00),
    LocationData("Badge Shop Mom Piranha Flag 2", 0x3c0634, 0x02000000, 0x00),
    LocationData("Badge Shop Mom Piranha Flag 3", 0x3c0636, 0x02000000, 0x00)
]

kidnappedFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Peach Kidnapped Flag 1", 0x3c0640, 0x02000000, 0x00),
    LocationData("Badge Shop Peach Kidnapped Flag 2", 0x3c0642, 0x02000000, 0x00),
    LocationData("Badge Shop Peach Kidnapped Flag 3", 0x3c0644, 0x02000000, 0x00),
    LocationData("Pants Shop Peach Kidnapped Flag 1", 0x3c0646, 0x02000000, 0x00),
    LocationData("Pants Shop Peach Kidnapped Flag 2", 0x3c0648, 0x02000000, 0x00),
    LocationData("Pants Shop Peach Kidnapped Flag 3", 0x3c064a, 0x02000000, 0x00),
    LocationData("Shop Peach Kidnapped Flag 1", 0x3c0606, 0x02000000, 0x00),
    LocationData("Shop Peach Kidnapped Flag 2", 0x3c0608, 0x02000000, 0x00)
]

beanstarFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Beanstar Complete Flag 1", 0x3c064e, 0x02000000, 0x00),
    LocationData("Badge Shop Beanstar Complete Flag 2", 0x3c0650, 0x02000000, 0x00),
    LocationData("Badge Shop Beanstar Complete Flag 3", 0x3c0652, 0x02000000, 0x00),
    LocationData("Pants Shop Beanstar Complete Flag 1", 0x3c0654, 0x02000000, 0x00),
    LocationData("Pants Shop Beanstar Complete Flag 2", 0x3c0656, 0x02000000, 0x00),
    LocationData("Pants Shop Beanstar Complete Flag 3", 0x3c0658, 0x02000000, 0x00),
    LocationData("Shop Beanstar Complete Flag 1", 0x3c060c, 0x02000000, 0x00),
    LocationData("Shop Beanstar Complete Flag 2", 0x3c060e, 0x02000000, 0x00),
    LocationData("Shop Beanstar Complete Flag 3", 0x3c0610, 0x02000000, 0x00)
]

birdoFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Birdo Flag 1", 0x3c065c, 0x02000000, 0x00),
    LocationData("Badge Shop Birdo Flag 2", 0x3c065e, 0x02000000, 0x00),
    LocationData("Badge Shop Birdo Flag 3", 0x3c0660, 0x02000000, 0x00), 
    LocationData("Pants Shop Birdo Flag 1", 0x3c0662, 0x02000000, 0x00),
    LocationData("Pants Shop Birdo Flag 2", 0x3c0664, 0x02000000, 0x00),
    LocationData("Pants Shop Birdo Flag 3", 0x3c0666, 0x02000000, 0x00),
    LocationData("Shop Birdo Flag", 0x3c0614, 0x02000000, 0x00)
]

winkle: typing.List[LocationData] = [
    LocationData("Chucklehuck Woods Winkle Cave Block 1", 0x39df70, 0x02000000, 0x00),
    LocationData("Chucklehuck Woods Winkle Cave Block 2", 0x39df78, 0x02000000, 0x00),
    LocationData("Winkle Area Beanstar Room Block", 0x39df21, 0x02000000, 0x00),
    LocationData("Winkle Area Digspot", 0x39df2e, 0x02000000, 0x00),
    LocationData("Winkle Area Outside Colloseum Block", 0x39df3b, 0x02000000, 0x00),
    LocationData("Winkle Area Colloseum Digspot", 0x39e8a3, 0x02000000, 0x00),
    LocationData("Beanstar Piece Winkle Area", 0x1e9440, 0x02000000, 0x00),
    LocationData("Winkle Area Winkle Card", 0x261658, 0x02000000, 0x00)
]

sewers: typing.List[LocationData] = [
    LocationData("Sewers Room 3 Block 1", 0x39dfe6, 0x02000000, 0x00),
    LocationData("Sewers Room 3 Block 2", 0x39dfee, 0x02000000, 0x00),
    LocationData("Sewers Room 3 Block 3", 0x39dff6, 0x02000000, 0x00),
    LocationData("Sewers Room 5 Block 1", 0x39e006, 0x02000000, 0x00),
    LocationData("Sewers Room 5 Block 2", 0x39e00e, 0x02000000, 0x00),
    LocationData("Sewers Prison Room Block 1", 0x39e026, 0x02000000, 0x00),
    LocationData("Sewers Prison Room Block 2", 0x39e02e, 0x02000000, 0x00),
    LocationData("Sewers Prison Room Block 3", 0x39e036, 0x02000000, 0x00),
    LocationData("Sewers Prison Room Block 4", 0x39e03e, 0x02000000, 0x00),
    LocationData("Beanbean Castle Beanbean Brooch", 0x2578e7, 0x02000000, 0x00)
]

hooniversity: typing.List[LocationData] = [
    LocationData("Woohoo Hooniversity South Of Star Room Block", 0x39e16f, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Digspot 1", 0x39e194, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 1", 0x39e19c, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 2", 0x39e1a4, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 3", 0x39e1ac, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 4", 0x39e1b4, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Digspot 2", 0x39e1bc, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Sun Door Block 1", 0x39e28c, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Sun Door Block 2", 0x39e294, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Sun Door Block 3", 0x39e29c, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Cackletta Room 1 Block", 0x39e2ac, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Block 1", 0x39e2bf, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Block 2", 0x39e2c7, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Digspot", 0x39e2cf, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Basement Room 1 Digspot", 0x39e4c6, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Basement Room 2 Digspot", 0x39e4d3, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Basement Room 3 Block", 0x39e4e0, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Basement Room 4 Block", 0x39e4ed, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Popple Room Digspot 1", 0x39e4fa, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Popple Room Digspot 2", 0x39e502, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 1", 0x39ec05, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 2", 0x39ec0d, 0x02000000, 0x00),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 3", 0x39ec15, 0x02000000, 0x00)
]

surfable: typing.List[LocationData] = [
    LocationData("Ocean North Whirlpool Block 1", 0x39e0a5, 0x02000000, 0x00),
    LocationData("Ocean North Whirlpool Block 2", 0x39e0ad, 0x02000000, 0x00),
    LocationData("Ocean North Whirlpool Block 3", 0x39e0b5, 0x02000000, 0x00),
    LocationData("Ocean North Whirlpool Block 4", 0x39e0bd, 0x02000000, 0x00),
    LocationData("Ocean North Whirlpool Digspot 1", 0x39e0c5, 0x02000000, 0x00),
    LocationData("Ocean North Whirlpool Digspot 2", 0x39e0cd, 0x02000000, 0x00),
    LocationData("Oho Ocean Fire Puzzle Room Digspot", 0x39e057, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 1", 0x39e0da, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 2", 0x39e0e2, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 3", 0x39e0ea, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 4", 0x39e0f2, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 5", 0x39e0fa, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Digspot 6", 0x39e102, 0x02000000, 0x00),
    LocationData("Ocean South Whirlpool Room 2 Digspot", 0x39e10f, 0x02000000, 0x00),
    LocationData("Jokes End Pipe Digspot", 0x39e6c2, 0x02000000, 0x00),
    LocationData("Jokes End Staircase Digspot", 0x39e6cf, 0x02000000, 0x00),
    LocationData("Surf Minigame", 0x2753ea, 0x02000000, 0x00),
    LocationData("North Ocean Whirlpool Mole", 0x277956, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Surf Beach Digspot 1", 0x39dcfb, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Surf Beach Digspot 2", 0x39dd0b, 0x02000000, 0x00),
    LocationData("Beanbean Outskirts Surf Beach Digspot 3", 0x39dd13, 0x02000000, 0x00)
]

airport: typing.List[LocationData] = [
    LocationData("Airport Entrance Digspot", 0x39e2dc, 0x02000000, 0x00),
    LocationData("Airport Lobby Digspot", 0x39e2e9, 0x02000000, 0x00),
    LocationData("Airport Leftside Digspot 1", 0x39e2f6, 0x02000000, 0x00),
    LocationData("Airport Leftside Digspot 2", 0x39e2fe, 0x02000000, 0x00),
    LocationData("Airport Leftside Digspot 3", 0x39e306, 0x02000000, 0x00),
    LocationData("Airport Leftside Digspot 4", 0x39e30e, 0x02000000, 0x00),
    LocationData("Airport Leftside Digspot 5", 0x39e316, 0x02000000, 0x00),
    LocationData("Airport Middle Digspot 1", 0x39e323, 0x02000000, 0x00),
    LocationData("Airport Middle Digspot 2", 0x39e32b, 0x02000000, 0x00),
    LocationData("Airport Middle Digspot 3", 0x39e333, 0x02000000, 0x00),
    LocationData("Airport Middle Digspot 4", 0x39e33b, 0x02000000, 0x00),
    LocationData("Airport Middle Digspot 5", 0x39e343, 0x02000000, 0x00),
    LocationData("Airport Right Digspot 1", 0x39e350, 0x02000000, 0x00),
    LocationData("Airport Right Digspot 2", 0x39e358, 0x02000000, 0x00),
    LocationData("Airport Right Digspot 3", 0x39e360, 0x02000000, 0x00),
    LocationData("Airport Right Digspot 4", 0x39e368, 0x02000000, 0x00),
    LocationData("Airport Right Digspot 5", 0x39e370, 0x02000000, 0x00)
]

gwarharEntrance: typing.List[LocationData] = [
    LocationData("Gwarhar Lagoon Pipe Room Digspot", 0x39e37d, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Massage Parlor Entrance Digspot", 0x39e396, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon First Underwater Area Room 1 Block", 0x39e438, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon First Underwater Area Room 2 Block 1", 0x39e445, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon First Underwater Area Room 2 Block 2", 0x39e44d, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Red Pearl Bean", 0x235c1c, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Green Pearl Bean", 0x235a5b, 0x02000000, 0x00)
]

gwarharMain: typing.List[LocationData] = [
    LocationData("Gwarhar Lagoon Past Hermie Digspot", 0x39e3a6, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon East of Stone Bridge Block", 0x39e403, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon North of Spangle Room Digspot", 0x39e40b, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon West of Spangle Room Digspot", 0x39e41b, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 4 Digspot", 0x39e462, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 2 Digspot 1", 0x39e46f, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 2 Digspot 2", 0x39e477, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 1", 0x39e484, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 2", 0x39e48c, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 3", 0x39e494, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 1 Block", 0x39e4a1, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Entrance to West Underwater Area Digspot", 0x39e3bc, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 1 Digspot 1", 0x39e3c9, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 1 Digspot 2", 0x39e3d1, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 2 Digspot", 0x39e3de, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 3 Digspot 1", 0x39e3eb, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 3 Digspot 2", 0x39e3f3, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Spangle Room Block", 0x39e428, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Spangle Reward", 0x236e73, 0x02000000, 0x00),
    LocationData("Beanstar Piece Hermie", 0x1e9443, 0x02000000, 0x00),
    LocationData("Gwarhar Lagoon Spangle", 0x1e9437, 0x02000000, 0x00)
]

teeheeValley: typing.List[LocationData] = [
    LocationData("Teehee Valley Room 1 Digspot 1", 0x39e51e, 0x02000000, 0x00),
    LocationData("Teehee Valley Room 1 Digspot 2", 0x39e526, 0x02000000, 0x00),
    LocationData("Teehee Valley Room 1 Digspot 3", 0x39e52e, 0x02000000, 0x00),
    LocationData("Teehee Valley Room 2 Digspot 1", 0x39e53b, 0x02000000, 0x00),
    LocationData("Teehee Valley Room 2 Digspot 2", 0x39e543, 0x02000000, 0x00),
    LocationData("Teehee Valley Room 2 Digspot 3", 0x39e54b, 0x02000000, 0x00),
    LocationData("Teehee Valley Past Ultra Hammers Block 1", 0x39e580, 0x02000000, 0x00),
    LocationData("Teehee Valley Past Ultra Hammers Block 2", 0x39e590, 0x02000000, 0x00),
    LocationData("Teehee Valley Past Ultra Hammers Digspot 1", 0x39e598, 0x02000000, 0x00),
    LocationData("Teehee Valley Past Ultra Hammers Digspot 3", 0x39e5a8, 0x02000000, 0x00),
    LocationData("Teehee Valley Solo Luigi Maze Room 1 Block", 0x39e5e0, 0x02000000, 0x00),
    LocationData("Teehee Valley Before Trunkle Digspot", 0x39e5f0, 0x02000000, 0x00),
    LocationData("S.S Chuckola Storage Room Block 1", 0x39e610, 0x02000000, 0x00),
    LocationData("S.S Chuckola Storage Room Block 2", 0x39e628, 0x02000000, 0x00),
    LocationData("S.S Chuckola Membership Card", 0x260637, 0x02000000, 0x00)
]

fungitown: typing.List[LocationData] = [
    LocationData("Teehee Valley Trunkle Room Digspot", 0x39e5fd, 0x02000000, 0x00),
    LocationData("Fungitown Embassy Room Block", 0x39e66b, 0x02000000, 0x00),
    LocationData("Fungitown Entrance Room Block", 0x39e67e, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Starting Flag 1", 0x3c0684, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Starting Flag 2", 0x3c0686, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Starting Flag 3", 0x3c0688, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 1", 0x3c066a, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 2", 0x3c066c, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 3", 0x3c066e, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 4", 0x3c0670, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 5", 0x3c0672, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 6", 0x3c0674, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 7", 0x3c0676, 0x02000000, 0x00),
    LocationData("Fungitown Shop Starting Flag 8", 0x3c0678, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Starting Flag 1", 0x3c068a, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Starting Flag 2", 0x3c068c, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Starting Flag 3", 0x3c068e, 0x02000000, 0x00)
]

fungitownBeanstar: typing.List[LocationData] = [
    LocationData("Fungitown Badge Shop Beanstar Complete Flag 1", 0x3c0692, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Beanstar Complete Flag 2", 0x3c0694, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Beanstar Complete Flag 1", 0x3c0696, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Beanstar Complete Flag 2", 0x3c0698, 0x02000000, 0x00),
    LocationData("Fungitown Shop Beanstar Complete Flag", 0x3c067c, 0x02000000, 0x00)
]

fungitownBirdo: typing.List[LocationData] = [
    LocationData("Fungitown Shop Birdo Flag", 0x3c0680, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Birdo Flag 1", 0x3c06a0, 0x02000000, 0x00),
    LocationData("Fungitown Pants Shop Birdo Flag 2", 0x3c06a2, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Birdo Flag 1", 0x3c069c, 0x02000000, 0x00),
    LocationData("Fungitown Badge Shop Birdo Flag 2", 0x3c069e, 0x02000000, 0x00)
]

bowsers: typing.List[LocationData] = [
    LocationData("Bowser's Castle Entrance Block 1", 0x39e9d2, 0x02000000, 0x00),
    LocationData("Bowser's Castle Entrance Block 2", 0x39e9da, 0x02000000, 0x00),
    LocationData("Bowser's Castle Entrance Digspot", 0x39e9e2, 0x02000000, 0x00),
    LocationData("Bowser's Castle Iggy & Morton Hallway Block 1", 0x39e9ef, 0x02000000, 0x00),
    LocationData("Bowser's Castle Iggy & Morton Hallway Block 2", 0x39e9f7, 0x02000000, 0x00),
    LocationData("Bowser's Castle Iggy & Morton Hallway Digspot", 0x39e9ff, 0x02000000, 0x00),
    LocationData("Bowser's Castle After Morton Block", 0x39ea0c, 0x02000000, 0x00),
    LocationData("Bowser's Castle Morton Room 1 Digspot", 0x39ea89, 0x02000000, 0x00),
    LocationData("Bowser's Castle Lemmy Room 1 Block", 0x39ea9c, 0x02000000, 0x00),
    LocationData("Bowser's Castle Lemmy Room 1 Digspot", 0x39eaa4, 0x02000000, 0x00),
    LocationData("Bowser's Castle Ludwig Room 1 Block", 0x39eaba, 0x02000000, 0x00),
    LocationData("Bowser's Castle Lemmy Room Mole", 0x277b1f, 0x02000000, 0x00)
]

bowsersMini: typing.List[LocationData] = [
    LocationData("Bowser's Castle Ludwig & Roy Hallway Block 1", 0x39ea1c, 0x02000000, 0x00),
    LocationData("Bowser's Castle Ludwig & Roy Hallway Block 2", 0x39ea24, 0x02000000, 0x00),
    LocationData("Bowser's Castle Roy Corridor Block 1", 0x39ea31, 0x02000000, 0x00),
    LocationData("Bowser's Castle Roy Corridor Block 2", 0x39ea39, 0x02000000, 0x00),
    LocationData("Bowser's Castle Mini Mario Sidescroller Block 1", 0x39ead6, 0x02000000, 0x00),
    LocationData("Bowser's Castle Mini Mario Sidescroller Block 2", 0x39eade, 0x02000000, 0x00),
    LocationData("Bowser's Castle Mini Mario Maze Block 1", 0x39eaeb, 0x02000000, 0x00),
    LocationData("Bowser's Castle Mini Mario Maze Block 2", 0x39eaf3, 0x02000000, 0x00),
    LocationData("Bowser's Castle Before Wendy Fight Block 1", 0x39eb12, 0x02000000, 0x00),
    LocationData("Bowser's Castle Before Wendy Fight Block 2", 0x39eb1a, 0x02000000, 0x00),
    LocationData("Bowser's Castle Larry Room Block", 0x39ebb6, 0x02000000, 0x00),
    LocationData("Bowser's Castle Wendy & Larry Hallway Digspot", 0x39ea46, 0x02000000, 0x00),
    LocationData("Bowser's Castle Before Fawful Fight Block 1", 0x39ea56, 0x02000000, 0x00),
    LocationData("Bowser's Castle Before Fawful Fight Block 2", 0x39ea5e, 0x02000000, 0x00),
    LocationData("Bowser's Castle Great Door Block 1", 0x39ea6b, 0x02000000, 0x00),
    LocationData("Bowser's Castle Great Door Block 2", 0x39ea73, 0x02000000, 0x00)
]

jokesEntrance: typing.List[LocationData] = [
    LocationData("Jokes End West of First Boiler Room Block 1", 0x39e6e5, 0x02000000, 0x00),
    LocationData("Jokes End West of First Boiler Room Block 2", 0x39e6ed, 0x02000000, 0x00),
    LocationData("Jokes End First Boiler Room Digspot 1", 0x39e6fa, 0x02000000, 0x00),
    LocationData("Jokes End First Boiler Room Digspot 2", 0x39e702, 0x02000000, 0x00),
    LocationData("Jokes End Second Floor West Room Block 1", 0x39e761, 0x02000000, 0x00),
    LocationData("Jokes End Second Floor West Room Block 2", 0x39e769, 0x02000000, 0x00),
    LocationData("Jokes End Second Floor West Room Block 3", 0x39e779, 0x02000000, 0x00),
    LocationData("Jokes End Second Floor West Room Block 4", 0x39e781, 0x02000000, 0x00),
    LocationData("Jokes End Mole Reward 1", 0x27788e, 0x02000000, 0x00),
    LocationData("Jokes End Mole Reward 2", 0x2778d2, 0x02000000, 0x00)
]

jokesMain: typing.List[LocationData] = [
    LocationData("Jokes End Furnace Room 1 Block 1", 0x39e70f, 0x02000000, 0x00),
    LocationData("Jokes End Furnace Room 1 Block 2", 0x39e717, 0x02000000, 0x00),
    LocationData("Jokes End Furnace Room 1 Block 3", 0x39e71f, 0x02000000, 0x00),
    LocationData("Jokes End Northeast of Boiler Room 1 Block", 0x39e732, 0x02000000, 0x00),
    LocationData("Jokes End Northeast of Boiler Room 3 Digspot", 0x39e73f, 0x02000000, 0x00),
    LocationData("Jokes End Northeast of Boiler Room 2 Block 1", 0x39e74c, 0x02000000, 0x00),
    LocationData("Jokes End Northeast of Boiler Room 2 Block 2", 0x39e754, 0x02000000, 0x00),
    LocationData("Jokes End Second Floor East Room Digspot", 0x39e794, 0x02000000, 0x00),
    LocationData("Jokes End Final Split up Room Digspot", 0x39e7a7, 0x02000000, 0x00),
    LocationData("Jokes End South of Bridge Room Block", 0x39e7b4, 0x02000000, 0x00),
    LocationData("Jokes End Solo Luigi Room 1 Block", 0x39e7c4, 0x02000000, 0x00),
    LocationData("Jokes End Solo Luigi Room 1 Digspot", 0x39e7cc, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Final Room Block 1", 0x39e7d9, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Final Room Block 2", 0x39e7e1, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Final Room Block 3", 0x39e7e9, 0x02000000, 0x00),
    LocationData("Jokes End Solo Luigi Room 2 Digspot", 0x39e7fc, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Room 1 Digspot", 0x39e809, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Room 2 Block 1", 0x39e819, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Room 2 Block 2", 0x39e821, 0x02000000, 0x00),
    LocationData("Jokes End Solo Mario Room 2 Block 3", 0x39e829, 0x02000000, 0x00),
    LocationData("Jokes End Second Boiler Room Digspot 1", 0x39e84f, 0x02000000, 0x00),
    LocationData("Jokes End Second Boiler Room Digspot 2", 0x39e857, 0x02000000, 0x00),
    LocationData("Jokes End North of Second Boiler Room Block 1", 0x39e864, 0x02000000, 0x00),
    LocationData("Jokes End North of Second Boiler Room Block 2", 0x39e86c, 0x02000000, 0x00),
    LocationData("Jokes End Before Jojora Room Block 1", 0x39e927, 0x02000000, 0x00),
    LocationData("Jokes End Before Jojora Room Block 2", 0x39e92f, 0x02000000, 0x00),
    LocationData("Jokes End Before Jojora Room Digspot", 0x39e937, 0x02000000, 0x00),
    LocationData("Jokes End Jojora Room Digspot", 0x39e944, 0x02000000, 0x00)
]

postJokes: typing.List[LocationData] = [
    LocationData("Teehee Valley Past Ultra Hammers Digspot 2", 0x39e5a0, 0x02000000, 0x00),
    LocationData("Teehee Valley Before Popple Digspot 1", 0x39e55b, 0x02000000, 0x00),
    LocationData("Teehee Valley Before Popple Digspot 2", 0x39e563, 0x02000000, 0x00),
    LocationData("Teehee Valley Before Popple Digspot 3", 0x39e56b, 0x02000000, 0x00),
    LocationData("Teehee Valley Before Popple Digspot 4", 0x39e573, 0x02000000, 0x00)
]

theater: typing.List[LocationData] = [
    LocationData("Yoshi Theater Blue Yoshi", 0x241155, 0x02000000, 0x00),
    LocationData("Yoshi Theater Red Yoshi", 0x240ebe, 0x02000000, 0x00),
    LocationData("Yoshi Theater Green Yoshi", 0x241afa, 0x02000000, 0x00),
    LocationData("Yoshi Theater Yellow Yoshi", 0x241c3c, 0x02000000, 0x00),
    LocationData("Yoshi Theater Purple Yoshi", 0x241297, 0x02000000, 0x00),
    LocationData("Yoshi Theater Orange Yoshi", 0x241000, 0x02000000, 0x00),
    LocationData("Yoshi Theater Azure Yoshi", 0x241d7e, 0x02000000, 0x00),
    LocationData("Beanstar Piece Yoshi Theater", 0x1e9442, 0x02000000, 0x00)
]
    
oasis: typing.List[LocationData] = [
    LocationData("Oho Oasis West Digspot", 0x39df9f, 0x02000000, 0x00),
    LocationData("Oho Oasis Fire Palace Block", 0x39dfbe, 0x02000000, 0x00),
    LocationData("Oho Ocean South Room 1 Block", 0x39e06a, 0x02000000, 0x00),
    LocationData("Oho Ocean South Room 2 Digspot", 0x39e077, 0x02000000, 0x00),
    LocationData("Oho Ocean Spike Room Digspot 1", 0x39e08a, 0x02000000, 0x00),
    LocationData("Oho Ocean Spike Room Digspot 2", 0x39e092, 0x02000000, 0x00),
    LocationData("Oho Oasis Firebrand", 0x1e9408, 0x02000000, 0x00),
    LocationData("Oho Oasis Thunderhand", 0x1e9409, 0x02000000, 0x00)
]

all_locations: typing.List[LocationData] = mainArea + booStatue + chucklehuck + castleTown + startingFlag + \
                                           chuckolatorFlag + piranhaFlag + kidnappedFlag + beanstarFlag + birdoFlag + \
                                           winkle + sewers + hooniversity + surfable + airport + gwarharEntrance + \
                                           teeheeValley + fungitown + fungitownBeanstar + fungitownBirdo + bowsers + \
                                           jokesEntrance + jokesMain + postJokes + theater + oasis + gwarharMain + bowsersMini + baseUltraRocks
