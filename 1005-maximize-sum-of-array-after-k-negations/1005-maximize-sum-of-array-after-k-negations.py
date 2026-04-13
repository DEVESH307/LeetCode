import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        min_heap = nums[:]
        heapq.heapify(min_heap)

        for _ in range(k):
            min_val = heapq.heappop(min_heap)
            heapq.heappush(min_heap, -min_val)

        return sum(min_heap)