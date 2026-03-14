from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        ans = []
        for char in word:
            mod *= 10
            num = int(char)
            mod = (mod + num) % m
            if mod == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans
