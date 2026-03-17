# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums.sort()
#         ans = 0

#         for i in range(1, n):
#             if nums[i] <= nums[i-1]:
#                 needed = nums[i-1] + 1
#                 ans += needed - nums[i]
#                 nums[i] = needed

#         return ans


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                needed = prev + 1
                ans += needed - nums[i]
                prev = needed
            else:
                prev = nums[i]

        return ans