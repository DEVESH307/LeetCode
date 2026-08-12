class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        curr_len = 0
        max_len = 0

        j = 0
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            curr_len += 1
            # print(freq)
            # if freq[num] > k:
            while freq[num] > k:
                freq[nums[j]] -= 1
                curr_len -= 1
                if freq[nums[j]] == 0:
                    del freq[nums[j]]
                j += 1
            # print(freq)
            max_len = max(max_len, curr_len)
            # print(curr_len)
            # print(max_len)

        return max_len