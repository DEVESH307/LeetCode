# class Solution:
#     def sumDigits(self, num):
#         if num < 10: return num
        
#         return num%10 + self.sumDigits(num//10)

#     def maxSumOfSquares(self, num: int, sum: int) -> str:
#         maxNum = (10**num)-1
#         minNum = 10**(num-1)

#         for val in range(maxNum, minNum-1, -1):
#             if self.sumDigits(val) == sum:
#                 return str(val)

#         return ""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum <= 0:
            return ""

        res = []
        for _ in range(num):
            digit = min(9, sum)
            res.append(str(digit))
            sum -= digit

        return "".join(res)


        