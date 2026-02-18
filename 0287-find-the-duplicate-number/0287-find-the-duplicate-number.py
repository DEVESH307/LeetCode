# class Solution:
#     def findDuplicate(self, nums):
#         left = 1
#         right = len(nums) - 1
        
#         while left < right:
#             mid = (left + right) // 2
#             count = 0
            
#             for num in nums:
#                 if num <= mid:
#                     count += 1
            
#             if count > mid:
#                 right = mid
#             else:
#                 left = mid + 1
        
#         return left


# class Solution:
#     def findDuplicate(self, nums):
#         n = len(nums) - 1
#         duplicate = 0
        
#         # Assume 32-bit integers
#         for bit in range(32):
#             bit_mask = 1 << bit
#             count_nums = 0
#             count_range = 0
            
#             # count bits in nums
#             for num in nums:
#                 if num & bit_mask:
#                     count_nums += 1
            
#             # count bits in 1..n
#             for i in range(1, n + 1):
#                 if i & bit_mask:
#                     count_range += 1
            
#             # if extra count, that bit belongs to duplicate
#             if count_nums > count_range:
#                 duplicate |= bit_mask
        
#         return duplicate


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        