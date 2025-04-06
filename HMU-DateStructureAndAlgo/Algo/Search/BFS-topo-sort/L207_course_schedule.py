from collections import deque
from typing import List

"""
topological sort
拓扑排序

存在于有向无环图中
先修课程问题，修这些课的顺序，这就是拓扑排序

Topo 其实就是类似于 BFS
"""

"""
经典先修课 -> topological sort

最直接的思路
传统建图，二维数组 -> 从入度是 0 的点 BFS，用一个 BFS 队列保存所有入度为 0 的点 -> 试图走遍所有
"""

class Solution:
    """ Topo BFS """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for to, pre in prerequisites:
            graph[pre].append(to)
            indegree[to] += 1
        visited = [False] * numCourses
        start_q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                start_q.append(i)
        while start_q:
            curr = start_q.popleft()
            visited[curr] = True
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    start_q.append(i)
        return all(visited)

    """
    这种最经典的图叫 adjacency
    
    indegrees = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    """

    """
    DFS 的思路略有不同，和拓扑排序关系不大了，DFS 是判断有没有环，没有环的话就 True，有就 False
    
    DFS
    """
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for to, pre in prerequisites:
            graph[pre].append(to)

        color = [0] * numCourses # 0 -> not visited, 1 -> visiting, 2 -> visited by others

        def dfs(index): # 只有 0 的才进来
            color[index] = 1
            for i in graph[index]:
                if color[i] == 1:
                    return True # 有环 返回 True
                elif color[i] == 0:
                    if dfs(i): return True
            color[index] = 2
            return False

        def hasCycle(k):
            for i in range(k):
                if color[i] == 0 and dfs(i):
                    return True # 有环
            return False # 没环
        return not hasCycle(numCourses)

