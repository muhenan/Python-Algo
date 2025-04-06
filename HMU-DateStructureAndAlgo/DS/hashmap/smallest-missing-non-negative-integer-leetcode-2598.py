class SmallestMissingFinder:
    """
    LeetCode 2598: Smallest Missing Non-negative Integer After Operations
    
    Given an array nums and value, you can add/subtract value from any element 
    any number of times. Find the smallest non-negative integer that cannot be 
    made equal to any element in nums after these operations.
    
    Example:
    Input: nums = [1,2,3,4], value = 5
    Output: 10
    
    Tags:
    - Math
    - Array
    - Hash Set
    - Modular Arithmetic
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Convert all numbers to their smallest non-negative equivalent mod value
        freq = {}
        for num in nums:
            mod = ((num % value) + value) % value
            freq[mod] = freq.get(mod, 0) + 1
            
        # Check each number in order
        i = 0
        while True:
            mod = i % value
            if mod not in freq or freq[mod] == 0:
                return i
            freq[mod] -= 1
            i += 1