# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)

#         def dfs(i):
#             if i >= n-1:
#                 return True

#             for jump in range(1, nums[i] + 1):
#                 if dfs(i + jump):
#                     return True

#             return False

#         return dfs(0)


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         memo = {}

#         def dfs(i):
#             if i >= n-1:
#                 return True

#             if i in memo:
#                 return memo[i]

#             for jump in range(1, nums[i] + 1):
#                 if dfs(i + jump):
#                     memo[i] = True
#                     return True

#             memo[i] = False
#             return False

#         return dfs(0)


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = [False] * n
#         dp[-1] = True

#         for i in range(n - 2, -1, -1):
#             farthest = min(i + nums[i], n - 1)

#             for j in range(i + 1, farthest + 1):
#                 if dp[j]:
#                     dp[i] = True
#                     break

#         return dp[0]


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         goal = n - 1

#         for i in range(n - 2, -1, -1):
#             if i + nums[i] >= goal:
#                 goal = i

#         return goal == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0

        for i in range(n):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])
        return True