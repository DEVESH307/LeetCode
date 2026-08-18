import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)

            if largest != second_largest:
                heapq.heappush(max_heap, -(largest - second_largest))

        return -max_heap[0] if max_heap else 0