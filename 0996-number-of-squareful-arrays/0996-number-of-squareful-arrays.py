class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            r = isqrt(num)
            return r * r == num

        nums.sort()
        n = len(nums)
        if n <= 1: 
            return 0
        used = [False] * n
        ans = 0

        def dfs(prev, count):
            nonlocal ans
            if count == n:
                ans += 1
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i - 1]:
                    continue

                if prev != -1 and not is_square(prev + nums[i]):
                    continue

                used[i] = True
                dfs(nums[i], count + 1)
                used[i] = False

        dfs(-1, 0)
        return ans        