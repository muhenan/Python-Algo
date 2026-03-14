class Solution:
    """
        Two Eggs Drop
        如果上来第一个就碎了，那就很简单了，后一个直接线性扫描即可
        问题是如果第一个没碎，之后要怎么操作
        为了简单，我用三个数组
        dp 表示在 i 处抛第一个，最少抛多少次找到答案
                dp[i] = max(dp_break[i], dp_fine[i])
                the final answer is min(dp)
        dp_break 表示在 i 处抛第一个，并且碎了，最少抛多少次找到答案，dp_break[3] = 1 + (3 - 1) = 3
                dp_break[i] = i
        dp_fine 表示在 i 处抛第一个，并且没碎，最少抛多少次找到答案

    """

    def twoEggDrop(self, n: int) -> int:
        memo = [float('inf')] * (n + 1)

        def dp(n):
            if n == 0: return 0
            if memo[n] != float('inf'): return memo[n]
            for i in range(1, n + 1):
                memo[n] = min(
                    memo[n],
                    max(
                        i,
                        dp(n - i) + 1
                    )
                )
            return memo[n]

        return dp(n)

    def twoEggDrop2(self, n: int) -> int:  # 自底向上
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):  # 对于 i 层，最多需要多少次
            for j in range(1, i + 1):  # 第一个从 j 开始扔
                dp[i] = min(dp[i], max(j, dp[i - j] + 1))  # 如果碎了，直接返回 j 因为只剩下一个鸡蛋线性扫描，如果没碎，那就和几个鸡蛋没关系
        return dp[-1]

    """
     tc n2
     sc n
     dp 计算中，计算当前 dp 总是用到之前 dp 已经算出的结果，这就是自顶向上
    """
