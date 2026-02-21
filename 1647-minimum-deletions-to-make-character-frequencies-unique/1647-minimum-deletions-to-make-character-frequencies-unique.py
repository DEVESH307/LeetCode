# # class Solution:
# #     def minDeletions(self, s: str) -> int:
# #         n = len(s)
# #         freq = [0]*26
        
# #         for ch in s:
# #             freq[ord(ch)-ord('a')] += 1

# #         freq.sort(reverse=True)

# #         used = set()
# #         ans = 0

# #         for i in range(26):
# #             while freq[i] > 0 and freq[i] in used:
# #                 freq[i] -= 1
# #                 ans += 1

# #             used.add(freq[i])

# #         return ans


# class Solution:
#     def minDeletions(self, s: str) -> int:
#         n = len(s)
#         freq = [0]*26
        
#         for ch in s:
#             freq[ord(ch)-ord('a')] += 1

#         freq.sort(reverse=True)

#         used = set()
#         ans = 0

#         for i in range(26):
#             while freq[i] > 0 and freq[i] in used:
#                 freq[i] -= 1
#                 ans += 1

#             used.add(freq[i])

#         return ans


class Solution:
    def minDeletions(self, s: str) -> int:
        n = len(s)
        freq = [0]*26
        
        for ch in s:
            freq[ord(ch)-ord('a')] += 1

        freq.sort(reverse=True)

        deletions = 0
        max_allowed = float('inf')

        for f in freq:
            if f == 0:
                break

            if f >= max_allowed:
                new_freq = max(0, max_allowed-1)
                deletions += f - new_freq
                f = new_freq

            max_allowed = f

        return deletions