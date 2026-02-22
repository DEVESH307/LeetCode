class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        n, m = len(a), len(b)

        freqA = [0] * 26
        freqB = [0] * 26

        for ch in a:
            freqA[ord(ch) - 97] += 1

        for ch in b:
            freqB[ord(ch) - 97] += 1

        # build prefix sums separately
        preA = freqA[:]
        preB = freqB[:]

        for i in range(1, 26):
            preA[i] += preA[i - 1]
            preB[i] += preB[i - 1]

        ans = float('inf')

        # Condition 1 & 2
        for i in range(25):

            # all chars in a < b
            ans = min(ans, (n - preA[i]) + preB[i])

            # all chars in b < a
            ans = min(ans, (m - preB[i]) + preA[i])

        # Condition 3 (IMPORTANT FIX)
        for i in range(26):
            ans = min(ans, n + m - freqA[i] - freqB[i])

        return ans
