# # SELECTION SORT
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         for i in range(n):
#             # min_elem = nums[i]
#             min_idx = i
#             for j in range(i+1, n):
#                 if nums[j] < nums[min_idx]:
#                     # min_elem = nums[j]
#                     min_idx = j

#             nums[i], nums[min_idx] = nums[min_idx], nums[i]

#         return nums


# # BUBBLE SORT
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         for i in range(n):
#             swap = 0
#             for j in range(n-i-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#                     swap += 1
#             if swap == 0:
#                 break

#         return nums


# Merge SORT
class Solution:
    # merge two sorted section within array
    def merge(self, arr, left, mid, right):
        i, j = left, mid
        temp = []

        while i < mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # remaining elements
        temp.extend(arr[i:mid]) 
        temp.extend(arr[j:right+1])

        # copy back to original array
        arr[left: right+1] = temp 

        return arr

    # merge sort
    def mergeSort(self, arr, left, right):
        if left >= right:
            return

        mid = (left+right)//2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid+1, right)
        self.merge(arr, left, mid+1, right)


    # main function
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums