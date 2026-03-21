class Solution:
    def check(self, position, m, d):
        last_pos = position[0]
        ball_placed = 1

        for i in range(1, len(position)):
            if position[i] - last_pos >= d:
                last_pos = position[i]
                ball_placed += 1
            if ball_placed == m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        left, right = 1, position[n-1]-position[0]
        ans = 0

        while left <= right:
            mid = (left+right)//2

            if self.check(position, m, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        