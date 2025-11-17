from typing import List


class Solution:
    """
    LeetCode 322: Coin Change

    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins,
    return -1.

    You may assume that you have an infinite number of each kind of coin.

    Example:
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Tags:
    - Dynamic Programming
    - Greedy

    Approaches in this class:
    - coinChange: DFS / backtracking search (exponential, for practice)
    - coinChange2: 1D DP with time complexity O(N * amount)
      and space complexity O(amount), where N is the number of coin types.
    """

    answer = float('inf')

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DFS / backtracking solution.

        Time Complexity:
            Exponential in the worst case, since we explore many combinations.
        Space Complexity:
            O(amount / min(coins)) for recursion depth.
        """
        if amount == 0:
            return 0

        # Reset answer for each call to avoid interference between multiple runs
        self.answer = float('inf')

        def dfs(index: int, current_amount: int, num_coins: int) -> None:
            if current_amount == 0:
                self.answer = min(self.answer, num_coins)
            elif current_amount > 0:
                for i in range(index, len(coins)):
                    current_num_coins = num_coins + 1
                    dfs(i, current_amount - coins[i], current_num_coins)

        for i in range(len(coins)):
            dfs(i, amount - coins[i], 1)

        return self.answer if self.answer != float("inf") else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        Classic 1D DP solution:

        dp[x] = minimum number of coins needed to make up amount x.

        Time Complexity: O(N * amount)
        Space Complexity: O(amount)
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.coinChange2([1, 2, 5], 11))


