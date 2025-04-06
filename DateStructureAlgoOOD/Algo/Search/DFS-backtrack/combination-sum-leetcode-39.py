import copy
from typing import List


class CombinationSumFinder:
    """
    LeetCode 39: Combination Sum
    
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers 
    sum to target. You may return the combinations in any order.
    
    The same number may be chosen from candidates an unlimited number of times.
    
    Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 + 2 + 3 = 7
    7 = 7
    
    Tags:
    - Array
    - Backtracking
    - DFS
    - Recursion
    
    Time Complexity: O(N^(T/M)) where:
    - N is length of candidates array
    - T is target value
    - M is minimal value in candidates
    Space Complexity: O(T/M) for recursion depth
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        First approach: Create new lists in recursion
        
        Strategy:
            - Use DFS to try different combinations
            - For each number, we can use it multiple times
            - Pass current sum and list to track progress
            - Create new list for each recursive call
        """
        answer = []
        
        def dfs(curr_sum: int, curr_list: List[int], start_idx: int):
            if curr_sum > target:
                return
            if curr_sum == target:
                answer.append(curr_list)  # Found valid combination
            else:
                # Try each candidate from start_idx
                for i in range(start_idx, len(candidates)):
                    # Create new list for next recursion
                    """
                    这里用了数组相加的操作
                    非常不高效，是一个不提倡，不可取的操作
                    这里的主要意思是展示DFS的思维
                    Backtrack的写法，只用一个数组，在树上，往前走了又回来，是高效的，空间优化了
                    """
                    dfs(curr_sum + candidates[i], 
                        curr_list + [candidates[i]], 
                        i)  # Keep same i to allow reuse
                        
        # Try each number as starting point
        for i in range(len(candidates)):
            dfs(candidates[i], [candidates[i]], i)
            
        return answer
        
    def combinationSumBacktrack(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Second approach: Backtracking with list modification
        
        Strategy:
            - Use backtracking pattern (add/remove elements)
            - Avoid creating new lists by modifying existing one
            - Need deep copy when adding to answer
            - More space efficient but slightly more complex
        """
        answer = []
        
        def dfs(curr_sum: int, curr_list: List[int], start_idx: int):
            if curr_sum + candidates[start_idx] > target:
                return
            if curr_sum + candidates[start_idx] == target:
                # Need deep copy since we modify curr_list
                one_answer = curr_list.copy()
                one_answer.append(candidates[start_idx])
                answer.append(one_answer)
            else:
                # Add current number
                curr_list.append(candidates[start_idx])
                # Try all possible next numbers
                for i in range(start_idx, len(candidates)):
                    dfs(curr_sum + candidates[start_idx], curr_list, i)
                # Backtrack by removing current number
                curr_list.pop()
                
        # Try each number as starting point
        for i in range(len(candidates)):
            dfs(0, [], i)
            
        return answer