"""
LeetCode 79: Word Search

Given an m x n grid of characters board and a string word, return true if word exists
in the grid. The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: True

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: True

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: False

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consist only of lowercase and uppercase English letters.

Tags:
- Array
- Backtracking
- Matrix
"""

from typing import List


class Solution:
    """
    LeetCode 79: Word Search

    Grid backtracking: try each cell as the starting point, DFS in 4 directions,
    mark visited by temporarily modifying the cell (restore on backtrack).

    Tags: Array, Backtracking, Matrix
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS + backtracking on grid. Mark visited by overwriting cell, restore on exit.

        Example:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: True

        Time Complexity: O(m * n * 4^L) where L = len(word)
        Space Complexity: O(L) recursion depth
        """
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(r, c, index):
            if index == len(word):
                return True
            for d in directions:
                r_n, c_n = r + d[0], c + d[1]
                if 0 <= r_n < rows and 0 <= c_n < cols and board[r_n][c_n] == word[index]:
                    tmp, board[r_n][c_n] = board[r_n][c_n], '#'
                    if dfs(r_n, c_n, index + 1):
                        return True
                    board[r_n][c_n] = tmp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    tmp, board[r][c] = board[r][c], '#'
                    if dfs(r, c, 1):
                        return True
                    board[r][c] = tmp
        return False


if __name__ == "__main__":
    s = Solution()

    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert s.exist([row[:] for row in board1], "ABCCED") == True
    assert s.exist([row[:] for row in board1], "SEE") == True
    assert s.exist([row[:] for row in board1], "ABCB") == False

    assert s.exist([["a"]], "a") == True
    assert s.exist([["a"]], "b") == False

    print("All tests passed!")
