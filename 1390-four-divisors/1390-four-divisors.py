# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         def is_prime(x):
#             if x < 2:
#                 return False
#             i = 2
#             while i * i <= x:
#                 if x % i == 0:
#                     return False
#                 i += 1
#             return True

#         ans = 0

#         for num in nums:

#             # Case 2: num = p^3
#             p = round(num ** (1/3))
#             if p**3 == num and is_prime(p):
#                 ans += 1 + p + p*p + p*p*p
#                 continue

#             # Case 1: num = p*q
#             i = 2
#             while i * i <= num:
#                 if num % i == 0:
#                     j = num // i
#                     if i != j and is_prime(i) and is_prime(j):
#                         ans += 1 + i + j + num
#                     break
#                 i += 1

#         return ans
        

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_div_sum(n):
            count = 0
            total = 0

            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    j = n // i

                    if i == j:
                        count += 1
                        total += i
                    else:
                        count += 2
                        total += i + j

                    if count > 4:
                        return 0

            return total if count == 4 else 0

        ans = 0
        for num in nums:
            ans += four_div_sum(num)

        return ans
