# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#         min_heap  = []

#          # push first element of each row
#         for i in range(n):
#             heapq.heappush(min_heap , (matrix[i][0], i, 0))

#         # pop B-1 elements
#         for _ in range(k-1):
#             min_val, i, j = heapq.heappop(min_heap )
#             if j + 1 < m:
#                 heapq.heappush(min_heap , (matrix[i][j+1], i, j+1))

#         min_val, i, j = heapq.heappop(min_heap )
#         return min_val


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])

        def count_leq(mid):
            i, j = n - 1, 0
            cnt = 0

            while i >= 0 and j < m:
                if matrix[i][j] <= mid:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1

            return cnt

        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo

