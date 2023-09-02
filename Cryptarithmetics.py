import itertools

def solve_cryptarithmetic(puzzle):
    letters = set("".join(puzzle))
    if len(letters) > 10:
        print("Invalid input: More than 10 unique letters.")
        return

    # Generate all possible digit permutations for the letters
    for perm in itertools.permutations("0123456789", len(letters)):
        digit_map = dict(zip(letters, perm))

        # Replace letters with digits in the puzzle
        puzzle_digits = ["".join([digit_map[c] for c in word]) for word in puzzle]

        # Check for leading zeros in each word
        if all(word[0] != '0' for word in puzzle_digits):
            # Convert puzzle words to integers
            values = [int(word) for word in puzzle_digits]

            # Check if the equation is valid
            if sum(values[:-1]) == values[-1]:
                return dict(zip(letters, map(int, perm)))

    return None

def main():
    puzzle = ["SEND", "MORE", "MONEY"]

    solution = solve_cryptarithmetic(puzzle)

    if solution:
        print("Solution:")
        for word in puzzle:
            print(f"{word}: {''.join([str(solution[c]) for c in word])}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
