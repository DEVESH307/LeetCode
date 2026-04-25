# class Solution:
#     def minimumDifference(self, nums):
#         n = len(nums)
#         total = sum(nums)
#         half = n // 2

#         def dfs(i, count, curr):
#             if i == n:
#                 if count == half:
#                     return abs(total - 2 * curr)
#                 return float('inf')

#             take = dfs(i + 1, count + 1, curr + nums[i])
#             skip = dfs(i + 1, count, curr)

#             return min(take, skip)

#         return dfs(0, 0, 0)


# class Solution:
#     def minimumDifference(self, nums):
#         n = len(nums)
#         total = sum(nums)
#         half = n // 2

#         memo = {}

#         def dfs(i, count, curr):
#             if i == n:
#                 if count == half:
#                     return abs(total - 2 * curr)
#                 return float('inf')

#             if (i, count, curr) in memo:
#                 return memo[(i, count, curr)]

#             take = dfs(i + 1, count + 1, curr + nums[i])
#             skip = dfs(i + 1, count, curr)

#             memo[(i, count, curr)] = min(take, skip)
#             return memo[(i, count, curr)]

#         return dfs(0, 0, 0)


# class Solution:
#     def minimumDifference(self, nums):
#         n = len(nums)
#         half = n // 2

#         dp = [set() for _ in range(half + 1)]
#         dp[0].add(0)

#         for num in nums:
#             for k in range(half, 0, -1):
#                 for s in dp[k - 1]:
#                     dp[k].add(s + num)

#         total = sum(nums)
#         ans = float('inf')

#         for s in dp[half]:
#             ans = min(ans, abs(total - 2 * s))

#         return ans


from collections import defaultdict
import bisect

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        half = n // 2
        total = sum(nums)
        target = total // 2

        # build dp[k] for ONE half only
        def build(arr):
            m = len(arr)
            dp = [[] for _ in range(m + 1)]
            dp[0] = [0]

            for num in arr:
                for k in range(m - 1, -1, -1):
                    for s in dp[k]:
                        dp[k + 1].append(s + num)

            return dp

        left = build(nums[:half])
        right = build(nums[half:])

        # sort right side for binary search
        for k in range(len(right)):
            right[k].sort()

        ans = float('inf')

        # combine
        for k in range(half + 1):
            L = left[k]
            R = right[half - k]

            for x in L:
                need = target - x
                idx = bisect.bisect_left(R, need)

                if idx < len(R):
                    s = x + R[idx]
                    ans = min(ans, abs(total - 2 * s))

                if idx > 0:
                    s = x + R[idx - 1]
                    ans = min(ans, abs(total - 2 * s))

        return ans