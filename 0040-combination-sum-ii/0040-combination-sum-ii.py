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