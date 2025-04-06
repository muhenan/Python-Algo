from typing import List


class LongestAlternatingSubarrayFinder:
    """
    LeetCode 2765: Longest Alternating Subarray
    
    Find the longest alternating subarray in nums where:
    - The subarray must start with nums[i], nums[i+1] where nums[i+1] = nums[i] + 1
    - For all indices in subarray, nums[k] = nums[k-2] (alternating pattern)
    
    Example:
    Input: nums = [2,3,4,3,4]
    Output: 5 (The entire array is alternating: 2,3,4,3,4)
    
    Tags:
    - Sliding Window
    - Array
    - Two Pointers
    - Pattern Matching
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """

    def alternatingSubarray(self, nums: List[int]) -> int:
        """
        First approach: Basic sliding window implementation
        
        Args:
            nums: List of integers
            
        Returns:
            int: Length of longest alternating subarray, -1 if none exists
            
        Strategy:
            - For each possible start position, check if it can start an alternating sequence
            - Extend the sequence as long as the alternating pattern holds
            - Track the maximum length found
        """
        max_length = -1
        for left in range(len(nums) - 1):
            if (nums[left + 1] - nums[left]) == 1:  # Valid start condition
                current_max = 2
                for i in range(left + 2, len(nums)):
                    if nums[i] != nums[i - 2]:  # Pattern breaks
                        break
                    current_max += 1
                max_length = max(max_length, current_max)
        return max_length

    def alternatingSubarray2(self, nums: List[int]) -> int:
        """
        Optimized approach: Sliding window with smart skipping
        
        Args:
            nums: List of integers
            
        Returns:
            int: Length of longest alternating subarray, -1 if none exists
            
        Strategy:
            - Similar to first approach but optimizes the outer loop
            - When pattern breaks at position i, we can safely skip to i-1
            - This avoids checking positions that cannot lead to longer sequences
        """
        max_length = -1
        for left in range(len(nums) - 1):
            if (nums[left + 1] - nums[left]) == 1:  # Valid start condition
                current_max = 2
                for i in range(left + 2, len(nums)):
                    if nums[i] != nums[i - 2]:  # Pattern breaks
                        left = i - 1  # Skip to last valid position
                        break
                    current_max += 1
                max_length = max(max_length, current_max)
        return max_length