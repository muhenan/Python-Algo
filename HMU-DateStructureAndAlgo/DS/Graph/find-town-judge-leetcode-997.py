from collections import Counter
from typing import List


class TownJudgeFinder:
    """
    LeetCode 997: Find the Town Judge
    
    Problem Description:
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
    
    The town judge must:
    1. Trust nobody
    2. Be trusted by everybody else
    3. There is exactly one person that satisfies properties 1 and 2
    
    Given an array 'trust' where trust[i] = [ai, bi] represents that person ai trusts person bi,
    return the label of the town judge if they exist, otherwise return -1.
    
    Examples:
    - Input: n = 2, trust = [[1,2]]
      Output: 2
    - Input: n = 3, trust = [[1,3],[2,3],[3,1]]
      Output: -1
    """
    
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Solution 1: Using Set and Dictionary
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Strategy:
        - Use a set to track people who trust others (can't be judge)
        - Use a dictionary to track who is trusted by whom
        - Judge must not trust anyone and must be trusted by n-1 others
        """
        if n == 1 and len(trust) == 0:
            return 1
        
        notJudge = set()  # People who trust others (can't be judge)
        my_dict = dict()  # Track who is trusted by whom
        
        # Build trust relationships
        for a, beTrustedB in trust:
            notJudge.add(a)
            if beTrustedB not in my_dict:
                my_dict[beTrustedB] = []
            my_dict[beTrustedB].append(a)
            
        # Check each person
        for i in range(1, n + 1):
            if i not in notJudge and i in my_dict and len(my_dict[i]) == n - 1:
                return i
        return -1

    def findJudge2(self, n: int, trust: List[List[int]]) -> int:
        """
        Solution 2: Using Counter for In-degree and Out-degree
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Strategy:
        - Use two counters to track:
          1. How many people trust each person (in-degree)
          2. How many people each person trusts (out-degree)
        - Judge must have in-degree of n-1 and out-degree of 0
        """
        beTrusted = Counter(y for _, y in trust)    # In-degree
        trustOthers = Counter(x for x, _ in trust)  # Out-degree
        
        for i in range(1, n + 1):
            if beTrusted[i] == n - 1 and trustOthers[i] == 0:
                return i
        return -1

    def findJudge3(self, n: int, trust: List[List[int]]) -> int:
        """
        Solution 3: Single Array Solution (Most Optimized)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Strategy:
        - Use a single array to track trust balance
        - For each person:
          * Trusting others decreases their score (-1)
          * Being trusted increases their score (+1)
        - Judge must have a final score of n-1
          (trusted by everyone else but trusts no one)
        """
        arr = [0] * (n + 1)  # Trust balance for each person
        
        for x, y in trust:
            arr[x] -= 1  # Person x trusts someone (can't be judge)
            arr[y] += 1  # Person y is trusted by someone
            
        for i in range(1, len(arr)):
            if arr[i] == n - 1:  # Found the judge
                return i
        return -1