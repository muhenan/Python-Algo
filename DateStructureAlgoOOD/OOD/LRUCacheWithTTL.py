import time


class Node:
    def __init__(self, key=0, value=0, expire_time=None):
        self.key = key
        self.value = value
        self.expire_time = expire_time
        self.prev = None
        self.next = None


class LRUCacheWithTTL:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # 哨兵节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _is_expired(self, node: Node) -> bool:
        return (node.expire_time is not None) and (time.time() > node.expire_time)
    
    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_tail(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        # 检查是否过期
        if self._is_expired(node):
            self._remove(node)
            del self.cache[key]
            return -1
        
        # 移到末尾（最近使用）
        self._remove(node)
        self._add_to_tail(node)
        return node.value
    
    def put(self, key: int, value: int, ttl: int = None):
        expire_time = (time.time() + ttl) if (ttl is not None) else None
        
        if key in self.cache:
            # key 已存在，更新值和过期时间
            node = self.cache[key]
            self._remove(node)
            node.value = value
            node.expire_time = expire_time
            self._add_to_tail(node)
        else:
            # 新建节点
            node = Node(key, value, expire_time)
            self.cache[key] = node
            self._add_to_tail(node)
            
            # 超出容量，删除最久未使用的
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]


# 测试
if __name__ == "__main__":
    cache = LRUCacheWithTTL(2)
    
    # 测试基本 LRU
    cache.put(1, 100)
    cache.put(2, 200)
    print(cache.get(1))  # 100
    
    cache.put(3, 300)    # 淘汰 key=2
    print(cache.get(2))  # -1
    
    # 测试 TTL
    cache.put(4, 400, ttl=1)  # 1秒后过期
    print(cache.get(4))  # 400
    
    time.sleep(1.1)
    print(cache.get(4))  # -1 (已过期)