from typing import List


class AssignCookiesSolver:
    """
    LeetCode 455: Assign Cookies
    
    Assume you are an awesome parent and want to give your children some cookies. 
    But, you should give each child at most one cookie.
    
    Each child i has a greed factor g[i], which is the minimum size of a cookie 
    that the child will be content with; and each cookie j has a size s[j]. 
    If s[j] >= g[i], we can assign the cookie j to the child i, and the child i 
    will be content.
    
    Return the maximum number of your content children.
    
    Example:
    Input: g = [1,2,3], s = [1,1]
    Output: 1 (You have 3 children and 2 cookies. The greed factors are 1,2,3. 
    You can only make the child whose greed factor is 1 content.)
    
    Tags:
    - Array
    - Two Pointers
    - Greedy
    - Sorting
    
    Time Complexity: O(nlogn) due to sorting
    Space Complexity: O(n) due to Python's Timsort implementation
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Greedy approach with sorting and two pointers
        
        Args:
            g: List of children's greed factors
            s: List of cookie sizes
            
        Returns:
            int: Maximum number of content children
            
        Strategy:
            - Sort both arrays to match smallest cookies with least greedy children
            - Use two pointers to track current child and cookie
            - Move to next cookie if current one is too small
            - Move to next child and cookie if current cookie satisfies child
            
        Time Complexity: O(nlogn) due to sorting
        Space Complexity: O(n) due to Python's Timsort implementation, which:
            - Uses temporary arrays for merging in Timsort
            - Requires O(n) auxiliary space even for in-place sort()
        """
        # Sort both arrays in-place, but still uses O(n) space due to Timsort
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes
        
        child_ptr = cookie_ptr = content_children = 0
        
        # Use two pointers to match cookies with children
        while child_ptr < len(g) and cookie_ptr < len(s):
            if g[child_ptr] <= s[cookie_ptr]:  # Current cookie satisfies current child
                content_children += 1
                child_ptr += 1
                cookie_ptr += 1
            else:  # Current cookie too small, try next cookie
                cookie_ptr += 1
                
        return content_children