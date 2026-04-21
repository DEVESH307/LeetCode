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


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [-1] * (n + 1)

#         def dfs(i):
#             if i < 0:
#                 return 0

#             if dp[i] != -1:
#                 return dp[i]

#             rob = nums[i] + dfs(i - 2)
#             not_rob = dfs(i - 1)
#             ans = max(rob, not_rob)

#             dp[i] = ans
#             return ans

#         return dfs(n - 1)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
            
#         dp = [-1] * (n + 1)
#         dp[0] = 0
#         dp[1] = nums[0]

#         for i in range(2, n + 1):
#             rob = nums[i - 1] + dp[i - 2]
#             not_rob = dp[i - 1]
#             dp[i] = max(rob, not_rob)

#         return dp[n]


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
            
        prev2 = 0       # dp[i-2]
        prev1 = nums[0] # dp[i-1]

        for num in nums[1:]:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1
