# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l1, l2, l3 = len(s1), len(s2), len(s3)

#         if l1 + l2 != l3:
#             return False

#         def dfs(i, j, k):
#             if k < 0:
#                 return i < 0 and j < 0

#             if i >= 0 and s1[i] == s3[k]:
#                 if dfs(i - 1, j, k - 1):
#                     return True

#             if j >= 0 and s2[j] == s3[k]:
#                 if dfs(i, j - 1, k - 1):
#                     return True

#             return False

#         return dfs(l1 - 1, l2 - 1, l3 - 1)


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l1, l2, l3 = len(s1), len(s2), len(s3)

#         if l1 + l2 != l3:
#             return False

#         memo = {}

#         def dfs(i, j, k):
#             if (i, j) in memo:
#                 return memo[(i, j)]

#             if k < 0:
#                 return i < 0 and j < 0

#             if i >= 0 and s1[i] == s3[k]:
#                 if dfs(i - 1, j, k - 1):
#                     memo[(i, j)] = True
#                     return True

#             if j >= 0 and s2[j] == s3[k]:
#                 if dfs(i, j - 1, k - 1):
#                     memo[(i, j)] = True
#                     return True

#             memo[(i, j)] = False
#             return False

#         return dfs(l1 - 1, l2 - 1, l3 - 1)


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l1, l2, l3 = len(s1), len(s2), len(s3)

#         if l1 + l2 != l3:
#             return False

#         dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]

#         def dfs(i, j, k):
#             if dp[i + 1][j + 1] != -1:
#                 return dp[i + 1][j + 1]

#             if k < 0:
#                 dp[i + 1][j + 1] = (i < 0 and j < 0)
#                 return dp[i + 1][j + 1]

#             if i >= 0 and s1[i] == s3[k]:
#                 if dfs(i - 1, j, k - 1):
#                     dp[i + 1][j + 1] = True
#                     return True

#             if j >= 0 and s2[j] == s3[k]:
#                 if dfs(i, j - 1, k - 1):
#                     dp[i + 1][j + 1] = True
#                     return True

#             dp[i + 1][j + 1] = False
#             return False

#         return dfs(l1 - 1, l2 - 1, l3 - 1)


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l1, l2, l3 = len(s1), len(s2), len(s3)

#         if l1 + l2 != l3:
#             return False

#         dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]

#         dp[0][0] = True

#         for i in range(1, l1 + 1):
#             dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

#         for j in range(1, l2 + 1):
#             dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 k = i + j - 1

#                 if s1[i - 1] == s3[k] and dp[i - 1][j]:
#                     dp[i][j] = True
#                 elif s2[j - 1] == s3[k] and dp[i][j - 1]:
#                     dp[i][j] = True

#         return dp[l1][l2]


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l1, l2, l3 = len(s1), len(s2), len(s3)

#         if l1 + l2 != l3:
#             return False

#         prev = [False] * (l2 + 1)

#         prev[0] = True
#         for j in range(1, l2 + 1):
#             prev[j] = prev[j - 1] and s2[j - 1] == s3[j - 1]

#         for i in range(1, l1 + 1):
#             curr = [False] * (l2 + 1)

#             curr[0] = prev[0] and s1[i - 1] == s3[i - 1]

#             for j in range(1, l2 + 1):
#                 k = i + j - 1

#                 take_A = prev[j] and s1[i - 1] == s3[k]
#                 take_B = curr[j - 1] and s2[j - 1] == s3[k]

#                 curr[j] = take_A or take_B

#             prev = curr

#         return prev[l2]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l1 + l2 != l3:
            return False

        dp = [False] * (l2 + 1)

        # base case
        dp[0] = True

        # first row (i = 0)
        for j in range(1, l2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, l1 + 1):
            # first column
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, l2 + 1):
                k = i + j - 1

                take_A = dp[j] and s1[i - 1] == s3[k]      # old dp[j] → previous row
                take_B = dp[j - 1] and s2[j - 1] == s3[k]  # updated dp[j-1] → current row

                dp[j] = take_A or take_B

        return dp[l2]