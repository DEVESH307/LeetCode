# class MedianFinder:

#     def __init__(self):
#         self.max_heap = []  # left (max heap using negatives)
#         self.min_heap = []  # right (min heap)        

#     def addNum(self, num: int) -> None:
#         # push to max heap
#         heapq.heappush(self.max_heap, -num)

#         # move largest of left to right
#         heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

#         # rebalance sizes
#         if len(self.min_heap) > len(self.max_heap):
#             heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

#     def findMedian(self) -> float:
#         if len(self.max_heap) > len(self.min_heap):
#             return -self.max_heap[0]

#         return (-self.max_heap[0] + self.min_heap[0]) / 2
        

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return

        median = self.findMedian()

        if num >= median:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        # rebalance
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()