
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

player_row = 1
player_col = 2

# Runs the game
def game_loop(): 
    while True:
        print_cell(player_row, player_col)
        process_commands()

# Prints the information associated with the cell at row, col for use by the player
def print_cell(row, col):
    print(cell_name[row][col], end="\n")
    print(cell_desc[row][col], end="\n")

    print("\n>", end="")

def process_commands():
    str = input()
    cmds = parse_input(str)
    # your code here

def parse_input(str):
    # your code here
    pass

def move_player(delta_row, delta_col):
    # your code here
    pass

def pickup(item):
    # your code here
    pass

def drop(item):
    # your code here
    pass

def final_boss():
    # your code here
    pass

game_loop()