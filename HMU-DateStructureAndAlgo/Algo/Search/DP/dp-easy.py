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