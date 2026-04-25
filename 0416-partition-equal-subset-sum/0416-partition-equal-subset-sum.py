# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
        
#         # if total is odd → impossible
#         if total % 2 != 0:
#             return False
        
#         target = total // 2
#         n = len(nums)

#         def dfs(i, curr_sum):
#             if curr_sum == target:
#                 return True

#             if i == n or curr_sum > target:
#                 return False
            
#             # take or skip
#             take = dfs(i + 1, curr_sum + nums[i])
#             skip = dfs(i + 1, curr_sum)

#             return take or skip

#         return dfs(0, 0)


# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         n = len(nums)

#         memo = {}

#         def dfs(i, curr):
#             if curr == target:
#                 return True
#             if i == n or curr > target:
#                 return False

#             if (i, curr) in memo:
#                 return memo[(i, curr)]

#             take = dfs(i + 1, curr + nums[i])
#             skip = dfs(i + 1, curr)

#             memo[(i, curr)] = take or skip
#             return memo[(i, curr)]

#         return dfs(0, 0)


# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         n = len(nums)

#         # dp[i][curr] = -1 (unvisited), 0 (False), 1 (True)
#         dp = [[-1] * (target + 1) for _ in range(n)]

#         def dfs(i, curr):
#             if curr == target:
#                 return True
#             if i == n or curr > target:
#                 return False

#             if dp[i][curr] != -1:
#                 return dp[i][curr]

#             take = dfs(i + 1, curr + nums[i])
#             skip = dfs(i + 1, curr)

#             dp[i][curr] = take or skip
#             return dp[i][curr]

#         return dfs(0, 0)


# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         n = len(nums)

#         # dp[i][s]
#         dp = [[False] * (target + 1) for _ in range(n + 1)]

#         # base case: sum 0 always possible
#         for i in range(n + 1):
#             dp[i][0] = True

#         # fill table
#         for i in range(1, n + 1):
#             num = nums[i - 1]
#             for s in range(1, target + 1):
#                 # skip
#                 dp[i][s] = dp[i - 1][s]

#                 # take
#                 if s >= num:
#                     dp[i][s] = dp[i][s] or dp[i - 1][s - num]

#         return dp[n][target]


# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2

#         prev = [False] * (target + 1)
#         prev[0] = True  # base case

#         for num in nums:
#             curr = prev[:]  # start with "skip" case

#             for s in range(1, target + 1):
#                 if s >= num:
#                     curr[s] = curr[s] or prev[s - num]

#             prev = curr  # move forward

#         return prev[target]


class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total & 1:   # faster than % 2
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # early exit if already possible
            if dp[target]:
                return True

            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True

        return dp[target]