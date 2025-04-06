from typing import List
import bisect

class Solution:

    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(edges) + 1
        my_map = [[] for _ in range(n)]
        for a, b in edges:
            my_map[a].append(b)
            my_map[b].append(a)
        visited = [False] * n
        def dfs(c):
            if visited[c]:
                return 0, 0
            visited[c] = True
            curr_lay, curr_res = 1 if c in coins else 0, 0
            for i in my_map[c]:
                i_lay, i_res = dfs(i)
                curr_lay = max(curr_lay, i_lay)
                curr_res += i_res
        return 0