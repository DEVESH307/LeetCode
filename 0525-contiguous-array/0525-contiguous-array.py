# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         ps = [0]*(n+1)
#         max_len = 0
#         curr_len = 0
#         first_index = {}

#         for i in range(n+1):
#             val = 1 if nums[i-1] == 1 else -1
#             ps[i] = ps[i-1] + val


#         for i in range(n+1):
#             if ps[i] not in first_index :
#                 first_index [ps[i]] = i
#             else:
#                 max_len = max(max_len, i-first_index [ps[i]])
                   
#         return max_len


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = 0
        first_index = {0: -1} # imp trick
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

            else:
                max_len = max(max_len, i-first_index[prefix_sum])     
                   
        return max_len