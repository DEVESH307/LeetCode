class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        B = sorted((val, i) for i, val in enumerate(nums))

        max_j = B[-1][1]
        ans = 0

        for val, idx in reversed(B):
            ans = max(ans, max_j - idx)
            max_j = max(max_j, idx)

        return ans
        