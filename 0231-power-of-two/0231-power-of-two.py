# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#        if n <= 0:
#            return False
#         pow2 = 1
#         while pow2 <= n:
#             if pow2 == n:
#                 return True 
#             pow2 <<= 1

#         return False
        

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False

#         while n % 2 == 0:
#             n //= 2

#         return n == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0