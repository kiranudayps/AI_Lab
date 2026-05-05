from collections import deque

def bfs(graph, start):
    visited = set()          # Keep track of visited nodes
    queue = deque([start])   # Initialize queue with the starting node

    while queue:
        node = queue.popleft()   # Get the first node from the queue
        if node not in visited:
            print(node, end=" ")   # Process the node (here we just print)
            visited.add(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal starting from node A:")
bfs(graph, 'A')