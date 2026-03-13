class Solution:
    """
    LeetCode 159: Longest Substring with At Most Two Distinct Characters
    
    Problem Description:
    给定一个字符串s，找出最长的子串，该子串最多包含两个不同的字符。
    
    Examples:
    - Input: "eceba"
      Output: 3
      Explanation: 子串 "ece" 包含两个不同的字符 'e' 和 'c'
    
    - Input: "ccaabbb"
      Output: 5
      Explanation: 子串 "aabbb" 包含两个不同的字符 'a' 和 'b'
    
    解题思路：
    使用滑动窗口 + 哈希表，统计窗口内字符出现次数
    """
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time: O(n), Space: O(1)，因为哈希表最多存储3个字符
        """
        # 哈希表记录窗口内每个字符的出现次数
        my_dict = dict()
        # left指向窗口左边界的前一个位置（方便计算长度）
        left = -1
        # 记录最长子串长度
        answer = 0
        
        # right指针遍历字符串
        for right in range(len(s)):
            # 更新当前字符的计数
            my_dict[s[right]] = 1 + my_dict.get(s[right], 0)
            
            # 如果窗口内不同字符数量不超过2，更新最大长度
            if len(my_dict) <= 2:
                answer = max(answer, right - left)
            # 如果不同字符数量超过2，需要收缩窗口
            else:
                # 不断移动左指针，直到窗口内只有2种字符
                while len(my_dict) > 2:
                    left += 1
                    # 减少左指针指向字符的计数
                    if my_dict[s[left]] > 1:
                        my_dict[s[left]] -= 1
                    else:
                        # 如果字符计数为1，直接从哈希表中删除
                        del my_dict[s[left]]
                        
        return answer


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "eceba",           # 应该返回 3
        "ccaabbb",         # 应该返回 5
        "aac",             # 应该返回 3
        "sdfghtererresdfff"  # 测试更长的输入
    ]
    
    for s in test_cases:
        result = solution.lengthOfLongestSubstringTwoDistinct(s)
        print(f"String: {s}")
        print(f"Longest substring length: {result}")
        print() 