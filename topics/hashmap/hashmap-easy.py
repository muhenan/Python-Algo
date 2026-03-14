import collections
import math
from typing import List
import copy


class DeckGrouper:
    """
    LeetCode 914: X of a Kind in a Deck of Cards
    
    Problem Description:
    给定一副牌，每张牌上都写着一个整数。
    判断是否可以把这副牌分成若干组，使得：
    1. 每组都有X张牌，X >= 2
    2. 同一组中的所有牌上的数字都相同
    
    Example:
    Input: [1,2,3,4,4,3,2,1]
    Output: true
    Explanation: 可以分成 4 组，每组 2 张牌
    """
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 统计每个数字出现的次数
        count = collections.Counter(deck)
        N = len(deck)
        
        # 尝试所有可能的组大小X
        for X in range(2, N + 1):
            # 如果总牌数能被X整除
            if N % X == 0:
                # 检查每个数字的出现次数是否都能被X整除
                if all(v % X == 0 for v in count.values()):
                    return True
        return False

class DistinctAveragesFinder:
    """
    LeetCode 2465: Number of Distinct Averages
    
    Problem Description:
    给定一个偶数长度的整数数组nums。每次操作：
    1. 选择数组中的最小值和最大值
    2. 计算它们的平均值
    3. 从数组中删除这两个数
    返回所有可能的不同平均值的数量。
    
    Example:
    Input: nums = [4,1,4,0,3,5]
    Output: 2
    Explanation: 
    1. 删除0和5，平均值2.5
    2. 删除1和4，平均值2.5
    3. 删除3和4，平均值3.5
    共有2个不同的平均值：2.5和3.5
    """
    def distinctAverages(self, nums: List[int]) -> int:
        # 先排序，这样最小值和最大值总是在两端
        nums.sort()
        n = len(nums)
        # 使用集合存储不同的平均值
        averages = set()
        
        # 每次取最左和最右的数计算平均值
        for i in range(n // 2):
            avg = (nums[i] + nums[n - i - 1]) / 2
            averages.add(avg)
            
        return len(averages)

class GroupAnagrams:
    """
    LeetCode 49: Group Anagrams
    
    Problem Description:
    给定一个字符串数组，将所有字母异位词组合在一起。
    字母异位词指字母相同，但排列不同的字符串。
    
    Example:
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        """
        方法一：排序法
        Time: O(nklogk), n是字符串数量，k是最长字符串长度
        Space: O(nk)
        """
        my_map = collections.defaultdict(list)
        for s in strs:
            # 将排序后的字符串作为key
            key = "".join(sorted(s))
            my_map[key].append(s)
        return list(my_map.values())
    
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        方法二：计数法
        Time: O(nk), n是字符串数量，k是最长字符串长度
        Space: O(nk)
        """
        my_map = collections.defaultdict(list)
        for s in strs:
            # 统计每个字符出现的次数
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            # 使用计数元组作为key
            my_map[tuple(counts)].append(s)
        return list(my_map.values())