# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         l1 = len(text1)
#         l2 = len(text2)

#         def dfs(i, j):
#             if i == 0 or j == 0:
#                 return 0

#             if text1[i-1] == text2[j-1]:
#                 return 1 + dfs(i-1, j-1)
#             else:
#                 return max(dfs(i-1, j), dfs(i, j-1))

#         return dfs(l1, l2)


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         l1 = len(text1)
#         l2 = len(text2)
#         dp =  [[None] * (l2+1) for _ in range(l1+1)]

#         def dfs(i, j):
#             if i == 0 or j == 0:
#                 return 0
            
#             if dp[i][j] is not None:
#                 return dp[i][j]

#             if text1[i-1] == text2[j-1]:
#                 dp[i][j] =  1 + dfs(i-1, j-1)
#             else:
#                 dp[i][j] = max(dfs(i-1, j), dfs(i, j-1))

#             return dp[i][j]

#         return dfs(l1, l2)


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         l1 = len(text1)
#         l2 = len(text2)
#         dp =  [[0] * (l2+1) for _ in range(l1+1)]

#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] =  1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#         return dp[l1][l2]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        
        prev = [0] * (l2 + 1)
        
        for i in range(1, l1 + 1):
            curr = [0] * (l2 + 1)
            
            for j in range(1, l2 + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            
            prev = curr
        
        return prev[l2]