# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         left = right = -1

#         for i in range(n-1):
#             if nums[i+1] < nums[i]:
#                 left = i
#                 break
        
#         if left == -1:
#             return 0

#         for i in range(n-1, 0, -1):
#             if nums[i-1] > nums[i]:
#                 right = i
#                 break
        
#         min_elem = max_elem = nums[left]
#         for i in range(left, right+1):
#             min_elem = min(min_elem, nums[i])
#             max_elem = max(max_elem, nums[i])


#         min_pos, max_pos = left, right
#         for i in range(n):
#             if nums[i] > min_elem:
#                 min_pos = i
#                 break
        
#         for i in range(n-1, -1, -1):
#             if nums[i] < max_elem:
#                 max_pos = i
#                 break

#         return max_pos - min_pos + 1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_seen = float('-inf')
        min_seen = float('inf')

        left = -1
        right = -1

        # left → right
        for i in range(n):
            if nums[i] >= max_seen:
                max_seen = nums[i]
            else:
                right = i

        # right → left
        for i in range(n - 1, -1, -1):
            if nums[i] <= min_seen:
                min_seen = nums[i]
            else:
                left = i

        if right == -1:
            return 0

        return right - left + 1