class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        # candidates = sorted(set(candidates))
        n = len(candidates)
        result = []

        def dfs(index, path, total):
            if total > target or index == n:
                return
            if total == target:
                result.append(sorted(path[:]))
                return

            path.append(candidates[index])
            dfs(index, path, total + candidates[index])
            path.pop()
            dfs(index + 1, path, total)

        dfs(0, [], 0)
        # result.sort()
        return result