# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)

#         def dfs(i, j):
#             # both exhausted
#             if i == 0 and j == 0:
#                 return True

#             # pattern empty
#             if j == 0:
#                 return False

#             # handle '*'
#             if j >= 2 and p[j-1] == '*':
#                 # match with preceding character of '*'
#                 match = (i > 0 and (p[j-2] == s[i-1] or p[j-2] == '.'))

#                 # 2 choices:
#                 # 1. ignore "x*" → dfs(i, j-2)
#                 # 2. use "x*" → if match, consume one char → dfs(i-1, j)
#                 return dfs(i, j-2) or (match and dfs(i-1, j))

#             # normal match or '.'
#             match = (i > 0 and (p[j-1] == s[i-1] or p[j-1] == '.'))
#             if match:
#                 return dfs(i-1, j-1)

#             return False

#         return dfs(ls, lp)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)
        
#         dp = [[None] * (lp + 1) for _ in range(ls + 1)]

#         def dfs(i, j):
#             # check cache
#             if dp[i][j] is not None:
#                 return dp[i][j]

#             # both exhausted
#             if i == 0 and j == 0:
#                 dp[i][j] = True
#                 return True

#             # pattern empty
#             if j == 0:
#                 dp[i][j] = False
#                 return False

#             # handle '*'
#             if j >= 2 and p[j-1] == '*':
#                 match = (i > 0 and (p[j-2] == s[i-1] or p[j-2] == '.'))
                
#                 dp[i][j] = dfs(i, j-2) or (match and dfs(i-1, j))
#                 return dp[i][j]

#             # normal match
#             match = (i > 0 and (p[j-1] == s[i-1] or p[j-1] == '.'))

#             if match:
#                 dp[i][j] = dfs(i-1, j-1)
#             else:
#                 dp[i][j] = False

#             return dp[i][j]

#         return dfs(ls, lp)


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ls, lp = len(s), len(p)

#         dp = [[False] * (lp + 1) for _ in range(ls + 1)]

#         # base case
#         dp[0][0] = True

#         # handle empty string with pattern like a*b*c*
#         for j in range(2, lp + 1):
#             if p[j-1] == '*':
#                 dp[0][j] = dp[0][j-2]

#         # fill table
#         for i in range(1, ls + 1):
#             for j in range(1, lp + 1):

#                 # '*' case (same as recursion)
#                 if j >= 2 and p[j-1] == '*':
#                     match = (p[j-2] == s[i-1] or p[j-2] == '.')
                    
#                     dp[i][j] = dp[i][j-2] or (match and dp[i-1][j])

#                 else:
#                     # normal match
#                     match = (p[j-1] == s[i-1] or p[j-1] == '.')
                    
#                     if match:
#                         dp[i][j] = dp[i-1][j-1]

#         return dp[ls][lp]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)

        prev = [False] * (lp + 1)
        prev[0] = True

        # base case: empty string vs pattern
        for j in range(2, lp + 1):
            if p[j-1] == '*':
                prev[j] = prev[j-2]

        for i in range(1, ls + 1):
            curr = [False] * (lp + 1)

            for j in range(1, lp + 1):

                if j >= 2 and p[j-1] == '*':
                    match = (p[j-2] == s[i-1] or p[j-2] == '.')
                    
                    curr[j] = curr[j-2] or (match and prev[j])

                else:
                    match = (p[j-1] == s[i-1] or p[j-1] == '.')
                    
                    if match:
                        curr[j] = prev[j-1]

            prev = curr

        return prev[lp]