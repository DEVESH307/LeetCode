class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        max_val = max(nums)

        # smallest prime factor sieve
        spf = list(range(max_val + 1))

        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i


        primes = set()

        for num in nums:
            while num > 1:
                p = spf[num]
                primes.add(p)
                while num % p == 0:
                    num //= p

        return len(primes)        