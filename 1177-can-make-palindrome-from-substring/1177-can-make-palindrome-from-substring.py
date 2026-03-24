# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         n = len(s)

#         # frefix freq array
#         prefix = [[0]*26 for _ in range(n+1)]

#         for i in range(n):
#             prefix[i+1] = prefix[i][:]
#             prefix[i+1][ord(s[i]) - ord('a')] += 1

#         result = []

#         for left, right, k in queries:
#             odd_count = 0

#             for char in range(26):
#                 count = prefix[right+1][char] - prefix[left][char]
#                 if count % 2:
#                     odd_count += 1

#             result.append(odd_count//2 <= k)

#         return result


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)

        prefix = [0] * (n + 1)

        for i in range(n):
            bit = 1 << (ord(s[i]) - ord('a'))
            prefix[i+1] = prefix[i] ^ bit

        result = []

        for left, right, k in queries:
            mask = prefix[right+1] ^ prefix[left]
            odd_count = mask.bit_count()
            result.append(odd_count//2 <= k)

        return result
