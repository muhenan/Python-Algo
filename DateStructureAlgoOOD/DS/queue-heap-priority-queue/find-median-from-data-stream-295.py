import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = [] # 最大堆，存储前半部分 -3,-2,-1
        self.min_heap = [] # 最小堆，存储后半部分 4,5,6

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
            return
        if num > self.min_heap[0]:
            if len(self.min_heap) > len(self.max_heap):
                to_move = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -to_move)
            heapq.heappush(self.min_heap, num)
        else:
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -num)
            else:
                peek_first_half = -self.max_heap[0]
                if num > peek_first_half:
                    heapq.heappush(self.min_heap, num)
                else:
                    to_move = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.max_heap, -num)
                    heapq.heappush(self.min_heap, to_move)
        return

    def findMedian(self) -> float:
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else (self.min_heap[0] - self.max_heap[0]) / 2


m = MedianFinder()
m.addNum(1)
m.addNum(2)
m.addNum(8)
m.addNum(7)
m.addNum(4)

print(m.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()