from typing import List

"""
经典 Segment Tree 线段树问题

LeetCode 307: Range Sum Query - Mutable
Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

直接用一个简单数据，update O(1), sumRange O(n)，最终的时间复杂度是 O(qn)
用前缀和，update O(n), sumRange O(1)，最终的时间复杂度是 O(qn)
用线段树，update O(logn), sumRange O(logn)，最终的时间复杂度是 O(qlogn)
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        size = 1
        while size < len(nums):
            size <<= 1
        self.size = size
        self.tree = [0] * (size * 2) # index 1 is the root, index 2 is the left child, index 3 is the right child
        for i in range(len(nums)):
            self.tree[i + size] = nums[i]
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        if index < 0 or index >= self.n:
            return
        index += self.size
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right >= self.n or left > right:
            return 0
        current_sum = 0
        left += self.size
        right += self.size
        while left <= right:
            if left % 2 == 1:
                current_sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                current_sum += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return current_sum

    def print_tree(self):
        print("Printing tree:")
        print("n: ", self.n)
        print("size: ", self.size)
        print("tree: ", self.tree)


nums = [1, 3, 5, 9, 3, 2, 3]
print("nums: ", nums)
numArray = NumArray(nums)
numArray.print_tree()
print("sumRange(0, 2): ", numArray.sumRange(0, 2))
print("sumRange(2, 5): ", numArray.sumRange(2, 5))
print("sumRange(0, 5): ", numArray.sumRange(0, 5))
numArray.update(0, 10)
numArray.print_tree()
