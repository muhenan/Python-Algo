class Solution:
    """
        Super Egg Drop
        先写一个 带 memo 的 top-down 的递归动态规划
    """

    def superEggDrop(self, k: int, n: int) -> int:

        memo = {}

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]

            res = float('inf')
            for i in range(1, n + 1):
                res = min(
                    res,
                    max(
                        dp(k, n - i) + 1,
                        dp(k - 1, i - 1) + 1
                    )
                )
            memo[(k, n)] = res
            return memo[(k, n)]

        return dp(k, n)

    ''' 该方法超时，通过 63 / 121 '''

    """
        国内的大佬真的太多了，换了一下状态转移方程，问题直接降维了
        dp[k][m] = n
        dp[3][7] = dp[3][6] + dp[2][6] + 1

        https://leetcode.cn/problems/super-egg-drop/solution/887-by-ikaruga/

        题目的重点在于理解 dp[k][m] 的意义
        描绘的是当前情况下最大的楼层，就是尽量要不碎，不断往上爬，碎了的话，下面的刚好也能算出来

        可以认为，给了 k，m，那么最多能算出多少楼层就是固定的，并且抛的顺序也是固定的

        这个时候再回过头，转念一想，如果 n 是固定的，其实真正不固定的是 f （在哪层碎）
        但是有了固定的 k，m，和顺序，就不管 f 在哪，都能最多完全匹配到 n，又转回来了！
        相当于 n 是问题给的
    """

    def superEggDrop2(self, k: int, n: int) -> int:
        dp, m = {}, 0
        while dp.get((k, m), 0) < n:
            m += 1
            for i_k in range(1, k + 1):
                dp[(i_k, m)] = dp.get((i_k, m - 1), 0) + dp.get((i_k - 1, m - 1), 0) + 1
        return m
