# dp[target] -> result
# dp[target - 2]
import copy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(currentSum, currentList, index):
            if currentSum > target:
                return
            if currentSum == target: # get an answer
                answer.append(currentList)
            else:
                for i in range(index, len(candidates)): # 做其他选择
                    dfs(currentSum + candidates[i], currentList + [candidates[i]], i)
        for i in range(len(candidates)):
            dfs(candidates[i], [candidates[i]], i)
        return answer

# 一个更好看的写法，带 pop，即带撤销操作的，不每次都开新数组

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(currentSum, currentList, index):
            if currentSum + candidates[index] > target:
                return
            if currentSum + candidates[index] == target: # get an answer
                oneAnswer = copy.deepcopy(currentList)
                oneAnswer.append(candidates[index])
                answer.append(oneAnswer)
            else:
                currentList.append(candidates[index]) # 做其他选择
                for i in range(index, len(candidates)):
                    dfs(currentSum + candidates[index], currentList, i)
                currentList.pop()
        for i in range(len(candidates)):
            dfs(0, [], i)
        return answer