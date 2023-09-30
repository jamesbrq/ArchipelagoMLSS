def can_dig(state, player):
    return (state.has("Green Goblet", player) and state.has("Hammers", player))
    
def can_mini(state, player):
    return (state.has("Red Goblet", player) and state.has("Hammers", player))
    
def can_dash(state, player):
    return (state.has("Red Pearl Bean", player) and state.has("Firebrand", player))
    
def can_crash(state, player):
    return (state.has("Green Pearl Bean", player) and state.has("Thunder hand", player))
    
def hammers(state, player)
    return state.has("Hammers", player)
    
def super(state, player):
    return state.has("Hammers", player, 2)

def ultra(state, player):
    return state.has("Hammers", player, 3)
    
def fruits(state, player):
    return (state.has("Red Chuckola Fruit", player) and state.has("Purple Chuckola Fruit", player) and state.has("White Chuckola Fruit", player))
    
def pieces(state, player):
    return (state.has("Beanstar Piece 1", player) and state.has("Beanstar Piece 2", player) and state.has("Beanstar Piece 3", player) and state.has("Beanstar Piece 4", player))
    
def neon(state, player):
    return (state.has("Blue Neon Egg", player) and state.has("Red Neon Egg", player) and state.has("Green Neon Egg", player) and state.has("Yellow Neon Egg", player) and state.has("Purple Neon Egg", player) and state.has("Orange Neon Egg", player) and state.has("Azure Neon Egg", player)))

def spangle(state, player):
    return state.has("Spangle", player)
    
def rose(state, player):
    return state.has("Peasley's Rose", player)
    
def brooch(state, player):
    return state.has("Beanbean Brooch", player)
    
def thunder(state, player):
    return state.has("Thunder Hand", player)
    
def fire(state, player):
    return state.has("Firebrand", player)