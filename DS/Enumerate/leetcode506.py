from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        titles = ["Gold Medal","Silver Medal","Bronze Medal"]
        ans = [""] * len(score)
        arr = sorted(list(enumerate(score)), key= lambda x : x[1], reverse=True)
        for i, (index, element) in enumerate(arr):
            ans[index] = titles[i] if i < 3 else str(i + 1)
        return ans