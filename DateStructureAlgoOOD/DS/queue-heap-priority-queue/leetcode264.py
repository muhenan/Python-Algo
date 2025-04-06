import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def getUN(a, b, c):
            return pow(2,a) * pow(3,b) * pow(5,c)

        q = []
        for i in range(33): q.append((getUN(i, 0, 0), (i, 0, 0))) # 重点在于这里，2 的初始值给的足够大
        heapq.heapify(q)

        ans = []
        while len(ans) < n:
            number, (a, b, c) = heapq.heappop(q)
            ans.append(number)
            heapq.heappush(q, (getUN(a, b + 1, c), (a, b + 1, c))) # 这里要没有重复，通过画树的方式作出 / 其实可以用一个 set 做，就不用考虑这么多了
            if b == 0:
                heapq.heappush(q, (getUN(a, b, c + 1), (a, b, c + 1)))

        return ans[-1]

    '''
    暴力放入最小堆，通过一个集合去重即可
    '''
    def nthUglyNumber2(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

    ''' DP '''
    ''' 有重复利用，用 DP '''
    def nthUglyNumber3(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1 # p5，下一次乘 5 的时候从哪个数开始乘

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


solu = Solution()

solu.nthUglyNumber(140)
solu.nthUglyNumber2(140)