# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         l1, l2 = len(s), len(t)
        
#         dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
#         return dp[l1][l2] == l1


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)        