from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        badNumbers = [4,8,9,12,16,18,20,24,25,27,28]
        nums = sorted(nums)

        return 0
    def findTheString(self, lcp: List[List[int]]) -> str:
        length = len(lcp)
        string = ["a"] * length
        newchar = chr(ord('a') - 1)
        for i in range(len(lcp)):
            finished = False
            for j in range(i - 1, -1, -1):
                if lcp[i][j] != 0:
                    string[i] = string[i - (i - j)]
                    finished = True
                    break
            if not finished:
                newchar = chr(ord(newchar) + 1)
                if ord(newchar) > ord('z'): return ""
                string[i] = newchar
        n = len(lcp)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                v = f[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                if string[i] == string[j]:
                    f[i][j] = v + 1
        if f == lcp:
            return ''.join(string)
        else:
            return ''

    # def findTheString(self, lcp: List[List[int]]) -> str:
    #     n = len(lcp)
    #     for i in range(n):
    #         if lcp[i][i] != n - i:
    #             return ''
    #     s = [''] * n
    #     p = 'a'
    #     for i in range(n):
    #         if not s[i]:
    #             if p > 'z':
    #                 return ''
    #             s[i] = p
    #             p = chr(ord(p) + 1)
    #         for j in range(i + 1, n):
    #             if lcp[i][j]:
    #                 s[j] = s[i]
    #
    #     f = [[0] * n for _ in range(n)]
    #     for i in range(n - 1, -1, -1):
    #         for j in range(n - 1, -1, -1):
    #             v = f[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
    #             if s[i] == s[j]:
    #                 f[i][j] = v + 1
    #
    #     if f == lcp:
    #         return ''.join(s)
    #     else:
    #         return ''

solu = Solution()

print(solu.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))
