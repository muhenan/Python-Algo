"""
LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously.

Example 1:
    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: Buy@1, sell@8 (profit=5), buy@4, sell@9 (profit=3). Total = 8.

Example 2:
    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6

Constraints:
    1 <= prices.length <= 5 * 10^4
    1 <= prices[i] <= 10^4
    0 <= fee <= 10^4

Tags:
- Array
- Dynamic Programming
- Greedy
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -10**9, 0
        for p in prices:
            buy  = max(buy,  sell - p)
            sell = max(sell, buy + p - fee)
        return sell


# Tests
if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert s.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    assert s.maxProfit([1, 2, 3], 3) == 0
    assert s.maxProfit([1], 0) == 0
    assert s.maxProfit([2, 1, 4], 1) == 2

    print("All tests passed!")
