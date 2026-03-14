import collections
import math
from typing import List
import copy


class ZigzagConverter:
    """
    LeetCode 6: Zigzag Conversion
    
    Problem Description:
    将字符串按照Z字形排列成给定的行数，然后按行读取得到新的字符串。
    
    Example:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    排列如下：
    P   A   H   N
    A P L S I I G
    Y   I   R
    
    解题思路：
    使用flag控制方向，在0和numRows-1处改变方向
    """
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情况处理：行数小于2时直接返回
        if numRows < 2:
            return s
            
        # 创建numRows个字符串数组，每个存储一行的字符
        res = ["" for _ in range(numRows)]
        # i表示当前行号，flag表示移动方向（1向下，-1向上）
        i, flag = 0, -1
        
        # 遍历每个字符
        for c in s:
            # 将字符添加到对应行
            res[i] += c
            # 在首行或末行时改变方向
            if i == 0 or i == numRows - 1:
                flag = -flag
            # 更新行号
            i += flag
            
        # 合并所有行
        return "".join(res)


