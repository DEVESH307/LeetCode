class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        curr_sum = 0
        max_window = -1

        left = 0
        for right in range(n):
            curr_sum += nums[right]

            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                curr_window = right - left + 1
                max_window = max(max_window, curr_window)

        return -1 if max_window == -1 else n - max_window


        