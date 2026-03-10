class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        return max_elem * k + ((k-1) * k)//2
        