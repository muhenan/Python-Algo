class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        my_dict = dict()
        left = -1
        answer = 0
        for rigth in range(len(s)):
            my_dict[s[rigth]] = 1 + my_dict.get(s[rigth], 0)
            if len(my_dict) <= 2:
                answer = max(answer, rigth - left)
            else:
                while len(my_dict) > 2:
                    left += 1
                    if my_dict[s[left]] != 1:
                        my_dict[s[left]] = my_dict[s[left]] - 1
                    else:
                        del my_dict[s[left]]
        return answer

solu = Solution()
solu.lengthOfLongestSubstringTwoDistinct("sdfghtererresdfff")