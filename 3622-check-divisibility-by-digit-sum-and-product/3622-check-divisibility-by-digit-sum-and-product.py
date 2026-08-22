class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        num = n
        while num:
            rem = num % 10
            digit_sum += rem
            digit_prod *= rem
            num //= 10
        
        total = digit_sum + digit_prod
        return not n % total