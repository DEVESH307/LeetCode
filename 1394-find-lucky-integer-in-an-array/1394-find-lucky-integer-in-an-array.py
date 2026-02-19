class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        freq = {}
        max_lucky = -1

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            if key == val:
                max_lucky = max(max_lucky, val)
        
        return max_lucky
