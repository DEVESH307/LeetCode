class Solution:
    def nearestSmallerOnLeft(self, arr):
        n = len(arr)
        stack = []
        result = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(i)

        return result


    def nearestSmallerOnRight(self, arr):
        n = len(arr)
        stack = []
        result = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]
                
            stack.append(i)

        return result


    def nearestGreaterOnLeft(self, arr):
        n = len(arr)
        stack = []
        result = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(i)

        return result


    def nearestGreaterOnRight(self, arr):
        n = len(arr)
        stack = []
        result = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(i)

        return result


    def subArrayRanges(self, nums: List[int]) -> int:
        NSL = self.nearestSmallerOnLeft(nums)
        NSR = self.nearestSmallerOnRight(nums)
        NGL = self.nearestGreaterOnLeft(nums)
        NGR = self.nearestGreaterOnRight(nums)

        total = 0
        for i, num in enumerate(nums):
            mx = (i - NGL[i]) * (NGR[i] - i) * num
            mn = (i - NSL[i]) * (NSR[i] - i) * num
            total += mx-mn

        return total