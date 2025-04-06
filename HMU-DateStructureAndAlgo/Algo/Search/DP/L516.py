class Solution:
    """
    按照不同的长度 dp
    外 for 长度
        内 for 起点
    时间复杂度 n2
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        for i in range(len(s)):
            dp[(i, i)] = 1
        for i in range(len(s) - 1):
            dp[(i, i + 1)] = 2 if s[i] == s[i + 1] else 1
        for offset in range(2, len(s)):
            for l in range(len(s)):
                if l + offset < len(s):
                    r = l + offset
                    dp[(l, r)] = max(dp[(l + 1, r)], dp[(l, r - 1)])
                    if s[l] == s[r]:
                        dp[(l, r)] = max(dp[(l, r)], dp[(l + 1, r - 1)] + 2)
        return dp[(0, len(s) - 1)]

    def longestPalindromeSubseq2(self, s: str) -> int:
        dp = {}
        for r in range(len(s)):
            dp[(r, r)] = 1
            for l in range(r - 1, -1, -1):
                dp[(l, r)] = max(dp[(l + 1, r)], dp[(l, r - 1)])
                if s[l] == s[r]:
                    dp[(l, r)] = max(dp[(l, r)], dp.get((l + 1, r - 1), 0) + 2)

        return dp[(0, len(s) - 1)]

    def longestPalindromeSubseq2(self, s: str) -> int:
        dp = {}
        for r in range(len(s)):
            dp[(r, r)] = 1
            for l in range(r - 1, -1, -1):
                dp[(l, r)] = max(dp[(l + 1, r)], dp[(l, r - 1)])
                if s[l] == s[r]:
                    dp[(l, r)] = max(dp[(l, r)], dp.get((l + 1, r - 1), 0) + 2)

        return dp[(0, len(s) - 1)]

    def longestPalindromeSubseq3(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for r in range(n):
            dp[r][r] = 1
            for l in range(r - 1, -1, -1):
                dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
                if s[l] == s[r]:
                    dp[l][r] = max(dp[l][r], dp[l + 1][r - 1] + 2)

        return dp[0][n - 1]
    """
    还有直接 dfs 的方法，自顶向下，也是一种思路简单，可以解决问题的办法
    还可以状态压缩，变成一维数组
    """

    """
    思路应该也差不多，但是自顶向下复杂度还是太高了，超时
    """
    def longestPalindromeSubseq4(self, s: str) -> int:
        dp = {}
        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1
            dp[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            if s[l] == s[r]:
                dp[(l, r)] = max(dp[(l, r)], dfs(l + 1, r - 1) + 2)
            return dp[(l, r)]
        return dfs(0, len(s) - 1)

    """
    状态压缩
    要压缩状态，就不能通过长度来推，因为那样的话，没法用一个变量就保存上次的内容
    必须要按范围推
    """
    def longestPalindromeSubseq_1d(self, s: str) -> int:
        dp = [1] * len(s)
        for left in range(len(s) - 2, -1, -1):
            prev = 0 # prev 表示上一次 left 和上一次 right 生成的值
            for right in range(left + 1, len(s)):
                temp = dp[right] # 这里记录的 dp[right] 是上一任 left 和 上一任 right 产生的
                if s[left] == s[right]:
                    dp[right] = prev + 2 # 在这，对于这个 prev 来说，left 和 right 都是新的
                else:
                    dp[right] = max(dp[right], dp[right - 1])
                prev = temp
        return dp[-1]
    # 外 for 控制 left 左移，内部的 for 控制 right 从 left + 1 向右移动，移动到最后，最后的是最终结果

solu = Solution()
solu.longestPalindromeSubseq_1d("bbbab")