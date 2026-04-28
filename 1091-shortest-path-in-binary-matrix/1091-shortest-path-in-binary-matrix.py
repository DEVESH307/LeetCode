from collections import defaultdict, deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
            
        if grid[0][0] == 1:
            return -1

        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        
        def bfs():
            queue = deque([((0, 0), 1)]) # (node, distance)
            grid[0][0] = 1

            while queue:
                (x, y ), dist = queue.popleft()
                if (x, y ) == (n-1, n-1):
                    return dist

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append(((nx, ny), dist + 1))

            return -1

        return bfs()