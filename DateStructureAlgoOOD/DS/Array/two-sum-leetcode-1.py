from typing import List


class TwoSumSolver:
    """
    LeetCode 1: Two Sum
    
    Given an array of integers nums and an integer target, return indices of the two numbers 
    in nums such that they add up to target. You may assume that each input would have exactly 
    one solution, and you may not use the same element twice.
    
    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (Because nums[0] + nums[1] == 9)
    
    Tags:
    - Array
    - Hash Table
    - Two Pointers
    - Sorting
    """

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force approach: Check every possible pair
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List[int]: Indices of two numbers that sum to target
            
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Sorting + Two Pointers approach
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List[int]: Indices of two numbers that sum to target
            
        Strategy:
            - Create pairs of (value, index) to maintain original indices
            - Sort pairs by value and use two pointers
            
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        pairs = [(value, index) for index, value in enumerate(nums)]
        pairs.sort()  # Sort by value
        left, right = 0, len(nums) - 1
        
        while left < right:
            curr_sum = pairs[left][0] + pairs[right][0]
            if curr_sum == target:
                return [pairs[left][1], pairs[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal Hash Table approach
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List[int]: Indices of two numbers that sum to target
            
        Strategy:
            - Use hash map to store complement values
            - Single pass through array
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_map = {}  # value -> index mapping
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i




