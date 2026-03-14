
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        def dfs(curr_node:'Node'):
            if not curr_node:
                return curr_node
            if curr_node in self.visited:
                return self.visited[curr_node]
            clone_node = Node(curr_node.val)
            self.visited[curr_node] = clone_node
            if len(curr_node.neighbors) != 0:
                for n in curr_node.neighbors:
                    clone_node.neighbors.append(dfs(n))
            return clone_node
        return dfs(node)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        self.result = True
        visited = [0] * numCourses
        def dfs(index):
            if not self.result: return
            visited[index] = 1
            for n in edges[index]:
                if visited[n] == 1:
                    self.result = False
                elif visited[n] == 0:
                    dfs(n)
            visited[index] = 2
        for i in range(numCourses):
            dfs(i)
        return self.result