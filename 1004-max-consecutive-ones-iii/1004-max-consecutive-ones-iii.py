class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = 0
        zero_cnt = 0
        max_len = 0

        for right in range(n):
            if nums[right] == 0:
                zero_cnt += 1

            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

            window_size = right-left+1
            max_len = max(max_len, window_size)
        
        return max_len