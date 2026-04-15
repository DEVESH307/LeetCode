import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap, min_heap = [], []
        delayed = defaultdict(int)
        max_size = min_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is max_heap else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal max_size, min_size

            if max_size > min_size + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                max_size -= 1
                min_size += 1
                prune(max_heap)
            elif max_size < min_size:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                max_size += 1
                min_size -= 1
                prune(min_heap)

        def get_median():
            if k % 2:
                return float(-max_heap[0])
            return (-max_heap[0] + min_heap[0]) / 2

        # initialize
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            max_size += 1

        for _ in range(k//2):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            max_size -= 1
            min_size += 1

        res = [get_median()]

        # sliding window
        for i in range(k, len(nums)):
            num_in = nums[i]
            num_out = nums[i-k]

            # add
            if num_in <= -max_heap[0]:
                heapq.heappush(max_heap, -num_in)
                max_size += 1
            else:
                heapq.heappush(min_heap, num_in)
                min_size += 1

            # remove (lazy)
            delayed[num_out] += 1
            if num_out <= -max_heap[0]:
                max_size -= 1
                if num_out == -max_heap[0]:
                    prune(max_heap)
            else:
                min_size -= 1
                if min_heap and num_out == min_heap[0]:
                    prune(min_heap)

            balance()
            res.append(get_median())

        return res