class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n+1

        for i, num in enumerate(nums):
            num = abs(nums[i])
            if num < n+1:
                nums[num-1] = -1 * abs(nums[num-1])

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1   

        return n + 1        