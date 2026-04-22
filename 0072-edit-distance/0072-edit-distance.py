# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         l1 = len(word1)
#         l2 = len(word2)

#         def dfs(i, j):
#             if i == 0:
#                 return j

#             if j == 0:
#                 return i

#             if word1[i-1] == word2[j-1]:
#                 return dfs(i-1, j-1)
#             else:
#                 return 1 + min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1))

#         return dfs(l1, l2)        


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]
        
        def dfs(i, j):
            if i == 0:
                return j
            
            if j == 0:
                return i
            
            if dp[i][j] is not None:
                return dp[i][j]
            
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dfs(i-1, j-1)
            else:
                insert = dfs(i, j-1)
                delete = dfs(i-1, j)
                replace = dfs(i-1, j-1)
                
                dp[i][j] = 1 + min(insert, delete, replace)
            
            return dp[i][j]
        
        return dfs(l1, l2)