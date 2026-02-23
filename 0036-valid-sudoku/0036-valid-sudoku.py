# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #check rows
#         for r in range(9):
#             vis = [False]*9
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
                
#                 num = ord(board[r][c]) - ord('1')
#                 if vis[num]:
#                     return False
#                 vis[num] = True

#         # check cols
#         for c in range(9):
#             vis = [False]*9
#             for r in range(9):
#                 if board[r][c] == '.':
#                     continue

#                 num = ord(board[r][c]) - ord('1')
#                 if vis[num]:
#                     return False
#                 vis[num] = True

#         # check boxes
#         for br in range(0, 9, 3):
#             for bc in range(0, 9, 3):
#                 vis = [False]*9
#                 for r in range(br, br+3):
#                     for c in range(bc, bc+3):
#                         if board[r][c] == '.':
#                             continue
                        
#                         num = ord(board[r][c]) - ord('1')
#                         if vis[num]:
#                             return False
#                         vis[num] = True

#         return True
        

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        #check rows
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = ord(board[r][c]) - ord('1')
                b = (r//3)*3 + (c//3)

                if num in row[r] or num in col[c] or num in box[b]:
                    return False

                row[r].add(num)
                col[c].add(num)
                box[b].add(num)

        return True