# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
#         count = 0

#         for i in range(1, n + 1):
#             if n % i == 0:
#                 count += 1
#                 if count == k:
#                     return i

#         return -1

        
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                small.append(i)
                if i != n//i:
                    large.append(n//i)

        factors = small + large[::-1]

        return -1 if k > len(factors) else factors[k - 1]