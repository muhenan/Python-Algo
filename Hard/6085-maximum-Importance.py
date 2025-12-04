from typing import List

nums = [4,1,2,6,5]


for index, value in enumerate(nums, start=1):
    print(index, value)

print(sum(index * value for index, value in enumerate(nums, start=1)))
print(index * value for index, value in enumerate(sorted(nums), start=1))
print([index * value for index, value in enumerate(sorted(nums), start=1)])


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