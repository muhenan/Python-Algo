import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        
        # 交换堆顶和末尾，删除末尾
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        
        # 如果堆不为空，下沉新的堆顶
        if self.heap:
            self._sift_down(0)
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def heapify(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_tree(self):
        """按层打印: 利用数组索引规律直接切片"""
        n = len(self.heap)
        if n == 0:
            print("Empty Heap")
            return
            
        index = 0  # 当前层起始下标
        width = 1  # 当前层节点数
        
        while index < n:
            # 切片范围 [index, index + width)
            print(self.heap[index : index + width])
            index += width
            width *= 2

def heap_sort(arr):
    mh = MinHeap()
    for x in arr:
        mh.push(x)
    return [mh.pop() for _ in range(len(arr))]

# --- 测试 ---
mh = MinHeap()
data = [10, 5, 20, 1, 3, 15, 30, 2]
print(f"依次插入: {data}")
for x in data:
    mh.push(x)

print("\n--- 堆的可视化 (Print Tree) ---")
mh.print_tree()

print(f"\nPeek: {mh.peek()}")
print(f"Pop:  {mh.pop()}")
print("\n--- Pop 后的可视化 ---")
mh.print_tree()

print(f"\nPeek: {mh.peek()}")
print(f"Pop:  {mh.pop()}")
print("\n--- Pop 后的可视化 ---")
mh.print_tree()

mh.push(7)
print("\n--- Push 7 后的可视化 ---")
mh.print_tree()

print(f"\nPeek: {mh.peek()}")
print(f"Pop:  {mh.pop()}")
print("\n--- Pop 后的可视化 ---")
mh.print_tree()

print(f"\nPeek: {mh.peek()}")
print(f"Pop:  {mh.pop()}")
print("\n--- Pop 后的可视化 ---")
mh.print_tree()

unsorted = [10, 5, 20, 1, 3, 15, 30, 2]
print("Unsorted: ", unsorted)
print("Sorted: ", heap_sort(unsorted))

random_arr = [random.randint(1, 100) for _ in range(10)]
print("Random Array: ", random_arr)
mh = MinHeap()
mh.heapify(random_arr)
print("Heapified: ", mh.heap)
mh.print_tree()