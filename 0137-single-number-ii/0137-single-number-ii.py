class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            count_ith_bit = 0
            for j in nums:
                if j & (1 << i):
                    count_ith_bit += 1

            if count_ith_bit % 3 != 0:
                ans |= (1 << i)

        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans
        