class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, var, value):
        for neighbor in self.constraints.get(var, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        var = next(iter([v for v in self.variables if v not in assignment]))

        for value in self.domains[var]:
            if self.is_consistent(assignment, var, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]

        return None

def main():
    # Define the variables (regions) and their possible colors (domains)
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains = {
        "WA": ["R", "G", "B"],
        "NT": ["R", "G", "B"],
        "SA": ["R", "G", "B"],
        "Q": ["R", "G", "B"],
        "NSW": ["R", "G", "B"],
        "V": ["R", "G", "B"],
        "T": ["R", "G", "B"]
    }

    # Define the constraints (adjacent regions)
    constraints = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["SA", "Q", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }

    csp = CSP(variables, domains, constraints)
    assignment = csp.backtrack()

    if assignment:
        print("Map Coloring Solution:")
        for var, color in assignment.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
