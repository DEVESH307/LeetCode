class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ans_row = 0
        one_cnt = 0
        max_cnt = 0

        for i in range(n):
            one_cnt = mat[i].count(1)
            if one_cnt > max_cnt:
                max_cnt = one_cnt
                ans_row = i

        return [ans_row, max_cnt]

        