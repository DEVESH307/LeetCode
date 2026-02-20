class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_idx = {0: -1} # map rem -> end index
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum%k
            if rem not in rem_idx:
                rem_idx[rem] = i
            elif i - rem_idx[rem] >= 2:
                return True
        
        return False

        