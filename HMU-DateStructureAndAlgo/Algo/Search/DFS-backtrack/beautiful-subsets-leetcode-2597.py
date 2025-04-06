from typing import List


class BeautifulSubsetCounter:
    """
    LeetCode 2597: Beautiful Subsets
    
    Given an array nums and an integer k, find the number of beautiful subsets.
    A subset is beautiful if it doesn't contain any pair of elements with difference k.
    
    Example:
    Input: nums = [2,4,6], k = 2
    Output: 4
    Explanation: Beautiful subsets are: [], [2], [4], [6]
    
    Tags:
    - DFS
    - Backtracking
    - Set
    """
    def __init__(self):
        self.count = 1  # Global counter for both methods
        
    def beautifulSubsetsDFS(self, nums: List[int], k: int) -> int:
        """
        DFS solution using global set to track used numbers
        
        Strategy:
            - Use DFS to try each number
            - Check k-difference constraint using set
            - Global counter for counting valid subsets
        """
        self.count = 1  # Initialize counter to 1, including empty set
        used = set()
        
        def dfs(index: int, k: int):
            # Check if current number can be used
            val_minus = nums[index] - k
            val_plus = nums[index] + k
            if val_minus in used or val_plus in used:
                return
                
            # Valid number found, add to count and set
            self.count += 1
            used.add(nums[index])
            
            # Try all next numbers
            for next_idx in range(index + 1, len(nums)):
                dfs(next_idx, k)
                
            # Backtrack by removing current number
            used.remove(nums[index])
            
        # Try each number as starting point
        for i in range(len(nums)):
            dfs(i, k)
            
        return self.count
        
    def beautifulSubsetsBacktrack(self, nums: List[int], k: int) -> int:
        """
        Backtracking solution making decision for each number
        
        Strategy:
            - For each number, decide whether to take it or not
            - Count immediately after adding a valid number
            - Use backtracking to try all possibilities
            - Global counter for counting valid subsets
        """
        self.count = 1  # Initialize counter to 1, including empty set
        used = set()
        
        def backtrack(index: int):
            # Base case: processed all numbers
            if index == len(nums):
                return
            
            # Don't take current number
            backtrack(index + 1)
            
            # Try to take current number if valid
            curr = nums[index]
            if (curr + k not in used) and (curr - k not in used):
                used.add(curr)
                self.count += 1  # Count immediately after adding valid number
                backtrack(index + 1)
                used.remove(curr)
        
        backtrack(0)
        return self.count  # No need to subtract 1 now