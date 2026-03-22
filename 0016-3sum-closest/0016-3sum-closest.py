class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # update closest_ans
                if abs(total - target) < abs(closest_ans - target):
                    closest_ans = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest_ans