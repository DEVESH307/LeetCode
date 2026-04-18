# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
        
#         def is_valid(r, c, val):
#             # row + col validity
#             for i in range(9):
#                 if board[r][i] == val or board[i][c] == val:
#                     return False

#             # box validity
#             br, bc = (r//3)*3, (c//3)*3
#             for i in range(br, br+3):
#                 for j in range(bc, bc+3):
#                     if board[i][j] == val:
#                         return False

#             return True

#         def dfs(r, c):
#             if r == 9:
#                 return True
            
#             if c == 9:
#                 return dfs(r+1, 0)

#             if board[r][c] != '.':
#                 return dfs(r, c+1)

#             for i in range(1, 10):
#                 val = str (i)
#                 if is_valid(r, c, val):
#                     board[r][c] = val

#                     if dfs(r, c+1):
#                         return True
                    
#                     board[r][c] = '.'

#             return False

#         dfs(0, 0)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # initialize
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + (c//3)].add(val)

        def dfs(i):
            if i == len(empty):
                return True

            r, c = empty[i]
            b = (r//3)*3 + (c//3)

            for val in '123456789':
                if val not in rows[r] and val not in cols[c] and val not in boxes[b]:

                    # place
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)

                    if dfs(i + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[b].remove(val)

            return False

        dfs(0)