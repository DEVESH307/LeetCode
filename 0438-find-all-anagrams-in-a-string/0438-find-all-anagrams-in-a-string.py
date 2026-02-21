class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        target = sorted(p)

        for i in range(n-m+1):
            if sorted(s[i:i+m]) == target:
                res.append(i)

        return res
            