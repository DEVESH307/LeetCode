import heapq

# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         n = len(arr)
#         min_heap = []
#         # heapq.heapify(min_heap)

#         for i in range(n-1, 0, -1):
#             for j in range(i):
#                 heapq.heappush(min_heap, (arr[j]/arr[i], j , i))

#         Bth, j, i = heapq.nsmallest(k, min_heap)[-1]

#         return [arr[j], arr[i]]
        

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # push 1st fraction of each denominator
        for i in range(1, n):
            heapq.heappush(min_heap, (arr[0]/arr[i], 0, i))

        # pop k-1 smallest
        for _ in range(k-1):
            _, j, i = heapq.heappop(min_heap)
            if j + 1 < i:
                heapq.heappush(min_heap, (arr[j+1]/arr[i], j+1, i))

        _, j, i = heapq.heappop(min_heap)
        return [arr[j], arr[i]]