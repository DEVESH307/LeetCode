# class NumArray:

#     def __init__(self, nums):
#         self.nums = nums
#         n = len(nums)
#         self.ps = [0]*(n+1)

#         for i in range(n):
#             self.ps[i+1] = self.ps[i] + nums[i]

#     def update(self, index, val):
#         diff = val - self.nums[index]
#         self.nums[index] = val

#         for i in range(index+1, len(self.ps)):
#             self.ps[i] += diff

#     def sumRange(self, left, right):
#         return self.ps[right+1] - self.ps[left]


class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0]*(self.n+1)
        self.arr = nums[:]

        for i in range(self.n):
            self._add(i+1, nums[i])

    def _add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, index, val):
        diff = val - self.arr[index]
        self.arr[index] = val
        self._add(index+1, diff)

    def sumRange(self, left, right):
        return self._sum(right+1) - self._sum(left)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)