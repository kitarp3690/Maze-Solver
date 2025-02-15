# making Maze solver using A* algorithm 
'''
    Write '0' for empty cells and '1' for blocked cells
'''

import numpy as np
import heapq

class Maze():
    def __init__(self)->None:
        """Initializing the initial state of Maze"""
        self.initial_state=np.array([[0,0,1,0,0],
                                    [1,0,0,1,0],
                                    [0,0,0,0,0],
                                    [1,0,0,0,0],
                                    [1,1,1,0,0]
                                    ])
    
    def set_initial_and_goal_cell(self)->None:
        """Takes input for both the initial and goal cell positions"""
        while True:
            try:
                user_input = input("Enter initial and goal cell positions as (row1,col1 row2,col2): ")
                positions = user_input.split()  # Splitting input by space
                # print(positions)
                if len(positions) != 2:
                    raise ValueError  # If not exactly two positions, trigger exception
                
                self.initial_cell = tuple(map(int, positions[0].split(',')))
                self.goal_cell = tuple(map(int, positions[1].split(',')))
                
                if len(self.initial_cell) != 2 or len(self.goal_cell) != 2:
                    raise ValueError  # Ensures two values in each tuple
                
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input! Please enter two cell positions as 'row1,col1 row2,col2' (e.g., '0,1 3,4'). \nNote is needed between after inital cell postion")
    
    def a_star(self):
        print(self.initial_state)

    def print_solution(self):
        pass

if __name__ == '__main__':
    maze = Maze()
    maze.set_initial_and_goal_cell()
    