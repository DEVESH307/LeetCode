class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.ps = [0] * (n+1)
        
        for i in range(n):
            self.ps[i+1] = self.ps[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right+1] - self.ps[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)