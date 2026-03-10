class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_value = max(nums)

        # Sum of sequence: max_value + (max_value+1) + ... + (max_value+k-1)
        total_sum = max_value * k + (k * (k - 1)) // 2

        return total_sum
        