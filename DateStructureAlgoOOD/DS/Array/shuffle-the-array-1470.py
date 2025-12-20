from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y_arr = nums[n:]
        for i in range(n - 1, -1, -1):
            nums[i * 2] = nums[i]
        for i in range(len(y_arr)):
            nums[i * 2 + 1] = y_arr[i]
        return nums
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)
        for i in range(n):
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[n + i]
        return ans
    """
    二进制解法：
    因为1 <= nums[i] <= 1000, 所以10 bits are enough (2^10 = 1024).
    每次都会 10 bit 来存这里的最终结果，10 bit 存原本的值
    """
    def shuffle3(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i * 2] |= (nums[i] & 1023) << 10
            nums[i * 2 + 1] |= (nums[i + n] & 1023) << 10
        for i in range(len(nums)):
            nums[i] = nums[i] >> 10
        return nums

solu = Solution()
print(solu.shuffle3([1,2,3,4,5,6], 3))