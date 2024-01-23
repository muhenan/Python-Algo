from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = -1
        for left in range(len(nums) - 1):
            if (nums[left + 1] - nums[left]) == 1:
                current_max = 2
                for i in range(left + 2, len(nums)):
                    if nums[i] != nums[i - 2]:
                        break
                    current_max += 1
                max_length = max(max_length, current_max)
        return max_length
    def alternatingSubarray2(self, nums: List[int]) -> int:
        max_length = -1
        for left in range(len(nums) - 1):
            if (nums[left + 1] - nums[left]) == 1:
                current_max = 2
                for i in range(left + 2, len(nums)):
                    if nums[i] != nums[i - 2]:
                        left = i - 1
                        break
                    current_max += 1
                max_length = max(max_length, current_max)
        return max_length