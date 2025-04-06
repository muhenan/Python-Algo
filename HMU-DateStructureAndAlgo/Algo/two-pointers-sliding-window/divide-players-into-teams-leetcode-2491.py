from typing import List

class TeamDivider:
    """
    LeetCode 2491: Divide Players Into Teams of Equal Skill (Weekly Contest 322)
    
    Given an array of player skills, divide players into teams of size 2 such that:
    - All teams have equal total skill
    - Each player is in exactly one team
    Return the sum of chemistry values (product of team members' skills) if possible, -1 if impossible
    
    Example:
    Input: skill = [3,2,5,1,3,4]
    Output: 22
    Explanation: Teams: (3,3), (2,4), (5,1), Total chemistry = 9 + 8 + 5 = 22
    
    Tags:
    - Array
    - Two Pointers
    - Sorting
    - Greedy
    
    Time Complexity: O(nlogn) due to sorting
    Space Complexity: O(1) excluding input array
    """
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Divide players into teams with equal total skill
        
        Args:
            skill: List of player skill levels
            
        Returns:
            int: Sum of team chemistry values, or -1 if impossible
            
        Strategy:
            - Sort array to match highest with lowest skills
            - Check if all pairs sum to same value
            - Calculate chemistry (product) for valid pairs
        """
        skill.sort()  # Sort skills in ascending order
        target_sum = skill[0] + skill[-1]  # Sum that all teams should have
        chemistry = skill[0] * skill[-1]  # First team's chemistry
        
        n = len(skill)
        # Check each pair from both ends
        for i in range(1, n//2):
            curr_sum = skill[i] + skill[n - i - 1]
            if curr_sum != target_sum:
                return -1  # Cannot form equal skill teams
            chemistry += skill[i] * skill[n - i - 1]
            
        return chemistry
