# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         m = len(matrix[0])

#         row = [1]*n
#         col = [1]*m

#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     row[i] = 0
#                     col[j] = 0
        
#         for i in range(n):
#             for j in range(m):
#                 if row[i] == 0 or col[j] == 0:
#                     matrix[i][j] = 0

#         return matrix
        

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        row_flag = 0
        col_flag = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = 1
                    if j == 0:
                        col_flag = 1

                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_flag == 1:
            for i in range(m):
                matrix[0][i] = 0
        
        if col_flag == 1:
            for i in range(n):
                matrix[i][0] = 0

        return matrix