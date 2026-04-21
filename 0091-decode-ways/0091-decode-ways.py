# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
        
#         def dfs(i):
#             # i = length of string considered
#             if i == 0:
#                 return 1

#             ways = 0

#             # take one digit (only if not '0')
#             if s[i - 1] != '0':
#                 ways += dfs(i - 1)

#             # take two digits (10–26)
#             if i - 2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
#                 ways += dfs(i - 2)

#             return ways

#         return dfs(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        
        def dfs(i):
            # i = length of string considered
            if i == 0:
                return 1

            if dp[i] != -1:
                return dp[i]

            ways = 0

            # take one digit (only if not '0')
            if s[i - 1] != '0':
                ways += dfs(i - 1)

            # take two digits (10–26)
            if i - 2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
                ways += dfs(i - 2)

            dp[i] = ways
            return dp[i]

        return dfs(n)
            