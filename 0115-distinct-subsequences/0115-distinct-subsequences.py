# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         if len(t) > len(s):
#             return 0

#         l1, l2 = len(s), len(t)

#         def dfs(i, j):
#             if j == 0:
#                 return 1
#             if i == 0:
#                 return 0

#             if s[i-1] != t[j-1]:
#                 return dfs(i-1, j)
#             else:
#                 return dfs(i-1, j-1) + dfs(i-1, j)

#         return dfs(l1, l2)
        
        
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         l1, l2 = len(s), len(t)
        
#         dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]
        
#         def dfs(i, j):
#             if j == 0:
#                 return 1
#             if i == 0:
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if s[i-1] != t[j-1]:
#                 dp[i][j] = dfs(i-1, j)
#             else:
#                 dp[i][j] = dfs(i-1, j-1) + dfs(i-1, j)
            
#             return dp[i][j]
        
#         return dfs(l1, l2)


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         l1, l2 = len(s), len(t)
        
#         dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
#         # base case: empty t
#         for i in range(l1 + 1):
#             dp[i][0] = 1
        
#         # fill table
#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j]
        
#         return dp[l1][l2]


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         l1, l2 = len(s), len(t)
#         if l2 > l1:
#             return 0
        
#         prev = [0] * (l2 + 1)
#         prev[0] = 1   # base case
        
#         for i in range(1, l1 + 1):
#             curr = [0] * (l2 + 1)
#             curr[0] = 1   # empty t
            
#             for j in range(1, l2 + 1):
#                 if s[i-1] == t[j-1]:
#                     curr[j] = prev[j-1] + prev[j]
#                 else:
#                     curr[j] = prev[j]
            
#             prev = curr
        
#         return prev[l2]\


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        
        if l2 > l1:
            return 0
        
        dp = [0] * (l2 + 1)
        dp[0] = 1   # empty t
        
        for i in range(1, l1 + 1):
            # iterate backwards
            for j in range(l2, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
        
        return dp[l2]