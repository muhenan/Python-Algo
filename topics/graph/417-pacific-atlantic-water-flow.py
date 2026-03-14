from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 最直接思路，从两个海 DFS，标记所有能到的
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(r, c, visited):
            visited[r][c] = True
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and heights[r][c] <= heights[nr][nc]:
                    dfs(r + d[0], c + d[1], visited)
        row, col = len(heights), len(heights[0])
        pVisited = [[False] * col for _ in range(row)]
        aVisited = [[False] * col for _ in range(row)]
        for i in range(col):
            dfs(0, i, pVisited)
        for i in range(row):
            dfs(i, 0, pVisited)
        for i in range(col):
            dfs(row - 1, i, aVisited)
        for i in range(row):
            dfs(i, col - 1, aVisited)
        ans = []
        for r in range(row):
            for c in range(col):
                if pVisited[r][c] and aVisited[r][c]:
                    ans.append([r, c])
        return ans