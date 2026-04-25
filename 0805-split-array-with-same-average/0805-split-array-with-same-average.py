# class Solution:
#     def splitArraySameAverage(self, nums: List[int]) -> bool:
#         n = len(nums)
#         total = sum(nums)

#         def dfs(i, count, curr_sum):
#             # skip empty and full set
#             if count > 0 and count < n:
#                 if curr_sum * n == total * count:
#                     return True

#             if i == n:
#                 return False

#             # take
#             if dfs(i+1, count+1, curr_sum + nums[i]):
#                 return True

#             # skip
#             if dfs(i+1, count, curr_sum):
#                 return True

#             return False

#         return dfs(0, 0, 0)


# class Solution:
#     def splitArraySameAverage(self, nums):
#         n = len(nums)
#         total = sum(nums)

#         # possible subset sizes
#         valid_k = set()
#         for k in range(1, n):
#             if (total * k) % n == 0:
#                 valid_k.add(k)

#         memo = set()  # visited states (i, count, sum)

#         def dfs(i, count, curr_sum):
#             # valid subset found
#             if count in valid_k and curr_sum * n == total * count:
#                 return True

#             if i == n or count > n // 2:
#                 return False

#             state = (i, count, curr_sum)
#             if state in memo:
#                 return False
#             memo.add(state)

#             # take
#             if dfs(i + 1, count + 1, curr_sum + nums[i]):
#                 return True

#             # skip
#             if dfs(i + 1, count, curr_sum):
#                 return True

#             return False

#         return dfs(0, 0, 0)


# class Solution:
#     def splitArraySameAverage(self, nums):
#         n = len(nums)
#         total = sum(nums)

#         # dp[k] = set of sums possible using k elements
#         dp = [set() for _ in range(n + 1)]
#         dp[0].add(0)

#         for num in nums:
#             for k in range(n - 1, -1, -1):
#                 for s in dp[k]:
#                     dp[k + 1].add(s + num)

#         # check valid subset sizes
#         for k in range(1, n):
#             if (total * k) % n != 0:
#                 continue

#             target = (total * k) // n
#             if target in dp[k]:
#                 return True

#         return False


# class Solution:
#     def splitArraySameAverage(self, nums):
#         n = len(nums)
#         total = sum(nums)

#         # transform array
#         nums = [num * n - total for num in nums]

#         # dp[k] = possible sums using k elements
#         dp = [set() for _ in range(n + 1)]
#         dp[0].add(0)

#         for num in nums:
#             for k in range(n - 1, 0, -1):
#                 for s in dp[k - 1]:
#                     new_sum = s + num

#                     if new_sum == 0:
#                         return True

#                     dp[k].add(new_sum)

#         return False


class Solution:
    def splitArraySameAverage(self, nums):
        total = sum(nums)
        n = len(nums)

        # quick pruning
        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                break
        else:
            return False

        dp = [0] * (n // 2 + 1)
        dp[0] = 1  # sum 0 possible

        for num in nums:
            for k in range(n // 2, 0, -1):
                dp[k] |= dp[k - 1] << num

        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                target = (total * k) // n
                if dp[k] & (1 << target):
                    return True

        return False