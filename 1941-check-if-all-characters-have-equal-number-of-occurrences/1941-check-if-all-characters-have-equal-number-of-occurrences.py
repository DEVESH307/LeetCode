class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n = len(s)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        count = freq[s[0]]
        for key, value in freq.items():
            if value != count:
                return False
            
        return True
