class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = [(val, idx) for idx, val in enumerate(nums)]
        
        # pick top k by value
        indexed.sort(reverse=True)
        top_k = indexed[:k]
        
        # restore original order
        top_k.sort(key=lambda x: x[1])
        
        return [val for val, idx in top_k]