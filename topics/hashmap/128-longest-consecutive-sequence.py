"""
LeetCode 128: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive sequence is [1,2,3,4], length 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Tags:
- Array
- Hash Table
- Union Find
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num - 1 not in s:
                current_ans = 0
                while num + current_ans in s:
                    current_ans += 1
                ans = max(ans, current_ans)
        return ans


# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    assert s.longestConsecutive([1]) == 1
    assert s.longestConsecutive([1, 2, 0, 1]) == 3

    print("All tests passed!")
