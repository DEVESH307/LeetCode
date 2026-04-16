class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def dfs(index):
            if index == n:
                result.append(nums[:])
                return
            used = set()
            for i in range(index, n):
                if nums[i] in used:
                    continue
                used.add(nums[i])

                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(0)
        return result                