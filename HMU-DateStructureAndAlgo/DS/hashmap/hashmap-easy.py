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