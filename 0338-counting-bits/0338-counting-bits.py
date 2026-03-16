# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         no_set_bits = 0
#         while n:
#             no_set_bits += 1
#             n = n & n - 1

#         return no_set_bits

#     def countBits(self, n: int) -> List[int]:
#         return [self.hammingWeight(num) for num in range(n+1)]
        

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         def bits(x):
#             if x == 0:
#                 return 0
            
#             offset = 1
#             while offset * 2 <= x:
#                 offset *= 2
            
#             return 1 + bits(x - offset)

#         return [bits(i) for i in range(n + 1)]


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp
