class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]

            left = max(first_start, second_start)
            right = min(first_end, second_end)

            if left <= right:
                res.append([left, right])

            if first_end < second_end:
                i += 1
            else:
                j += 1

        return res