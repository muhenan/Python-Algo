"""
单调栈基础 (Monotonic Stack Basics)

单调栈是一种特殊的栈，其中的元素保持单调递增或单调递减的顺序。
主要用于解决 "下一个更大/小元素" 或 "前一个更大/小元素" 类型的问题。

特点：
1. 时间复杂度通常是 O(n)：每个元素最多入栈出栈各一次
2. 空间复杂度通常是 O(n)：最坏情况下栈需要存储所有元素
3. 常用于解决数组中元素之间的关系问题
"""

class MonotonicStack:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        """
        找出数组中每个元素的下一个更大元素
        使用单调递减栈（从栈底到栈顶递减）
        
        Example:
        Input: [2,1,2,4,3]
        Output: [4,2,4,-1,-1]
        """
        n = len(nums)
        result = [-1] * n  # 默认值为-1，表示没有更大的元素
        stack = []  # 存储索引
        
        for i in range(n):
            # 当前元素大于栈顶元素时，栈顶元素找到了下一个更大元素
            while stack and nums[i] > nums[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = nums[i]
            stack.append(i)
            
        return result
    
    def prevSmallerElement(self, nums: List[int]) -> List[int]:
        """
        找出数组中每个元素的前一个更小元素
        使用单调递增栈（从栈底到栈顶递增）
        
        Example:
        Input: [2,1,2,4,3]
        Output: [-1,-1,1,2,2]
        """
        n = len(nums)
        result = [-1] * n  # 默认值为-1，表示没有更小的元素
        stack = []  # 存储索引
        
        for i in range(n):
            # 保持栈内元素单调递增
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = nums[stack[-1]]
            stack.append(i)
            
        return result
    
    def nextSmallerElement(self, nums: List[int]) -> List[int]:
        """
        找出数组中每个元素的下一个更小元素
        使用单调递增栈
        
        Example:
        Input: [2,1,2,4,3]
        Output: [1,−1,1,3,-1]
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = nums[i]
            stack.append(i)
            
        return result
    
    def prevGreaterElement(self, nums: List[int]) -> List[int]:
        """
        找出数组中每个元素的前一个更大元素
        使用单调递减栈
        
        Example:
        Input: [2,1,2,4,3]
        Output: [-1,2,2,-1,4]
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = nums[stack[-1]]
            stack.append(i)
            
        return result

def test_monotonic_stack():
    """测试单调栈的各种基本操作"""
    solution = MonotonicStack()
    nums = [2,1,2,4,3]
    
    # 测试所有四种基本操作
    print("原始数组:", nums)
    print("下一个更大元素:", solution.nextGreaterElement(nums))
    print("前一个更小元素:", solution.prevSmallerElement(nums))
    print("下一个更小元素:", solution.nextSmallerElement(nums))
    print("前一个更大元素:", solution.prevGreaterElement(nums))

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


"""
LeetCode 739: Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Problem Description:
给定一个整数数组 temperatures，表示每天的温度，返回一个数组 answer，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

解释：
第 0 天温度是 73，第 1 天温度是 74，比 73 高，所以等待 1 天
第 1 天温度是 74，第 2 天温度是 75，比 74 高，所以等待 1 天
第 2 天温度是 75，需要等到第 6 天（76）才会有更高温度，所以等待 4 天
以此类推...
"""

class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        单调栈解法
        Time: O(n) - 每个元素最多入栈出栈各一次
        Space: O(n) - 栈的空间
        """
        length = len(temperatures)
        result = [0] * length  # 初始化结果数组，默认为0
        stack = []  # 单调递减栈，存储温度的索引
        
        # 从左向右遍历温度数组
        for curr_day in range(length):
            # 当前温度大于栈顶温度时，可以更新栈顶温度的等待天数
            while stack and temperatures[curr_day] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day  # 计算等待天数
            
            # 将当前温度的索引入栈
            stack.append(curr_day)
            
        return result

    def dailyTemperatures_bruteforce(self, temperatures: List[int]) -> List[int]:
        """
        暴力解法（超时）
        Time: O(n^2)
        Space: O(1)
        """
        length = len(temperatures)
        result = [0] * length
        
        for i in range(length):
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                    
        return result


def test_daily_temperatures():
    """测试每日温度的解法"""
    solution = DailyTemperatures()
    
    # 测试用例
    test_cases = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
        ([90,80,70,60], [0,0,0,0])
    ]
    
    for temperatures, expected in test_cases:
        result = solution.dailyTemperatures(temperatures)
        assert result == expected, f"Failed: {temperatures}"
        print(f"Test case passed: {temperatures} -> {result}")
