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


# # INSERTION SORT
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         for i in range(1, n):
#             j = i - 1

#             while j >= 0 and nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 j -= 1

#         return nums


# # STACK SORT
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         stack1 = []
#         # stack2 = []

#         for i, num in enumerate(nums):
#             stack2 = []
#             if not stack1 or stack1[-1] <= num:
#                 stack1.append(num)
#             else:
#                 while stack1 and stack1[-1] > num:
#                     stack2.append(stack1.pop())
#                 stack1.append(num)
#                 while stack2:
#                     stack1.append(stack2.pop())

#         return stack1  


# # Merge SORT
# class Solution:
#     # merge two sorted section within array
#     def merge(self, arr, left, mid, right):
#         i, j = left, mid
#         temp = []

#         while i < mid and j <= right:
#             if arr[i] <= arr[j]:
#                 temp.append(arr[i])
#                 i += 1
#             else:
#                 temp.append(arr[j])
#                 j += 1

#         # remaining elements
#         temp.extend(arr[i:mid]) 
#         temp.extend(arr[j:right+1])

#         # copy back to original array
#         arr[left: right+1] = temp 

#         return arr

#     # merge sort
#     def mergeSort(self, arr, left, right):
#         if left >= right:
#             return

#         mid = (left+right)//2
#         self.mergeSort(arr, left, mid)
#         self.mergeSort(arr, mid+1, right)
#         self.merge(arr, left, mid+1, right)


#     # main function
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.mergeSort(nums, 0, len(nums)-1)
#         return nums      


# # QUICK SORT
# class Solution:
#     # get pivot index
#     def partition(self, arr, left, right):
#         pivot_index = left
#         pivot = arr[pivot_index]
#         p1 = left + 1
#         p2 = right

#         while p1 <= p2:
#             if arr[p1] <= pivot:
#                 p1 += 1
#             elif arr[p2] > pivot:
#                 p2 -= 1
#             else:
#                 arr[p1], arr[p2] = arr[p2], arr[p1]
#                 p1 += 1
#                 p2 -= 1

#         # pivot go to p2 not p1
#         arr[pivot_index], arr[p2] = arr[p2], arr[pivot_index]
#         return p2

#     # quick sort
#     def quickSort(self, arr, left, right):
#         if left >= right:
#             return

#         pivot_index = self.partition(arr, left, right)
#         self.quickSort(arr, left, pivot_index-1)
#         self.quickSort(arr, pivot_index+1, right)


#     # main function
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quickSort(nums, 0, len(nums)-1)
#         return nums


import random
class Solution:
    def partition(self, arr, left, right):
        # Partition the array into 3 parts:
        pivot = arr[random.randint(left, right)]

        p1 = left      # boundary for < pivot
        i = left       # current element
        p2 = right     # boundary for > pivot

        while i <= p2:
            if arr[i] < pivot:
                # move smaller element to left side
                arr[i], arr[p1] = arr[p1], arr[i]
                p1 += 1
                i += 1
            elif arr[i] > pivot:
                # move larger element to right side
                arr[i], arr[p2] = arr[p2], arr[i]
                p2 -= 1
            else:
                # element equals pivot → stay in middle
                i += 1

        return p1, p2


    def quickSort(self, arr, left, right):
        # Recursively sorts the array using 3-way QuickSort.
        if left >= right:
            return

        start, end = self.partition(arr, left, right)

        # sort elements smaller than pivot
        self.quickSort(arr, left, start - 1)

        # sort elements greater than pivot
        self.quickSort(arr, end + 1, right)


    def sortArray(self, nums):
        # main function
        self.quickSort(nums, 0, len(nums) - 1)
        return nums