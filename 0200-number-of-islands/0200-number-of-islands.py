# import sys
# sys.setrecursionlimit(10**6)
# from collections import defaultdict, deque

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         n, m = len(grid), len(grid[0])
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

#         def dfs(r, c):
#             if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "0":
#                 return

#             grid[r][c] = "0"
#             for dr, dc in directions:
#                 nr, nc = r+dr, c+dc
#                 dfs(nr, nc)
        
#         island = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     island += 1

#         return island        



from collections import defaultdict, deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))
        
        island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    island += 1

        return island