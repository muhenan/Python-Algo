from typing import List


class Solution:
    """
    LeetCode 54: Spiral Matrix

    Problem Description:
    给你一个 m x n 的矩阵 matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while left <= right or top <= bottom:
            if top == bottom:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                return res
            if left == right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][left])
                return res
            # extend + generator expression: 无额外空间，惰性求值，每次只产出一个元素直接塞进 res
            # 对比 extend([... for ...])：有方括号会先建临时 list，多用 O(k) 空间
            # 对比 append 循环：空间一样，但 extend 底层走 C 内存拷贝，常数更小
            res.extend(matrix[top][i]        for i in range(left,  right))
            res.extend(matrix[i][right]       for i in range(top,   bottom))
            res.extend(matrix[bottom][i]      for i in range(right, left, -1))
            res.extend(matrix[i][left]        for i in range(bottom, top, -1))
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
        ([[1]], [1]),
        ([[1,2],[3,4]], [1,2,4,3]),
    ]

    for matrix, expected in test_cases:
        result = solution.spiralOrder(matrix)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: {matrix}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        print()
