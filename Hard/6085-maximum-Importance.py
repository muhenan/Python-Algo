from typing import List

nums = [4,1,2,6,5]


for index, value in enumerate(nums, start=1):
    print(index, value)

print(sum(index * value for index, value in enumerate(nums, start=1)))
print(index * value for index, value in enumerate(sorted(nums), start=1))
print([index * value for index, value in enumerate(sorted(nums), start=1)])

"""
gather and scatter
time complexity: O(n)
"""
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.row_seats_left = [m] * n

    def gather(self, k: int, maxRow: int) -> List[int]:
        for i in range(0, maxRow + 1):
            if self.row_seats_left[i] >= k:
                print("Found contiguous seats in row ", i)
                ans = [i, self.m - self.row_seats_left[i]]
                self.row_seats_left[i] -= k
                return ans
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        current_total_seats_left = 0
        for i in range(0, maxRow + 1):
            current_total_seats_left += self.row_seats_left[i]
        if current_total_seats_left < k:
            return False
        for i in range(0, maxRow + 1):
            if self.row_seats_left[i] >= k:
                self.row_seats_left[i] -= k
                break
            else:
                k -= self.row_seats_left[i]
                self.row_seats_left[i] = 0
        return True
    
    def print_seats(self):
        print("Printing seats:")
        print("row_seats_left: ", self.row_seats_left)


# 输入：
# ["BookMyShow", "gather", "gather", "scatter", "scatter"]
# [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
# 输出：
# [null, [0, 0], [], true, false]

b = BookMyShow(2, 5)
b.print_seats()



print(b.gather(4, 0))
b.print_seats()

print(b.gather(2, 0))
b.print_seats()

print(b.scatter(5, 1))
b.print_seats()

print(b.scatter(5, 1))
b.print_seats()


"""
gather and scatter
time complexity: O(logn)
"""
class BookMyShow2:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (2 << n.bit_length())  # 相比 4n 空间更小
        self.sum = [0] * (2 << n.bit_length())

    # 线段树：把下标 i 上的元素值增加 val
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 线段树：返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = self.query_sum(o * 2, l, m, L, R)
        if R > m:
            res += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return res

    # 线段树：返回区间 [0,R] 中 <= val 的最靠左的位置，不存在时返回 -1
    def find_first(self, o: int, l: int, r: int, R: int, val: int) -> int:
        if self.min[o] > val:
            return -1  # 整个区间的元素值都大于 val
        if l == r:
            return l
        m = (l + r) // 2
        if self.min[o * 2] <= val:
            return self.find_first(o * 2, l, m, R, val)
        if R > m:
            return self.find_first(o * 2 + 1, m + 1, r, R, val)
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        # 找第一个能倒入 k 升水的水桶
        r = self.find_first(1, 0, self.n - 1, maxRow, self.m - k)
        if r < 0:  # 没有这样的水桶
            return []
        c = self.query_sum(1, 0, self.n - 1, r, r)
        self.update(1, 0, self.n - 1, r, k)  # 倒水
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        # [0,maxRow] 的接水量之和
        s = self.query_sum(1, 0, self.n - 1, 0, maxRow)
        if s > self.m * (maxRow + 1) - k:
            return False  # 水桶已经装了太多的水
        # 从第一个没有装满的水桶开始
        i = self.find_first(1, 0, self.n - 1, maxRow, self.m - 1)
        while k:
            left = min(self.m - self.query_sum(1, 0, self.n - 1, i, i), k)
            self.update(1, 0, self.n - 1, i, left)  # 倒水
            k -= left
            i += 1
        return True