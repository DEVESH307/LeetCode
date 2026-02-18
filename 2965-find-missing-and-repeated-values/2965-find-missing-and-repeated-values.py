# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
#         n = len(grid)
#         N = n * n
        
#         sum_actual = 0
#         sq_sum_actual = 0
        
#         for row in grid:
#             for num in row:
#                 sum_actual += num
#                 sq_sum_actual += num * num
        
#         sum_expected = N * (N + 1) // 2
#         sq_sum_expected = N * (N + 1) * (2 * N + 1) // 6
        
#         diff1 = sum_actual - sum_expected          # R - M
#         diff2 = sq_sum_actual - sq_sum_expected   # R² - M²
        
#         sum_rm = diff2 // diff1                   # R + M
        
#         R = (diff1 + sum_rm) // 2
#         M = R - diff1
        
#         return [R, M]


# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
#         n = len(grid)
#         N = n * n
        
#         freq = [0] * (N + 1)
        
#         for row in grid:
#             for num in row:
#                 freq[num] += 1
        
#         repeated = missing = -1
        
#         for i in range(1, N + 1):
#             if freq[i] == 2:
#                 repeated = i
#             elif freq[i] == 0:
#                 missing = i
        
#         return [repeated, missing]


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        xor_all = 0

        for row in grid:
            for val in row:
                xor_all ^= val

        for i in range(1, n*n+1):
            xor_all ^= i

        mask = xor_all & -xor_all

        x = 0
        y = 0

        for row in grid:
            for val in row:
                if val & mask:
                    x ^= val
                else:
                    y ^= val
                
        for i in range(1, n*n+1):
            if i & mask:
                x ^= i
            else:
                y ^= i
        
        return [x, y] if sum(row.count(x) for row in grid) == 2 else [y, x]
        
