class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dp(i, j):
            lengthOfS, lengthOfP = len(s), len(p)

            # base case
            if j == lengthOfP: return i == lengthOfS
            if i == lengthOfS: return isMatchEmpty(j)

            # memo
            if (i, j) in memo: return memo[(i, j)]

            # match
            res = False
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < lengthOfP and p[j + 1] == '*':
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    res = dp(i + 1, j + 1)
            else:
                if j + 1 < lengthOfP and p[j + 1] == '*':
                    res = dp(i, j + 2)
                else:
                    res = False
            memo[(i, j)] = res
            return memo[(i, j)]

        def isMatchEmpty(j):
            if (len(p) - j) % 2 == 1:
                return False
            while j + 1 < len(p):
                if p[j + 1] != '*':
                    return False
                j += 2
            return True

        return dp(0, 0)