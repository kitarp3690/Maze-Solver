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
                                    ],dtype=int)
        self.initial_state_rows, self.initial_state_colums = self.initial_state.shape
        # print(self.initial_state_rows, self.initial_state_colums)

    def set_initial_and_goal_cell(self)->None:
        """Takes input for both the initial and goal cell positions"""
        while True:
            try:
                print("\nHint: for 1st row 2nd column write 0,1 ")
                user_input = input("Enter initial and goal cell positions as (row1,col1 row2,col2): ")
                positions = user_input.split()  # Splitting input by space
                # print(positions)
                if len(positions) != 2:
                    raise ValueError  # If not exactly two positions, trigger exception
                
                self.initial_cell = tuple(map(int, positions[0].split(',')))
                self.goal_cell = tuple(map(int, positions[1].split(',')))
                
                if len(self.initial_cell) != 2 or len(self.goal_cell) != 2:
                    raise ValueError  # Ensures two values in each tuple

                # Checking if the positions are within the maze boundaries
                if not (0 <= self.initial_cell[0] < self.initial_state_rows and 
                        0 <= self.initial_cell[1] < self.initial_state_colums and
                        0 <= self.goal_cell[0] < self.initial_state_rows and 
                        0 <= self.goal_cell[1] < self.initial_state_colums):
                    raise ValueError  

                # Ensuring that the selected positions are not blocked (1 in the maze)
                if (self.initial_state[self.initial_cell] == 1 or
                    self.initial_state[self.goal_cell] == 1):
                    print("\nInvalid selection! Initial or goal cell is blocked (1). Try again.")
                    continue  # Restart the loop

                break  # Exit loop if input is valid
            except ValueError:
                print("\nInvalid input! Please enter two cell positions as 'row1,col1 row2,col2' (e.g., '0,1 3,4'). \nNote is needed between after inital cell postion")
    
    def calculate_heuristic_value(self, state: tuple[int,int])->int:
        """This calculates the heuristic value(also known as Manhattan distance)"""
        # heursitic:int = 0
        goal_i, goal_j = self.goal_cell
        # print(goal_i,goal_j)
        # heursitic += abs(i - goal_i) + abs(j - goal_j)
        return abs(state[0] - goal_i) + abs(state[1] - goal_j)

    def possible_moves(self, start_cell, goal_cell, given_state:np)->list:
        """Generating all possible moves from given_state position and adding 2 in the path"""
        moves:list[tuple[int, int]] = []
        directions:list[tuple[int, int]] = [(-1,0),(1,0),(0,-1),(0,1)] # Up, Down, Left, Right
        d = 0
        for dx, dy in directions:
            new_x, new_y = start_cell[0] + dx, start_cell[1] + dy
            
            if (
                0 <= new_x < self.initial_state_rows 
                and 0 <= new_y < self.initial_state_colums 
                and given_state[new_x, new_y] != 1
            ):
                # print(d)
                # new_state = given_state.copy()
                # new_state[start_cell[0], start_cell[1]], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[start_cell[0], start_cell[1]]
                # new_state[start_cell[0], start_cell[1]], new_state[new_x, new_y] = 2, 2
                moves.append((new_x, new_y))
            d += 1
        return moves

    def a_star(self):
        """Solving the maze using A* algorithm"""
        priority_queue = []
        came_from = {} # To reconstruct path
        g_costs = {self.initial_cell: 0}
        
        heapq.heappush(priority_queue,(self.calculate_heuristic_value(self.initial_cell), 0, self.initial_cell))

        visited = set()
        
        while priority_queue:
            _, g, current_cell = heapq.heappop(priority_queue)

            # If this state is the goal state
            if current_cell == self.goal_cell:
                print("Goal Reached")
                self.print_solution(came_from)
                return 
            
            visited.add(current_cell)
            
        # print(f"Initial_state: \n{self.initial_state}\n")
            for move in self.possible_moves(current_cell, self.goal_cell, self.initial_state):
                # print(f'm={move}')
                pos_move = tuple(move)

                if pos_move in visited:
                    continue
                new_g = g + 1 # g means no. of move

                if pos_move not in g_costs or new_g < g_costs[pos_move]:
                    g_costs[pos_move] = new_g
                    f = new_g + self.calculate_heuristic_value(pos_move)  # f = g + h
                    heapq.heappush(priority_queue, (f, new_g, pos_move))
                    came_from[pos_move] = current_cell  # Store parent node
        print("No Solution Found")

    def print_solution(self, came_from: dict):
        path=[]
        current = self.goal_cell

        while current != self.initial_cell:
            path.append(current)
            current = came_from.get(current)

            if current is None:
                print("No valid path found.")
                return
        path.append(self.initial_cell)
        path.reverse()

        print("Path to goal:", path)

if __name__ == '__main__':
    maze = Maze()
    maze.set_initial_and_goal_cell()
    maze.a_star()
    