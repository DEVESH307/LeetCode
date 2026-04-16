# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # nums.sort()
#         n = len(nums)
#         result = []

#         for i in range(1<<n):
#             subset = []
#             for j in range(n):
#                 if i & (1 << j):
#                     subset.append(nums[j])

#             result.append(subset)

#         # result.sort()
#         return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        n = len(nums)
        result = []

        def dfs(curr_idx, curr_list):
            if curr_idx == n:
                result.append(curr_list[:])
                return

            curr_list.append(nums[curr_idx])
            dfs(curr_idx + 1, curr_list)
            curr_list.pop()
            dfs(curr_idx + 1, curr_list)            

        dfs(0, [])
        # result.sort()
        return result

