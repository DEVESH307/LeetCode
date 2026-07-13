# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix_prod = [1] * n
#         suffix_prod = [1] * n
#         prefix_prod[0] = nums[0]
#         suffix_prod[n-1] = nums[n-1]

#         for i in range(1, n):
#             prefix_prod[i] = prefix_prod[i-1] * nums[i]

#         for i in range(n-2, -1, -1):
#             suffix_prod[i] = suffix_prod[i+1] * nums[i]    

#         ans = []
#         for i in range(len(nums)):
#             if i == 0:
#                 ans.append(suffix_prod[1])
#             elif i == n-1:
#                 ans.append(prefix_prod[n-2])
#             else:
#                 ans.append(prefix_prod[i-1] * suffix_prod[i+1])
        
#         return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]