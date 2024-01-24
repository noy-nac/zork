

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
        process_commands()

def print_cell(x, y):
    print(cell_name[x][y], end="\n")
    print(cell_desc[x][y], end="\n")

def process_commands():
    str = input()
    commands = parse_input(str)
    # complete this function

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