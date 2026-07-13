# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix = [1] * n
#         suffix = [1] * n
#         prefix[0] = nums[0]
#         suffix[n-1] = nums[n-1]

#         for i in range(1, n):
#             prefix[i] = prefix[i-1] * nums[i]

#         for i in range(n-2, -1, -1):
#             suffix[i] = suffix[i+1] * nums[i]    

#         ans = []
#         for i in range(len(nums)):
#             if i == 0:
#                 ans.append(suffix[1])
#             elif i == n-1:
#                 ans.append(prefix[n-2])
#             else:
#                 ans.append(prefix[i-1] * suffix[i+1])
        
#         return ans


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix = [1] * n
#         suffix = [1] * n
#         ans = [1] * n

#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]

#         for i in range(n - 2, -1, -1):
#             suffix[i] = suffix[i + 1] * nums[i + 1]

#         for i in range(n):
#             ans[i] = prefix[i] * suffix[i]

#         return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(1, n):
            prefix = prefix * nums[i - 1]
            ans[i] = prefix

        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix

        return ans