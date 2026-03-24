class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Depth-Limited Search
    def dls(self, node, target, depth):
        if node == target:
            return True

        if depth <= 0:
            return False

        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, target, depth - 1):
                return True

        return False

    # Iterative Deepening DFS
    def iddfs(self, start, target, max_depth):
        for depth in range(max_depth + 1):
            print(f"Checking depth: {depth}")
            if self.dls(start, target, depth):
                return True
        return False


# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'G')

start = 'A'
target = 'G'
max_depth = 3

if g.iddfs(start, target, max_depth):
    print("Target found!")
else:
    print("Target not found.")