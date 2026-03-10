class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        count_1 = s.count('1')
        count_0 = 0
        # print(count_1)
        curr_sum = 0
        max_sum = 0

        for i in range(n-1):
            if s[i] == '0':
                count_0 += 1
            
            if s[i] == '1':
                count_1 -= 1

            curr_sum = count_0 + count_1
            max_sum = max(max_sum, curr_sum)

        return max_sum

        