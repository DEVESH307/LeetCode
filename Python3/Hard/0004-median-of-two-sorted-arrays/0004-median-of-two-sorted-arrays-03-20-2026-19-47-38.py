# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         # always binary search on smaller array
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
        
#         n, m = len(nums1), len(nums2)
#         total = n + m
#         half = (total + 1) // 2
        
#         left, right = 0, n
        
#         while left <= right:
#             cut1 = (left + right) // 2
#             cut2 = half - cut1
            
#             l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
#             l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
#             r1 = nums1[cut1] if cut1 < n else float('inf')
#             r2 = nums2[cut2] if cut2 < m else float('inf')
            
#             if l1 <= r2 and l2 <= r1:
#                 # correct partition
#                 if total % 2 == 1:
#                     return max(l1, l2)
#                 else:
#                     return (max(l1, l2) + min(r1, r2)) / 2
            
#             elif l1 > r2:
#                 right = cut1 - 1
#             else:
#                 left = cut1 + 1


class Solution:
    def countSmallerElement(self, nums, val):
        left, right = 0, len(nums) - 1
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= val:
                ans = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        
        return ans


    def KthElementInTwoSortedArrays(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]

        left = min(nums1[0], nums2[0])
        right = max(nums1[-1], nums2[-1])

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            count = (
                self.countSmallerElement(nums1, mid) +
                self.countSmallerElement(nums2, mid)
            )

            if count >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        total = n + m

        if total % 2 == 1:
            return self.KthElementInTwoSortedArrays(nums1, nums2, total // 2 + 1)
        else:
            left_median = self.KthElementInTwoSortedArrays(nums1, nums2, total // 2)
            right_median = self.KthElementInTwoSortedArrays(nums1, nums2, total // 2 + 1)
            return (left_median + right_median) / 2