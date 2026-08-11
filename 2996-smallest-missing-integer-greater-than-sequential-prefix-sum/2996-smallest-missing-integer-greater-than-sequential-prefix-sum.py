# class Solution:
#     def missingInteger(self, nums: List[int]) -> int:
#         prefix_sum = nums[0]

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1] + 1:
#                 break
#             prefix_sum += nums[i]

#         seen = set(nums)

#         while prefix_sum in seen:
#             prefix_sum += 1

#         return prefix_sum


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # 1. Find sum of longest consecutive prefix
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            prefix_sum += nums[i]

        # 2. Find smallest integer >= total that isn't in nums
        seen = set(nums)

        while prefix_sum in seen:
            prefix_sum += 1

        return prefix_sum