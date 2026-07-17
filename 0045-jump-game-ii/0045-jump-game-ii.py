# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)

#         def dfs(i):
#             if i >= n - 1:
#                 return 0

#             ans = float('inf')
#             for jump in range(1, nums[i] + 1):
#                 ans = min(ans, 1 + dfs(i + jump))

#             return ans

#         return dfs(0)
        

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         memo = {}

#         def dfs(i):
#             if i >= n - 1:
#                 return 0
            
#             if i in memo:
#                 return memo[i]

#             ans = float('inf')
#             for jump in range(1, nums[i] + 1):
#                 ans = min(ans, 1 + dfs(i + jump))
            
#             memo[i] = ans
#             return ans

#         return dfs(0)
        

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [float('inf')] * n
#         dp[-1] = 0

#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1, min(n, i + nums[i] + 1)):
#                 dp[i] = min(dp[i], 1 + dp[j])

#         return dp[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        left = right = 0

        while right < n - 1:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            jumps += 1

        return jumps