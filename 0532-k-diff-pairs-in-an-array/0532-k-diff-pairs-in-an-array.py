# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         seen = set()
#         pairs = set()

#         for i, num in enumerate(nums):
#             if num - k in seen:
#                 pairs.add((num - k, num))

#             if num + k in seen:
#                 pairs.add((num, num + k))

#             seen.add(num)

#         return len(pairs)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        seen = set()
        pairs = set()

        for num in nums:
            if num - k in seen:
                pairs.add(num - k)

            if num + k in seen:
                pairs.add(num)

            seen.add(num)

        return len(pairs)
