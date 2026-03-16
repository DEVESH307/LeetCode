class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = [-1] * 10
        ans = -1

        for num in nums:
            temp = num
            max_digit = 0

            while temp > 0:
                digit = temp % 10
                if digit > max_digit:
                    max_digit = digit
                temp //= 10

            if best[max_digit] != -1:
                ans = max(ans, best[max_digit] + num)

            best[max_digit] = max(best[max_digit], num)

        return ans