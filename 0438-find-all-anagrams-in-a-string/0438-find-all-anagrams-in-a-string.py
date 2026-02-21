# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         n = len(s)
#         m = len(p)
#         res = []
#         target = sorted(p)

#         for i in range(n-m+1):
#             if sorted(s[i:i+m]) == target:
#                 res.append(i)

#         return res
            

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m > n: return []
        
        res = []
        
        p_count = [0]*26
        window = [0]*26

        # build freq of p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        # first window
        for i in range(m):
            window[ord(s[i]) - ord('a')] += 1

        if window == p_count:
            res.append(0)

        # slide window
        for i in range(1, n-m+1):
            window[ord(s[i-1]) - ord('a')] -= 1
            window[ord(s[i+m-1]) - ord('a')] += 1

            if window == p_count:
                res.append(i)

        return res