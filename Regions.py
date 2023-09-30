import typing

from BaseClasses import MultiWorld, Region, Entrance
from worlds.generic.Rules import add_rule, set_rule
from Locations import MLSSLocation, mainArea, chucklehuck, castleTown, startingFlag, chuckolatorFlag, piranhaFlag, kidnappedFlag, beanstarFlag, birdoFlag, surfable, hooniversity, gwarhar, fungitown, teeheeValley, winkle, sewers, airport, \
                      bowsers, jokes_entrance, jokes_main, theater
from . import StateLogic

def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", player, world)
    world.regions.append(menu_region)
    
    main_region = create_region(world, player, "Main Area", mainArea)
    world.regions.append(main_region)
    
    chucklehuck_region = create_region(world, player, "Chucklehuck Woods", chucklehuck)
    world.regions.append(chucklehuck_region)
    
    castleTown_region = create_region(world, player, "Beanbean Castle Town", castleTown)
    world.regions.append(castleTown_region)
    
    startingFlag_region = create_region(world, player, "Shop Starting Flag", startingFlag)
    world.regions.append(startingFlag_region)
    
    chuckolatorFlag_region = create_region(world, player, "Shop Chuckolator Flag", chuckolatorFlag)
    world.regions.append(chuckolatorFlag_region)
    
    piranhaFlag_region = create_region(world, player, "Shop Piranha Flag", piranhaFlag)
    world.regions.append(piranhaFlag_region)
    
    kidnappedFlag_region = create_region(world, player, "Shop Peach Kidnapped Flag", kidnappedFlag)
    world.regions.append(kidnappedFlag_region)
    
    beanstarFlag_region = create_region(world, player, "Shop Beanstar Complete Flag", beanstarFlag)
    world.regions.append(beanstarFlag_region)
    
    birdoFlag_region = create_region(world, player, "Ship Birdo Flag", birdoFlag)
    world.regions.append(birdoFlag_region)
    
    surfable_region = create_region(world, player, "Surfable", surfable)
    world.regions.append(surfable_region)
    
    hooniversity_region = create_region(world, player, "Hooniversity", hooniversity)
    world.regions.append(hooniversity_region)

    gwarhar_region = create_region(world, player, "Gwarhar", gwarhar)
    world.regions.append(gwarhar_region)

    teehee_valley_region = create_region(world, player, "TeeheeValley", teeheeValley)
    world.regions.append(teehee_valley_region)

    winkle_region = create_region(world, player, "Winkle", winkle)
    world.regions.append(winkle_region)

    sewers_region = create_region(world, player, "Sewers", sewers)
    world.regions.append(sewers_region)

    airport_region = create_region(world, player, "Airport", airport)
    world.regions.append(airport_region)

    bowsers_region = create_region(world, player, "Bowsers", bowsers)
    world.regions.append(bowsers_region)

    jokes_entrance_region = create_region(world, player, "JokesEntrance", jokes_entrance)
    world.regions.append(jokes_entrance_region)

    jokes_main_region = create_region(world, player, "JokesMain", jokes_main)
    world.regions.append(jokes_main_region)
    
    postJokes_region = Region("PostJokes", player, world)
    world.regions.append(postJokes_region)

    theater_region = create_region(world, player, "Theater", theater)
    world.regions.append(theater_region)
    
    fungitown_region = create_region(world, player, "Fungitown", fungitown)
    world.regions.append(fungitown_region)
    
def connect_regions(world, player):
    names: typing.Dict[str, int] = {}
    
    connect(world, player, names, "Menu", "Main Area")
    connect(world, player, names, "Main Area", "Chucklehuck Woods", lambda state: StateLogic.brooch(state, player))
    connect(world, player, names, "Main Area", "Hooniversity", lambda state: StateLogic.canDig(state, player) and StateLogic.canMini(state, player))
    connect(world, player, names, "Main Area", "TeeheeValley", lambda state: StateLogic.super(state, player) or StateLogic.canDash(state, player))
    connect(world, player, names, "TeeheeValley", "Gwarhar", lambda state: StateLogic.membership(state, player))
    connect(world, player, names, "TeeheeValley", "Fungitown", lambda state: state.can_reach("Airport", "Region", player) and state.can_reach("Beanbean Castle Town", "Region", player))
    connect(world, player, names, "Main Area", "Shop Starting Flag", lambda state: StateLogic.brooch(state, player) or StateLogic.rose(state, player))
    connect(world, player, names, "Shop Starting Flag", "Shop Chuckolator Flag", lambda state: (StateLogic.brooch(state, player) and StateLogic.fruits(state, player)) or state.can_reach("Shop Piranha Flag", "Region", player))
    connect(world, player, names, "Shop Starting Flag", "Shop Piranha Flag", lambda state: StateLogic.thunder(state, player) or state.can_reach("Shop Peach Kidnapped Flag", "Region", player))
    connect(world, player, names, "Shop Starting Flag", "Shop Peach Kidnapped Flag", lambda state: (StateLogic.thunder(state, player) and state.can_reach("Fungitown", "Region", player)) or state.can_reach("Shop Beanstar Complete Flag", "Region", player))
    connect(world, player, names, "Shop Starting Flag", "Shop Beanstar Complete Flag", lambda state: (state.can_reach("Beanbean Castle Town", "Region", player) and StateLogic.pieces(state, player)) or state.can_reach("Shop Birdo Flag", "Region", player))
    connect(world, player, names, "Shop Starting Flag", "Shop Birdo Flag", lambda state: state.can_reach("PostJokes", "Region", player))
    connect(world, player, names, "Main Area", "Sewers", lambda state: StateLogic.rose(state, player))
    connect(world, player, names, "Main Area", "Airport", lambda state: StateLogic.thunder(state, player))
    connect(world, player, names, "Main Area", "Theater", lambda state: StateLogic.canDash(state, player))
    connect(world, player, names, "Main Area", "Surfable", lambda state: StateLogic.ultra(state, player) and ((StateLogic.canMini(state, player) and StateLogic.canDig(state, player)) or StateLogic.membership(state, player)))
    connect(world, player, names, "Surfable", "Gwarhar")
    connect(world, player, names, "Surfable", "JokesEntrance", lambda state: StateLogic.fire(state, player))
    connect(world, player, names, "JokesEntrance", "JokesMain", lambda state: StateLogic.canCrash(state, player) and StateLogic.canDig(state, player))
    connect(world, player, names, "JokesMain", "PostJokes", lambda state: StateLogic.canDash(state, player) and StateLogic.pieces(state, player) and state.can_reach("Beanbean Castle Town", "Region", player) and StateLogic.rose(state, player))
    connect(world, player, names, "Chucklehuck Woods", "Winkle", lambda state: StateLogic.canDash(state, player))
    connect(world, player, names, "Chucklehuck Woods", "Beanbean Castle Town", lambda state: StateLogic.fruits(state, player))
    
def create_region(world, player, name, locations):
    ret = Region(name, player, world)
    ret.add_locations(locations, MLSSLocation)
    return ret
    
def connect(world: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)