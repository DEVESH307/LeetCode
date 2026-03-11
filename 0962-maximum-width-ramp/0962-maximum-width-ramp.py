# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         B = sorted((val, i) for i, val in enumerate(nums))

#         max_j = B[-1][1]
#         ans = 0

#         for val, idx in reversed(B):
#             ans = max(ans, max_j - idx)
#             max_j = max(max_j, idx)

#         return ans
        

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        LMin = [0] * n
        RMax = [0] * n

        LMin[0] = nums[0]
        for i in range(1, n):
            LMin[i] = min(LMin[i-1], nums[i])

        RMax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            RMax[i] = max(RMax[i+1], nums[i])

        i = j = 0
        max_gap = 0

        while i < n and j < n:
            if LMin[i] <= RMax[j]:
                max_gap = max(max_gap, j-i)
                j += 1
            else:
                i += 1

        return max_gap

