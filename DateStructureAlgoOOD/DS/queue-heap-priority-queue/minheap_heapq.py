import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def to_list(self):
        return self.heap

myHeap = MinHeap()
myHeap.push(6)
myHeap.push(2)
myHeap.push(5)
myHeap.push(3)
print(myHeap.to_list())
print(myHeap.peek())
print(myHeap.pop())
print(myHeap.to_list())
print(myHeap.peek())
print(myHeap.pop())
print(myHeap.to_list())
print(myHeap.peek())
print(myHeap.pop())