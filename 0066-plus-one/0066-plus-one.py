class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        while len(digits) > 1 and digits[0] == 0:
            digits.pop(0)

        if not digits:
            return [1]

        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits