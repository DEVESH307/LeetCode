# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
        
#         for x in range(n + 1):
#             idx = bisect.bisect_left(nums, x)
#             count = n - idx
            
#             if count == x:
#                 return x
        
#         return -1


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            x = n-i

            # check if exactly x elements >= x
            if nums[i] >= x and (i==0 or nums[i-1] < x):
                return x
            
        return -1

