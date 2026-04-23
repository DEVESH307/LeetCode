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


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[None] * (lp + 1) for _ in range(ls + 1)]

        def dfs(i, j):
            # both exhausted
            if i == 0 and j == 0: 
                return True

            # pattern empty but string not
            if j == 0:
                return False

            # string empty
            if i == 0:
                if p[j-1] == '*':
                    return dfs(i, j-1)
                else:
                    return False

            # if i == 0:
            #     # only valid if all remaining pattern are '*'
            #     return all(p[k] == '*' for k in range(j))

            if dp[i][j] is not None:
                return dp[i][j]

            # char match or '?'
            if s[i-1] == p[j-1] or p[j-1] == '?':
                dp[i][j] = dfs(i-1, j-1)

            # '*'
            elif p[j-1] == '*':
                # 2 choices:
                # 1. match empty -> dfs(i, j-1)
                # 2. match one char -> dfs(i-1, j)
                dp[i][j] = dfs(i, j-1) or dfs(i-1, j)

            else:
                dp[i][j] = False
            
            return dp[i][j]
        
        return dfs(ls, lp)