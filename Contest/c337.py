from typing import List


class Solution:
    def __init__(self):
        self.gAns = False

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        directions = [[-2, -1], [2, -1], [-2, 1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

        def dfs(row, col, next_des):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
                return
            if grid[row][col] != next_des:
                return
            if next_des == len(grid) * len(grid) - 1:
                self.gAns = True
            for d in directions:
                dfs(row + d[0], col + d[1], next_des + 1)
        dfs(0,0,0)
        return self.gAns

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        my_set = set()
        self.count = 0

        def dfs(index, kk):
            val1, val2 = nums[index] - kk, nums[index] + kk
            if val1 in my_set or val2 in my_set:
                return
            self.count += 1
            my_set.add(nums[index])
            for i in range(index + 1, len(nums)):
                dfs(i, kk)
            if nums[index] in my_set:
                my_set.remove(nums[index])

        for i in range(len(nums)):
            dfs(i, k)
        return self.count
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        my_set = [False] * len(nums)
        for n in range(len(nums)):
            ok = False
            for i in range(len(nums)):
                if not my_set[i] and (n - nums[i]) % value == 0:
                    my_set[i] = True
                    ok = True
                    break
            if not ok:
                return n
        return len(nums)
    def findSmallestInteger1(self, nums: List[int], value: int) -> int:
        my_set = [False] * (len(nums) * 2)
        for i in range(len(nums)):
            while nums[i] < 0:
                nums[i] += value
            while nums[i] >= value:
                nums[i] -= value
            while nums[i] < len(nums) and my_set[nums[i]]:
                nums[i] += value
            my_set[nums[i]] = True
        print(my_set)
        for i in range(len(my_set)):
            if not my_set[i]:
                return i
        return 0

solu = Solution()
#print(solu.beautifulSubsets([2,4,6], 2))


print(solu.findSmallestInteger1([4,1,0,1,1,1,1,3,2,3,1,2,4], 5))