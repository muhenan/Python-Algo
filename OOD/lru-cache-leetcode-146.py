"""
LeetCode 146: LRU Cache (最近最少使用缓存)
https://leetcode.com/problems/lru-cache/

Problem Description:
设计一个LRU (Least Recently Used) 缓存机制，需要支持以下操作：
- get(key)：获取值，如果key不存在则返回-1
- put(key, value)：插入或更新值，当缓存达到上限时，删除最久未使用的项

要求：get 和 put 操作的时间复杂度必须是 O(1)

实现方式比较：
1. 使用OrderedDict（内置有序字典）
2. 使用双向链表+哈希表（手动实现）
3. 使用队列+字典（不推荐，因为队列中元素没有具体地址）
"""

# 方法一：使用 OrderedDict
class LRUCache(collections.OrderedDict):
    """
    利用Python内置的OrderedDict实现LRU缓存
    OrderedDict能记住键值对的插入顺序
    """
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)  # 移动到末尾表示最近使用
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)  # 删除最早插入的项

# 方法二：双向链表节点
class DLinkedNode:
    """双向链表节点的定义"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache146:
    """
    使用双向链表+哈希表实现LRU缓存
    - 双向链表按照使用顺序存储节点
    - 哈希表存储key到节点的映射
    """
    def __init__(self, capacity: int):
        self.cache = dict()  # 哈希表：key -> node
        # 使用伪头部和伪尾部节点简化边界情况
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        """获取值并将节点移到头部（最近使用）"""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """插入或更新值"""
        if key not in self.cache:
            # 创建新节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 删除最久未使用的节点
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 更新已存在的节点
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        """将节点添加到头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        """删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        """将节点移动到头部"""
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        """删除尾部节点（最久未使用）"""
        node = self.tail.prev
        self.removeNode(node)
        return node 