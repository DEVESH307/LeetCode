# class Solution:
#     def waysToMakeFair(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 0
#         even_ps = [0]*(n+1)
#         odd_ps = [0]*(n+1)

#         for i in range(n):
#             even_ps[i+1] = even_ps[i]
#             odd_ps[i+1] = odd_ps[i]

#             if i & 1:
#                 odd_ps[i+1] += nums[i]
#             else:
#                 even_ps[i+1] += nums[i]

        
#         for i in range(1, n+1):
#             left_even = even_ps[i-1]
#             left_odd = odd_ps[i-1]

#             right_even = even_ps[n] - even_ps[i]
#             right_odd = odd_ps[n] - odd_ps[i]

#             new_even = left_even + right_odd
#             new_odd = left_odd + right_even

#             if new_even == new_odd:
#                 ans += 1

#         return ans

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        total_even = 0
        total_odd = 0

        for i in range(n):
            if i & 1:
                total_odd += nums[i]
            else:
                total_even += nums[i]

        left_even = 0
        left_odd = 0

        for i in range(n):
            if i & 1:
                total_odd -= nums[i]
            else:
                total_even -= nums[i]

            new_even = left_even + total_odd
            new_odd = left_odd + total_even

            if new_even == new_odd:
                ans += 1

            if i & 1:
                left_odd += nums[i]
            else:
                left_even += nums[i]

        return ans