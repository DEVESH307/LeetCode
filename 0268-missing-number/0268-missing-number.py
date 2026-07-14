class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for num in nums:
            ans ^= num

        for i in range(n+1):
            ans ^= i

        return ans
        