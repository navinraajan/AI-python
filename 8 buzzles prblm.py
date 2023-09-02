import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        if parent:
            self.cost = parent.cost + 1

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance

    def is_goal(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == goal_state

    def get_neighbors(self):
        neighbors = []
        i, j = self.find_empty()
        possible_moves = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for move in possible_moves:
            x, y = move
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [list(row) for row in self.state]
                new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
                neighbors.append(PuzzleNode(new_state, self, move))
        return neighbors

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    priority_queue = [initial_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.is_goal():
            return get_solution_path(current_node)

        visited.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor not in visited:
                heapq.heappush(priority_queue, neighbor)

    return None

def get_solution_path(node):
    path = []
    while node:
        path.append(node.move)
        node = node.parent
    path.reverse()
    return path

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    solution_path = solve_8_puzzle(initial_state)

    if solution_path:
        print("Solution Path:")
        for move in solution_path:
            print(move)
    else:
        print("No solution found.")
