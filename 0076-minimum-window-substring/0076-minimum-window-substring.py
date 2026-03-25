from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)          # required frequencies
        window = defaultdict(int)  # current window frequencies

        required = len(need)       # number of unique chars needed
        formed = 0                 # how many chars satisfied

        left = 0
        start = 0
        min_len = float('inf')

        for right, ch in enumerate(s):
            window[ch] += 1

            # if this char is satisfied exactly
            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            # try shrinking window
            while formed == required:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    start = left

                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[start:start+min_len]