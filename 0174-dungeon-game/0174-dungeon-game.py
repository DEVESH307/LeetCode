# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])

#         def dfs(i, j):
#             if i >= m or j >= n:
#                 return float('inf')

#             # base case (start cell)
#             if i == m - 1 and j == n - 1:
#                 return max(1, 1 - dungeon[i][j])

#             need = min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j]

#             return max(1, need)

#         return dfs(0, 0)


# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
#         dp = [[None] * n for _ in range(m)]

#         def dfs(i, j):
#             if i >= m or j >= n:
#                 return float('inf')

#             # base case (start cell)
#             if i == m - 1 and j == n - 1:
#                 return max(1, 1 - dungeon[i][j])

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             need = min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j]

#             dp[i][j] = max(1, need)
#             return dp[i][j]

#         return dfs(0, 0)


# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
#         dp = [[0] * n for _ in range(m)]

#         # base case (princess cell)
#         dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

#         # fill last row
#         for j in range(n-2, -1, -1):
#             need = dp[m-1][j+1] - dungeon[m-1][j]
#             dp[m-1][j] = max(1, need)

#         # fill last col
#         for i in range(m-2, -1, -1):
#             need = dp[i+1][n-1] - dungeon[i][n-1]
#             dp[i][n-1] = max(1, need)

#         # fill rest
#         for i in range(m - 2, -1, -1):
#             for j in range(n - 2, -1, -1):
#                 need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
#                 dp[i][j] = max(1, need)

#         return dp[0][0]


# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
        
#         dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
#         # trick: set boundary
#         dp[m][n-1] = dp[m-1][n] = 1
        
#         for i in range(m-1, -1, -1):
#             for j in range(n-1, -1, -1):
#                 need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
#                 dp[i][j] = max(1, need)
        
#         return dp[0][0]
   

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [float('inf')] * (n + 1)
        dp[n-1] = 1   # base setup
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[j], dp[j+1]) - dungeon[i][j]
                dp[j] = max(1, need)
        
        return dp[0]