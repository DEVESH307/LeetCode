class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for val in arr:
            freq[val] = freq.get(val, 0) + 1

        # for key, val in freq.items():
        if len(freq.values()) != len(set(freq.values())):
            return False
        return True