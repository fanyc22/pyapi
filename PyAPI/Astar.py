import sys
import PyAPI.structures as THUAI7
from PyAPI.Interface import IShipAPI, ITeamAPI, IAI
from PyAPI.utils import AssistFunction
from typing import Union, Final, cast, List,Dict
from PyAPI.constants import Constants
import queue
import time
from enum import Enum

if sys.version_info < (3, 9):
    from typing import Tuple
else:
    Tuple = tuple


def Astar(grid: List[List[THUAI7.PlaceType]], start: Tuple[int, int], goal: Tuple[int, int],allow_diag:bool) -> List[Tuple[int, int]]:
    # Define the possible movements (up, down, left, right, diagonal)
    if(allow_diag):
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    else:
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Define the heuristic function (Manhattan distance)
    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Check if a position is valid and can be traversed
    def is_valid_position(x: int, y: int) -> bool:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            place_type = grid[x][y]
            return place_type == THUAI7.PlaceType.Space or place_type == THUAI7.PlaceType.Shadow
        return False

    # Initialize the open and closed sets
    open_set = [start]
    closed_set = []

    # Initialize the cost and came_from dictionaries
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}

    # A* algorithm
    while open_set:
        # Find the node with the lowest f_score in the open set
        current = min(open_set, key=lambda x: f_score[x])

        # Check if the goal has been reached
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        # Move the current node from the open set to the closed set
        open_set.remove(current)
        closed_set.append(current)

        # Explore the neighbors of the current node
        for movement in movements:
            neighbor = (current[0] + movement[0], current[1] + movement[1])

            # Skip if the neighbor is not a valid position
            if not is_valid_position(neighbor[0], neighbor[1]):
                continue

            # Calculate the tentative g_score for the neighbor
            tentative_g_score = g_score[current] + 1

            # Skip if the neighbor has already been evaluated with a lower g_score
            if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            # Update the g_score and f_score for the neighbor
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

            # Add the neighbor to the open set if it's not already there
            if neighbor not in open_set:
                open_set.append(neighbor)

    # No path found
    return []

# Test the Astar function
if __name__ == "__main__":
    # Define the grid
    grid = [
        [THUAI7.PlaceType.Space, THUAI7.PlaceType.Space,THUAI7.PlaceType.Space],
        [THUAI7.PlaceType.Space, THUAI7.PlaceType.Home, THUAI7.PlaceType.Space],
        [THUAI7.PlaceType.Space, THUAI7.PlaceType.Space,THUAI7.PlaceType.Space]
    ]
    # Define the start and goal positions
    start = (0, 0)
    goal = (2, 2)
    # Find the path using Astar algorithm
    path = Astar(grid, start, goal,allow_diag=True)
    # Print the path
    print("Path:", path)