class MinimumOperationsCalculator:
    """
    LeetCode 2571: Minimum Operations to Reach a Number
    (From Weekly Contest 333)
    
    Given a positive integer n, in one operation you can:
    1. Add or subtract a power of 2 (2^x) from n
    Find the minimum number of operations to reduce n to 0.
    
    Example:
    Input: n = 54
    Output: 3
    Explanation: 
    54 -> (54-32=22) -> (22-16=6) -> (6-4=2) -> (2-2=0)
    
    Tags:
    - Dynamic Programming
    - Math
    - Binary Operations
    
    Time Complexity: O(logn)
    Space Complexity: O(logn)
    """
    def minOperations(self, n: int) -> int:
        """
        Calculate minimum operations using dynamic programming
        
        Args:
            n: Target number to reduce to 0
            
        Returns:
            int: Minimum number of operations needed
            
        Strategy:
            - Use DP to store minimum operations for each number
            - For each number, try nearest powers of 2 above and below
            - Memoize results to avoid recalculation
        """
        # Initialize set of powers of 2
        powers_of_two = set(2**i for i in range(19))  # 2^19 > 10^5
        memo = {}
        
        def dp(number: int) -> int:
            # Base case: if number is power of 2
            if number in powers_of_two:
                return 1
                
            # Check memoized result
            if number in memo:
                return memo[number]
                
            # Find nearest power of 2 above number
            next_power = 1
            while next_power < number:
                next_power *= 2
                
            # Try both options: next_power - number or number - (next_power//2)
            memo[number] = 1 + min(
                dp(next_power - number),
                dp(number - next_power // 2)
            )
            
            return memo[number]
            
        return dp(n)