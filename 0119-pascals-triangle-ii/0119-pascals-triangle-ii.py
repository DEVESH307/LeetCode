class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []

        for row in range(rowIndex + 1):
            curr = []
            for col in range(row+1):
                if row == col or col == 0:
                    curr.append(1)
                else:
                    curr.append(prev[col-1] + prev[col])

            prev = curr

        return prev
            
        