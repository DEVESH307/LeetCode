class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        curr = set()
        res = set()

        for i, num in enumerate(arr):
            for x in prev:
                curr.add(x | num)
                res.add(x | num)

            curr.add(num)
            res.add(num)

            prev = curr.copy()
            curr.clear()

        return len(res)