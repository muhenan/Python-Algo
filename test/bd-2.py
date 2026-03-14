# encoding: utf-8
# a = input("please input a number:")
print("hello world")
# -+++-
# -+-+-
class Solution:
    def my_function(self, matrix):
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        print(str(rows) + " " + str(cols))
        bitmap = [[False] * cols for _ in range(rows)]
        ans = 0
        def dfs(start_row, start_col, rows_count, cols_counts):
            if start_row == rows_count or start_col == cols_counts or start_col < 0 or start_row < 0:
                return
            if matrix[start_row][start_col] == '+' and bitmap[start_row][start_col] == False:
                bitmap[start_row][start_col] = True
                dfs(start_row + 1, start_col, rows_count, cols_counts)
                dfs(start_row, start_col + 1, rows_count, cols_counts)
                dfs(start_row - 1, start_col, rows_count, cols_counts)
                dfs(start_row, start_col - 1, rows_count, cols_counts)
        for r in range(0, rows):
            for c in range(0, cols):
                if matrix[r][c] == '+' and bitmap[r][c] == False:
                    print("found start point " + str(r) + " " + str(c))
                    ans += 1
                    dfs(r, c, rows, cols)
        return ans

solu = Solution()
print(solu.my_function(["---++---", "++-++---", "-------+"]))