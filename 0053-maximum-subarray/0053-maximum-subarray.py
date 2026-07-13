# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr_sum = max_sum = nums[0]
#         curr_start = start = end = 0

#         for i in range(1, len(nums)):
#             if curr_sum < 0:
#                 curr_sum = nums[i]
#                 curr_start = i
#             else:
#                 curr_sum += nums[i]

#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#                 start = curr_start
#                 end = i
            
#         # print(start, end)
#         return max_sum
                          

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        curr_start = 0
        start = end = 0

        for i, val in enumerate(nums):
            curr_sum += val

            if curr_sum > max_sum:
                max_sum = curr_sum
                start = curr_start
                end = i

            if curr_sum < 0:
                curr_sum = 0
                curr_start = i + 1

        # print(start, end)

        return max_sum