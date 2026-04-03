"""
LeetCode 122: Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of
the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price=1), sell on day 3 (price=5), profit=4.
                 Then buy on day 4 (price=3), sell on day 5 (price=6), profit=3.
                 Total profit = 4+3 = 7.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1, sell on day 5, profit = 4.

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No profitable transaction.

Constraints:
    1 <= prices.length <= 3 * 10^4
    0 <= prices[i] <= 10^4

Tags:
- Array
- Dynamic Programming
- Greedy
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i-1])
        return ans


# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([2, 1, 2, 0, 1]) == 2

    print("All tests passed!")
