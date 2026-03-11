class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        n = len(matrix)
        m = len(matrix[0])
        ans = float('-inf')

        for top in range(n):

            col_sum = [0] * m

            for bottom in range(top, n):

                for c in range(m):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                sorted_prefix = [0]

                for val in col_sum:

                    prefix += val

                    idx = bisect.bisect_left(sorted_prefix, prefix - k)

                    if idx < len(sorted_prefix):
                        ans = max(ans, prefix - sorted_prefix[idx])

                    bisect.insort(sorted_prefix, prefix)

        return ans