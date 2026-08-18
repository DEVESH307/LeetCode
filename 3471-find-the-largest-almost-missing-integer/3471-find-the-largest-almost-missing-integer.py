# from collections import defaultdict

# class Solution(object):
#     def largestInteger(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n = len(nums)
#         count = defaultdict(int)

#         for i in range(n-k+1):
#             seen = set(nums[i:i+k])
#             for x in seen:
#                 count[x] += 1

#         ans = -1
#         for x in count:
#             if count[x] == 1:
#                 ans = max(ans, x)

#         return ans


from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        freq = Counter(nums)

        if k == n:
            return max(nums)

        if k == 1:
            ans = -1
            for x in freq:
                if freq[x] == 1:
                    ans = max(ans, x)
            return ans

        ans = -1
        if freq[nums[0]] == 1:
            ans = nums[0]

        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans