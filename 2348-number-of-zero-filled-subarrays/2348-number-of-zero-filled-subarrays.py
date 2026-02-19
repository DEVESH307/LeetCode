class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_count = 0
        total_count = 0

        for num in nums:
            if num == 0:
                curr_count += 1
                total_count += curr_count
            else:
                curr_count = 0

        return total_count
