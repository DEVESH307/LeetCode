import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)

            heapq.heappush(max_heap, -(largest - second_largest))

        return -heapq.heappop(max_heap)