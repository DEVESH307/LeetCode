class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        res = []

        for curr_start, curr_end in intervals[1:]:
            if end < curr_start:
                res.append([start, end])
                start, end = curr_start, curr_end
            else:
                # start = min(start, curr_start)
                end = max(end, curr_end)

        res.append([start, end])
        return res

        