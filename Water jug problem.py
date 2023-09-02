from collections import deque

class State:
    def __init__(self, x, y):
        self.x = x  # Current water level in the first jug
        self.y = y  # Current water level in the second jug

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

def water_jug_problem(capacity_x, capacity_y, target):
    initial_state = State(0, 0)
    visited = set()
    queue = deque()
    queue.append((initial_state, []))

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.x == target or current_state.y == target:
            path.append(current_state)
            return path

        # Fill jug X
        if current_state.x < capacity_x:
            new_state = State(capacity_x, current_state.y)
            queue.append((new_state, path + [current_state]))

        # Fill jug Y
        if current_state.y < capacity_y:
            new_state = State(current_state.x, capacity_y)
            queue.append((new_state, path + [current_state]))

        # Empty jug X
        if current_state.x > 0:
            new_state = State(0, current_state.y)
            queue.append((new_state, path + [current_state]))

        # Empty jug Y
        if current_state.y > 0:
            new_state = State(current_state.x, 0)
            queue.append((new_state, path + [current_state]))

        # Pour water from X to Y
        if current_state.x > 0 and current_state.y < capacity_y:
            pour = min(current_state.x, capacity_y - current_state.y)
            new_state = State(current_state.x - pour, current_state.y + pour)
            queue.append((new_state, path + [current_state]))

        # Pour water from Y to X
        if current_state.y > 0 and current_state.x < capacity_x:
            pour = min(current_state.y, capacity_x - current_state.x)
            new_state = State(current_state.x + pour, current_state.y - pour)
            queue.append((new_state, path + [current_state]))

    return None

def main():
    capacity_x = 4  # Capacity of the first jug
    capacity_y = 3  # Capacity of the second jug
    target = 2     # Target quantity of water to measure

    solution_path = water_jug_problem(capacity_x, capacity_y, target)

    if solution_path:
        print("Solution:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
