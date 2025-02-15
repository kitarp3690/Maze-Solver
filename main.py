# making Maze solver using A* algorithm 
'''
    Write '0' for empty cells and '1' for blocked cells
'''

import numpy as np
import heapq

class Maze():
    def __init__(self):
        self.initial_state=np.array([[0,0,1,0,0],
                                    [1,0,0,1,0],
                                    [0,0,0,0,0],
                                    [1,0,0,0,0],
                                    [1,1,1,0,0]
                                    ])

    def a_star(self):
        print(self.initial_state)

    def print_solution(self):
        pass

if __name__ == '__main__':
    maze = Maze()
    maze.a_star()
    