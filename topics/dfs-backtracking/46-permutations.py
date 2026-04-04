"""
LeetCode 46: Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

Tags:
- Array
- Backtracking
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        ans = []
        def dfs(current):
            if len(current) == len(nums):
                ans.append(list(current))
                return
            for i in range(len(nums)):
                if not visited[i]:
                    current.append(nums[i])
                    visited[i] = True
                    dfs(current)
                    current.pop()
                    visited[i] = False
        dfs([])
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        # swap-based: 原地交换，O(1) 额外空间
        ans = []
        def dfs(start):
            if start == len(nums):
                ans.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)
        return ans



# Tests
if __name__ == "__main__":
    s = Solution()

    assert sorted(s.permute([1, 2, 3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert sorted(s.permute([0, 1])) == sorted([[0,1],[1,0]])
    assert s.permute([1]) == [[1]]
    from itertools import permutations
    assert sorted(s.permute([1,2,3,4,5])) == sorted([list(p) for p in permutations([1,2,3,4,5])])

    assert sorted(s.permute2([1, 2, 3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert sorted(s.permute2([0, 1])) == sorted([[0,1],[1,0]])
    assert s.permute2([1]) == [[1]]
    assert sorted(s.permute2([1,2,3,4,5])) == sorted([list(p) for p in permutations([1,2,3,4,5])])

    print("All tests passed!")
