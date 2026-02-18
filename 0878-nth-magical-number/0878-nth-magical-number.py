from math import gcd
MOD = 10**9+7
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = a*b//gcd(a,b)
        left = 1
        right = n*min(a, b)

        while left < right:
            mid = (left+right)//2

            count = mid//a + mid//b - mid//lcm

            if count < n:
                left = mid+1
            else:
                right = mid

        return left%MOD