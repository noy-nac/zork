

cell_name = [
    ["","","",""],
    ["","","West of House",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
]

cell_desc = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
]

cell_invent = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""],
]

x_pos = 2 # row
y_pos = 1 # col

def game_loop():
    
    while True:
        print_cell(x_pos, y_pos)
        read_input()

def print_cell(x, y):
    print(cell_name())

# parse_input takes in a string written by the user and returns a list of 2-tuples
# The input string is made up of commands in the form of a VERB plus an OBJECT, for example "move west"
# The input string might contain more than one command, in which case a COMMA will separate each command, for example "move west, pick up sword"

# Input:
# move west
# Returns:
# [("MOVE", "WEST")]

# Input:
# go west, pick up sword, drop bat
# Returns:
# [("MOVE", "WEST"), ("PICKUP", "SWORD"), ("DROP", "BAT")]

# Since the input string is written by the user, the parser should recognize substantially similar VERBs
# For example, "move west" and "go west" should mean the same thing
# Likewise, "open door" and "enter door" should mean the same thing
# 

# Input:
# enter door
# Returns:
# [("OPEN", "DOOR")]

# If the input string is malformed in any way, the parser should return a single 2-tuple indicating the string could not be parsed

# Input:
# west go 
# Returns:
# [("ERROR", "west go")]

# Input:
# go west, go esat
# Returns:
# [("ERROR", "go west, go esat")]

def parse_input(str):


def read_input():

    string = input()



def move_player(dx, dy):
    pass

def pickup(item):
    pass

def drop(item):
    pass

game_loop()