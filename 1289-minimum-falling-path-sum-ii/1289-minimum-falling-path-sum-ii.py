# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)

#         def dfs(i, j):
#             if j < 0 or j >= n:
#                 return float('inf')

#             if i == 0:
#                 return grid[0][j]

#             res = float('inf')
#             for k in range(n):
#                 if k != j:
#                     res = min(res, dfs(i - 1, k))

#             return grid[i][j] + res

#         return min(dfs(n - 1, j) for j in range(n))        


# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         dp = [[None] * n for _ in range(n)]

#         def dfs(i, j):
#             if j < 0 or j >= n:
#                 return float('inf')

#             if i == 0:
#                 return grid[0][j]

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             res = float('inf')
#             for k in range(n):
#                 if k != j:
#                     res = min(res, dfs(i - 1, k))

#             dp[i][j] = grid[i][j] + res
#             return dp[i][j]

#         return min(dfs(n - 1, j) for j in range(n))


# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         dp = [[0] * n for _ in range(n)]
#         # base case
#         dp[0] = grid[0][:]

#         for i in range(1, n):
#             for j in range(n):
#                 res = float('inf')
#                 for k in range(n):
#                     if k != j:
#                         res = min(res, dp[i - 1][k])

#                 dp[i][j] = grid[i][j] + res

#         return min(dp[n - 1])


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        # base case
        prev = grid[0][:]

        for i in range(1, n):
            curr = [0] * n
            for j in range(n):
                res = float('inf')
                for k in range(n):
                    if k != j:
                        res = min(res, prev[k])

                curr[j] = grid[i][j] + res
            prev = curr

        return min(prev)