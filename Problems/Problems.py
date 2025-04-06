import collections
import math
from typing import List
import copy



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
