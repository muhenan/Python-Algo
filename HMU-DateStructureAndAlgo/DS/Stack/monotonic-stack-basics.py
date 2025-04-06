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

if __name__ == "__main__":
    test_monotonic_stack() 