# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums[:] = sorted(list(set(nums)))
#         return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        i = 0
        for j in range(n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1