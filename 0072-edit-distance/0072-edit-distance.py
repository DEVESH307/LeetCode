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


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         l1, l2 = len(word1), len(word2)
        
#         dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]
        
#         def dfs(i, j):
#             if i == 0:
#                 return j
            
#             if j == 0:
#                 return i
            
#             if dp[i][j] is not None:
#                 return dp[i][j]
            
#             if word1[i-1] == word2[j-1]:
#                 dp[i][j] = dfs(i-1, j-1)
#             else:
#                 insert = dfs(i, j-1)
#                 delete = dfs(i-1, j)
#                 replace = dfs(i-1, j-1)
                
#                 dp[i][j] = 1 + min(insert, delete, replace)
            
#             return dp[i][j]
        
#         return dfs(l1, l2)


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         l1, l2 = len(word1), len(word2)
        
#         dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
#         # base cases
#         for i in range(l1 + 1):
#             dp[i][0] = i   # delete all chars
        
#         for j in range(l2 + 1):
#             dp[0][j] = j   # insert all chars
        
#         # fill table
#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 if word1[i-1] == word2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     insert = dp[i][j-1]
#                     delete = dp[i-1][j]
#                     replace = dp[i-1][j-1]
                    
#                     dp[i][j] = 1 + min(insert, delete, replace)
        
#         return dp[l1][l2]


class Solution:
    def minDistance(self, A, B):
        # always use smaller string for columns (less space)
        if len(A) < len(B):
            A, B = B, A
        
        la, lb = len(A), len(B)
        
        prev = list(range(lb + 1))  # base row
        
        for i in range(1, la + 1):
            curr = [0] * (lb + 1)
            curr[0] = i
            
            for j in range(1, lb + 1):
                if A[i-1] == B[j-1]:
                    curr[j] = prev[j-1]
                else:
                    insert = curr[j-1]
                    delete = prev[j]
                    replace = prev[j-1]
                    
                    curr[j] = 1 + min(insert, delete, replace)
            
            prev = curr
        
        return prev[lb]