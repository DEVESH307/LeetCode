class Solution:
    # @param A : list of list of integers
    # @return an integer
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
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]
                
            stack.append(i)

        return result
        
    def largestRectangleArea(self, A):
        NSL = self.nearestSmallerOnLeft(A)
        NSR = self.nearestSmallerOnRight(A)
        max_area = float('-inf')

        for i, ht in enumerate(A):
            wd = (NSR[i] - NSL[i] - 1)
            area = ht * wd
            max_area = max(max_area, area)

        return max_area


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            curr_area = self.largestRectangleArea(heights)
            max_area = max(max_area, curr_area)

        return max_area
        