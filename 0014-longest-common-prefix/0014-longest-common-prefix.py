class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        m = len(strs[0])

        res = ""
        if m == 0:
            return res

        for j in range(m):
            isQualified = True
            for i in range(1, n):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    isQualified = False
                    break

            if isQualified:
                res += strs[0][j]
            else:
                break

        return res
