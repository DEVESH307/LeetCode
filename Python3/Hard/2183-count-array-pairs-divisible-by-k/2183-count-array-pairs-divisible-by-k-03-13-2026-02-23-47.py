from math import gcd

class Solution:
    def countPairs(self, nums, k):
        count_gcd = {}
        ans = 0

        for num in nums:
            curr_gcd = gcd(num, k)

            for prev_gcd in count_gcd:
                if (curr_gcd * prev_gcd) % k == 0:
                    ans += count_gcd[prev_gcd]

            count_gcd[curr_gcd] = count_gcd.get(curr_gcd, 0) + 1

        return ans