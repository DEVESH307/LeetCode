class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni_start, ni_end = newInterval
        result = []
        inserted = False

        for start, end in intervals:
            if end < ni_start:
                result.append([start, end])
            elif start > ni_end:
                if not inserted:
                    result.append([ni_start, ni_end])
                    inserted = True
                result.append([start, end])
            else:
                ni_start = min(ni_start, start)
                ni_end = max(ni_end, end)

        if not inserted:
            result.append([ni_start, ni_end])

        return result