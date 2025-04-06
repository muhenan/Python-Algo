import collections
import math
from typing import List
import copy

class UniqueBST:
    """
    LeetCode 96: Unique Binary Search Trees
    
    Problem Description:
    给定一个整数n，求恰由n个节点组成且节点值从1到n互不相同的
    二叉搜索树有多少种？
    
    Example:
    Input: n = 3
    Output: 5
    
    动态规划解法：
    dp[i] 表示i个节点能形成的不同BST的数量
    对于每个i，考虑每个数字作为根节点的情况
    """
    def numTrees(self, n: int) -> int:
        """
        方法一：动态规划（带初始值）
        Time: O(n^2), Space: O(n)
        """
        # dp[i]表示i个节点的BST数量
        dp = [1, 1] + [0] * (n - 1)  # 初始化0和1个节点的情况
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # 左子树节点个数：j-1
                # 右子树节点个数：i-j
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
    
    def numTrees_compact(self, n: int) -> int:
        """
        方法二：更简洁的动态规划
        Time: O(n^2), Space: O(n)
        """
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


"""
LeetCode 221: Maximal Square
https://leetcode.com/problems/maximal-square/

Problem Description:
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

Example:
Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 4
解释：最大的正方形是2×2的，位于右下角部分。

注意事项：
不要使用 [[v]*n]*n 来初始化二维数组！这会导致所有行引用同一个列表。
正确的初始化方式是：[[v for i in range(n)] for j in range(n)]
"""

class MaximalSquare:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        动态规划解法
        dp[i][j] 表示以(i,j)为右下角的最大正方形边长
        
        状态转移方程：
        if matrix[i][j] == '1':
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        Time: O(m*n), m和n是矩阵的行数和列数
        Space: O(m*n)
        """
        if not matrix or not matrix[0]:
            return 0
            
        max_side = 0
        rows, cols = len(matrix), len(matrix[0])
        
        # 创建dp数组，注意正确的初始化方式
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # 遍历矩阵的每个位置
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # 边界情况：第一行或第一列
                        dp[i][j] = 1
                    else:
                        # 状态转移：取左边、上边、左上三个位置的最小值加1
                        dp[i][j] = min(
                            dp[i-1][j],     # 上边
                            dp[i][j-1],     # 左边
                            dp[i-1][j-1]    # 左上
                        ) + 1
                    # 更新最大边长
                    max_side = max(max_side, dp[i][j])
        
        # 返回最大正方形的面积
        return max_side * max_side


def test_maximal_square():
    """测试最大正方形的解法"""
    solution = MaximalSquare()
    
    # 测试用例
    test_cases = [
        ([
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ], 4),
        ([
            ["0","1"],
            ["1","0"]
        ], 1),
        ([["0"]], 0),
        ([["1"]], 1),
    ]
    
    for matrix, expected in test_cases:
        result = solution.maximalSquare(matrix)
        assert result == expected, f"Failed: {matrix}"
        print(f"Test case passed: result = {result}")
