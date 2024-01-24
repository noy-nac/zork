# Zork!

## Play Zork
http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq

## Background

## 

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

```
Input:
move west
Returns:
[("MOVE", "WEST")]
```

```
Input:
go west, pick up sword, drop bat
Returns:
[("MOVE", "WEST"), ("PICKUP", "SWORD"), ("DROP", "BAT")]
```

Since the input string is written by the user, the parser should __**recognize substantially similar VERBs.**__ For example, **"move west" and "go west" should mean the same thing.** Likewise, **"open door" and "enter door" should mean the same thing.**

```
Input:
enter door
Returns:
[("OPEN", "DOOR")]
```

If the input string has a malformed VERB, the parser should return a single 2-tuple indicating the string could not be parsed.

```
Input:
pcik up sword
Returns:
[("ERROR", "pcik up sword")]
```

```
Input:
west go 
Returns:
[("ERROR", "west go")]
```

```
Input:
go west, og east, fly away
Returns:
[("ERROR", "go west, og east", fly away)]
```

There's no need to check the OBJECTs make sense in the parser.

```
Input:
go into the sky
Returns
[("MOVE", "INTO THE SKY")]
```

- print_cell()