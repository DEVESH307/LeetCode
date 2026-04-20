# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         costs = [0] + costs  # now costs[1..n]

#         def dfs(i):
#             if i == 0:
#                 return 0

#             res = float('inf')

#             if i - 1 >=  0:
#                 res = min(res, dfs(i-1) + costs[i] + 1)

#             if i - 2 >=  0:
#                 res = min(res, dfs(i-2) + costs[i] + 4)

#             if i - 3 >=  0:
#                 res = min(res, dfs(i-3) + costs[i] + 9)

#             return res

#         return dfs(n)


# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         costs = [0] + costs  # now costs[1..n]
#         dp = [float('inf')] * (n + 1)

#         def dfs(i):
#             if i == 0:
#                 return 0

#             if dp[i] != float('inf'):
#                 return dp[i]

#             res = float('inf')

#             if i - 1 >=  0:
#                 res = min(res, dfs(i-1) + costs[i] + 1)
#             if i - 2 >=  0:
#                 res = min(res, dfs(i-2) + costs[i] + 4)
#             if i - 3 >=  0:
#                 res = min(res, dfs(i-3) + costs[i] + 9)

#             dp[i] = res
#             return dp[i]

#         return dfs(n)


# class Solution:
#     def climbStairs(self, n: int, costs: List[int]) -> int:
#         costs = [0] + costs  # now costs[1..n]
#         dp = [float('inf')] * (n + 1)
#         dp[0] = 0

#         for i in range(1, n+1):
#             if i - 1 >=  0:
#                 dp[i] = min(dp[i], dp[i-1] + costs[i] + 1)
#             if i - 2 >=  0:
#                 dp[i] = min(dp[i], dp[i-2] + costs[i] + 4)
#             if i - 3 >=  0:
#                 dp[i] = min(dp[i], dp[i-3] + costs[i] + 9)

#         return dp[n]


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs  # now costs[1..n]
        dp0 = float('inf')   # dp[i-3] = dp[3]
        dp1 = float('inf')   # dp[i-2] = dp[1]
        dp2 = 0              # dp[i-1] = dp[0]

        for i in range(1, n+1):
            curr = float('inf')
            if i - 1 >=  0:
                curr = min(curr, dp2 + costs[i] + 1)
            if i - 2 >=  0:
                curr = min(curr, dp1 + costs[i] + 4)
            if i - 3 >=  0:
                curr = min(curr, dp0 + costs[i] + 9)

            dp0, dp1, dp2 = dp1, dp2, curr

        return dp2