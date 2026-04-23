# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)

#         def dfs(i, j):
#             # both exhausted
#             if i == 0 and j == 0: 
#                 return True

#             # pattern empty but string not
#             if j == 0:
#                 return False

#             # string empty
#             if i == 0:
#                 if p[j-1] == '*':
#                     return dfs(i, j-1)
#                 else:
#                     return False

#             # if i == 0:
#             #     # only valid if all remaining pattern are '*'
#             #     return all(p[k] == '*' for k in range(j))

#             # char match or '?'
#             if s[i-1] == p[j-1] or p[j-1] == '?':
#                 return dfs(i-1, j-1)

#             # '*'
#             if p[j-1] == '*':
#                 # 2 choices:
#                 # 1. match empty -> dfs(i, j-1)
#                 # 2. match one char -> dfs(i-1, j)
#                 return dfs(i, j-1) or dfs(i-1, j)

#             return False

#         return dfs(ls, lp)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)
#         dp = [[None] * (lp + 1) for _ in range(ls + 1)]

#         def dfs(i, j):
#             # both exhausted
#             if i == 0 and j == 0: 
#                 return True

#             # pattern empty but string not
#             if j == 0:
#                 return False

#             # string empty
#             if i == 0:
#                 if p[j-1] == '*':
#                     return dfs(i, j-1)
#                 else:
#                     return False

#             # if i == 0:
#             #     # only valid if all remaining pattern are '*'
#             #     return all(p[k] == '*' for k in range(j))

#             if dp[i][j] is not None:
#                 return dp[i][j]

#             # char match or '?'
#             if s[i-1] == p[j-1] or p[j-1] == '?':
#                 dp[i][j] = dfs(i-1, j-1)

#             # '*'
#             elif p[j-1] == '*':
#                 # 2 choices:
#                 # 1. match empty -> dfs(i, j-1)
#                 # 2. match one char -> dfs(i-1, j)
#                 dp[i][j] = dfs(i, j-1) or dfs(i-1, j)

#             else:
#                 dp[i][j] = False
            
#             return dp[i][j]
        
#         return dfs(ls, lp)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)
#         dp = [[False] * (lp + 1) for _ in range(ls + 1)]
#         dp[0][0] = True

#         # pattern vs empty string
#         for j in range(1, lp + 1):
#             if p[j-1] == '*':
#                 dp[0][j] = dp[0][j-1]

#         for i in range(1, ls + 1):
#             for j in range(1, lp + 1):
#                 # char match or '?'
#                 if s[i-1] == p[j-1] or p[j-1] == '?':
#                     dp[i][j] = dp[i-1][j-1]

#                 # '*'
#                 elif p[j-1] == '*':
#                     # 2 choices:
#                     # 1. match empty -> dfs(i, j-1)
#                     # 2. match one char -> dfs(i-1, j)
#                     dp[i][j] = dp[i][j-1] or dp[i-1][j]

#         return dp[ls][lp]


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)
#         prev = [False] * (lp + 1)
#         prev[0] = True

#         # pattern vs empty string
#         for j in range(1, lp + 1):
#             if p[j-1] == '*':
#                 prev[j] = prev[j-1]

#         for i in range(1, ls + 1):
#             curr = [False] * (lp + 1)

#             for j in range(1, lp + 1):
#                 # char match or '?'
#                 if s[i-1] == p[j-1] or p[j-1] == '?':
#                     curr[j] =prev[j-1]

#                 # '*'
#                 elif p[j-1] == '*':
#                     # 2 choices:
#                     # 1. match empty -> dfs(i, j-1)
#                     # 2. match one char -> dfs(i-1, j)
#                     curr[j] = curr[j-1] or prev[j]

#             prev = curr

#         return prev[lp]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        match = 0
        
        while i < len(s):
            # match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            
            # '*' found
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            
            # mismatch but we had previous '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            
            else:
                return False
        
        # remaining pattern should be all '*'
        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)