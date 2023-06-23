from collections import deque

'''
a breadth-first search (BFS) implementation that processes vertices level by level, 
where each level is processed separately
'''

def bfs_levels(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_size = len(queue)

        for _ in range(current_size):
            vertex = queue.popleft()
            visited.add(vertex)
            print(vertex)  # Process the vertex (in this example, we print it)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
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

# Call BFS with levels
bfs_levels(graph, start_vertex)
