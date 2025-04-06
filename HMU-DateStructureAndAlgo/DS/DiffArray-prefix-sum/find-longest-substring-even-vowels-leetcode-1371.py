class EvenVowelSubstringFinder:
    """
    LeetCode 1371: Find the Longest Substring Containing Even Counts of Vowels
    
    Problem Description:
    给定字符串 s，找到最长的子串，使得所有元音字母在子串中都出现偶数次。
    
    Examples:
    - Input: s = "eleetminicoworoep" -> Output: 13
    - Input: s = "leetcodeisgreat" -> Output: 5
    - Input: s = "bcbcbc" -> Output: 6
    """
    def findTheLongestSubstring(self, s: str) -> int:
        # 定义元音字母映射，直接对应到位置
        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        # 初始化状态字典，空状态(0)的位置为-1
        seen = {0: -1}
        
        # max_length: 记录最长子串长度
        # current_state: 使用二进制位记录当前元音出现次数的奇偶性
        max_length = current_state = 0
        
        for i in range(len(s)):
            # 如果当前字符是元音，更新状态
            if s[i] in vowels:
                # 使用位运算更新状态：
                # 1. vowels[s[i]] 直接获取元音位置(0-4)
                # 2. 1 << pos 创建对应位置的掩码
                # 3. current_state ^= mask 翻转对应位置的奇偶性
                current_state ^= 1 << vowels[s[i]]
            
            # 如果是新状态，记录它第一次出现的位置
            if current_state not in seen:
                seen[current_state] = i
            else:
                # 如果状态重复，说明中间的子串所有元音都是偶数次
                # 更新最大长度
                max_length = max(max_length, i - seen[current_state])
        
        return max_length 