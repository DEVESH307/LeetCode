# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)

#         if nums[0] != nums[1]:
#             return nums[0]
#         if nums[n-1] != nums[n-2]:
#             return nums[n-1]

#         left, right = 0, len(nums)-1
#         while left <= right:
#             if left == right:
#                 return nums[left]
                
#             mid = (left+right)//2
#             if mid % 2 == 0:
#                 if nums[mid] == nums[mid+1]:
#                     left = mid + 2
#                 else:
#                     right = mid
#             else:
#                 if nums[mid] == nums[mid-1]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

            
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         left, right = 0, len(nums)-1

#         while left <= right:
#             if left == right:
#                 return nums[left]
                
#             mid = (left+right)//2
#             if mid % 2 == 0:
#                 if nums[mid] == nums[mid+1]:
#                     left = mid + 2
#                 else:
#                     right = mid
#             else:
#                 if nums[mid] == nums[mid-1]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return nums[left]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # force mid to be even
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]