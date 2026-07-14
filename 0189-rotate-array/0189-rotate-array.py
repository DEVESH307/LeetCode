class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, i, j):
            while i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

            # return arr

        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

        