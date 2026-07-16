class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        start, end = intervals[0]
                            
        intervals.sort(key=lambda x: x[0])
        last_end = intervals[0][1]
        count = 0

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if last_end <= start:
                last_end = end
            else:
                count += 1
                last_end = min(last_end, end)
        
        return count