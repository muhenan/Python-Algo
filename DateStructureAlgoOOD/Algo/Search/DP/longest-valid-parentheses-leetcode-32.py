class LongestValidParenthesesSolver:
    """
    LeetCode 32: Longest Valid Parentheses

    Given a string containing just the characters '(' and ')', return the
    length of the longest valid (well-formed) parentheses substring.

    Example:
    Input: s = "(()"
    Output: 2
    Explanation:
    The longest valid parentheses substring is "()".

    Tags:
    - String
    - Dynamic Programming
    - Stack

    Time Complexity: O(N) where N is the length of the string.
    Space Complexity: O(N) for the DP array.
    """

    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case "...()"
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                else:
                    # Case "...))" — try to connect with a previous valid substring
                    last_length = dp[i - 1]
                    if (
                        i - last_length - 1 >= 0
                        and s[i - last_length - 1] == '('
                    ):
                        dp[i] = (
                            2
                            + last_length
                            + (
                                dp[i - last_length - 2]
                                if i - last_length - 2 >= 0
                                else 0
                            )
                        )
                answer = max(answer, dp[i])

        return answer


