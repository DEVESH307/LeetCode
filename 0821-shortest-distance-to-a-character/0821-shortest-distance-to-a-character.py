# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         res = [0]*n

#         i = 0
#         prev = float('-inf') # previous c index

#         for j in range(n):
#             if s[j] == c:
#                 while i <= j:
#                     res[i] = min(j - i, i - prev)
#                     i += 1
#                 prev = j
        
#         # remaining characters after last c
#         while i < n:
#             res[i] = i - prev
#             i += 1

#         return res
        

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [n] * n

        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev

        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)

        return res
