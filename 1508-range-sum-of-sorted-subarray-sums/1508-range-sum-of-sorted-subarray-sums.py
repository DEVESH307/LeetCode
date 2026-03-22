class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        subarr_sum = []
        
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                subarr_sum.append(total)

        subarr_sum.sort()
        return sum(subarr_sum[left-1:right]) % MOD