class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        n = len(A)
        C = [0] * (n)

        for i in range(n):
            prev = 0 if i == 0 else C[i-1]
            freq[A[i]] = freq.get(A[i], 0) + 1
            if freq[A[i]] > 1:
                C[i] += 1

            freq[B[i]] = freq.get(B[i], 0) + 1
            if freq[B[i]] > 1:
                C[i] += 1

            C[i] += prev

        return C
                