# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        
#         return []
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        idx_map = {}
        
        for i in range(n):
            complement = target - nums[i]
            if complement in idx_map:
                res.extend([idx_map[complement], i])
                break
            else:
                idx_map[nums[i]] = i

        return res