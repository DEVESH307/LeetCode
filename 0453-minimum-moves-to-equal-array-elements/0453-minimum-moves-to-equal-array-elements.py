# class Solution:
#     def minMoves(self, nums: List[int]) -> int:
#         mn = min(nums)
#         ans = 0

#         for num in nums:
#             ans += num - mn

#         return ans

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        total = 0
        mn = float('inf')

        for num in nums:
            total += num

            if num < mn:
                mn = num
            
        return total - n*mn
