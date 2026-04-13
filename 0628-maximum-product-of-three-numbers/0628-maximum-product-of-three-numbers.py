# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         return max(
#         nums[-1] * nums[-2] * nums[-3],
#         nums[0] * nums[1] * nums[-1]
#         )


from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for x in nums:
            # update max
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

            # update min
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return max(max1*max2*max3, min1*min2*max1)