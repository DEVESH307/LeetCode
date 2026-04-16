# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         # candidates = sorted(set(candidates))
#         candidates.sort()
#         n = len(candidates)
#         result = []

#         def dfs(start, path, total):
#             if total == target:
#                 result.append(path[:])
#                 return
#             if total > target or start == n:
#                 return

#             path.append(candidates[start])
#             dfs(start + 1, path, total + candidates[start])
#             path.pop()

#             # skip duplicates while excluding
#             next_index = start + 1
#             while next_index < n and candidates[next_index] == candidates[start]:
#                 next_index += 1

#             dfs(next_index, path, total)

#         dfs(0, [], 0)
#         return result


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = sorted(set(candidates))
        candidates.sort()
        n = len(candidates)
        result = []

        def dfs(start, path, total):
            if total > target:
                return
            if total == target:
                result.append(path[:])
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)
        result.sort()
        return result