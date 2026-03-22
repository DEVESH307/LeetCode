# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         n = len(arr)
#         arr.sort()
#         min_diff = float('inf')
#         res = []

#         for i in range(n-1):
#             min_diff = min(min_diff, abs(arr[i+1]-arr[i]))

#         for i in range(n-1):
#             if abs(arr[i+1]-arr[i]) == min_diff:
#                 res.append([arr[i], arr[i+1]])

#         return res


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        
        min_diff = float('inf')
        res = []

        for i in range(n - 1):
            diff = arr[i+1] - arr[i]

            if diff < min_diff:
                min_diff = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                res.append([arr[i], arr[i+1]])

        return res


        