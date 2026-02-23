class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        window_sum = 0
        ans = 0
        left = 0

        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            window_sum += val

            # window size == k
            if right-left+1 > k:
                remove = nums[left]
                freq[remove] -= 1
                if freq[remove] == 0:
                    del freq[remove]
                window_sum -= remove
                left += 1

            # valid distinct window
            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, window_sum)   

        return ans
            


        