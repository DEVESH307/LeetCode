# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         ans = -1

#         # -------- 1. Find pivot --------
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2

#             if nums[mid] >= nums[0]:
#                 left = mid + 1
#             else:
#                 right = mid

#         pivot = left
        
#         # -------- 2. Choose search space --------
#         if target >= nums[pivot] and target <= nums[n-1]:
#             left, right = pivot, n-1
#         else:
#             left, right = 0, pivot-1

#          # -------- 3. Standard binary search --------
#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 ans = mid
#                 break
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return ans


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # mid in left half
            if nums[mid] >= nums[0]:
                if target >= nums[0] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # mid in right half
            else:
                if target < nums[0] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1