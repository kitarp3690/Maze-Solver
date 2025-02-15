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
        self.initial_state_rows, self.initial_state_colums = self.initial_state.shape
        print(self.initial_state_rows, self.initial_state_colums)

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
    
    def calculate_heuristic_value(self, state:np)->int:
        heursitic:int = 0

    def possible_moves(self, start_cell, goal_cell, given_state:np)->list:
        moves:list[tuple[int, int]] = []
        directions:list[tuple[int, int]] = [(-1,0),(1,0),(0,-1),(0,1)] # Up, Down, Left, Right
        d = 0
        for dx, dy in directions:
            new_x, new_y = start_cell[0] + dx, start_cell[1] + dy
            
            if 0 <= new_x < self.initial_state_rows-1 and 0 <= new_y < self.initial_state_colums-1 and given_state[new_x, new_y] != 1:
                print(d)
                new_state = given_state.copy()
                new_state[start_cell[0], start_cell[1]], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[start_cell[0], start_cell[1]]
                moves.append(new_state)
            d += 1
        return moves

    def a_star(self):
        for move in Maze().possible_moves(self.initial_cell, self.goal_cell, self.initial_state):
            print(f'm={move}')
        # moves = self.possible_moves(self.initial_cell, self.goal_cell, self.initial_state)
        print(self.initial_state)
        # print(moves)

    def print_solution(self):
        pass

if __name__ == '__main__':
    maze = Maze()
    maze.set_initial_and_goal_cell()
    maze.a_star()
    