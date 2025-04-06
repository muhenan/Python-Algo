from typing import List


class KnightTourChecker:
    """
    LeetCode 2596: Check Knight Tour Configuration
    
    Given an n x n grid, check if it represents a valid knight's tour.
    A valid tour means:
    - Starting from cell (0,0) with value 0
    - Each move is a valid knight move (L-shape: 2 steps + 1 step perpendicular)
    - Visit each cell exactly once with values 0 to n²-1 in order
    
    Example:
    Input: grid = [[0,3,6],[5,8,1],[2,7,4]]
    Output: true
    
    Tags:
    - Matrix
    - DFS
    - Graph
    - Validation
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        """
        Check if grid represents valid knight's tour using DFS
        """
        if grid[0][0] != 0:  # Must start from (0,0)
            return False
            
        n = len(grid)
        target = n * n - 1  # Last number to reach
        
        # All possible knight moves
        directions = [
            [-2,-1], [-2,1], [2,-1], [2,1],
            [-1,-2], [-1,2], [1,-2], [1,2]
        ]
        
        def dfs(row: int, col: int, curr: int) -> bool:
            if curr == target:
                return True
                
            # Try all possible knight moves
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < n and 
                    0 <= new_col < n and 
                    grid[new_row][new_col] == curr + 1):
                    return dfs(new_row, new_col, curr + 1)
            return False # return false 不是很好看，也可以用一个全局变量来记录，最后返回全局变量，不搞bool
            
        return dfs(0, 0, 0)