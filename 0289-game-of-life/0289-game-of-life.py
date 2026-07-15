class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(m):
            for c in range(n):
                live = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 1 or board[nr][nc] == -1:
                            live += 1

                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = -1
                else:
                    if live == 3:
                        board[r][c] = 2


        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1