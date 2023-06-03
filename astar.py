import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(position, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    x, y = position

    # Define the possible neighboring positions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

def calculate_heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def reconstruct_path(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Initialize the start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Create open and closed sets
    open_set = []
    closed_set = set()

    # Add the start node to the open set
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        # Check if the goal has been reached
        if current_node.position == goal_node.position:
            return reconstruct_path(current_node)

        # Get the neighboring positions
        neighbors = get_neighbors(current_node.position, grid)

        for neighbor in neighbors:
            if neighbor in closed_set:
                continue

            # Calculate the cost to move to the neighbor
            g = current_node.g + 1

            # Check if the neighbor is already in the open set
            is_in_open_set = False
            for node in open_set:
                if node.position == neighbor:
                    is_in_open_set = True
                    break

            if not is_in_open_set or g < node.g:
                h = calculate_heuristic(neighbor, goal_node.position)
                new_node = Node(neighbor, current_node, g, h)

                if not is_in_open_set:
                    heapq.heappush(open_set, new_node)
                else:
                    node.g = g
                    node.parent = current_node
                    node.f = g + node.h

    return []

# Example usage:
grid = [[0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
print("Path:", path)

