from typing import List


class MatrixRotator:
    """
    LeetCode 48: Rotate Image
    
    Problem Description:
    给定一个 n × n 的二维矩阵 matrix 表示一个图像，将图像顺时针旋转 90 度。
    要求：必须在原地旋转图像，不能使用额外的数组空间。
    
    Example:
    Input: matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]
    Output: [[7,4,1],
             [8,5,2],
             [9,6,3]]
             
    解题思路：
    四个位置之间的循环替换，每次旋转四个数
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        原地旋转矩阵90度
        Time: O(n^2), Space: O(1)
        """
        n = len(matrix)
        
        # 只需要遍历四分之一的矩阵
        # i的范围是[0, n//2)，确保不会重复处理行
        # j的范围是[0, (n+1)//2)，确保不会重复处理列
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 四个位置的元素循环替换
                # 对于位置(i,j)，顺时针90度旋转后：
                # (i,j) -> (j,n-1-i) -> (n-1-i,n-1-j) -> (n-1-j,i) -> (i,j)
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
                    matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]


# 测试代码
if __name__ == "__main__":
    solution = MatrixRotator()
    test_cases = [
        [[1,2,3],
         [4,5,6],
         [7,8,9]],
        
        [[5,1,9,11],
         [2,4,8,10],
         [13,3,6,7],
         [15,14,12,16]]
    ]
    
    for matrix in test_cases:
        print("Original matrix:")
        for row in matrix:
            print(row)
        
        solution.rotate(matrix)
        
        print("\nRotated matrix:")
        for row in matrix:
            print(row)
        print() 