# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         def scan(arr):
#             curr_prod = 1
#             max_prod = float("-inf")

#             for num in arr:
#                 curr_prod *= num
#                 max_prod = max(max_prod, curr_prod)

#                 if num == 0:
#                     curr_prod = 1

#             return max_prod

#         return max(scan(nums), scan(nums[::-1]))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = max_prod = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            max_prod = max(max_prod, curr_max)

        return max_prod