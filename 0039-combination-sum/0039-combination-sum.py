# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # candidates.sort()
#         # candidates = sorted(set(candidates))
#         n = len(candidates)
#         result = []

#         def dfs(start, path, total):
#             if total > target or start == n:
#                 return
#             if total == target:
#                 result.append(sorted(path[:]))
#                 return

#             path.append(candidates[start])
#             dfs(start, path, total + candidates[start])
#             path.pop()
#             dfs(start + 1, path, total)

#         dfs(0, [], 0)
#         # result.sort()
#         return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(set(candidates))
        n = len(candidates)
        result = []

        def dfs(start, path, total):
            if total > target:
                return
            if total == target:
                result.append(path[:])
                return

            for i in range(start, n):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)
        result.sort()
        return result