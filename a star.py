import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # Actual cost from the start node to this node
        self.h = 0  # Heuristic cost from this node to the goal node
        self.parent = None

    def __lt__(self, other):
        # Comparison for priority queue (heap)
        return (self.g + self.h) < (other.g + other.h)

def calculate_heuristic(current, goal):
    # Manhattan distance heuristic
    return abs(current.x - goal.x) + abs(current.y - goal.y)

def a_star(grid, start, goal):
    open_set = []  # Priority queue (heap) of open nodes
    closed_set = set()  # Set of closed nodes

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    open_set.append(start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to start from the start node

        closed_set.add((current_node.x, current_node.y))

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible moves (up, down, right, left)

        for dx, dy in neighbors:
            new_x, new_y = current_node.x + dx, current_node.y + dy

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                neighbor_node = Node(new_x, new_y)

                if (new_x, new_y) in closed_set:
                    continue

                neighbor_node.g = current_node.g + 1  # Cost to reach the neighbor
                neighbor_node.h = calculate_heuristic(neighbor_node, goal_node)
                neighbor_node.parent = current_node

                if neighbor_node not in open_set:
                    heapq.heappush(open_set, neighbor_node)

    return None

def main():
    # Example grid with 0s as empty cells and 1s as obstacles
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)  # Starting point (row, column)
    goal = (4, 4)   # Goal point (row, column)

    path = a_star(grid, start, goal)

    if path:
        print("Shortest Path:")
        for x, y in path:
            print(f"({x}, {y})")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
