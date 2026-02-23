# class Solution:
#     def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
#         n = len(nums1)
#         m = len(nums2)

#         xor_nums1 = 0
#         for num in nums1:
#             xor_nums1 ^= num

#         xor_nums2 = 0
#         for num in nums2:
#             xor_nums2 ^= num
        
#         if n % 2 == 0 and m % 2 == 0:
#             return 0
#         elif n % 2 == 0 and m % 2 != 0:
#             return xor_nums1
#         elif n % 2 != 0 and m % 2 == 0:
#             return xor_nums2
#         else:
#             return xor_nums1 ^ xor_nums2 


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums2) % 2:
            for x in nums1:
                ans ^= x

        if len(nums1) % 2:
            for x in nums2:
                ans ^= x

        return ans