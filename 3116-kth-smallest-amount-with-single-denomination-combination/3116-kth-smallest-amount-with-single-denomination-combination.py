# class Solution:
#     def findKthSmallest(self, coins: List[int], k: int) -> int:
#         values = set()

#         for num in coins:
#             for i in range(1, k + 1):
#                 values.add(num * i)
                
#         comb = list(values)
#         comb.sort()
#         return comb[k - 1]

from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                # subset = []
                bits = 0
                curr_lcm = 1

                for i in range(n):
                    if mask & (1 << i):
                        # subset.append(coins[i])
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            break
                
                # print(subset)
                # print(bits, curr_lcm)

                if curr_lcm > x:
                    continue

                if bits % 2:
                    total += x // curr_lcm
                else:
                    total -= x // curr_lcm

            return total

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
