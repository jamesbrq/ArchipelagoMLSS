from worlds.generic.Rules import add_rule
from BaseClasses import MultiWorld
from .Names.LocationName import LocationName
from .Locations import all_locations
from . import StateLogic


def set_rules(world: MultiWorld, player: int):
    for location in all_locations:
        if "Digspot" in location.name:
            add_rule(world.get_location(location.name, player), lambda state: StateLogic.canDig(state, player))
        if "Beanstone" in location.name:
            add_rule(world.get_location(location.name, player), lambda state: StateLogic.canDig(state, player))

    add_rule(world.get_location(LocationName.HoohooVillageHammerHouseBlock, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.HoohooMountainBaseBoostatueRoomBlock2, player),
             lambda state: StateLogic.canCrash(state, player) or StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBooStatueMole, player),
             lambda state: StateLogic.canMini(state, player) and StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.HoohooMountainBaseBoostatueRoomDigspot2, player),
             lambda state: StateLogic.canCrash(state, player) or StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.HoohooVillageSuperHammerCaveBlock, player),
             lambda state: StateLogic.canCrash(state, player) or StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.HoohooVillageSuperHammerCaveDigspot, player),
             lambda state: StateLogic.canCrash(state, player) or StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsFarmRoomDigspot1, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsFarmRoomDigspot2, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsFarmRoomDigspot3, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsFarmRoomMoleReward1, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsFarmRoomMoleReward2, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsThunderHandMole, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsNWBlock, player),
             lambda state: StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit1, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit2, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit3, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit4, player),
             lambda state: StateLogic.super(state, player) and StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit5, player),
             lambda state: StateLogic.super(state, player) and StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit6, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsBeanFruit7, player),
             lambda state: state.can_reach("TeeheeValley", "Region", player) and StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSRoom1Block, player),
             lambda state: StateLogic.ultra(state, player) and StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSRoom1Digspot2, player),
             lambda state: StateLogic.ultra(state, player) and StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsNEDigspot1, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsEDigspot2, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsNorthBeachDigspot3, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.WoohooHooniversityMiniMarioPuzzleSecretAreaBlock1, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.WoohooHooniversityMiniMarioPuzzleSecretAreaBlock2, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.WoohooHooniversityMiniMarioPuzzleSecretAreaBlock3, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.WoohooHooniversityMiniMarioPuzzleSecretAreaBlock4, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.WoohooHooniversityMiniMarioPuzzleBlock, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSecretScroll1, player),
             lambda state: StateLogic.thunder(state, player) and StateLogic.super(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSecretScroll2, player),
             lambda state: StateLogic.thunder(state, player) and StateLogic.ultra(state, player))
    add_rule(world.get_location(LocationName.HoohooVillageMoleBehindTurtle, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsNESoloMarioMole1, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsNESoloMarioMole2, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.HoohooVillageMoleBehindTurtle, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSuperHammerUpgrade, player),
             lambda state: StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsUltraHammerUpgrade, player),
             lambda state: StateLogic.thunder(state, player) and StateLogic.pieces(state, player) and state.can_reach(
                 "Beanbean Castle Town", "Region", player))
    add_rule(world.get_location(LocationName.BeanbeanOutskirtsSoloLuigiCaveMole, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsRedChuckolaFruit, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsWhiteChuckolaFruit, player),
             lambda state: StateLogic.canDig(state, player) and StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock1, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock2, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock3, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock4, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock5, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsAfterChucklerootBlock6, player),
             lambda state: StateLogic.fruits(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsWhiteFruitRoomDigspot2, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsWhiteFruitRoomDigspot3, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsRoom7Block1, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsRoom7Block2, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsPipeRoomBlock1, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.ChucklehuckWoodsPipeRoomBlock2, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleTownMiniMarioBlock1, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleTownMiniMarioBlock2, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleTownMiniMarioBlock3, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleTownMiniMarioBlock4, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleTownMiniMarioBlock5, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastleFakeBeastar, player),
             lambda state: StateLogic.pieces(state, player))
    add_rule(world.get_location(LocationName.BeanbeanCastlePeachsExtraDress, player),
             lambda state: StateLogic.pieces(state, player))
    add_rule(world.get_location(LocationName.SewersRoom5Block1, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.SewersRoom5Block2, player),
             lambda state: StateLogic.hammers(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonFirstUnderwaterAreaRoom1Block, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonFirstUnderwaterAreaRoom2Block1, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonFirstUnderwaterAreaRoom2Block2, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonRedPearlBean, player),
             lambda state: StateLogic.fire(state, player) and StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonGreenPearlBean, player),
             lambda state: StateLogic.fire(state, player) and StateLogic.thunder(state, player))
    add_rule(world.get_location(LocationName.TeeheeValleyPastUltraHammersDigspot1, player),
             lambda state: StateLogic.ultra(state, player))
    add_rule(world.get_location(LocationName.TeeheeValleyPastUltraHammersDigspot3, player),
             lambda state: StateLogic.ultra(state, player))
    add_rule(world.get_location(LocationName.TeeheeValleyPastUltraHammersBlock1, player),
             lambda state: StateLogic.ultra(state, player))
    add_rule(world.get_location(LocationName.TeeheeValleyPastUltraHammersBlock2, player),
             lambda state: StateLogic.ultra(state, player))
    add_rule(world.get_location(LocationName.TeeheeValleySoloLuigiMazeRoom1Block, player),
             lambda state: StateLogic.ultra(state, player) or state.can_reach("Fungitown", "Region", player))
    add_rule(world.get_location(LocationName.JokesEndJojoraRoomDigspot, player),
             lambda state: StateLogic.canDash(state, player))
    add_rule(world.get_location(LocationName.OhoOasisFirebrand, player),
             lambda state: StateLogic.canMini(state, player))
    add_rule(world.get_location(LocationName.OhoOasisThunderhand, player),
             lambda state: StateLogic.canDig(state, player))
    add_rule(world.get_location(LocationName.BeanstarPieceYoshiTheater, player),
             lambda state: StateLogic.neon(state, player))
    add_rule(world.get_location(LocationName.BeanstarPieceYoshiTheater, player),
             lambda state: StateLogic.neon(state, player))
    add_rule(world.get_location(LocationName.WinkleAreaBeanstarRoomBlock, player),
             lambda state: StateLogic.winkle(state, player))
    add_rule(world.get_location(LocationName.BeanstarPieceWinkleArea, player),
             lambda state: StateLogic.winkle(state, player))
    add_rule(world.get_location(LocationName.GwarharLagoonSpangleReward, player),
             lambda state: StateLogic.spangle(state, player))
