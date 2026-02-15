# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         cnt_good_pairs = 0

#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j]:
#                     cnt_good_pairs += 1

#         return cnt_good_pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt_good_pairs = 0
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for val in freq.values():
            if val > 1:
                cnt_good_pairs += (val * (val-1))//2

        return cnt_good_pairs