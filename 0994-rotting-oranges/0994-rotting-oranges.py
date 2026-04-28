# from collections import deque

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         directions = [
#             (1, 0),   # down
#             (-1, 0),  # up
#             (0, 1),   # right
#             (0, -1)   # left
#         ]


#         queue = deque()
#         fresh = 0

#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 2:
#                     queue.append((i, j, 0))
#                 elif grid[i][j] == 1:
#                     fresh += 1

#         max_time = 0
#         while queue:
#             x, y, t = queue.popleft()
#             max_time = max(max_time, t)

#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
#                     grid[nx][ny] = 2
#                     fresh -= 1
#                     queue.append((nx, ny, t + 1))


#         return max_time if fresh == 0 else -1


from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque()
        fresh = 0

        # initialize
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if not fresh:
            return 0
        if not queue:
            return -1

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):  # process one level
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))

            time += 1

        return time if fresh == 0 else -1