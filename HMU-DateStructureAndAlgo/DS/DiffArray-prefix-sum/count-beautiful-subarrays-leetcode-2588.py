from typing import List


class BeautifulSubarrayCounter:
    """
    LeetCode 2588: Count Beautiful Subarrays
    
    A subarray is beautiful if the bitwise XOR of all elements is equal to 0.
    Return the number of beautiful subarrays in the given array.
    
    Example:
    Input: nums = [4,3,1,2,4]
    Output: 2
    
    Tags:
    - Prefix XOR
    - Hash Map
    - Bit Manipulation
    """
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """
        Use prefix XOR and hash map to find subarrays with XOR sum = 0
        
        Strategy:
        1. Use running XOR (state) to track cumulative XOR
        2. If we find same state again, means subarray between has XOR=0
        3. Use hash map to track frequency of each state
        4. Initialize with state 0 having count 1 (empty subarray)
        """
        # Initialize hash map with state 0
        state_map = {0: 1}  # state -> frequency
        
        beautiful_count = 0
        current_state = 0
        
        for num in nums:
            # Update running XOR state
            current_state ^= num
            
            # Add count of previous same states
            if current_state in state_map:
                beautiful_count += state_map[current_state]
            
            # Update state frequency
            state_map[current_state] = state_map.get(current_state, 0) + 1
            """
            也可以这样设置好初始默认值
            my_dictionary = defaultdict(lambda : 0)
            """
            
        return beautiful_count