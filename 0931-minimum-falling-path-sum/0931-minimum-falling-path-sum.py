# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)

#         def dfs(i, j):
#             if j < 0 or j >= n:
#                 return float('inf')

#             if i == 0:
#                 return matrix[0][j]

#             left = dfs(i - 1, j - 1)
#             up = dfs(i - 1, j)
#             right = dfs(i - 1, j + 1)

#             return matrix[i][j] + min(left, up, right)

#         return min(dfs(n - 1, j) for j in range(n))

    
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         dp = [[None] * n for _ in range(n)]
#         def dfs(i, j):
#             if j < 0 or j >= n:
#                 return float('inf')

#             if i == 0:
#                 return matrix[0][j]

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             left = dfs(i - 1, j - 1)
#             up = dfs(i - 1, j)
#             right = dfs(i - 1, j + 1)

#             dp[i][j] = matrix[i][j] + min(left, up, right)
#             return dp[i][j]

#         return min(dfs(n - 1, j) for j in range(n))\


# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         dp = [[float('inf')] * n for _ in range(n)]
#         # base case
#         dp[0] = matrix[0][:]

#         for i in range(1, n):
#             for j in range(n):    
#                 left = dp[i - 1][j - 1] if j > 0 else float('inf')
#                 up = dp[i - 1][j]
#                 right = dp[i - 1][j + 1] if j < n - 1 else float('inf')

#                 dp[i][j] = matrix[i][j] + min(left, up, right)

#         return min(dp[n-1])
            

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
        
#         for i in range(1, n):
#             for j in range(n):    
#                 left = matrix[i - 1][j - 1] if j > 0 else float('inf')
#                 up = matrix[i - 1][j]
#                 right = matrix[i - 1][j + 1] if j < n - 1 else float('inf')

#                 matrix[i][j] = matrix[i][j] + min(left, up, right)

#         return min(matrix[n-1])
            

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[0][:]   # base case (first row)
        
        for i in range(1, n):
            curr = [0] * n
            for j in range(n):    
                left = prev[j - 1] if j > 0 else float('inf')
                up = prev[j]
                right = prev[j + 1] if j < n - 1 else float('inf')

                curr[j] = matrix[i][j] + min(left, up, right)
            prev = curr

        return min(prev)
