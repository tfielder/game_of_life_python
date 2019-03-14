## Conway's Game of Life in Python
* Designed by: Tim Fielder
* Last Updated: 03/14/19
* Version: 1.0

## Instructions to run:

1. Go to https://github.com/tfielder/game_of_life_python.
2. From your command line (on a linux based-system) and the directory of your choice run `git clone https://github.com/tfielder/game_of_life_python.git`.
3. Change into the directory by running `cd game_of_life`. (Make sure you have a Python version installed).
4. Run `python solution.py`.
5. Enjoy the game of life.

## Rules
### For a space that is 'populated':
* Each cell with one or no neighbors dies, as if by solitude.
* Each cell with four or more neighbors dies, as if by overpopulation.
* Each cell with two or three neighbors survives.
### For a space that is 'empty' or 'unpopulated'
* Each cell with three neighbors becomes populated.

Sample input =
[[0,0,0,0,0],
[0,0,0,0,0],
[1,1,1,1,1],
[0,0,0,0,0],
[0,0,0,0,0]]
