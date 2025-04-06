import collections
import math
from typing import List
import copy


class Solution448:
    # use a 额外数组 which is a bit map
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        bitmap = [False] * (length + 1)
        for val in nums: bitmap[val] = True
        for i in range(1, length + 1):
            if not bitmap[i]: res.append(i)
        return res
    """
    由于 nums 的数字范围均在[1, n][1, n]
    中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。

    具体来说，遍历 nums，每遇到一个数
    x，就让 nums[x−1] 增加
    n。由于 nums 中所有数均在[1, n][1, n]
    中，增加以后，这些数必然大于 n。
    """
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for num in nums:
            x = (num - 1) % length
            nums[x] += length
        res = [i + 1 for i, num in enumerate(nums) if num <= length]
        return res


from collections import deque

# class LRUCache146:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.my_dict = dict()
#         self.que = deque()
#         return None
#
#     def get(self, key: int) -> int:
#         if not key in self.my_dict: return -1
#         self.updataQue(key)
#         return self.my_dict[key]
#
#     def put(self, key: int, value: int) -> None:
#         self.updataQue(key)
#         self.my_dict[key] = value
#         if len(self.my_dict) > self.capacity:
#             self.my_dict.pop(self.que[0])
#             self.que.popleft()
#
#     def updataQue(self, key:int):
#         if self.que and self.que[0] == key:
#             self.que.popleft()
#         if not self.que or self.que and self.que[-1] != key:
#             self.que.append(key)

"""
数组，队列 和 LinkedList 最大的区别在于
队列中的每个元素没有具体的地址
而 LinkedList 中的每个 node 都有具体的地址
"""

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

"""
hashmap (dictionary) + delinkedlist
"""
"""
加 head 和 tail node，避免特殊情况
"""
class LRUCache146:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

"""
Don't use [[v]*n]*n, it is a trap!
"""
class Solution221:
    def maximalSquare(self, matrix: List[List[str]]) -> int: # dp
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0 for i in range(columns)] for j in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: # 避免特殊情况
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide * maxSide


