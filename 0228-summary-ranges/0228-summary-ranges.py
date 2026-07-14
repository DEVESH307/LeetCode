# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         if not nums:
#             return []

#         n = len(nums)
#         start = end = nums[0]
#         res = []

#         for i in range(1, n):
#             if end + 1 == nums[i]:
#                 end = nums[i]
#             else:            
#                 if start == end:
#                     res.append(str(start))
#                 else:
#                     res.append(str(start)+"->"+str(end))
                    
#                 start = nums[i]
#                 end = nums[i]

#         if start == end:
#             res.append(str(start))
#         else:
#             res.append(str(start)+"->"+str(end))

#         return res


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i = 0

        while i < n:
            start = nums[i]

            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")

            i += 1

        return res