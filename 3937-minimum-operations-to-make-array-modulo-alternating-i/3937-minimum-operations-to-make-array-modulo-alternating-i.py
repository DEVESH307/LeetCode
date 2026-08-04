class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ans = float('inf')
        
        for x in range(k):
            for y in range(k):
                # 1. Enforce distinct condition
                if x == y:
                    continue
                    
                count = 0
                for i, num in enumerate(nums):
                    remainder = num % k
                    
                    if i % 2 == 0:
                        # 2. Find the minimum steps to change remainder to x
                        diff = abs(x - remainder)
                        count += min(diff, k - diff)
                    else:
                        # 2. Find the minimum steps to change remainder to y
                        diff = abs(y - remainder)
                        count += min(diff, k - diff)
                        
                ans = min(ans, count)

        return ans
