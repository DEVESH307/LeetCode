# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         result = []

#         cols = set() # columns
#         diag1 = set() # (row - col)
#         diag2 = set() # (row + col)

#         board = [['.']*n for _ in range(n)]

#         def is_safe(row, col):
#             if col in cols:
#                 return False
#             if (row - col) in diag1:
#                 return False
#             if (row + col) in diag2:
#                 return False
#             return True

#         def dfs(row):
#             if row == n:
#                 result.append(["".join(r) for r in board])
#                 return

#             for col in range(n):
#                 if not is_safe(row, col):
#                     continue

#                 # place
#                 board[row][col] = 'Q'
#                 cols.add(col)
#                 diag1.add(row - col)
#                 diag2.add(row + col)

#                 dfs(row + 1)

#                 # undo
#                 board[row][col] = '.'
#                 cols.remove(col)
#                 diag1.remove(row - col)
#                 diag2.remove(row + col)

#         dfs(0)
#         return len(result)


# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         cols = set() # columns
#         diag1 = set() # (row - col)
#         diag2 = set() # (row + col)
#         count = 0

#         def is_safe(row, col):
#             if col in cols:
#                 return False
#             if (row - col) in diag1:
#                 return False
#             if (row + col) in diag2:
#                 return False
#             return True

#         def dfs(row):
#             nonlocal count

#             if row == n:
#                 count += 1
#                 return

#             for col in range(n):
#                 if not is_safe(row, col):
#                     continue

#                 # place
#                 cols.add(col)
#                 diag1.add(row - col)
#                 diag2.add(row + col)

#                 dfs(row + 1)

#                 # undo
#                 cols.remove(col)
#                 diag1.remove(row - col)
#                 diag2.remove(row + col)

#         dfs(0)
#         return count


class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

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
                return 1  # found valid arrangement

            count = 0
            for col in range(n):
                if not is_safe(row, col):
                    continue

                # place
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                count += dfs(row + 1)

                # undo
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return dfs(0)