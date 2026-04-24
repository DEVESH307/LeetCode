# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         def dfs(rem):
#             if rem == 0:
#                 return 0
#             if rem < 0:
#                 return float('inf')
#             res = float('inf')
#             for coin in coins:
#                 res = min(res, 1 + dfs(rem - coin))

#             return res
#         ans = dfs(amount)
#         return ans if ans != float('inf') else -1
        

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = {}

#         def dfs(rem):
#             if rem == 0:
#                 return 0
#             if rem < 0:
#                 return float('inf')

#             if rem in dp:
#                 return dp[rem]

#             res = float('inf')
#             for coin in coins:
#                 res = min(res, 1 + dfs(rem - coin))

#             dp[rem] = res
#             return res

#         ans = dfs(amount)
#         return ans if ans != float('inf') else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [-1] * (amount + 1)  # -1 means uncomputed

#         def dfs(rem):
#             if rem == 0:
#                 return 0
#             if rem < 0:
#                 return float('inf')

#             if dp[rem] != -1:
#                 return dp[rem]

#             res = float('inf')

#             for coin in coins:
#                 res = min(res, 1 + dfs(rem - coin))

#             dp[rem] = res
#             return res

#         ans = dfs(amount)
#         return ans if ans != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1