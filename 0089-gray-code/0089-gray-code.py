class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        newseq = []
        seq = self.grayCode(n-1)

        for i in range(len(seq)):
            newseq.append(seq[i])

        for i in range(len(seq)-1, -1, -1):
            newseq.append((1 << (n-1)) + seq[i])

        return newseq
  