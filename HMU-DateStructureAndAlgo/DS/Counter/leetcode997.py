from collections import Counter
from typing import List


class Solution:
    """
    Set -> not Judge
    record its be trusted times
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        notJudge = set()
        my_dict = dict()
        for a, beTrustedB in trust:
            notJudge.add(a)
            if beTrustedB not in my_dict:
                my_dict[beTrustedB] = []
            my_dict[beTrustedB].append(a)
        for i in range(1, n + 1):
            if i not in notJudge and i in my_dict and len(my_dict[i]) == n - 1:
                return i
        return -1

    """
    一个图的出度入度问题
    """
    def findJudge2(self, n: int, trust: List[List[int]]) -> int:
        beTrusted = Counter(y for _, y in trust)
        trustOthers = Counter(x for x, _ in trust)
        for i in range(1, n + 1):
            if beTrusted[i] == n - 1 and trustOthers[i] == 0: return i
        return -1

    """
    直接一个数组解决问题
    """
    def findJudge3(self, n: int, trust: List[List[int]]) -> int:
        arr = [0] * (n + 1)
        for x, y in trust:
            arr[x] -= 1
            arr[y] += 1
        for i in range(1, len(arr)):
            if arr[i] == n - 1: return i
        return -1