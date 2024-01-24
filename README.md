# Zork!

## Play Zork
http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq

## Background
Internally, Zork uses a 2D array for the player to move through the world. Moving NORTH takes the player from their current cell to the same cell in the same cell in the ROW directly above, moving SOUTH takes the player down, EAST to the right, and WEST to the left.

## Minimum Requirements
 - 10 open cells
    - Each cell should have a name, description, and a list of items available for pickup.
 
 - 4 internal walls, it's not possible to move through walls
    - Option 1. Create walls between cells. For example attempting to move from cell (1,2) to cell (2,2) isn't possible because there's a wall between the two.
    - Option 2. Create cells that are walls and therefore impossible to move into.
  
 - Moving off the edge of the world
    - Option 1. Treat any attempt to move outside the 2D array as an attempt to move through a wall.
    - Option 2. Wrap the grid so that moving off the edge of the 2D array puts the player on the opposite edge.

 - Picking up items
    - Each cell stores items that the user can choose to pick up
    - Multiple items can be stored in a cell
    - Picking up an item adds the item to the player's inventory AND removes the item from the cell
    - Player can hold up to 3 items at a time

 - Dropping items
    - Dropping an item removes the item from the player's inventory AND adds the item to the current cell
    - The player can't drop an item if it isn't in their inventory

## Provided Functions
 - game_loop()

## Required Functions
 - print_cell(x, y)
 - parse_input(str)
 - move(dx, dy)

### Printing Cells

```python
def print_cell(x, y):
    ...
```

### Parsing User Input

Parsing means to take in a string and break it into smaller parts according to the grammar of the language. In Zork, the language consists of verbs and objects.

```python
def parse_input(str):
    ...
```

`parse_input` takes in a string written by the user and returns a list of 2-tuples. The input string is made up of commands in the form of a VERB plus an OBJECT, **for example "move west".** The input string might contain more than one command, in which case a COMMA will separate each command, **for example "move west, pick up sword".**

```python
Input:
parse_input("move west")
Returns:
[("MOVE", "WEST")]
```

```python
Input:
parse_input("go west, pick up sword, drop bat")
Returns:
[("MOVE", "WEST"), ("PICKUP", "SWORD"), ("DROP", "BAT")]
```

Since the input string is written by the user, the parser should __**recognize substantially similar VERBs.**__ For example, **"move west" and "go west" should mean the same thing.** Likewise, **"open door" and "enter door" should mean the same thing.**

```python
Input:
parse_input("enter door")
Returns:
[("OPEN", "DOOR")]
```

If the input string has a malformed VERB, the parser should return a single 2-tuple indicating the string could not be parsed.

```python
Input:
parse_input("pcik up sword")
Returns:
[("ERROR", "pcik up sword")]
```

```python
Input:
parse_input("west go") 
Returns:
[("ERROR", "west go")]
```

```python
Input:
parse_input("go west, og east, fly away")
Returns:
[("ERROR", "go west, og east", fly away)]
```

There's no need to check the OBJECTs make sense in the parser.

```python
Input:
parse_input("go into the sky")
Returns
[("MOVE", "INTO THE SKY")]
```

### hjh


###
