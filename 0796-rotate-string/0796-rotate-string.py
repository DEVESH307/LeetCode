class Solution:
    def compute_lps(self, s):
        n = len(s)
        LPS = [0] * n

        for i in range(1, n):
            x = LPS[i-1]

            while x > 0 and s[i] != s[x]:
                x = LPS[x-1]

            if s[i] == s[x]:
                x += 1

            LPS[i] = x 

        return LPS


    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)
        ans = 0
        string = s + '$' + goal + goal
        LPS = self.compute_lps(string)

        for i in range(len(LPS)):
            if LPS[i] == n:
                return True
        return False
