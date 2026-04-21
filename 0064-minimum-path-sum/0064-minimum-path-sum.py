# class Solution:
#     # 1️⃣ Pure Recursion (Brute Force) — WILL TLE
#     def minPathSum_recursion(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])

#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return float('inf')

#             if i == 0 and j == 0:
#                 return grid[0][0]
            
#             return grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))

#         return dfs(m - 1, n - 1)


# class Solution:
#     # 2️⃣ Top-Down DP (Memoization)
#     def minPathSum_memo(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[-1] * n for _ in range(m)]

#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return float('inf')

#             if i == 0 and j == 0:
#                 dp[0][0] = grid[0][0]
#                 return dp[0][0]
            
#             if dp[i][j] != -1:
#                 return dp[i][j]

#             dp[i][j] = grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
#             return dp[i][j]

#         return dfs(m - 1, n - 1)


# class Solution:
#     # 3️⃣ Bottom-Up DP (Full Matrix)
#     def minPathSum_tabulation(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[0]*n for _ in range(m)]

#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     dp[i][j] = grid[i][j]
#                 elif i == 0:
#                     dp[i][j] = grid[i][j] + dp[i][j-1]
#                 elif j == 0:
#                     dp[i][j] = grid[i][j] + dp[i-1][j]
#                 else:
#                     dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

#         return dp[-1][-1]


class Solution:
    # 4️⃣ Space Optimized (O(n)) — BEST
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = grid[i][j] + dp[j - 1]
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        
        return dp[-1]