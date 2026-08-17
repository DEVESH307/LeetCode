# from functools import cache

# class Solution:
#     def stoneGameV(self, stoneValue: List[int]) -> int:
#         n = len(stoneValue)

#         prefix_sum = [0] * (n + 1)
#         for i in range(n):
#             prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

#         dp = [[-1] * n for _ in range(n)]

#         # @cache
#         def dfs(left, right):
#             if left == right:
#                 return 0

#             if dp[left][right] != -1:
#                 return dp[left][right]

#             ans = 0
#             for mid in range(left, right):

#                 left_sum = prefix_sum[mid + 1] - prefix_sum[left]
#                 right_sum = prefix_sum[right + 1] - prefix_sum[mid + 1]

#                 if left_sum < right_sum:
#                     ans = max(ans, left_sum + dfs(left, mid))

#                 elif left_sum > right_sum:
#                     ans = max(ans, right_sum + dfs(mid + 1, right))

#                 else:
#                     ans = max(ans, left_sum + dfs(left, mid), right_sum + dfs(mid + 1, right))

#             dp[left][right] = ans
#             return ans

#         return dfs(0, n - 1)


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def getSum(l, r):
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]
        bestLeft = [[0] * n for _ in range(n)]
        bestRight = [[0] * n for _ in range(n)]

        for i in range(n):
            bestLeft[i][i] = stoneValue[i]
            bestRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0

            for left in range(n - length + 1):
                right = left + length - 1

                if mid < left:
                    mid = left

                # mid becomes the first split where leftSum > rightSum
                while mid < right and getSum(left, mid) <= getSum(mid + 1, right):
                    mid += 1

                ans = 0

                # Splits before mid satisfy leftSum <= rightSum
                if mid > left:
                    ans = max(ans, bestLeft[left][mid - 1])

                # Splits from mid onward satisfy leftSum > rightSum
                if mid < right:
                    ans = max(ans, bestRight[mid + 1][right])

                # Check if split mid-1 is exactly equal
                if mid > left and getSum(left, mid - 1) == getSum(mid, right):
                    ans = max(ans, bestRight[mid][right])

                dp[left][right] = ans

                val = getSum(left, right) + ans

                bestLeft[left][right] = max(bestLeft[left][right - 1], val)
                bestRight[left][right] = max(bestRight[left + 1][right], val)

        return dp[0][n - 1]