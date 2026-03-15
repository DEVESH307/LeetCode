from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # frequency of each number
        freq = [0] * (max_val + 1)
        for val in nums:
            freq[val] += 1

        # count numbers divisible by each g
        div_count = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                div_count[g] += freq[multiple]

        # count pairs with exact gcd = g
        gcd_pairs = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            pairs = div_count[g] * (div_count[g] - 1) // 2

            multiple = 2 * g
            while multiple <= max_val:
                pairs -= gcd_pairs[multiple]
                multiple += g

            gcd_pairs[g] = pairs

        # build prefix distribution of gcd values
        gcd_values = []
        prefix = []
        running = 0

        for g in range(1, max_val + 1):
            if gcd_pairs[g] > 0:
                running += gcd_pairs[g]
                gcd_values.append(g)
                prefix.append(running - 1)

        # answer queries
        result = []
        for q in queries:
            idx = bisect_left(prefix, q)
            result.append(gcd_values[idx])

        return result