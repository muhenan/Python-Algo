"""
LeetCode 188: Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day,
and an integer k. Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price=2), sell on day 2 (price=4), profit=2.

Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price=2), sell on day 3 (price=6), profit=4.
                 Then buy on day 5 (price=0), sell on day 6 (price=3), profit=3.
                 Total profit = 7.

Constraints:
    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000

Tags:
- Array
- Dynamic Programming

Hint: 123 的状态机推广，把固定的 buy1/sell1/buy2/sell2 换成长度为 k 的数组。
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        pass


# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit(2, [2, 4, 1]) == 2
    assert s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert s.maxProfit(2, [7, 6, 4, 3, 1]) == 0
    assert s.maxProfit(1, [1, 2]) == 1
    assert s.maxProfit(3, [1, 2, 3, 4, 5]) == 4    # k 足够大时等同于无限次
    assert s.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]) == 6

    print("All tests passed!")
