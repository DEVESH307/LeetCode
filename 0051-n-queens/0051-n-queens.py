# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         board = [['.']*n for _ in range(n)]
#         result = []

#         def is_safe(board, row, col):
#             # check column
#             for i in range(row):
#                 if board[i][col] == 'Q':
#                     return False

#             # upper-left diagonal
#             i, j = row-1, col-1
#             while i >= 0 and j >= 0:
#                 if board[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j -= 1
            
#             # upper-right diagonal
#             i, j = row-1, col+1
#             while i >= 0 and j < n:
#                 if board[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j += 1

#             return True


#         def dfs(row):
#             if row == n:
#                 result.append(["".join(r) for r in board])
#                 return
            
#             for col in range(n):
#                 if not is_safe(board, row, col):  
#                     continue
                    
#                 board[row][col] = 'Q'
#                 dfs(row + 1)
#                 board[row][col] = '.'

#         dfs(0)
#         return result


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        cols = set() # columns
        diag1 = set() # (row - col)
        diag2 = set() # (row + col)

        board = [['.']*n for _ in range(n)]

        def is_safe(row, col):
            if col in cols:
                return False
            if (row - col) in diag1:
                return False
            if (row + col) in diag2:
                return False
            return True

        def dfs(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if not is_safe(row, col):
                    continue

                # place
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                dfs(row + 1)

                # undo
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        dfs(0)
        return result