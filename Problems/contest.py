from typing import List


class Solution2460:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # for i in range(length - 1):
        #     if nums[i] == nums[i + 1]:
        #         nums[i] *= 2
        #         nums[i + 1] = 0
        # result = [0 for _ in range(length)]
        # index = 0
        # for i in range(length):
        #     if nums[i] != 0:
        #         result[index] = nums[i]
        #         index += 1
        # return result
        index = 0
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i]:
                old = nums[i]
                nums[i] = 0
                nums[index] = old
                index += 1
        if nums[-1]:
            old = nums[-1]
            nums[-1] = 0
            nums[index] = old
        return nums

solu = Solution2460()
solu.applyOperations([1,2,2,1,1,0])