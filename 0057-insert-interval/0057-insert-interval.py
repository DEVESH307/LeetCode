# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         ni_start, ni_end = newInterval
#         res = []

#         for i, (start, end) in enumerate(intervals):
#             if end < ni_start:
#                 res.append([start, end])

#             elif start > ni_end:
#                 res.append([ni_start, ni_end])

#                 # Append the remaining intervals
#                 for j in range(i, len(intervals)):
#                     res.append(intervals[j])

#                 return res

#             else:
#                 ni_start = min(ni_start, start)
#                 ni_end = max(ni_end, end)

#         # newInterval belongs at the end
#         res.append([ni_start, ni_end])
#         return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni_start, ni_end = newInterval
        res = []
        inserted = False

        for start, end in intervals:
            if end < ni_start:
                res.append([start, end])
            elif start > ni_end:
                if not inserted:
                    res.append([ni_start, ni_end])
                    inserted = True
                res.append([start, end])
            else:
                ni_start = min(ni_start, start)
                ni_end = max(ni_end, end)

        if not inserted:
            res.append([ni_start, ni_end])

        return res