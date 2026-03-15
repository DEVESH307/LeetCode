class Solution:
    def largestPrime(self, n: int) -> int:
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False

        ans = 0
        total = 0
        for i in range(2, n+1):
            if not prime[i]:
                continue

            total += i

            if total > n:
                break

            if prime[total]:
                ans = total

        return ans