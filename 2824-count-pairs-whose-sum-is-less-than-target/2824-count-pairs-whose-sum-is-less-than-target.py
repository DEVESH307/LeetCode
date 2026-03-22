# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         ans = 0

#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] < target:
#                     ans += 1
#         return ans


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum < target:
                ans += (right - left)
                left += 1
            else:
                right -= 1

        return ans