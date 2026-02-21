# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         n = len(s)
#         m = len(p)
#         res = []
#         target = sorted(p)

#         for i in range(n-m+1):
#             if sorted(s[i:i+m]) == target:
#                 res.append(i)

#         return res
            

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         n = len(s)
#         m = len(p)
#         if m > n: return []
        
#         res = []
        
#         p_count = [0]*26
#         window = [0]*26

#         # build freq of p
#         for ch in p:
#             p_count[ord(ch) - ord('a')] += 1

#         # first window
#         for i in range(m):
#             window[ord(s[i]) - ord('a')] += 1

#         if window == p_count:
#             res.append(0)

#         # slide window
#         for i in range(1, n-m+1):
#             window[ord(s[i-1]) - ord('a')] -= 1
#             window[ord(s[i+m-1]) - ord('a')] += 1

#             if window == p_count:
#                 res.append(i)

#         return res


# class Solution:
#     def findAnagrams(self, s: str, p: str):

#         n, m = len(s), len(p)
#         if m > n:
#             return []

#         result = []

#         p_count = [0] * 26
#         window = [0] * 26

#         # frequency of pattern
#         for ch in p:
#             p_count[ord(ch) - ord('a')] += 1

#         left = 0

#         for right in range(n):
#             # include current character
#             window[ord(s[right]) - ord('a')] += 1

#             # maintain window size = m
#             if right - left + 1 > m:
#                 window[ord(s[left]) - ord('a')] -= 1
#                 left += 1

#             # check anagram
#             if window == p_count:
#                 result.append(left)

#         return result


class Solution:
    def findAnagrams(self, s: str, p: str):
        n, m = len(s), len(p)
        if m > n:
            return []

        res = []

        p_freq = {}
        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0) + 1

        window = {}
        # build first window
        for i in range(m):
            window[s[i]] = window.get(s[i], 0) + 1

        if window == p_freq:
            res.append(0)

        # slide window
        for i in range(m, n):
            window[s[i]] = window.get(s[i], 0) + 1

            left_char = s[i - m]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == p_freq:
                res.append(i - m + 1)

        return res
