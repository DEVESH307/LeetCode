class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        # print(prefix_sum)
        seen = set(nums)
        num = prefix_sum[-1]
        # print(num)
        while True:
            if num not in seen:
                return num
            num += 1
        