class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False

        result = []
        for i in range(2, n//2+1):
            if prime[i] and prime[n-i]:
                result.append([i, n-i])

        return result 