# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#         ans = 0

#         # 1-based prefix sum matrix
#         psm = [[0]*(m+1) for _ in range(n+1)]

#         # build prefix sum
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 psm[i][j] = psm[i-1][j] + psm[i][j-1] - psm[i-1][j-1] + matrix[i-1][j-1]

#         # iterate all submatrices and look for target
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 # TL(i, j)
#                 for p in range(i, n+1):
#                     for q in range(j, m+1):
#                         # BR(p, q)
#                         submatrix_sum = psm[p][q] - psm[i-1][q] - psm[p][j-1] + psm[i-1][j-1]

#                         if submatrix_sum == target:
#                             ans += 1

#         return ans



class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0

        for top in range(n):
            col_sum = [0] * m
            for bottom in range(top, n):
                # compress rows into 1D array
                for c in range(m):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                count = {0: 1}

                for val in col_sum:
                    prefix += val

                    # if prefix - target in count:
                    #     ans += count[prefix - target]

                    # if prefix in count:
                    #     count[prefix] += 1
                    # else:
                    #     count[prefix] = 1

                    ans += count.get(prefix - target, 0)
                    count[prefix] = count.get(prefix, 0) + 1

        return ans