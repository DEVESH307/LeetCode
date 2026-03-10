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