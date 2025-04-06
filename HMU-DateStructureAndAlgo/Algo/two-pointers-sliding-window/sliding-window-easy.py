import collections
import math
from typing import List
import copy


class FindAnagrams:
    """
    LeetCode 438: Find All Anagrams in a String
    
    Problem Description:
    给定两个字符串s和p，找到s中所有p的字母异位词的起始索引。
    字母异位词指字母相同，但排列不同的字符串。
    
    Example:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    解释：
    - "cba" 是 "abc" 的字母异位词，从索引 0 开始
    - "bac" 是 "abc" 的字母异位词，从索引 6 开始
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        滑动窗口 + 字符计数解法
        Time: O(n), n为字符串s的长度
        Space: O(1), 因为只使用固定大小的数组(26个字母)
        """
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
            
        ans = []
        # 使用数组记录字符出现次数（26个小写字母）
        s_count = [0] * 26
        p_count = [0] * 26
        
        # 初始化第一个窗口
        for i in range(len_p):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(p[i]) - ord("a")] += 1
            
        # 检查第一个窗口是否是字母异位词
        if s_count == p_count:
            ans.append(0)
            
        # 滑动窗口，每次移动一位
        for i in range(len_s - len_p):
            # 移除窗口最左边的字符
            s_count[ord(s[i]) - ord("a")] -= 1
            # 添加窗口右边新的字符
            s_count[ord(s[i + len_p]) - ord("a")] += 1
            # 比较当前窗口是否形成字母异位词
            if s_count == p_count:
                ans.append(i + 1)
                
        return ans

