# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         max_diff = -1
#         min_so_far = float('inf')
#         for i, val in enumerate(nums):
#             if val < min_so_far:
#                 min_so_far = val

#             max_diff = max(max_diff, val - min_so_far)

#         return -1 if max_diff == 0 else max_diff

        
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1

        for num in nums[1:]:
            if num > min_val:
                max_diff = max(max_diff, num - min_val)
            else:
                min_val = num

        return max_diff