# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         n = len(nums)

#         prefix_sum = [0] * (n + 1)

#         for i in range(n):
#             prefix_sum[i+1] = prefix_sum[i] + nums[i]

#         # fn to chk if curr len works or not
#         def valid(length):
#             for i in range(n - length + 1):
#                 if prefix_sum[i + length] - prefix_sum[i] >= target:
#                     return True
#             return False

#         left, right = 1, n
#         ans = 0

#         while left <= right:
#             mid = (left+right)//2

#             if valid(mid):
#                 ans = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         return ans


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                curr_len = right - left + 1
                min_len = min(min_len, curr_len)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

        