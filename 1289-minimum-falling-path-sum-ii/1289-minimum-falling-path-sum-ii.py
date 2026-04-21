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


# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         dp = [[0] * n for _ in range(n)]
#         # base case
#         prev = grid[0][:]

#         for i in range(1, n):
#             curr = [0] * n
#             for j in range(n):
#                 res = float('inf')
#                 for k in range(n):
#                     if k != j:
#                         res = min(res, prev[k])

#                 curr[j] = grid[i][j] + res
#             prev = curr

#         return min(prev)


# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
        
#         prev = grid[0][:]
        
#         for i in range(1, n):
#             prefix = [0] * n
#             suffix = [0] * n
            
#             # build prefix
#             prefix[0] = prev[0]
#             for j in range(1, n):
#                 prefix[j] = min(prefix[j-1], prev[j])
            
#             # build suffix
#             suffix[n-1] = prev[n-1]
#             for j in range(n-2, -1, -1):
#                 suffix[j] = min(suffix[j+1], prev[j])
            
#             curr = [0] * n
            
#             for j in range(n):
#                 left = prefix[j-1] if j > 0 else float('inf')
#                 right = suffix[j+1] if j < n-1 else float('inf')
                
#                 curr[j] = grid[i][j] + min(left, right)
            
#             prev = curr
        
#         return min(prev)


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        prev = grid[0][:]
        
        for i in range(1, n):
            # find min1, min2, idx1
            min1 = min2 = float('inf')
            idx1 = -1
            
            for j in range(n):
                if prev[j] < min1:
                    min2 = min1
                    min1 = prev[j]
                    idx1 = j
                elif prev[j] < min2:
                    min2 = prev[j]
            
            curr = [0] * n
            
            for j in range(n):
                if j == idx1:
                    curr[j] = grid[i][j] + min2
                else:
                    curr[j] = grid[i][j] + min1
            
            prev = curr
        
        return min(prev)