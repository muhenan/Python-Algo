"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like
with the following restriction:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously.

Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: Buy@1, sell@2, cooldown, buy@0, sell@2. Profit = 1+2 = 3.

Example 2:
    Input: prices = [1]
    Output: 0

Constraints:
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

Tags:
- Array
- Dynamic Programming

Hint: 和 122/714 的 2 变量状态机一样，但 buy 转移时不能用上一天的 sell，要用前天的 sell。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, sell_prev = -10**9, 0, 0
        for i in range(len(prices)):
            buy = max(buy, sell_prev - prices[i])
            sell_prev = sell
            sell = max(sell, buy + prices[i])
        return sell

# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([1, 2, 3, 0, 2]) == 3
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([2, 1]) == 0
    assert s.maxProfit([6, 1, 3, 2, 4, 7]) == 6

    print("All tests passed!")
