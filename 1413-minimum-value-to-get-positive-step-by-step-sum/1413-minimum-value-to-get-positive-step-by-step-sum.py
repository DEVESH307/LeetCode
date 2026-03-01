class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = 0
        min_ps = 0

        for num in nums:
            ps += num
            min_ps = min(min_ps, ps)

        return 1 if min_ps > 0 else abs(min_ps-1)
        