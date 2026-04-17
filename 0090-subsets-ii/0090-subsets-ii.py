# class Solution:
# 	# @param nums : list of integers
# 	# @return a list of list of integers
# 	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         result = []

#         def dfs(start, path):
#             if start == n:
#                 result.append(path[:])
#                 return

#             path.append(nums[start])
#             dfs(start + 1, path)
#             path.pop()

#             next_index = start + 1
#             while next_index < n and nums[next_index] == nums[start]:
#                 next_index += 1
#             dfs(next_index, path)

#         dfs(0, [])
#         result.sort()
#         return result


# class Solution:
# 	# @param nums : list of integers
# 	# @return a list of list of integers
# 	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         result = []

#         def dfs(start, path):
#             result.append(path[:])  # capture at every step

#             for i in range(start, n):
#                 if i > start and nums[i-1] == nums[i]:
#                     continue
#                 path.append(nums[i])
#                 dfs(i + 1, path)
#                 path.pop()

#         dfs(0, [])
#         return result


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = set()

        def dfs(start, path):
            res.add(tuple(path))  # already sorted because nums is sorted
            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        # convert to sorted list of lists
        return sorted([list(x) for x in res])