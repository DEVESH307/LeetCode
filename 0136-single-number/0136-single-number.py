class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=nums[0]
        for i in range(len(nums)-1):
            num=num^nums[i+1]
        return num

        