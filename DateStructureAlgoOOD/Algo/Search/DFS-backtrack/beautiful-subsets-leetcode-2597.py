from typing import List


class BeautifulSubsetCounter:
    """
    LeetCode 2597: Beautiful Subsets
    
    Given an array nums and an integer k, find the number of beautiful subsets.
    A subset is beautiful if it doesn't contain any pair of elements with difference k. (non-empty)
    
    Example:
    Input: nums = [2,4,6], k = 2
    Output: 4
    Explanation: Beautiful subsets are: [2, 6], [2], [4], [6]
    
    Tags:
    - DFS
    - Backtracking
    - Set
    """
    def beautifulSubsetsBacktrack(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = {}
        def dfs(i):
            nonlocal ans
            if i == len(nums):
                ans += 1
                return
            dfs(i + 1)
            if cnt.get(nums[i] - k, 0) == 0 and cnt.get(nums[i] + k, 0) == 0:
                cnt[nums[i]] = cnt.get(nums[i], 0) + 1
                dfs(i + 1)
                cnt[nums[i]] -= 1

        dfs(0)
        return ans - 1