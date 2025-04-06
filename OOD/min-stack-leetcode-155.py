import math

class MinStack:
    """
    LeetCode 155: Min Stack (最小栈)
    
    实现一个栈，支持push、pop、top操作，并能在常数时间内检索到最小元素。
    
    实现思路：
    - 使用两个栈：一个正常栈(stack)和一个最小值栈(min_stack)
    - min_stack的栈顶始终保存当前stack中的最小值
    - 每次push操作时，同时更新两个栈
    
    时间复杂度：所有操作均为 O(1)
    空间复杂度：O(n)，其中n为栈中元素个数
    """

    def __init__(self):
        """
        初始化两个栈：
        - stack: 存储所有元素
        - min_stack: 存储最小值，初始化为正无穷以处理边界情况
        """
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        """
        将元素压入栈中
        同时更新最小值栈，确保min_stack栈顶为当前最小值
        
        Args:
            val: 要压入的值
        """
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        """
        弹出栈顶元素
        同时也要弹出最小值栈的栈顶，保持两个栈同步
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        返回栈顶元素
        
        Returns:
            栈顶的值
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        获取栈中的最小值
        
        Returns:
            当前栈中的最小值（即min_stack的栈顶）
        """
        return self.min_stack[-1] 