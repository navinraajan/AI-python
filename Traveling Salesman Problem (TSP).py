import itertools
import sys

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    if num_cities <= 2:
        return list(range(num_cities))

    min_path = None
    min_distance = sys.maxsize

    cities = list(range(num_cities))
    for perm in itertools.permutations(cities[1:], num_cities - 1):
        path = [0] + list(perm) + [0]
        distance = calculate_total_distance(path, distances)
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance

def main():
    # Example distances between cities (replace with your own data)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    optimal_path, optimal_distance = traveling_salesman_bruteforce(distances)

    print("Optimal Path:", optimal_path)
    print("Optimal Distance:", optimal_distance)

if __name__ == "__main__":
    main()
