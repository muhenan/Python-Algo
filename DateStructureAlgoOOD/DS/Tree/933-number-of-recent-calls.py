from collections import defaultdict

class RecentCounter:

    def __init__(self):
        self.arr = []
        self.index = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.index < len(self.arr):
            if self.arr[self.index] < t - 3000:
                self.index += 1
            else:
                break
        return len(self.arr) - self.index

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


from collections import deque

class RecentCounter3:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

class BIT:
    def __init__(self, n: int):
        self.size = n
        self.tree = defaultdict(int)

    @staticmethod
    def _lowbit(index: int) -> int:
        return index & -index

    def add(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += self._lowbit(index)

    def query(self, index: int) -> int:
        if index > self.size:
            index = self.size
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self._lowbit(index)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)

class RecentCounter2:
    def __init__(self):
        self.bit = BIT(int(1e9 + 10))

    def ping(self, t: int) -> int:
        self.bit.add(t, 1)
        return self.bit.sumRange(t - 3000, t)


r = RecentCounter()

arr = []
arr.append(r.ping(10))
arr.append(r.ping(1000))
arr.append(r.ping(2000))
arr.append(r.ping(5000))
arr.append(r.ping(7000))
arr.append(r.ping(10000))

print("Hello")