import random
from typing import List
from itertools import accumulate
from bisect import bisect_left


"""
LeetCode 528: Random Pick with Weight

思路：
1. 使用前缀和数组，pre[i] = pre[i-1] + w[i]，得到的前缀和数组一定是递增的
    random.randint(1, self.pre[-1]) 会生成一个1到self.pre[-1]之间的随机整数
    这个随机数落在哪个区间，就返回哪个索引
2. 使用二分查找，找到第一个大于等于target的索引
3. 返回索引
"""

class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(1, self.pre[-1])
        return bisect_left(self.pre, target)


"""
操作系统中的彩票调度算法
"""

solu = Solution([1,3])
while True:
    print(solu.pickIndex())