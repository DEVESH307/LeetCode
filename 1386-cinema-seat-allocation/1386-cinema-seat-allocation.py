from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)

        for row, seat in reservedSeats:
            reserved[row].add(seat)

        ans = (n - len(reserved)) * 2

        for seats in reserved.values():
            left = all(x not in seats for x in range(2, 6))
            middle = all(x not in seats for x in range(4, 8))
            right = all(x not in seats for x in range(6, 10))

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans