"""
LeetCode 581: Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Problem Description:
给定一个整数数组nums，找出一个最短的连续子数组，如果对这个子数组进行升序排序，
则整个数组都会变为升序排序。返回需要排序的最短子数组的长度。

Examples:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
解释: 需要排序的子数组是 [6,4,8,10,9]，排序后整个数组变为升序
"""

class ShortestUnsortedSubarray:
    def findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        """
        方法一：排序比较法
        Time: O(nlogn) - 主要是排序的时间复杂度
        Space: O(n) - 需要额外的排序数组
        """
        sorted_arr = sorted(nums)
        left, right = -1, -2  # 特殊初始值处理空数组情况
        
        # 从左向右找第一个不同的位置
        for i in range(len(nums)):
            if sorted_arr[i] != nums[i]:
                left = i
                break
                
        # 从左向右找最后一个不同的位置
        for i in range(len(nums)):
            if sorted_arr[i] != nums[i]:
                right = i
                
        return right - left + 1  # 当数组已排序时返回0
    
    def findUnsortedSubarray_twopass(self, nums: List[int]) -> int:
        """
        方法二：两次遍历法
        Time: O(n)
        Space: O(1)
        """
        if len(nums) == 1:
            return 0
            
        # 找左边界
        left = -3  # 特殊初始值
        for i in range(1, len(nums)):
            if left == -1:
                break
            if nums[i] < nums[i - 1]:  # 找到逆序对
                if left == -3:
                    left = i - 1
                # 向左扩展边界
                while left != -1 and nums[left] > nums[i]:
                    left -= 1
                    
        # 找右边界
        right = -2
        for i in reversed(range(len(nums) - 1)):
            if right == len(nums):
                break
            if nums[i] > nums[i + 1]:  # 找到逆序对
                if right == -2:
                    right = i + 1
                # 向右扩展边界
                while right != len(nums) and nums[right] < nums[i]:
                    right += 1
                    
        return right - left - 1
    
    def findUnsortedSubarray_onepass(self, nums: List[int]) -> int:
        """
        方法三：一次遍历法
        这种方法其实最直观
        以找 right 为例：
            从左到右，维护一个 max_value，如果这个 max_value 一直升高，那么不需要排序
            如果碰到一个比 max_value 小的，那么这个就需要排序，也就是最新的 right
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            # 从左向右维护最大值，更新右边界
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            # 从右向左维护最小值，更新左边界
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1 