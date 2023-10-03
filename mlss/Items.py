import typing

from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    progression: ItemClassification
    itemID: int


class MLSSItem(Item):
    game: str = "Mario & Luigi Superstar Saga"
    
    
itemList: typing.List[ItemData] = [
    ItemData(0x01, "Mushroom", ItemClassification.filler, 0xA),
    ItemData(0x02, "Super Mushroom", ItemClassification.filler, 0xB),
    ItemData(0x03, "Ultra Mushroom", ItemClassification.filler, 0xC),
    ItemData(0x04, "Max Mushroom", ItemClassification.filler, 0xD),
    ItemData(0x05, "Nuts", ItemClassification.filler, 0xE),
    ItemData(0x06, "Super Nuts", ItemClassification.filler, 0xF),
    ItemData(0x07, "Ultra Nuts", ItemClassification.useful, 0x10),
    ItemData(0x08, "Max Nuts", ItemClassification.useful, 0x11),
    ItemData(0x09, "Syrup", ItemClassification.filler, 0x12),
    ItemData(0x0A, "Super Syrup", ItemClassification.filler, 0x13),
    ItemData(0x0B, "Ultra Syrup", ItemClassification.useful, 0x14),
    ItemData(0x0C, "Max Syrup", ItemClassification.useful, 0x15),
    ItemData(0x0D, "1-UP Mushroom", ItemClassification.useful, 0x16),
    ItemData(0x0E, "1-UP Super", ItemClassification.useful, 0x17),
    ItemData(0x0F, "Golden Mushroom", ItemClassification.useful, 0x18),
    ItemData(0x10, "Refreshing Herb", ItemClassification.filler, 0x19),
    ItemData(0x11, "Red Pepper", ItemClassification.filler, 0x1A),
    ItemData(0x12, "Green Pepper", ItemClassification.filler, 0x1B),
    ItemData(0x13, "Hoo Bean", ItemClassification.filler, 0x1D),
    ItemData(0x14, "Chuckle Bean", ItemClassification.filler, 0x1E),
    ItemData(0x16, "Woohoo blend", ItemClassification.useful, 0x20),
    ItemData(0x17, "Hoohoo Blend", ItemClassification.useful, 0x21),
    ItemData(0x18, "Chuckle Blend", ItemClassification.useful, 0x22),
    ItemData(0x19, "Teehee Blend", ItemClassification.useful, 0x23),
    ItemData(0x1A, "Hoolumbian", ItemClassification.useful, 0x24),
    ItemData(0x1B, "Chuckoccino", ItemClassification.useful, 0x25),
    ItemData(0x1C, "Teeheespresso", ItemClassification.useful, 0x26),
    ItemData(0x1D, "Peasley's Rose", ItemClassification.progression, 0x31),
    ItemData(0x1E, "Beanbean Brooch", ItemClassification.progression, 0x32),
    ItemData(0x1F, "Red Goblet", ItemClassification.progression, 0x33),
    ItemData(0x20, "Green Goblet", ItemClassification.progression, 0x34),
    ItemData(0x21, "Red Chuckola Fruit", ItemClassification.progression, 0x35),
    ItemData(0x22, "White Chuckola Fruit", ItemClassification.progression, 0x36),
    ItemData(0x23, "Purple Chuckola Fruit", ItemClassification.progression, 0x37),
    ItemData(0x24, "Hammers", ItemClassification.progression, 0x38),
    ItemData(0x25, "Firebrand", ItemClassification.progression, 0x39),
    ItemData(0x26, "Thunder Hand", ItemClassification.progression, 0x3A),
    ItemData(0x27, "Membership Card", ItemClassification.progression, 0x40),
    ItemData(0x28, "Winkle Card", ItemClassification.progression, 0x41),
    ItemData(0x29, "Peach's Extra Dress", ItemClassification.progression, 0x42),
    ItemData(0x2A, "Fake Beanstar", ItemClassification.progression, 0x43),
    ItemData(0x2B, "Red Pearl Bean", ItemClassification.progression, 0x45),
    ItemData(0x2C, "Green Pearl Bean", ItemClassification.progression, 0x46),
    ItemData(0x2D, "Bean Fruit 1", ItemClassification.progression, 0x47),
    ItemData(0x2E, "Bean Fruit 2", ItemClassification.progression, 0x50),
    ItemData(0x2F, "Bean Fruit 3", ItemClassification.progression, 0x51),
    ItemData(0x30, "Bean Fruit 4", ItemClassification.progression, 0x52),
    ItemData(0x31, "Bean Fruit 5", ItemClassification.progression, 0x53),
    ItemData(0x32, "Bean Fruit 6", ItemClassification.progression, 0x54),
    ItemData(0x33, "Bean Fruit 7", ItemClassification.progression, 0x55),
    ItemData(0x34, "Blue Neon Egg", ItemClassification.progression, 0x56),
    ItemData(0x35, "Red Neon Egg", ItemClassification.progression, 0x57),
    ItemData(0x36, "Green Neon Egg", ItemClassification.progression, 0x60),
    ItemData(0x37, "Yellow Neon Egg", ItemClassification.progression, 0x61),
    ItemData(0x38, "Purple Neon Egg", ItemClassification.progression, 0x62),
    ItemData(0x39, "Orange Neon Egg", ItemClassification.progression, 0x63),
    ItemData(0x3A, "Azure Neon Egg", ItemClassification.progression, 0x64),
    ItemData(0x3B, "Beanstar Piece 1", ItemClassification.progression, 0x65),
    ItemData(0x3C, "Beanstar Piece 2", ItemClassification.progression, 0x66),
    ItemData(0x3D, "Beanstar Piece 3", ItemClassification.progression, 0x67),
    ItemData(0x3E, "Beanstar Piece 4", ItemClassification.progression, 0x70),
    ItemData(0x3F, "Spangle", ItemClassification.progression, 0x72),
    ItemData(0x40, "Beanlet 1", ItemClassification.useful, 0x73),
    ItemData(0x41, "Beanlet 2", ItemClassification.useful, 0x74),
    ItemData(0x42, "Beanlet 3", ItemClassification.useful, 0x75),
    ItemData(0x43, "Beanlet 4", ItemClassification.useful, 0x76),
    ItemData(0x44, "Beanlet 5", ItemClassification.useful, 0x77),
    ItemData(0x45, "Beanstone 1", ItemClassification.useful, 0x80),
    ItemData(0x46, "Beanstone 2", ItemClassification.useful, 0x81),
    ItemData(0x47, "Beanstone 3", ItemClassification.useful, 0x82),
    ItemData(0x48, "Beanstone 4", ItemClassification.useful, 0x83),
    ItemData(0x49, "Beanstone 5", ItemClassification.useful, 0x84),
    ItemData(0x4A, "Beanstone 6", ItemClassification.useful, 0x85),
    ItemData(0x4B, "Beanstone 7", ItemClassification.useful, 0x86),
    ItemData(0x4C, "Beanstone 8", ItemClassification.useful, 0x87),
    ItemData(0x4D, "Beanstone 9", ItemClassification.useful, 0x90),
    ItemData(0x4E, "Beanstone 10", ItemClassification.useful, 0x91),
    ItemData(0x4F, "Secret Scroll 1", ItemClassification.useful, 0x92),
    ItemData(0x50, "Secret Scroll 2", ItemClassification.useful, 0x93),
    ItemData(0x51, "Castle Badge", ItemClassification.useful, 0x9F),
    ItemData(0x52, "Pea Badge", ItemClassification.useful, 0xA0),
    ItemData(0x53, "Bean B. Badge", ItemClassification.useful, 0xA1),
    ItemData(0x54, "Counter Badge", ItemClassification.useful, 0xA2),
    ItemData(0x55, "Charity Badge", ItemClassification.useful, 0xA3),
    ItemData(0x56, "Bros. Badge", ItemClassification.useful, 0xA4),
    ItemData(0x57, "Miracle Badge", ItemClassification.useful, 0xA5),
    ItemData(0x58, "Ohoracle Badge", ItemClassification.useful, 0xA6),
    ItemData(0x59, "Mush Badge", ItemClassification.useful, 0xA7),
    ItemData(0x5A, "Mari-Lui Badge", ItemClassification.useful, 0xA8),
    ItemData(0x5B, "Muscle Badge", ItemClassification.useful, 0xA9),
    ItemData(0x5C, "Spiny Badge AA", ItemClassification.useful, 0xAA),
    ItemData(0x5D, "Mush Badge A", ItemClassification.useful, 0xAB),
    ItemData(0x5E, "Grab Badge", ItemClassification.useful, 0xAC),
    ItemData(0x5F, "Mush Badge AA", ItemClassification.useful, 0xAD),
    ItemData(0x60, "Power Badge", ItemClassification.useful, 0xAE),
    ItemData(0x61, "Wonder Badge", ItemClassification.useful, 0xAF),
    ItemData(0x62, "Beauty Badge", ItemClassification.useful, 0xB0),
    ItemData(0x63, "Salvage Badge", ItemClassification.useful, 0xB1),
    ItemData(0x64, "Oh-Pah Badge", ItemClassification.useful, 0xB2),
    ItemData(0x65, "Brilliant Badge", ItemClassification.useful, 0xB3),
    ItemData(0x66, "Sarge Badge", ItemClassification.useful, 0xB4),
    ItemData(0x67, "General Badge", ItemClassification.useful, 0xB5),
    ItemData(0x68, "Tank Badge", ItemClassification.useful, 0xB6),
    ItemData(0x69, "Bros. Rock", ItemClassification.useful, 0xBD),
    ItemData(0x6A, "Soulful Bros.", ItemClassification.useful, 0xC0),
    ItemData(0x6B, "High-End Badge", ItemClassification.useful, 0xC1),
    ItemData(0x6C, "Bean Pants", ItemClassification.useful, 0xCC),
    ItemData(0x6D, "Bean Trousers", ItemClassification.useful, 0xCD),
    ItemData(0x6E, "Blue Jeans", ItemClassification.useful, 0xCE),
    ItemData(0x6F, "Parasol Pants", ItemClassification.useful, 0xCF),
    ItemData(0x70, "Hard Pants", ItemClassification.useful, 0xD0),
    ItemData(0x71, "Heart Jeans", ItemClassification.useful, 0xD1),
    ItemData(0x72, "Plaid Trousers", ItemClassification.useful, 0xD2),
    ItemData(0x73, "#1 Trousers", ItemClassification.useful, 0xD3),
    ItemData(0x74, "Safety Slacks", ItemClassification.useful, 0xD4),
    ItemData(0x75, "Shroom Pants", ItemClassification.useful, 0xD5),
    ItemData(0x76, "Shroom Bells", ItemClassification.useful, 0xD6),
    ItemData(0x77, "Shroom Slacks", ItemClassification.useful, 0xD7),
    ItemData(0x78, "Peachy Jeans", ItemClassification.useful, 0xD8),
    ItemData(0x79, "Mushwin Pants", ItemClassification.useful, 0xD9),
    ItemData(0x7A, "Mushluck Pants", ItemClassification.useful, 0xDA),
    ItemData(0x7B, "Scandal Jeans", ItemClassification.useful, 0xDB),
    ItemData(0x7C, "Street Jeans", ItemClassification.useful, 0xDC),
    ItemData(0x7D, "Tropic Slacks", ItemClassification.useful, 0xDD),
    ItemData(0x7E, "Hermetic Pants", ItemClassification.useful, 0xDE),
    ItemData(0x7F, "Beanstar Pants", ItemClassification.useful, 0xDF),
    ItemData(0x80, "Peasley Slacks", ItemClassification.useful, 0xE0),
    ItemData(0x81, "Queen B. Jeans", ItemClassification.useful, 0xE1),
    ItemData(0x82, "B. Brand Jeans", ItemClassification.useful, 0xE2),
    ItemData(0x83, "Heart Slacks", ItemClassification.useful, 0xE3),
    ItemData(0x84, "Casual Slacks", ItemClassification.useful, 0xE4),
    ItemData(0x85, "Casual Coral", ItemClassification.useful, 0xEB),
    ItemData(0x86, "Harhall's Jeans", ItemClassification.useful, 0xF1),
    ItemData(0x87, "Wool Trousers", ItemClassification.useful, 0xF3),
    ItemData(0x88, "Iron Pants", ItemClassification.useful, 0xF7),
    ItemData(0x89, "Greed Wallet", ItemClassification.useful, 0xF8),
    ItemData(0x8A, "Bonus Ring", ItemClassification.useful, 0xF9),
    ItemData(0x8B, "Excite Spring", ItemClassification.useful, 0xFA),
    ItemData(0x8C, "Great Force", ItemClassification.useful, 0xFB),
    ItemData(0x8D, "Power Grip", ItemClassification.useful, 0xFC),
    ItemData(0x8E, "Cobalt Necktie", ItemClassification.useful, 0xFD),
    ItemData(0x8F, "Gameboy Horror SP", ItemClassification.useful, 0xFE)
]

item_frequencies: typing.Dict[str, int] = {
    "Mushroom": 55,
    "Super Mushroom": 15,
    "Ultra Mushroom": 12,
    "Nuts": 10,
    "Super Nuts": 5,
    "Ultra Nuts": 5,
    "Max Nuts": 2,
    "Syrup": 28,
    "Super Syrup": 10,
    "Ultra Syrup": 10,
    "Max Syrup": 2,
    "1-Up Mushroom": 15,
    "1-Up Super": 5,
    "Golden Mushroom": 3,
    "Refreshing Herb": 9,
    "Red Pepper": 2,
    "Green Pepper": 2,
    "Hoo Bean": 100,
    "Chuckle Bean": 200,
    "Hammers": 3
}

item_table: typing.Dict[str, ItemData] = {item.itemName: item for item in itemList}
items_by_id: typing.Dict[int, ItemData] = {item.code: item for item in itemList}
