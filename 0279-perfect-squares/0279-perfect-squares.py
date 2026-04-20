# class Solution:
#     def numSquares(self, n: int) -> int:

#         def dfs(i):
#             if i == 0:
#                 return 0

#             ans = float('inf')
#             for j in range(1, int(i**0.5) + 1):
#                 ans = min(ans, 1 + dfs(i - j * j))

#             return ans

#         return dfs(n)


# import sys
# sys.setrecursionlimit(10**6)
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [-1] * (n + 1)
        
#         def dfs(i):
#             if i == 0:
#                 dp[0] = 0
#                 return dp[0]

#             if dp[i] != -1:
#                 return dp[i]

#             ans = float('inf')
#             for j in range(1, int(i**0.5) + 1):
#                 ans = min(ans, 1 + dfs(i - j * j))

#             dp[i] = ans
#             return dp[i]

#         return dfs(n)


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j * j])

        return dp[n]