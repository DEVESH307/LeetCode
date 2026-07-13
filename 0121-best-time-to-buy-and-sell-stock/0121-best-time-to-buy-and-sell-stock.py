class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for i, val in enumerate(prices):
            min_so_far = min(min_so_far, val)
            max_profit = max(max_profit, val - min_so_far)

        return max_profit
        