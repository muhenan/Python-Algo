from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        row, col = len(grid), len(grid[0])
        queue = deque()
        directions = [[1, 1], [-1, 1], [1, -1], [-1, -1], [0, 1], [1, 0], [0, -1], [-1, 0]]
        queue.append([0, 0])
        pathLength = 0
        visited = set((0,0))
        while queue:
            size = len(queue)
            pathLength += 1
            # print(pathLength)
            while size:
                cr, cc = queue.popleft()
                # print(cr, cc)
                if cr == row - 1 and cc == col - 1:
                    return pathLength
                grid[cr][cc] = 1
                for d in directions:
                    nr, nc = cr + d[0], cc + d[1]
                    if nr < 0 or nc < 0 or nr >= row or nc >= col or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    else:
                        # print("next ", nr, nc)
                        visited.add((nr, nc))
                        queue.append([nr, nc])
                size -= 1
        return -1