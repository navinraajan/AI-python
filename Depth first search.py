class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start_node)
        print(start_node, end=' ')

        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

def main():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')

    print("Depth-First Traversal (starting from 'A'):")
    graph.dfs('A')

if __name__ == "__main__":
    main()
