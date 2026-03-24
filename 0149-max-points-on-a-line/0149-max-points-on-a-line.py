from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1

            for j in range(i+1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # normalize sign
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                slopes[(dx, dy)] += 1

            max_line = max(slopes.values(), default=0)
            ans = max(ans, max_line + duplicates)

        return ans