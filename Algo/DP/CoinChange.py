from typing import List


class Solution:
    answer = float('inf')
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        def dfs(index, current_amount, num_coins):
            if current_amount == 0:
                self.answer = min(self.answer, num_coins)
            elif current_amount > 0:
                for i in range(index, len(coins)):
                    current_num_coins = num_coins + 1
                    dfs(i, current_amount - coins[i], current_num_coins)
        for i in range(len(coins)):
            dfs(i, amount - coins[i], 1)
        return self.answer if self.answer != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(len(dp)):
                if i < coin:
                    continue
                elif i == coin:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    print("here")
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                else:
                    lastLength = dp[i - 1]
                    if i - lastLength - 1 >= 0 and s[i - lastLength - 1] == '(':
                        dp[i] = 2 + lastLength + (dp[i - lastLength - 2] if i - lastLength - 2 >= 0 else 0)
                answer = max(answer, dp[i])
        return answer



solu = Solution()
solu.coinChange([],0)

solu.longestValidParentheses(")(((((()())()()))()(()))(")

# class Solution {
#     public int longestValidParentheses(String s) {
#         int maxans = 0;
#         int[] dp = new int[s.length()];
#         for (int i = 1; i < s.length(); i++) {
#             if (s.charAt(i) == ')') {
#                 if (s.charAt(i - 1) == '(') {
#                     dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
#                 } else if (i - dp[i - 1] > 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
#                     dp[i] = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
#                 }
#                 maxans = Math.max(maxans, dp[i]);
#             }
#         }
#         return maxans;
#     }
# }