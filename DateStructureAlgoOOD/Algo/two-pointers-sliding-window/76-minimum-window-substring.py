class MinWindowSubstringFinder:
    """
    LeetCode 76: Minimum Window Substring (Hard)
    
    Given two strings s and t, return the minimum window substring of s that contains 
    all characters in t. If there is no such substring, return empty string "".
    
    Example:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: Minimum window containing all characters from "ABC"
    
    Tags:
    - Sliding Window
    - Hash Table
    - String
    - Two Pointers
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is size of character set
    """
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window approach with character frequency counting
        
        Strategy:
        1. Use hash map to track needed characters
        2. Use sliding window to find valid substrings
        3. Track difference count to optimize validation
        4. Keep track of minimum window seen so far
        """
        # Edge cases
        if len(s) < len(t) or not t:
            return ""

        # Initialize character frequency map
        need = {}
        for c in t:
            need[c] = need.get(c, 0) - 1  # Count needed occurrences

        diff = len(need)  # Number of characters we still need

        # Initialize window and result tracking
        """-1 就像 Dummy node 一样，是不要的，是虚拟的，是用来占位的"""
        left = -1  # Open left boundary (actual window starts at left+1)
        min_length = len(s) + 1  # Initialize to impossible length
        min_left, min_right = 0, 0  # Track boundaries of minimum window

        # Slide right pointer
        for i, c in enumerate(s):
            if c in need:
                need[c] += 1
                if need[c] == 0:  # Found all occurrences of this character
                    diff -= 1
                    
            # Try to minimize window when valid
            while diff == 0:  # Current window is valid
                if i - left < min_length:  # Found smaller window
                    min_length = i - left
                    min_left = left
                    min_right = i
                    
                # Shrink window from left
                left += 1
                if s[left] in need:
                    need[s[left]] -= 1
                    if need[s[left]] == -1:  # Need this character again
                        diff += 1

        # Return result
        return s[min_left + 1:min_right + 1] if min_length < len(s) + 1 else ""
