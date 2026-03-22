class Solution:
    def countKDifference(self, nums, k):
        countPair = 0
        arr = [0] * 101

        for num in nums:
            arr[num] += 1

        for i in range(101 - k):
            countPair += arr[i] * arr[i + k]

        return countPair