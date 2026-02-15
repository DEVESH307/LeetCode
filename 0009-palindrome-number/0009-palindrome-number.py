# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         if x % 10 == 0 and x != 0:
#             return False
        
#         res = 0
#         while x > res:
#             res = res * 10 + x % 10
#             x //= 10
        
#         return x == res or res // 10 == x
        

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         originalNum = x
#         if (x < 0): 
#             return False
#         else:
#             revNum=0
#             while(x>0):
#                 revNum = revNum * 10 + x%10
#                 x = x//10
#             if revNum == originalNum: 
#                 return True
#             else: return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x==x[::-1]:
            return True
        else:
            return False