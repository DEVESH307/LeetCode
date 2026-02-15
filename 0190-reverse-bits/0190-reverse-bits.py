class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        for i in range(32):
            ans <<= 1
            if n & (1<<i):
                ans |= 1
            
        return ans

        