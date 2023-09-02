import random

class VacuumCleaner:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]
        self.position = [random.randint(0, grid_size-1), random.randint(0, grid_size-1)]

    def display_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
        print()

    def clean(self):
        while True:
            self.display_grid()
            dirty = self.grid[self.position[0]][self.position[1]]

            if dirty:
                print(f"Cleaning cell ({self.position[0]}, {self.position[1]})")
                self.grid[self.position[0]][self.position[1]] = 0

            if self.check_complete():
                print("Cleaning complete!")
                break

            self.move()

    def check_complete(self):
        for row in self.grid:
            if 1 in row:
                return False
        return True

    def move(self):
        options = ["up", "down", "left", "right"]
        random.shuffle(options)

        for direction in options:
            new_position = self.calculate_new_position(direction)
            if self.is_valid_position(new_position):
                self.position = new_position
                return

    def calculate_new_position(self, direction):
        x, y = self.position
        if direction == "up":
            return [x - 1, y]
        elif direction == "down":
            return [x + 1, y]
        elif direction == "left":
            return [x, y - 1]
        elif direction == "right":
            return [x, y + 1]

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

def main():
    grid_size = 5
    vacuum = VacuumCleaner(grid_size)
    vacuum.clean()

if __name__ == "__main__":
    main()
