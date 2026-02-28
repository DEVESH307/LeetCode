# class Solution:
#     def subarrayBitwiseORs(self, arr: List[int]) -> int:
#         prev = set()
#         curr = set()
#         res = set()

#         for i, num in enumerate(arr):
#             for x in prev:
#                 curr.add(x | num)
#                 res.add(x | num)

#             curr.add(num)
#             res.add(num)

#             prev = curr.copy()
#             curr.clear()

#         return len(res)


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        res = set()

        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(val | num)

            res.update(curr)
            prev = curr

        return len(res)