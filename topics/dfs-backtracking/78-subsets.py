"""
LeetCode 78: Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

Tags:
- Array
- Backtracking
- Bit Manipulation
"""

from typing import List


class Solution:
    """
    LeetCode 78: Subsets

    Tags: Array, Backtracking
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking: collect path at every DFS node (not just leaves).

        Example:
        Input: nums = [1, 2, 3]
        Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n) recursion depth + output
        """
        ans = []
        def backtrack(index, current: List[int]):
            if index == len(nums):
                ans.append(list(current))
                return
            # do not include nums[index]
            backtrack(index + 1, current)
            # include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()
        backtrack(0, [])
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking: for-loop style, collect at every node before branching.

        Example:
        Input: nums = [1, 2, 3]
        Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n) recursion depth + output
        """
        ans = []
        def backtrack(start: int, current: List[int]):
            ans.append(list(current))
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        backtrack(0, [])
        return ans


if __name__ == "__main__":
    s = Solution()

    def normalize(res):
        return sorted(sorted(sub) for sub in res)

    assert normalize(s.subsets([1, 2, 3])) == normalize([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert normalize(s.subsets([0])) == normalize([[], [0]])

    assert normalize(s.subsets2([1, 2, 3])) == normalize([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert normalize(s.subsets2([0])) == normalize([[], [0]])

    print("All tests passed!")
