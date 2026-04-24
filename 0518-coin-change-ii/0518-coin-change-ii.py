# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)

#         def dfs(i, rem):
#             if rem == 0:
#                 return 1
#             if i < 0 or rem < 0:
#                 return 0

#             pick = dfs(i, rem - coins[i])
#             skip = dfs(i - 1, rem)

#             return pick + skip

#         return dfs(n - 1, amount)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[-1] * (amount + 1) for _ in range(n)]

#         def dfs(i, rem):
#             if rem == 0:
#                 return 1
#             if i < 0 or rem < 0:
#                 return 0

#             if dp[i][rem] != -1:
#                 return dp[i][rem]

#             pick = dfs(i, rem - coins[i])
#             skip = dfs(i - 1, rem)

#             dp[i][rem] = pick + skip
#             return dp[i][rem]

#         return dfs(n - 1, amount)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = {}

#         def dfs(i, rem):
#             if rem == 0:
#                 return 1
#             if i < 0 or rem < 0:
#                 return 0

#             if (i, rem) in dp:
#                 return dp[(i, rem)]

#             pick = dfs(i, rem - coins[i])
#             skip = dfs(i - 1, rem)

#             dp[(i, rem)] = pick + skip
#             return dp[(i, rem)]

#         return dfs(len(coins) - 1, amount)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0] * (amount + 1) for _ in range(n)]

#         for i in range(n):
#             dp[i][0] = 1

#         for i in range(n):
#             for j in range(amount + 1):
#                 pick = dp[i][j - coins[i]] if j >= coins[i] else 0
#                 skip = dp[i - 1][j] if i > 0 else 0
#                 dp[i][j] = pick + skip

#         return dp[n - 1][amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)

#         prev = [0] * (amount + 1)
#         prev[0] = 1

#         for i in range(n):
#             curr = [0] * (amount + 1)
#             curr[0] = 1

#             for j in range(amount + 1):
#                 pick = curr[j - coins[i]] if j >= coins[i] else 0
#                 skip = prev[j]
#                 curr[j] = pick + skip

#             prev = curr

#         return prev[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[amount]