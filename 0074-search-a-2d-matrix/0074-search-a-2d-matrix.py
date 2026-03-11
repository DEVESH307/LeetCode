class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_left, bisect_right

        first_col = [row[0] for row in matrix]
        row_idx = bisect_right(first_col, target) - 1

        if row_idx < 0:
            return False

        col_idx = bisect_left(matrix[row_idx], target)

        if col_idx < len(matrix[0]) and matrix[row_idx][col_idx] == target:
            return True

        return False


        