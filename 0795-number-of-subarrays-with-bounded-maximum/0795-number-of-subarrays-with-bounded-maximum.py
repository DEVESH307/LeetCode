# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#         def count(bound):
#             ans = 0
#             length = 0

#             for num in nums:
#                 if num <= bound:
#                     length += 1
#                 else:
#                     length = 0

#                 ans += length

#             return ans

#         return count(right) - count(left-1)


# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#         ans = 0
#         last_valid = -1
#         last_invalid = -1

#         for i, num in enumerate(nums):
#             if num > right:
#                 last_invalid = i

#             if left <= num <= right:
#                 last_valid = i

#             ans += max(0, last_valid-last_invalid)

#         return ans


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        count = 0
        last_invalid = -1

        for i, num in enumerate(nums):
            if num > right:
                last_invalid = i
                count = 0

            if left <= num <= right:
                count = i - last_invalid

            ans += count            

        return ans