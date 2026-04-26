# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]

#         def dfs(arr, i):
#             if i < 0:
#                 return 0

#             rob = arr[i] + dfs(arr, i - 2)
#             not_rob = dfs(arr, i - 1)
#             return max(rob, not_rob)
        
#         # case 1: exclude last
#         case1 = dfs(nums[:-1], len(nums) - 2)

#         # case 2: exclude first
#         case2 = dfs(nums[1:], len(nums) - 2)

#         return max(case1, case2)


# class Solution:
#     def rob(self, nums):
#         n = len(nums)

#         if n == 1:
#             return nums[0]

#         def solve(arr):
#             m = len(arr)
#             dp = [-1] * m

#             def dfs(i):
#                 if i < 0:
#                     return 0

#                 if dp[i] != -1:
#                     return dp[i]

#                 rob = arr[i] + dfs(i - 2)
#                 not_rob = dfs(i - 1)

#                 dp[i] = max(rob, not_rob)
#                 return dp[i]

#             return dfs(m - 1)

#         # two cases for circular constraint
#         return max(
#             solve(nums[:-1]),  # exclude last
#             solve(nums[1:])    # exclude first
#         )


# class Solution:
#     def rob(self, nums):
#         n = len(nums)

#         if n == 1:
#             return nums[0]

#         def solve(arr):
#             m = len(arr)

#             if m == 0:
#                 return 0
#             if m == 1:
#                 return arr[0]

#             dp = [0] * m
#             dp[0] = arr[0]
#             dp[1] = max(arr[0], arr[1])

#             for i in range(2, m):
#                 dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

#             return dp[m - 1]

#         # two cases
#         return max(
#             solve(nums[:-1]),  # exclude last
#             solve(nums[1:])    # exclude first
#         )


class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )