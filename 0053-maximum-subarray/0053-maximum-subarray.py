class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        curr_sum = 0
        start = 0
        end = 0
        temp_start = 0

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum
                start = temp_start
                end = i

            if curr_sum < 0:
                curr_sum = 0
                temp_start = i + 1

        return max_sum
