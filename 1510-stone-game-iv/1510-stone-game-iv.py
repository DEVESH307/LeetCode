# from functools import cache
# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:

#         @cache
#         def dfs(i):
#             if i == 0:
#                 return False

#             j = 1
#             while j * j <= i:
#                 if not dfs(i - j * j):
#                     return True
#                 j += 1

#             return False
     
#         return dfs(n)
        

# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#         dp = [-1] * (n + 1)

#         def dfs(i):
#             if i == 0:
#                 return False

#             if dp[i] != -1:
#                 return dp[i]

#             j = 1
#             while j * j <= i:
#                 if not dfs(i - j * j):
#                     dp[i] = True
#                     return True
#                 j += 1

#             dp[i] = False
#             return False
     
#         return dfs(n)
        

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]        