class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = set()
        pairs = set()

        for i, num in enumerate(nums):
            if num - k in seen:
                pairs.add((num - k, num))

            if num + k in seen:
                pairs.add((num, num + k))

            seen.add(num)

        return len(pairs)
