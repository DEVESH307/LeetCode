class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        
        reversed_x = sign * int(str(abs(x))[::-1])

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x