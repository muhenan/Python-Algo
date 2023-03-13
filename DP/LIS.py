from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bf n2
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for index2 in range(1, len(text2) + 1):
            for index1 in range(1, len(text1) + 1):
                if text1[index1 - 1] == text2[index2 - 1]:
                    dp[index2][index1] = 1 + dp[index2 - 1][index1 - 1]
                else:
                    dp[index2][index1] = max(dp[index2 - 1][index1], dp[index2][index1 - 1])
        # for row in dp:
        #     print(row)
        return dp[-1][-1]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return False

solu = Solution()
solu.lengthOfLIS2([0,1,0,3,2,3])


solu.longestCommonSubsequence("abcde", "ace")


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n=len(s)
#         dp=[False]*(n+1)
#         dp[0]=True
#         for i in range(n):
#             for j in range(i+1,n+1):
#                 if(dp[i] and (s[i:j] in wordDict)):
#                     dp[j]=True
#         return dp[-1]