"""
LeetCode 123: Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price=0), sell on day 6 (price=3), profit=3.
                 Then buy on day 7 (price=1), sell on day 8 (price=4), profit=3.
                 Total profit = 6.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1, sell on day 5, profit=4. Only one transaction needed.

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No profitable transaction.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5

Tags:
- Array
- Dynamic Programming
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态机：交易过程只能单向推进
        # 还没买 → 持有第1笔 → 卖出第1笔 → 持有第2笔 → 卖出第2笔
        #
        # buy1  = 截至今天，完成"买入第1笔"后的最大净值，初始 -inf（未买入不是合法状态）
        # sell1 = 截至今天，完成"卖出第1笔"后的最大利润
        # buy2  = 截至今天，完成"买入第2笔"后的最大净值
        # sell2 = 截至今天，完成"卖出第2笔"后的最大利润
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1  = max(buy1,  -p)          # 今天买入第1笔
            sell1 = max(sell1, buy1  + p)   # 今天卖出第1笔
            buy2  = max(buy2,  sell1 - p)   # 今天买入第2笔（用第1笔利润扣掉买价）
            sell2 = max(sell2, buy2  + p)   # 今天卖出第2笔
        return sell2


# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1, 2, 1, 2]) == 2   # two separate transactions, each profit 1
    assert s.maxProfit([0, 3, 0, 5]) == 8   # buy@0 sell@3 + buy@0 sell@5

    print("All tests passed!")
