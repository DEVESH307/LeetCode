# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         freq = {}
#         n = len(nums)

#         for i in range(min(k + 1, len(nums))):
#             if freq.get(nums[i], 0) > 0:
#                 return True

#             freq[nums[i]] = freq.get(nums[i], 0) + 1

#         for i in range(k+1, n):
#             freq[nums[i-k-1]] = freq.get(nums[i-k-1], 0) - 1
#             if freq[nums[i-k-1]] == 0:
#                 del freq[nums[i-k-1]]

#             if freq.get(nums[i], 0) > 0:
#                 return True
            
#             freq[nums[i]] = freq.get(nums[i], 0) + 1

#         return False


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])

            if num in window:
                return True

            window.add(num)

        return False
