class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1

            if nums[i] == 0 or i == n-1:
                ans = max(ans, count)
                count = 0
        
        return ans