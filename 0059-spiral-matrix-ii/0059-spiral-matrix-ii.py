class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        right = n-1
        bottom = n-1
        left = 0
        val = 0
        
        res = [[0]*n for _ in range(n)]

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                val += 1
                res[top][i] = val
            top += 1

            for i in range(top, bottom+1):
                val += 1
                res[i][right] = val
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    val += 1
                    res[bottom][i] = val
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    val += 1
                    res[i][left] = val
                left += 1

        return res
