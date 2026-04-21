# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])

#         if obstacleGrid[0][0] == 1:
#             return 0

#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return 0

#             if i == 0 and j == 0:
#                 return 1

#             if obstacleGrid[i][j] == 1:
#                 return 0

#             return dfs(i - 1, j) + dfs(i, j - 1)

#         return dfs(m - 1, n - 1)        


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[-1] * n for _ in range(m)]

#         if obstacleGrid[0][0] == 1:
#             return 0

#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return 0

#             if i == 0 and j == 0:
#                 return 1

#             if obstacleGrid[i][j] == 1:
#                 return 0

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             dp[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
#             return dp[i][j]

#         return dfs(m - 1, n - 1)        


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])

#         if obstacleGrid[0][0] == 1:
#             return 0
        
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = 1

#         # first column
#         for i in range(1, m):
#             if obstacleGrid[i][0] == 0:
#                 dp[i][0] = dp[i-1][0]

#         # first row
#         for j in range(1, n):
#             if obstacleGrid[0][j] == 0:
#                 dp[0][j] = dp[0][j-1]

#         for i in range(1, m):
#             for j in range(1, n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

#         return dp[m - 1][n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]