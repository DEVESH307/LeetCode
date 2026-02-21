class Solution:
    def minDeletions(self, s: str) -> int:
        n = len(s)
        freq = [0]*26
        
        for ch in s:
            freq[ord(ch)-ord('a')] += 1

        freq.sort(reverse=True)

        used = set()
        ans = 0

        for i in range(26):
            while freq[i] > 0 and freq[i] in used:
                freq[i] -= 1
                ans += 1

            used.add(freq[i])

        return ans
