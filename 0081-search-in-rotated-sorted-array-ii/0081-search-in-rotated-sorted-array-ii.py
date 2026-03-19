class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        ans = False

        # -------- 1. Find pivot --------
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid

        pivot = left
        
        # -------- 2. Choose search space --------
        if target >= nums[pivot] and target <= nums[n-1]:
            left, right = pivot, n-1
        else:
            left, right = 0, pivot-1

         # -------- 3. Standard binary search --------
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = True
                break

            # handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:  # left half sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:  # right half sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return ans