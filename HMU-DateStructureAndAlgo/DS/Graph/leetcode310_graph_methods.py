from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        """ Build Graph """
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1      # unnecessary
            deg[y] += 1

        """ BFS """
        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                parent = q.popleft()
                for child in g[parent]:
                    if not vis[child]:
                        vis[child] = True
                        q.append(child)

        """ DFS """
        def dfs(start):
            vis = [False] * n
            vis[start] = True
            for child in g[start]:
                if not vis[child]:
                    vis[child] = True
                    dfs(child)

        """
        拓扑排序
        逐渐去掉最外圈度为 1 的结点
        """
        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for outsider in tmp:
                for insider in g[outsider]:
                    deg[insider] -= 1
                    if deg[insider] == 1:
                        q.append(insider)



        return None