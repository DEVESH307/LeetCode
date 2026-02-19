# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0]*n

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i != j:
#                     prod *= nums[j]

#             res[i] = prod
        
#         return res


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [1]*n
#         pref_mul = [1]*n
#         suff_mul = [1]*n
        
#         pref_mul[0] = nums[0]
#         suff_mul[n-1] = nums[n-1]

#         for i in range(1, n):
#             pref_mul[i] = pref_mul[i-1]*nums[i]
#             suff_mul[n-i-1] = suff_mul[n-i]*nums[n-i-1]

#         for i in range(n):
#             if i == 0:
#                 res[0] = suff_mul[1]
#             elif i == n-1:
#                 res[n-1] = pref_mul[n-2]
#             else:
#                 res[i] = pref_mul[i-1]*suff_mul[i+1]
        
#         return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        left = 1

        for i in range(n):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res