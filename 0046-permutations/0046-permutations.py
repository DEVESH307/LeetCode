# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = []

#         def dfs(index):
#             if index == n:
#                 result.append(nums[:])
#                 return

#             for i in range(index, n):
#                 nums[index], nums[i] = nums[i], nums[index]
#                 dfs(index + 1)
#                 nums[i], nums[index] = nums[index], nums[i]

#         dfs(0)
#         return result        


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return result