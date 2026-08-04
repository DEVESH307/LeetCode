# class Solution:
#     def findMissingElements(self, nums: List[int]) -> List[int]:
#         mn = min(nums)
#         mx = max(nums)
#         ans = []

#         for i in range(mn, mx):
#             if i not in nums:
#                 ans.append(i)
        
#         return ans


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        i = 0

        for num in range(nums[0], nums[-1]):
            if nums[i] != num:
                ans.append(num)
            else:
                i += 1
        
        return ans