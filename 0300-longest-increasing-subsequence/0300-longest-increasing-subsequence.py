# class Solution:
#     def lengthOfLIS(self, nums):
#         n = len(nums)

#         def dfs(index, prev):
#             if index == n:
#                 return 0

#             not_take = dfs(index + 1, prev)

#             take = 0
#             if prev == -1 or nums[index] > nums[prev]:
#                 take = 1 + dfs(index + 1, index)

#             return max(take, not_take)

#         return dfs(0, -1)


# class Solution:
#     def lengthOfLIS(self, nums):
#         n = len(nums)
#         dp = [[-1] * (n + 1) for _ in range(n)]

#         def dfs(index, prev):
#             if index == n:
#                 return 0

#             if dp[index][prev + 1] != -1:
#                 return dp[index][prev + 1]

#             not_take = dfs(index + 1, prev)

#             take = 0
#             if prev == -1 or nums[index] > nums[prev]:
#                 take = 1 + dfs(index + 1, index)

#             dp[index][prev + 1] = max(take, not_take)
#             return dp[index][prev + 1]

#         return dfs(0, -1)


# class Solution:
#     def lengthOfLIS(self, nums):
#         n = len(nums)

#         dp = [[0] * (n + 1) for _ in range(n + 1)]

#         for index in range(n - 1, -1, -1):
#             for prev in range(index - 1, -2, -1):

#                 not_take = dp[index + 1][prev + 1]

#                 take = 0
#                 if prev == -1 or nums[index] > nums[prev]:
#                     take = 1 + dp[index + 1][index + 1]

#                 dp[index][prev + 1] = max(take, not_take)

#         return dp[0][0]


# class Solution:
#     def lengthOfLIS(self, nums):
#         n = len(nums)
#         if n == 0:
#             return 0

#         dp = [1] * n
#         max_len = 1

#         for i in range(n):
#             curr = 1
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     curr = max(curr, dp[j] + 1)

#             dp[i] = curr
#             max_len = max(max_len, dp[i])

#         return max_len


from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):

        tails = []

        for num in nums:
            idx = bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)