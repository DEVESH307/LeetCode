from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        
        while mn != 0:
            temp = mx
            mx = mn
            mn = temp % mn
        return mx
        # return gcd(mx, mn)