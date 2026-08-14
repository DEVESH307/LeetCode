class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        max_len = 0
        left = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            while freq[ch] > 2:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            
        return max_len