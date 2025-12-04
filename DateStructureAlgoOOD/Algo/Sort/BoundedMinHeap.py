class BoundedMinHeap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def push(self, val):
        """
        Push (入堆):
        尝试把元素压入堆中。
        如果是 Top K 场景：堆满了且新元素更大时，它会把堆顶挤走。
        """
        # 1. 堆未满：直接加入，上浮
        if len(self.heap) < self.k:
            self.heap.append(val)
            self._sift_up(len(self.heap) - 1)

        # 2. 堆已满：如果新来的比堆顶大，说明新来的更有资格留下来（针对 Top K Largest）
        elif val > self.heap[0]:
            self.heap[0] = val
            self._sift_down(0)

    def pop(self):
        """
        Pop (出堆):
        移除并返回堆顶元素（最小值）。
        """
        if not self.heap:
            return None

        min_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return min_val

    def peek(self):
        """
        Peek (偷看):
        只返回堆顶元素，不删除。
        用于 O(1) 查看当前最小值/门槛值。
        """
        return self.heap[0] if self.heap else None

    # --- 内部核心逻辑保持不变 ---
    def _sift_up(self, idx):
        current = idx
        while current > 0:
            parent = (current - 1) // 2
            if self.heap[current] < self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        current = idx
        while True:
            left = 2 * current + 1
            right = 2 * current + 2
            smallest = current

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != current:
                self.heap[current], self.heap[smallest] = self.heap[smallest], self.heap[current]
                current = smallest
            else:
                break# --- 新增：可视化函数 ---

    def visualize_levels(self):
        """
        利用堆数组本身就是层序遍历的特性，
        直接按层切片打印。
        """
        if not self.heap:
            print("(Empty Heap)")
            return

        n = len(self.heap)
        import math
        # 计算树的总深度，用于控制缩进
        # log2(n) 向下取整
        depth = int(math.log2(n))

        idx = 0
        level = 0

        print("\n--- Heap Level Order ---")
        while idx < n:
            # 当前层应有的节点数: 2^level
            # 位运算 1 << level 等价于 2 ** level，速度更快
            count = 1 << level

            # 这里的切片处理了最后一层节点不满的情况
            # 如果 idx + count 超过 n，切片会自动截止到 n
            current_nodes = self.heap[idx: idx + count]

            # 简单的视觉缩进：层级越浅，左边空格越多，形成金字塔感
            padding = "   " * (depth - level)

            print(f"Lv{level}: {padding}{current_nodes}")

            idx += count
            level += 1
        print("------------------------\n")


# --- 教练演示 ---
# 创建一个容量为 7 的堆，方便看 3 层满二叉树结构
bmh = BoundedMinHeap(7)
data = [10, 5, 20, 3, 8, 15, 30, 2, 7]

print(f"输入数据: {data}")
for num in data:
    bmh.push(num)
    bmh.visualize_levels()

while bmh.peek():
    print(bmh.pop())