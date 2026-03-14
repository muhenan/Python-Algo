# countOfS = {}
# countOfS['a'] += 1
# print(countOfS['a'])
from collections import defaultdict
from typing import List


# print(10**10)
#
# print(2**3)


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0
        def dfs(index, current_dict, k):
            nonlocal ans
            if index == len(nums):
                return
            if current_dict[nums[index] + k] > 0 or current_dict[nums[index] - k] > 0:
                return
            ans += 1
            current_dict[nums[index]] += 1
            # print(current_dict)
            for i in range(index+1, len(nums)):
                dfs(i, current_dict, k)
            current_dict[nums[index]] -= 1
        for i in range(0, len(nums)):
            dfs(i, defaultdict(int), k)
        return ans
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        # ans = [0] * len(nums)
        # index_of_ans = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != 0:
        #         ans[index_of_ans] = nums[i]
        #         index_of_ans += 1
        # return ans
        index_of_ans = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                old = nums[i]
                nums[i] = 0
                nums[index_of_ans] = old
                index_of_ans += 1
        return nums

solu = Solution()
print(solu.beautifulSubsets([4,2,5,9,10,3], 1))