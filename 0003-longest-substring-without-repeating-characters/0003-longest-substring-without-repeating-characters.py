# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = [0] * 256   # ASCII
#         left = 0
#         max_len = 0

#         for right in range(len(s)):
#             while seen[ord(s[right])] == 1:
#                 seen[ord(s[left])] = 0
#                 left += 1

#             seen[ord(s[right])] = 1
#             max_len = max(max_len, right - left + 1)

#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len