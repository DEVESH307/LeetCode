# class Solution:
#     def missingMultiple(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         nums.sort()
#         # ans = k
#         count = 1

#         for num in nums:
#             if num % k == 0:
#                 if num // k == count:
#                     count += 1
#                 else:
#                     return count * k

#         return count * k
        

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = [False] * 101

        for x in nums:
            seen[x] = True

        x = k
        while x <= 100 and seen[x]:
            x += k

        return x