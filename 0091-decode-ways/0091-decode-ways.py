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


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         dp = [-1] * (n + 1)
        
#         def dfs(i):
#             # i = length of string considered
#             if i == 0:
#                 return 1

#             if dp[i] != -1:
#                 return dp[i]

#             ways = 0

#             # take one digit (only if not '0')
#             if s[i - 1] != '0':
#                 ways += dfs(i - 1)

#             # take two digits (10–26)
#             if i - 2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
#                 ways += dfs(i - 2)

#             dp[i] = ways
#             return dp[i]

#         return dfs(n)


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * (n + 1)
#         dp[0] = 1 # empty string

#         for i in range(1, n + 1):
#             # take one digit (only if not '0')
#             if s[i - 1] != '0':
#                 dp[i] = dp[i] + dp[i - 1]

#             # take two digits (10–26)
#             if i - 2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
#                 dp[i] = dp[i] + dp[i - 2]

#         return dp[n]


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev2 = 1 # dp[0] -> empty string
        prev1 = 1 if s[0] != '0' else 0  # dp[1]

        for i in range(2, n + 1):
            curr = 0

            # take one digit (only if not '0')
            if s[i - 1] != '0':
                curr += prev1

            # take two digits (10–26)
            if 10 <= int(s[i-2:i]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1