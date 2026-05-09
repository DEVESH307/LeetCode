# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)

#         for i in range(1, n):
#             if nums[i-1] == nums[i]:
#                 return True
#         return False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         n = len(nums)
#         unique = set()
#         for num in nums:
#             if num in unique:
#                 return True
#             else:
#                 unique.add(num)
#         return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))