# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num < 10:
#             return num

#         digit_sum = 0
#         while num:
#             digit_sum += num % 10
#             num //= 10

#         return self.addDigits(digit_sum)
        

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0
        return 1 + (num-1)%9