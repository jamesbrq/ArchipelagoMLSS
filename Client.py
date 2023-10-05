from typing import TYPE_CHECKING, Optional, Dict, Set
import struct
from NetUtils import ClientStatus
from .Locations import roomCount, nonBlock, beanstones
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
            ctx.items_handling = 0b001
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
                read_state = await bizhawk.read(ctx.bizhawk_ctx, [(0x4564, 59, "EWRAM")])
                flags = read_state[0]


                # TODO Confirm a save has been made

                locs_to_send = set()

                # Check for set location flags.
                for byte_i, byte in enumerate(bytearray(flags)):
                    for i in range(8):
                        and_value = 1 << i
                        if byte & and_value != 0:
                            flag_id = byte_i * 8 + (i + 1)
                            room, item = find_key(roomCount, flag_id)
                            pointer_arr = await bizhawk.read(ctx.bizhawk_ctx, [(ROOM_ARRAY_POINTER + ((room - 1) * 4), 4, "ROM")])
                            pointer = (struct.unpack('<I', pointer_arr[0])[0])
                            pointer = pointer & 0xFFFFFF
                            offset = await bizhawk.read(ctx.bizhawk_ctx, [(pointer, 1, "ROM")])
                            offset = offset[0][0]
                            if offset != 0:
                                offset = 2
                            pointer += (item * 8) + 1 + offset
                            if pointer in beanstones:
                                pointer = beanstones[pointer]
                            if pointer in ctx.server_locations:
                                locs_to_send.add(pointer)

                for item in nonBlock:
                    address, mask, location = item
                    flag_byte = await bizhawk.read(ctx.bizhawk_ctx, [(address, 1, "ROM")])
                    flag_byte = flag_byte[0][0]
                    if flag_byte & mask != 0:
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
