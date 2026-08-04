class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = 0

        while left < right:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                ans += 1
                left += 1
                right -= 1
            elif nums[left] != 0:
                left += 1
            elif nums[right] == 0:
                right -= 1

        return ans