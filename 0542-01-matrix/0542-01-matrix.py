from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = deque()

        # Step 1: initialize
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1   # mark unvisited

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == -1:
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))

        return mat