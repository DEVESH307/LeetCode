# class Solution:
#     def isprimes(self, num):
#         if num < 2: return False

#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False

#         return True


#     def countprimess(self, n: int) -> int:
#         ans = 0

#         for num in range(n):
#             if self.isprimes(num):
#                 ans += 1

#         return ans
        

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        prime = [True] * (n)
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False

        return sum(prime)