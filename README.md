
# Maze Solver Using A* algorithm

This project implements a Maze Solver using the A (A-star) algorithm* in Python. The algorithm finds the shortest path from a given initial position to a goal position in a grid-based maze. The heuristic used is Manhattan Distance, which guides the search towards the goal while avoiding blocked cells.

## Features

- Solves a given maze using the A algorithm*.
- Allows custom input for initial and goal positions.
- Uses Manhattan Distance as the heuristic function.
- Prints the shortest path from start to goal if one exists.
- Handles invalid inputs and ensures the initial/goal positions are within the maze and not blocked.

## Requirements

- Python 3.12.0
- numpy for matrix manipulations.
- heapq for implementing the priority queue used in the A* algorithm.
  
## Installation

```bash
git clone https://github.com/kitarp3690/Maze-Solver.git
```
```bash
pip install numpy
```
```bash
cd Maze-Solver
```
```bash
python main.py
```
    
## Usage/Examples

To use the maze solver, run the script below. It will prompt you to enter the initial and goal positions in the format row1,col1 row2,col2.
```bash
python main.py
```

### Sample Input:
```
Hint: for 1st row 2nd column write 0,1
Enter initial and goal cell positions as (row1,col1 row2,col2): 0,1 4,4
```

### Sample Output
```Goal Reached
Path to goal: [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```

## How it works

### Maze Representation:
- 0 represents open paths.
- 1 represents blocked cells.
- The program ensures that both initial and goal positions are valid and not blocked.

### A Algorithm Process:A*
- Uses a priority queue (heap) to explore the most promising paths first.
- g(n): Cost from the start to the current cell.
- h(n): Manhattan Distance heuristic to the goal.
- f(n) = g(n) + h(n): The total estimated cost.
- Keeps track of visited nodes and reconstructs the path when the goal is reached.

## Acknowledgements

- Inspired by pathfinding techniques in AI and robotics.
- A* algorithm concept taken from standard graph search algorithms.
- Thanks to contributors and the Python community for the great libraries and tools!

## Contact Information

For any questions, feel free to contact me via GitHub or at my email: pratikshrestha362@gmail.com.

## Author

- [Pratik Shrestha](https://www.github.com/kitarp3690)

