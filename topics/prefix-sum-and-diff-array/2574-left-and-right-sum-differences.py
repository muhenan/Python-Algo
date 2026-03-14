from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            LeftSum = 0
            for j in range(0, i):
                LeftSum += nums[j]
            RightSum = 0
            for j in range(i+1, len(nums)):
                RightSum += nums[j]
            answer.append(abs(RightSum - LeftSum))
        return answer
