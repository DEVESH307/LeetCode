# from collections import defaultdict

# class Solution:
#     def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#         reserved = defaultdict(set)

#         for row, seat in reservedSeats:
#             reserved[row].add(seat)

#         ans = (n - len(reserved)) * 2

#         for seats in reserved.values():
#             left = all(x not in seats for x in range(2, 6))
#             middle = all(x not in seats for x in range(4, 8))
#             right = all(x not in seats for x in range(6, 10))

#             if left and right:
#                 ans += 2
#             elif left or middle or right:
#                 ans += 1

#         return ans


from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(int)

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= 1 << (seat - 2)

        LEFT  = 0b00001111
        MID   = 0b00111100
        RIGHT = 0b11110000

        ans = (n - len(rows)) * 2

        for mask in rows.values():

            left = (mask & LEFT) == 0
            mid = (mask & MID) == 0
            right = (mask & RIGHT) == 0

            if left and right:
                ans += 2
            elif left or mid or right:
                ans += 1

        return ans