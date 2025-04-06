from collections import deque

"""
这里关于 bfs，我觉得最重要的是搞懂 queue的概念

queue存的到底是什么

我的queue存的是已经发现了，但是还没有处理的节点

这里就涉及了两个事：
1. 发现
2. 处理

比如 start 节点，这个节点一开始就发现了，但我并不处理，所以我只是把它丢进 queue
后面的也是一样，我发现了，但不处理，就丢进 q
只有真正出 queue 之后我才处理
"""

def bfs(graph, start):
    visited = set()  # 使用 set 而不是 dict 来跟踪访问过的节点
    queue = deque([start]) # 已发现但尚未完全探索（处理）的节点
    visited.add(start)  # 将起始节点标记为已访问

    while queue:
        vertex = queue.popleft()
        print(vertex)  # 处理当前节点

        # 访问所有未访问的相邻节点
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # 将邻居节点标记为已访问
                queue.append(neighbor)  # 将邻居节点加入队列

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


########################################################

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

# Call BFS with levels
bfs_levels(graph, start_vertex)
