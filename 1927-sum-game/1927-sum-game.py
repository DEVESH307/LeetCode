class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n >> 1
        qL = qR = 0
        diff = 0

        for i, x in enumerate(num):
            if i < half:
                if x == '?':
                    qL += 1
                else:
                    diff += int(x)
            else:
                if x == '?':
                    qR += 1
                else:
                    diff -= int(x)

        # Odd number of '?' → Alice always wins
        if (qR + qL) & 1:
            return True

        # Even number of '?' → Alice wins unless the difference is exactly compensable by the imbalance of '?'
        return diff != 9 * (qR - qL) >> 1