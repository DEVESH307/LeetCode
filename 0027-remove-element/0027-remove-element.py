class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        # print(nums)
        return i
        