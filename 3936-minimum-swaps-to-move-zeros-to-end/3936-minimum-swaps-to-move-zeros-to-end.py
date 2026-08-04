class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)-1
        ans = 0

        while i < j:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1
                i += 1
                j -= 1
            elif nums[i] != 0:
                i += 1
            elif nums[j] == 0:
                j -= 1

        return ans