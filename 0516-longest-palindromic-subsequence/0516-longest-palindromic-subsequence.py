# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         s_rev = s[::-1]
#         n = len(s)

#         dp = [[None] * (n + 1) for _ in range(n + 1)]

#         def dfs(i, j):
#             if i == 0 or j == 0:
#                 return 0

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             if s[i - 1] == s_rev[j - 1]:
#                 dp[i][j] = 1 + dfs(i - 1, j - 1)
#             else:
#                 dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))

#             return dp[i][j]

#         return dfs(n, n)


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         dp = [[None] * n for _ in range(n)]

#         def dfs(i, j):
#             if i > j:
#                 return 0
#             if i == j:
#                 return 1

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             if s[i] == s[j]:
#                 dp[i][j] = 2 + dfs(i + 1, j - 1)
#             else:
#                 dp[i][j] = max(dfs(i + 1, j), dfs(i, j - 1))

#             return dp[i][j]

#         return dfs(0, n - 1)


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]

#         for i in range(n):
#             dp[i][i] = 1

#         for length in range(2, n + 1):
#             for i in range(n - length + 1):
#                 j = i + length - 1

#                 if s[i] == s[j]:
#                     if length == 2:
#                         dp[i][j] = 2
#                     else:
#                         dp[i][j] = 2 + dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

#         return dp[0][n - 1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            prev_diag = 0
            dp[i] = 1

            for j in range(i + 1, n):
                temp = dp[j]

                if s[i] == s[j]:
                    dp[j] = 2 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev_diag = temp

        return dp[n - 1]