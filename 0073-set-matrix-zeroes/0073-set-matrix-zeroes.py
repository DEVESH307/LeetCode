# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m, n = len(matrix), len(matrix[0])
#         row = [1] * n
#         col = [1] * m 

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row[j] = 0
#                     col[i] = 0

#         for i in range(m):
#             for j in range(n):
#                 if row[j] == 0 or col[i] == 0:
#                     matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_flag = 0
        col_flag = 0 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = 1
                    if j == 0:
                        col_flag = 1

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_flag == 1:
            for col in range(n):
                matrix[0][col] = 0

        if col_flag == 1:
            for row in range(m):
                matrix[row][0] = 0
