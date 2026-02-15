class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            num_i = start + 2*i
            ans ^= num_i

        return ans

        