# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)

#         for i in range(k):
#             # max_elem = nums[i]
#             max_idx = i
#             for j in range(i+1, n):
#                 if nums[j] > nums[max_idx]:
#                     # max_elem = nums[j]
#                     max_idx = j

#             nums[i], nums[max_idx] = nums[max_idx], nums[i]

#         return nums[k-1]


# import random
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k -= 1  # 0-based index for kth largest

#     def partition(left, right):
#         pivot_index = random.randint(left, right)
#         nums[left], nums[pivot_index] = nums[pivot_index], nums[left]

#         pivot = nums[left]
#         p1 = left + 1
#         p2 = right

#         while p1 <= p2:
#             if nums[p1] >= pivot:
#                 p1 += 1
#             elif nums[p2] < pivot:
#                 p2 -= 1
#             else:
#                 nums[p1], nums[p2] = nums[p2], nums[p1]
#                 p1 += 1
#                 p2 -= 1

#         nums[left], nums[p2] = nums[p2], nums[left]
#         return p2

#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             pivot_index = partition(left, right)

#             if pivot_index == k:
#                 return nums[pivot_index]
#             elif pivot_index > k:
#                 right = pivot_index - 1
#             else:
#                 left = pivot_index + 1


# import random
# class Solution:
#     def findKthLargest(self, nums, k):
#         k -= 1  # 0-based index

#         def partition(left, right):
#             pivot = nums[random.randint(left, right)]

#             p1 = left      # > pivot region
#             i = left       # current
#             p2 = right     # < pivot region

#             while i <= p2:
#                 if nums[i] > pivot:
#                     nums[i], nums[p1] = nums[p1], nums[i]
#                     p1 += 1
#                     i += 1
#                 elif nums[i] < pivot:
#                     nums[i], nums[p2] = nums[p2], nums[i]
#                     p2 -= 1
#                 else:
#                     i += 1

#             return p1, p2  # equal range

#         left = 0
#         right = len(nums) - 1

#         while True:
#             start, end = partition(left, right)

#             if k < start:
#                 right = start - 1
#             elif k > end:
#                 left = end + 1
#             else:
#                 return nums[k]


class Solution:
    def check(self, nums, k, target):
        count = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                count += 1
        return count >= k

    def findKthLargest(self, nums, k):
        left, right = min(nums), max(nums)
        ans = 0

        while left <= right:
            mid = (left+right)//2

            if self.check(nums, k, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
