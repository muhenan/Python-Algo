from typing import List


class Solution:
    """
    LeetCode 39: Combination Sum

    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen
    numbers sum to target. The same number may be chosen unlimited times.

    Example:
    Input: candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]

    Tags:
    - Array
    - Backtracking
    - DFS
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking solution with one mutable path.

        Example:
        Input: candidates = [2, 3, 6, 7], target = 7
        Output: [[2, 2, 3], [7]]

        Tags:
        - Backtracking
        - DFS

        Time Complexity: Exponential in the number of valid search states
        Space Complexity: O(target / min(candidates)) for recursion depth and path
        """
        answer: List[List[int]] = []
        path: List[int] = []

        def dfs(start_idx: int, curr_sum: int) -> None:
            if curr_sum == target:
                answer.append(path.copy())
                return
            if curr_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                path.append(candidates[i])
                dfs(i, curr_sum + candidates[i])
                path.pop()

        dfs(0, 0)
        return answer


if __name__ == "__main__":
    solu = Solution()
    assert sorted(solu.combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]])
    assert sorted(solu.combinationSum([2, 3, 5], 8)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    print("All tests passed!")
