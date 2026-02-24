class Solution:
    def fastPow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1.0
        
        halfPow = self.fastPow(x, n//2)

        if n % 2 == 0:
            return halfPow * halfPow
        else:
            return halfPow * halfPow * x


    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        return self.fastPow(x, n)

