from typing import TYPE_CHECKING, Optional, Dict, Set
import struct
from NetUtils import ClientStatus
from .Locations import roomCount, nonBlock, beanstones, roomException, shop, badge, pants
from .Items import items_by_id, ItemData
import sys
import logging
import math

# This imports the bizhawk apworld if it's not already imported. This code block should be removed for a PR.
if "worlds._bizhawk" not in sys.modules:
    import importlib
    import os
    import zipimport

    bh_apworld_path = os.path.join(os.path.dirname(sys.modules["worlds"].__file__), "_bizhawk.apworld")
    if os.path.isfile(bh_apworld_path):
        importer = zipimport.zipimporter(bh_apworld_path)
        spec = importer.find_spec(os.path.basename(bh_apworld_path).rsplit(".", 1)[0])
        mod = importlib.util.module_from_spec(spec)
        mod.__package__ = f"worlds.{mod.__package__}"
        mod.__name__ = f"worlds.{mod.__name__}"
        sys.modules[mod.__name__] = mod
        importer.exec_module(mod)
    elif not os.path.isdir(os.path.splitext(bh_apworld_path)[0]):
        raise Exception("Did not find _bizhawk.apworld required to play Mario & Luigi Superstar Saga.")

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object

ROOM_ARRAY_POINTER = 0x51fa00


class MLSSClient(BizHawkClient):
    game = "Mario & Luigi Superstar Saga"
    system = "GBA"
    local_checked_locations: Set[int]
    goal_flag: int
    rom_slot_name: Optional[str]
    player_name: Optional[str]

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}
        self.rom_slot_name = None

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            rom_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 14, "ROM")]))[0])
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("UTF-8")
            if not rom_name.startswith("MARIO&LUIGIU"):
                return False
            if rom_name == "MARIO&LUIGIUA8":
                logger.info("ERROR: You appear to be running an unpatched version of Mario & Luigi Superstar Saga. "
                            "You need to generate a patch file and use it to create a patched ROM.")
                return False
            if rom_name != "MARIO&LUIGIUAP":
                logger.info(rom_name)
                logger.info("ERROR: The patch file used to create this ROM is not compatible with "
                            "this client. Double check your client version against the version being "
                            "used by the generator.")
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125
        self.rom_slot_name = rom_name
        name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xB0, 16, "ROM")]))[0])
        name = bytes([byte for byte in name_bytes if byte != 0]).decode("UTF-8")
        self.player_name = name

        return True

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        ctx.auth = self.player_name

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        from CommonClient import logger
        try:
            read_state = await bizhawk.read(ctx.bizhawk_ctx, [(0x4564, 59, "EWRAM"),
                                                              (0x2330, 2, "IWRAM"), (0x3FE0, 1, "IWRAM"), (0x3FE4, 1, "IWRAM"), (0x304B, 1, "EWRAM"), (0x304C, 4, "EWRAM"), (0x3058, 6, "EWRAM"), (0x4808, 2, "EWRAM")])
            flags = read_state[0]
            room = (read_state[1][1] << 8) + read_state[1][0]
            shop_init = read_state[2][0]
            shop_scroll = read_state[3][0]
            is_buy = (read_state[4][0] != 0)
            shop_address = (struct.unpack('<I', read_state[5])[0]) & 0xFFFFFF
            logo = bytes([byte for byte in read_state[6] if byte < 0x70]).decode("UTF-8")
            received_index = (read_state[7][0] << 8) + read_state[7][1]
            logger.info(read_state[7][0])
            logger.info(read_state[7][1])

            if logo != "MLSSAP":
                return

            locs_to_send = set()
            location = 0
            i = 0
            for item in ctx.items_received:
                if i < received_index:
                    i += 1
                    continue
                item_data = items_by_id[item.item]
                b = await bizhawk.read(ctx.bizhawk_ctx, [(0x3057, 1, "EWRAM")])
                if b[0][0] == 0:
                    await bizhawk.write(ctx.bizhawk_ctx, [(0x3057, [id_to_RAM(item_data.itemID)], "EWRAM"), (0x4808, [(i + 1) // 0x100, (i + 1) % 0x100], "EWRAM")])
                else:
                    break

            if is_buy:
                is_buy = False
                if shop_address != 0x3c0618 and shop_address != 0x3c0684:
                    location = shop[shop_address][shop_scroll]
                else:
                    if shop_init & 0x1 != 0:
                        location = badge[shop_address][shop_scroll & 0x1F]
                    else:
                        location = pants[shop_address][shop_scroll & 0x1F]
                await bizhawk.write(ctx.bizhawk_ctx, [(0x304B, [0x0], "EWRAM")])

            if location in ctx.server_locations:
                locs_to_send.add(location)

            # Check for set location flags.
            for byte_i, byte in enumerate(bytearray(flags)):
                for i in range(8):
                    and_value = 1 << i
                    if byte & and_value != 0:
                        flag_id = byte_i * 8 + (i + 1)
                        room, item = find_key(roomCount, flag_id)
                        pointer_arr = await bizhawk.read(ctx.bizhawk_ctx,
                                                         [(ROOM_ARRAY_POINTER + ((room - 1) * 4), 4, "ROM")])
                        pointer = (struct.unpack('<I', pointer_arr[0])[0])
                        pointer = pointer & 0xFFFFFF
                        offset = await bizhawk.read(ctx.bizhawk_ctx, [(pointer, 1, "ROM")])
                        offset = offset[0][0]
                        if offset != 0:
                            offset = 2
                        pointer += (item * 8) + 1 + offset
                        for key, value in beanstones.items():
                            if pointer == value:
                                pointer = key
                                break
                        if pointer in ctx.server_locations:
                            locs_to_send.add(pointer)

            for item in nonBlock:
                address, mask, location = item
                flag_bytes = await bizhawk.read(ctx.bizhawk_ctx, [(address, 1, "EWRAM")])
                flag_byte = flag_bytes[0][0]
                if flag_byte & mask != 0:
                    if location in roomException:
                        if roomException[location] == room:
                            exception = True
                        else:
                            exception = False
                    else:
                        exception = True
                    if location in ctx.server_locations and exception:
                        locs_to_send.add(location)

            # Send locations if there are any to send.
            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send

                if locs_to_send is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(locs_to_send)
                    }])

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect.
            pass


def find_key(dictionary, target):
    from CommonClient import logger
    leftover = target

    for key, value in dictionary.items():
        if leftover > value:
            leftover -= value
        else:
            return key, leftover


def id_to_RAM(id_: int):
    code = id_
    if code == 0x1D or code == 0x1E:
        code += 0xE
    if 0x20 <= code <= 0x26:
        code -= 0x4
    return code