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
        
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        
        dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]
        
        def dfs(i, j):
            if j == 0:
                return 1
            if i == 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i-1] != t[j-1]:
                dp[i][j] = dfs(i-1, j)
            else:
                dp[i][j] = dfs(i-1, j-1) + dfs(i-1, j)
            
            return dp[i][j]
        
        return dfs(l1, l2)