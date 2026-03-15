class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if num < 2:
                return False

            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True

        n = len(nums)
        prime = [isPrime(num) for num in nums]
        
        first = last = -1

        for i in range(n):
            if prime[i]:
                first = i
                break

        for i in range(n-1, -1, -1):
            if prime[i]:
                last = i
                break

        return last-first