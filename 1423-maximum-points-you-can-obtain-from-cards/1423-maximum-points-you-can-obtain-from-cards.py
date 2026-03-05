class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # max_sum = float('-inf')
        curr_sum = 0
        for i in range(k):
            curr_sum += cardPoints[i]

        max_sum = curr_sum
        p1 = k - 1
        p2 = n-1

        while p1 >= 0:
            curr_sum -= cardPoints[p1]
            curr_sum += cardPoints[p2]
            p1 -= 1
            p2 -= 1

            max_sum = max(max_sum, curr_sum)

        return max_sum

