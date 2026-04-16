from typing import Dict, List


class Solution:
    """
    LeetCode 2597: The Number of Beautiful Subsets

    Given an integer array nums and an integer k, return the number of
    non-empty beautiful subsets. A subset is beautiful if it does not contain
    two integers whose absolute difference equals k.

    Example:
    Input: nums = [2, 4, 6], k = 2
    Output: 4

    Tags:
    - DFS
    - Backtracking
    - Hash Map
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        Count valid subsets with DFS and a frequency map.

        Example:
        Input: nums = [2, 4, 6], k = 2
        Output: 4

        Tags:
        - DFS
        - Backtracking

        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        count: Dict[int, int] = {}

        def dfs(index: int) -> int:
            if index == len(nums):
                return 1
            res = dfs(index + 1)
            num = nums[index]
            if count.get(num - k, 0) == 0 and count.get(num + k, 0) == 0:
                count[num] = count.get(num, 0) + 1
                res += dfs(index + 1)
                count[num] -= 1
            return res

        return dfs(0) - 1 # exclude the empty subset


if __name__ == "__main__":
    solu = Solution()
    assert solu.beautifulSubsets([2, 4, 6], 2) == 4
    assert solu.beautifulSubsets([1], 1) == 1
    assert solu.beautifulSubsets([10, 4, 5, 7, 2, 1], 3) == 23
    print("All tests passed!")
