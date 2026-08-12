class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans