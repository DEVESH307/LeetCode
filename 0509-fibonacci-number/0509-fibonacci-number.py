class Solution:
    def fib(self, n: int) -> int:
        F0 = 0
        F1 = 1

        if n == 0: return 0
        if n == 1: return 1

        for i in range(2, n+1):
            Fi = F0 + F1
            F0 = F1
            F1 = Fi

        return Fi
        