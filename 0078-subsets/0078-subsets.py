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


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # nums.sort()
#         n = len(nums)
#         result = []

#         def dfs(index, path):
#             if index == n:
#                 result.append(path[:])
#                 return

#             path.append(nums[index])
#             dfs(index + 1, path)
#             path.pop()
#             dfs(index + 1, path)            

#         dfs(0, [])
#         # result.sort()
#         return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            result.append(path[:])  # capture at every step

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return result
