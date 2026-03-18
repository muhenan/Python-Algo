from typing import List


class Solution:
    """
    LeetCode 59: Spiral Matrix II

    Problem Description:
    给你一个正整数 n，生成一个包含 1 到 n² 所有元素，
    且元素按顺时针螺旋顺序填充的 n x n 正方形矩阵。

    Example 1:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

    Example 2:
    Input: n = 1
    Output: [[1]]
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        value = 1
        while left <= right:
            if left == right:
                ans[left][left] = value
                return ans
            for i in range(left, right):
                ans[left][i] = value
                value += 1
            for i in range(left, right):
                ans[i][right] = value
                value += 1
            for i in range(right, left, -1):
                ans[right][i] = value
                value += 1
            for i in range(right, left, -1):
                ans[i][left] = value
                value += 1
            left += 1
            right -= 1
        return ans

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (3, [[1,2,3],[8,9,4],[7,6,5]]),
        (1, [[1]]),
        (2, [[1,2],[4,3]]),
        (4, [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]),
    ]

    for n, expected in test_cases:
        result = solution.generateMatrix(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] n = {n}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
        print()
