class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def dp(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left >= right or left >= len(s) or right < 0:
                return 0
            if s[left] == s[right]:
                memo[(left, right)] = dp(left + 1, right - 1)
            else:
                memo[(left, right)] = 1 + min(dp(left, right - 1), dp(left + 1, right))
            return memo[(left, right)]
        return dp(0, len(s) - 1)