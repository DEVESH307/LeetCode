class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for row in range(numRows):
            temp = []
            for col in range(row+1):
                if row == col or col == 0:
                    temp.append(1)
                else:
                    temp.append(res[row-1][col-1] + res[row-1][col])

            res.append(temp)

        return res
            
        