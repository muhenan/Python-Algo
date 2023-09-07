from collections import deque
from typing import List

"""
迪杰斯特拉是到每个点的最短路径
我们这里要算的就是到每个点的最大安全距离

dijkstra -> min path
for this question -> max safeness
"""

class Solution1:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        pts = deque([])
        cost = [[-1 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    pts.append((i, j))
                    cost[i][j] = 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pts:
            b = pts.popleft()
            x, y = b[0], b[1]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n or cost[nx][ny] != -1:
                    continue
                pts.append((nx, ny))
                cost[nx][ny] = cost[x][y] + 1



        return None

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]], xs, ys, xe, ye) -> int:
        xLen = len(grid)
        yLen = len(grid[0])
        q = []
        dis = [[-1] * yLen for _ in range(xLen)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0

        groups = [q]
        while q:  # 多源 BFS
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < xLen and 0 <= y < yLen and dis[x][y] < 0:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)  # 相同 dis 分组记录

        # 并查集模板
        fa = list(range(xLen * yLen))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < xLen and 0 <= y < yLen and dis[x][y] >= dis[i][j]:
                        # 这里是重中之重，这里是让 x，y 的父亲指着 i，j也就是把 x 和 y 和之前的全指着 i，j 了
                        # 并查集，把一个很深远的父亲改了，就相当于把整个那块的根都改了
                        fa[find(x * yLen + y)] = find(i * yLen + j)
            if find(xs * yLen + ys) == find(xe * yLen + ye):  # 写这里判断更快些
                return d
        return 0

solu = Solution()
solu.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,1],[0,0,0],[0,0,0]], 1, 1, 4,2)