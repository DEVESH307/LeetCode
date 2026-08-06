class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            prod = 1
            while num:
                prod *= num%10
                num //= 10

            return prod

        num = n
        while True:
            prod = digit_product(num)
            if prod == 0 or prod % t == 0:
                return num
            num += 1