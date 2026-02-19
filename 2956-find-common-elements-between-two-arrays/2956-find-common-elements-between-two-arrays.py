# class Solution:
#     def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1 = set(nums1)
#         set2 = set(nums2)
#         ans1 = 0
#         ans2 = 0

#         for num1 in nums1:
#             if num1 in set2:
#                 ans1 += 1

#         for num2 in nums2:
#             if num2 in set1:
#                 ans2 += 1

#         return [ans1, ans2]


class Solution:
    def findIntersectionValues(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        answer1 = sum(1 for num in nums1 if num in set2)
        answer2 = sum(1 for num in nums2 if num in set1)
        
        return [answer1, answer2]
