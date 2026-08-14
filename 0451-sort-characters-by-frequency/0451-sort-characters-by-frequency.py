import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

        max_heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(max_heap)

        res = []
        while max_heap:
            neg_val, key = heapq.heappop(max_heap)
            res.append(-neg_val * key)

        print(res)
        return "".join(res)