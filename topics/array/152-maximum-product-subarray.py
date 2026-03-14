from typing import List


class Solution:
    def maxProduct(self, nums):
        result = nums[0]
        currentMax = 1
        currentMin = 1
        for element in nums:
            arr = sorted([currentMax * element, currentMin * element, element])
            currentMax = arr[2]
            currentMin = arr[0]
            result = max(result, currentMax)
        return result

solu = Solution()

solu.maxProduct([2,3,-2,4])