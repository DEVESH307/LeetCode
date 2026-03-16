class Solution:
    def hammingWeight(self, n: int) -> int:
        no_set_bits = 0
        while n:
            no_set_bits += 1
            n = n & n - 1

        return no_set_bits

    def countBits(self, n: int) -> List[int]:
        return [self.hammingWeight(num) for num in range(n+1)]
        