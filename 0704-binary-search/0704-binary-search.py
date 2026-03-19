# class Solution:
#     def binarySearch(self, arr, left, right, target):
#         if left > right:
#             return -1

#         mid = (left+right)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return self.binarySearch(arr, mid+1, right, target)
#         else:
#             return self.binarySearch(arr, left, mid-1, target)

#     def search(self, nums: List[int], target: int) -> int:
#         return self.binarySearch(nums, 0, len(nums)-1, target)
        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1