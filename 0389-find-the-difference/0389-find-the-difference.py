# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         s = sorted(s)
#         t = sorted(t)

#         for i in range(len(s)):
#             if s[i] != t[i]:
#                 return t[i]

#         return t[-1]


# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         freq = {}

#         for ch in s:
#             freq[ch] = freq.get(ch, 0) + 1

#         for ch in t:
#             if ch not in freq or freq[ch] == 0:
#                 return ch
#             freq[ch] -= 1


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0

        for ch in s:
            xor ^= ord(ch)

        for ch in t:
            xor ^= ord(ch)

        return chr(xor)