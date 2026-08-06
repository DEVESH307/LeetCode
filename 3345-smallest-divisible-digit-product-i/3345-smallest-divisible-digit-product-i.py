class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            while num:
                product *= num%10
                num //= 10

            return product

        num = n
        while True:
            product = digit_product(num)
            if product % t == 0:
                return num
            num += 1