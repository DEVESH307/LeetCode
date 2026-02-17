class Solution:
    def transpose(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    def reverse_rows(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            left = 0
            right = m - 1
            
            while left < right:
                mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
                left += 1
                right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        self.transpose(matrix)
        self.reverse_rows(matrix)

        return matrix