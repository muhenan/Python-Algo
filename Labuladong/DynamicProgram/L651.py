class Solution:
    """
    3 operations
        A
        Ctrl A and Ctrl C
        Ctrl V
    """

    def maxA(self, n: int) -> int:
        memo = {}

        def dp(current, n, copy):
            if n <= 0: return current
            if (current, n, copy) in memo:
                return memo[(current, n, copy)]
            memo[(current, n, copy)] = max(
                dp(current + 1, n - 1, copy),
                dp(current, n - 2, current),
                dp(current + copy, n - 1, copy)
            )
            return memo[(current, n, copy)]

        return dp(0, n, 0)

    ''' N 3 超时超内存，被带跑了！'''

    """
    二维数组，元素的值代表已经生成了多少 A
    """

    def maxA2(self, n: int) -> int:
        dp = [0] * (n + 1) # 表示是次 dp[i] 次结束时，最多的 A，从结束条件，减少情况；最后操作要么 A，要么粘贴
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(2, i): # j 表示 复制的那个点
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1)) # 加一是因为最开始还有一个
        return dp[-1]
