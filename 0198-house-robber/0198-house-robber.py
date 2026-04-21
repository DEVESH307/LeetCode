# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)

#         def dfs(i):
#             if i < 0:
#                 return 0

#             rob = nums[i] + dfs(i - 2)
#             not_rob = dfs(i - 1)
#             ans = max(rob, not_rob)

#             return ans

#         return dfs(n - 1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)

        def dfs(i):
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            rob = nums[i] + dfs(i - 2)
            not_rob = dfs(i - 1)
            ans = max(rob, not_rob)

            dp[i] = ans
            return ans

        return dfs(n - 1)
