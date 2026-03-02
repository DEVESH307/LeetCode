# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0

#         left_max = [0] * n
#         right_max = [0] * n

#         left_max[0] = height[0]
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], height[i])

#         right_max[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])

#         water = 0
#         for i, ht in enumerate(height):
#             water += max(0, min(left_max[i], right_max[i]) - ht)

#         return water
        

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water

