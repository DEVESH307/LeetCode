# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = []

#         def dfs(index):
#             if index == n:
#                 result.append(nums[:])
#                 return
#             used = set()
#             for i in range(index, n):
#                 if nums[i] in used:
#                     continue
#                 used.add(nums[i])

#                 nums[index], nums[i] = nums[i], nums[index]
#                 dfs(index + 1)
#                 nums[i], nums[index] = nums[index], nums[i]

#         dfs(0)
#         return result                


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        result = []

        def dfs(path):
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                # duplicate control
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return result