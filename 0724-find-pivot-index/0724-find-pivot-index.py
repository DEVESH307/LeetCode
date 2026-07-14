# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n = len(nums)
#         prefix_sum = [0] * n
#         suffix_sum = [0] * n

#         # Build prefix sums
#         for i in range(1, n):
#             prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

#         # Build suffix sums
#         for i in range(n - 2, -1, -1):
#             suffix_sum[i] = suffix_sum[i + 1] + nums[i + 1]

#         # Find the pivot index
#         for i in range(n):
#             if prefix_sum[i] == suffix_sum[i]:
#                 return i

#         return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i

            left_sum += num

        return -1