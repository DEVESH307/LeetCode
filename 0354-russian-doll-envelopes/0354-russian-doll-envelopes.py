# class Solution:
#     def lis(self, A):
#         n = len(A)
#         if n == 0:
#             return 0

#         dp = [1] * n
#         max_len = 1

#         for i in range(1, n):
#             curr = 1
#             for j in range(i):
#                 if A[j] < A[i]:
#                     curr = max(curr, dp[j] + 1)

#             dp[i] = curr
#             max_len = max(max_len, dp[i])

#         return max_len

#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         # Step 1: Sort (CRITICAL)
#         envelopes.sort(key=lambda x: (x[0], -x[1]))

#         # Step 2: Extract widths
#         widths = [w for h, w in envelopes]

#         # Step 3: Apply your LIS
#         return self.lis(widths)
        

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort properly
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract widths
        widths = [w for h, w in envelopes]
        
        # Step 3: LIS (O(N log N))
        lis = []
        
        for w in widths:
            idx = bisect_left(lis, w)
            if idx == len(lis):
                lis.append(w)
            else:
                lis[idx] = w
        
        return len(lis)