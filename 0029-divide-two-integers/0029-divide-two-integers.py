class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # 32-bit overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # determine sign
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                quotient += (1 << i)
        
        if negative:
            quotient = -quotient
        
        return quotient