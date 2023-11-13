from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s) # nlogn, sort
        # g.sort()
        i, j, ans = 0, 0, 0 # i = j = count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans