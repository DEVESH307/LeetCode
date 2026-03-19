# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left , right = 0, len(nums)-1
#         left_index = -1
#         while left <= right:
#             mid = (left+right)//2

#             if nums[mid] == target:
#                 left_index = mid
#                 right = mid - 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         left , right = 0, len(nums)-1
#         right_index = -1
#         while left <= right:
#             mid = (left+right)//2

#             if nums[mid] == target:
#                 right_index = mid
#                 left = mid + 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
#         return [left_index, right_index]
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(bound):
            left , right = 0, len(nums)-1
            index = -1
            while left <= right:
                mid = (left+right)//2

                if nums[mid] == target:
                    index = mid
                    if bound == "left":
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        return [find("left"), find("right")]        