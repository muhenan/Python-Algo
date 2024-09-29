from typing import List


class Solution:
    # for for
    # in the first loop we go through all the elements
    # in the inner loop we go through all the elements to the a match of the previous element
    # [2, 7, 11, 15] 26
    # 2 -> 7 11 15
    # 7 -> 11 15
    # time: n2
    # space: O(1)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    # sort the array
    # two pointer, left pointer and right pointer
    # [3, 2, 4]
    # (3, 0), (2, 1), (4, 2) pairs
    # (2, 1), (3, 0), (4, 2)
    # left_p          right_p
    # time: nlogn
    # space: O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        pairs = [(value, index) for index, value in enumerate(nums)]
        pairs = sorted(pairs)
        left_p, right_p = 0, len(nums) - 1
        while left_p < right_p:
            if pairs[left_p][0] + pairs[right_p][0] == target:
                return [pairs[left_p][1], pairs[right_p][1]]
            elif pairs[left_p][0] + pairs[right_p][0] < target:
                left_p += 1
            else:
                right_p -= 1
    def twoSum2_1(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1
        while left < right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                for i in range(len(nums)):
                    if nums[i] == sorted_nums[left]:
                        left = i
                        break
                for i in range(len(nums) - 1, -1, -1):
                    if nums[i] == sorted_nums[right]:
                        right = i
                        break
                return [left, right]

    def twoSum2_2(self, nums: List[int], target: int) -> List[int]:
        # Create a list of tuples, where each tuple contains (value, index)
        indexed_nums = list(enumerate(nums))

        # Sort the list based on the values, using a lambda function for the key
        indexed_nums.sort(key=lambda x: x[1])

        left, right = 0, len(indexed_nums) - 1

        while left < right:
            sum = indexed_nums[left][1] + indexed_nums[right][1]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [indexed_nums[left][0], indexed_nums[right][0]]

    # dictionary
    # key -> value of the element
    # value -> index of the element
    # time: O(n)
    # space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            if target - nums[i] in my_map:
                return [i, my_map[target - nums[i]]]
            else:
                my_map[nums[i]] = i




