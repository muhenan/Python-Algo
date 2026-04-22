"""
LeetCode 1091: Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell `(0, 0)` to the
bottom-right cell `(n - 1, n - 1)` such that:
- All visited cells are `0`
- All adjacent cells in the path are 8-directionally connected
- The length of the path is the number of visited cells

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 2

Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

Tags:
- Array
- Breadth-First Search
- Depth-First Search
- Matrix
"""

from collections import deque
from typing import List


class Solution:
    """
    LeetCode 1091: Shortest Path in Binary Matrix

    Tags: Array, Breadth-First Search, Depth-First Search, Matrix
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS level-order traversal on the grid.

        Example:
        Input: grid = [[0,1],[1,0]]
        Output: 2

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
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

    def shortestPathBinaryMatrix_dfs(self, grid: List[List[int]]) -> int:
        """
        DFS + backtracking: enumerate reachable paths and keep the shortest one.

        This version is mainly for comparison. BFS is the optimal approach for
        shortest path in an unweighted grid.

        Example:
        Input: grid = [[0,1],[1,0]]
        Output: 2

        Time Complexity: O(8^(n^2)) worst case
        Space Complexity: O(n^2)
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        row, col = len(grid), len(grid[0])
        directions = [[1, 1], [-1, 1], [1, -1], [-1, -1], [0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        ans = float("inf")

        def dfs(r: int, c: int, pathLength: int) -> None:
            nonlocal ans
            if pathLength >= ans:
                return
            if r == row - 1 and c == col - 1:
                ans = min(ans, pathLength)
                return

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                dfs(nr, nc, pathLength + 1)
            visited.remove((r, c))

        dfs(0, 0, 1)
        return ans if ans != float("inf") else -1