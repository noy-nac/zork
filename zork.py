
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

def game_loop(): 
    while True:
        print_cell(player_row, player_col)
        process_commands()

def print_cell(row, col):
    print(cell_name[row][col], end="\n")
    print(cell_desc[row][col], end="\n")

    print("\n>", end="")

def process_commands():
    str = input()
    cmds = parse_input(str)
    # complete this function

def parse_input(str):
    pass

def move_player(dx, dy):
    pass

def pickup(item):
    pass

def drop(item):
    pass

game_loop()