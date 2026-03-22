# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         seen = set()
#         pairs = set()

#         for i, num in enumerate(nums):
#             if num - k in seen:
#                 pairs.add((num - k, num))

#             if num + k in seen:
#                 pairs.add((num, num + k))

#             seen.add(num)

#         return len(pairs)


# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k < 0:
#             return 0

#         seen = set()
#         pairs = set()

#         for num in nums:
#             if num - k in seen:
#                 pairs.add(num - k)

#             if num + k in seen:
#                 pairs.add(num)

#             seen.add(num)

#         return len(pairs)


# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
#         left = 0
#         right = 1
#         ans = 0
#         pair = set()

#         while right < n :
#             if left == right:
#                 right += 1
#                 continue

#             diff = nums[right] - nums[left]

#             if diff == k:
#                 pair.add((nums[left], nums[right]))
#                 left += 1
#                 right += 1
#             elif diff < k:
#                 right += 1
#             else:
#                 left += 1

#         return len(pair)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 1
        ans = 0

        while right < n :
            if left == right:
                right += 1
                continue

            diff = nums[right] - nums[left]

            if diff == k:
                ans += 1
                left_val = nums[left]
                right_val = nums[right]

                # skip duplicates
                while left < n and nums[left] == left_val:
                    left += 1
                while right < n and nums[right] == right_val:
                    right += 1

            elif diff < k:
                right += 1
            else:
                left += 1

        return ans

