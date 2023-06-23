from collections import deque

def bfs(graph, start):
    visited = set()  # Track visited vertices
    queue = deque([start])  # Initialize the queue with the starting vertex

    while queue:
        vertex = queue.popleft()
        print(vertex)  # Process the vertex (in this example, we print it)

        # Visit all adjacent vertices that haven't been visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting vertex for BFS
start_vertex = 'A'

# Call BFS function
bfs(graph, start_vertex)
