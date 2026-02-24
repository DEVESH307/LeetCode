class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow2 = 1
        while pow2 <= n:
            if pow2 == n:
                return True 
            pow2 <<= 1

        return False
        