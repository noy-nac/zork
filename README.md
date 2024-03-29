# Zork!

> ## Link: [Play Zork (1977)](http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq)
> ## Link: [Play Zork (1977)](https://playclassic.games/games/adventure-dos-games-online/play-zork-great-underground-empire-online/play/)
> ## Link: [Play Zork (1977)](https://www.pcjs.org/software/pcx86/game/infocom/zork1/)
> > [Walkthrough 1](https://web.mit.edu/marleigh/www/portfolio/Files/zork/transcript.html)
> > [Walkthrough 2](http://www.eristic.net/games/infocom/zork1.html)
> If you get webfiltered, Google until you find one that works

> ## Link: [Play Zork II (1981)](https://playclassic.games/games/adventure-dos-games-online/play-zork-ii-wizard-frobozz-online/play/)

## Background
Internally, Zork uses a 2D array for the player to move through the world. Moving NORTH takes the player from their current cell to the same cell in the row above, moving SOUTH takes the player to the same cell in the row below, moving EAST takes the player to the next cell to the right, and moving WEST takes the player to the previous cell to the left.

The original Zork is set in a fantasy world, but you can make whatever world you want. It could be your house, the school, your neighborhood, Mars, underwater, etc.

## Minimum Requirements
 - Create 2D lists to represent information about 

 - 10 open cells
    - Each cell should have a name, description, and a list of items available for pickup
    - Player types simple directional commands to move cells (go north, go south, go east, go west)
 
 - 3 internal walls, it's not possible to move through walls
    - Option 1. Create walls between cells. For example attempting to move from cell (1,2) to cell (2,2) isn't possible because there's a wall between the two
    - Option 2. Create cells that are walls and therefore impossible to move into. For example the cell (3,3) would be impossible to move to from any adjacent cell because it is a wall
  
 - Moving off the edge of the world
    - Option 1. Treat any attempt to move outside the 2D array as an attempt to move through a wall
    - Option 2. Wrap the grid so that moving off the edge of the 2D array puts the player on the opposite edge

 - Picking up items
    - Each cell stores items that the user can choose to pick up
    - Multiple items can be stored in a cell
    - Picking up an item adds the item to the player's inventory AND removes the item from the cell
    - Player can hold up to 3 items at a time

 - Dropping items
    - Dropping an item removes the item from the player's inventory AND adds the item to the current cell
    - The player can't drop an item if it isn't in their inventory

 - Final boss
    - The more cells of the world the player explores, the greater their chance of defeating the boss

## Suggested Functions
 - `game_loop()`
 - `print_cell(row, col)`
    - Prints the information associated with the cell at row, col for the player
    - Include the cell name, description, and any present items

For example:
```
== West of House ==
This is an open field west of a white house, with a boarded front door.
There is a small mailbox here.

>
```

 - `process_commands()`
    - Reads in the user input, decodes it, and decides which function to call
 - `move_player(delta_row, delta_col)`
    - `delta_row` and `delta_col` mean the difference between the previous cell and the new cell's row and col values
       - Hint: Moving NORTH moves up 1 row and 0 cols, moving SOUTH moves DOWN 1 row and 0 cols, moving EAST moves 0 rows and RIGHT 1 col, moving WEST moves 0 rows and LEFT 1 col
    - First check if the player would be moving into a wall
    - Then change the player's position to the new cell
 - `pickup(item)`
    - First check that `item` is present in the current cell
    - Then add the item to the player's inventory IF there's enough space
    - Finally remove the item from the current cell
 - `drop(item)`
    - First check that `item` is presnet in the player's inventory
    - Then add the item to the current cell
    - Finally remove the item from the player's inventory

## Map of Zork
![image](./map.jpg)
