class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1: return j + 1
            if j == -1: return i + 1
            memo[(i, j)] = min(
                dp(i - 1, j) + 1,
                dp(i, j - 1) + 1,
                dp(i - 1, j - 1) + 1
            )
            if word1[i] == word2[j]:
                memo[(i, j)] = min(memo[(i, j)], dp(i - 1, j - 1))
            return memo[(i, j)]
        return dp(len(word1) - 1, len(word2) - 1)
    """
    改成 if else 分开会更快
    用 dp 二维数组会更快
    dp 二维数组又可以压缩成一维
    """