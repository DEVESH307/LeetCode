class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diag_sum = 0

        for i in range(n):
            diag_sum += mat[i][i]
            diag_sum += mat[i][n-i-1]

        if n % 2 == 1:
            diag_sum -= mat[n//2][n//2]

        return diag_sum