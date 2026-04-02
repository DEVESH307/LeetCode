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


    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        NSL = self.nearestSmallerOnLeft(arr)
        NSR = self.nearestSmallerOnRight(arr)

        total = 0
        for i, num in enumerate(arr):
            mn = (i - NSL[i]) * (NSR[i] - i) * num
            total += mn

        return total % MOD        