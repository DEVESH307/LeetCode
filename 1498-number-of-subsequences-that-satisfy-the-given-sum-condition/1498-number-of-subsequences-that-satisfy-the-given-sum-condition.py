class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        n = len(nums)       
        left = 0
        right = n-1
        ans = 0
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += 1 << (right-left)
                left += 1

        return ans % MOD