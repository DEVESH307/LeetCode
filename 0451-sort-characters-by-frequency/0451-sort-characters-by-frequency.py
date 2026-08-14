
# from collections import Counter

# class Solution:
#     def frequencySort(self, s: str) -> str:
#         freq = Counter(s)

#         buckets = [[] for _ in range(len(s) + 1)]

#         for ch, count in freq.items():
#             buckets[count].append(ch)

#         result = []

#         for count in range(len(s), 0, -1):
#             for ch in buckets[count]:
#                 result.append(ch * count)

#         return "".join(result)


import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        max_heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(max_heap)

        result = []

        while max_heap:
            count, ch = heapq.heappop(max_heap)
            result.append(ch * (-count))

        return "".join(result)

