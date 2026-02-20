# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         ps = [0]*(n+1)
#         ans = 0
#         freq = {}

#         for i in range(n):
#             ps[i+1] = ps[i] + nums[i]

#         for val in ps:
#             if val-k in freq:
#                 ans += freq[val-k]

#             freq[val] = freq.get(val, 0) + 1
        
#         return ans

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps_count = {0: 1}
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in ps_count:
                ans += ps_count[curr_sum-k]

            ps_count[curr_sum] = ps_count.get(curr_sum, 0) + 1
        
        return ans