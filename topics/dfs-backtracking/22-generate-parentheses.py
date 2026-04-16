"""
LeetCode 22: Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8

Tags:
- String
- Backtracking
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid parentheses strings with backtracking.

        Example:
        Input: n = 3
        Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

        Tags:
        - String
        - Backtracking

        Time Complexity: O(Cn * n), where Cn is the nth Catalan number
        Space Complexity: O(n) recursion depth, excluding output
        """
        ans: List[str] = []

        def backtrack(left: int, right: int, current: List[str]) -> None:
            if left == 0 and right == 0:
                ans.append(''.join(current))
                return
            if left > 0:
                current.append('(')
                backtrack(left - 1, right, current)
                current.pop()
            if left < right:
                current.append(')')
                backtrack(left, right - 1, current)
                current.pop()
        backtrack(n, n, [])
        return ans


# Tests
if __name__ == "__main__":
    s = Solution()

    assert sorted(s.generateParenthesis(1)) == sorted(["()"])
    assert sorted(s.generateParenthesis(2)) == sorted(["(())", "()()"])
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])
    assert len(s.generateParenthesis(4)) == 14  # Catalan number C(4)

    print("All tests passed!")
