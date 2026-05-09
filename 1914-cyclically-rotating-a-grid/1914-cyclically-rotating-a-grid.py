class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            elems = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            # top row
            for j in range(left, right + 1):
                elems.append(grid[top][j])

            # right column
            for i in range(top + 1, bottom):
                elems.append(grid[i][right])

            # bottom row
            for j in range(right, left - 1, -1):
                elems.append(grid[bottom][j])

            # left column
            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])

            # rotate
            rot = k % len(elems)
            elems = elems[rot:] + elems[:rot]

            idx = 0

            # put back top
            for j in range(left, right + 1):
                grid[top][j] = elems[idx]
                idx += 1

            # put back right
            for i in range(top + 1, bottom):
                grid[i][right] = elems[idx]
                idx += 1

            # put back bottom
            for j in range(right, left - 1, -1):
                grid[bottom][j] = elems[idx]
                idx += 1

            # put back left
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elems[idx]
                idx += 1

        return grid