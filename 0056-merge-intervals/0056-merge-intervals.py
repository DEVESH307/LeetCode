class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        li_start, li_end = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if li_end < start:
                res.append([li_start, li_end])
                li_start = start
                li_end = end
            else:
                li_start = min(li_start, start)
                li_end = max(li_end, end)
        res.append([li_start, li_end])
        return res

        