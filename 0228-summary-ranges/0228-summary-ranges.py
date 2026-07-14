class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        n = len(nums)
        start = end = nums[0]
        res = []

        for i in range(1, n):
            if end + 1 == nums[i]:
                end = nums[i]
            else:            
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                    
                start = nums[i]
                end = nums[i]

        if start == end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))

        return res