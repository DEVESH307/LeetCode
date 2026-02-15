
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        n = len(mat)
        m = len(mat[0])
        
        res = []
        row = col = 0
        direction = 1

        for _ in range(n*m):
            res.append(mat[row][col])
            
            if direction == 1:  # moving up-right
                if col == m-1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else: # moving down-left
                if row == n-1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return res
