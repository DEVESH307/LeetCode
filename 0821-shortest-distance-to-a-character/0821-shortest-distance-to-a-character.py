class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0]*n

        i = 0
        j = 0
        prev = float('-inf') # previous c index

        while j < n:
            if s[j] != c:
                j += 1
            else:
                while i <= j:
                    res[i] = min(j - i, i - prev)
                    i += 1
                prev = j
                j += 1
        
        # remaining characters after last c
        while i < n:
            res[i] = i - prev
            i += 1

        return res
        