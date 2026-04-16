# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda x: x[0])
#         prevEnd = intervals[0][1]
#         ans = 0

#         for start, end in intervals[1:]:
#             if start >= prevEnd:
#                 prevEnd = end
#             else:
#                 ans += 1
#                 prevEnd = min(prevEnd, end)

#         return ans
         

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end time
        
        count = 0
        last_end = float('-inf')
        
        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
        
        return len(intervals) - count