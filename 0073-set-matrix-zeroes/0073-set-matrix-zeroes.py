class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row = [1] * n
        col = [1] * m 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[j] = 0
                    col[i] = 0

        for i in range(m):
            for j in range(n):
                if row[j] == 0 or col[i] == 0:
                    matrix[i][j] = 0
