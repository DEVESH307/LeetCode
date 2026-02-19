# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
#         n = len(arr)
#         freq = {}
#         max_lucky = -1

#         for num in arr:
#             freq[num] = freq.get(num, 0) + 1

#         for key, val in freq.items():
#             if key == val:
#                 max_lucky = max(max_lucky, val)
        
#         return max_lucky


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        freq = [0]*501
        max_lucky = -1

        for num in arr:
            freq[num] += 1

        for i in range(500, 0, -1):
            if freq[i] == i:
                return i
        
        return -1
