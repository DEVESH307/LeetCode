class Solution:
    def atMost(self, nums, k):
        freq = {}
        n = len(nums)
        i = 0
        ans = 0

        for j in range(n):
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while len(freq) > k:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1

            ans += j-i+1

        return ans


    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
        