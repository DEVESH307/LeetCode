# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)

#         def is_pal(l, r):
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         def dfs(i):
#             if i == n:
#                 return -1

#             ans = float('inf')
#             for j in range(i, n):
#                 if is_pal(i, j):
#                     ans = min(ans, 1 + dfs(j + 1))
#             return ans

#         return dfs(0)


# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         dp = [-1] * n

#         def is_pal(l, r):
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         def dfs(i):
#             if i == n:
#                 return -1

#             if dp[i] != -1:
#                 return dp[i]

#             ans = float('inf')
#             for j in range(i, n):
#                 if is_pal(i, j):
#                     ans = min(ans, 1 + dfs(j + 1))

#             dp[i] = ans
#             return ans

#         return dfs(0)


# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)

#         def is_pal(l, r):
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         dp = [0] * (n + 1)
#         dp[n] = -1

#         for i in range(n - 1, -1, -1):
#             ans = float('inf')
#             for j in range(i, n):
#                 if is_pal(i, j):
#                     ans = min(ans, 1 + dp[j + 1])
#             dp[i] = ans

#         return dp[0]


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # Precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * (n + 1)
        dp[n] = -1

        for i in range(n - 1, -1, -1):
            ans = float('inf')
            for j in range(i, n):
                if pal[i][j]:
                    ans = min(ans, 1 + dp[j + 1])
            dp[i] = ans

        return dp[0]

