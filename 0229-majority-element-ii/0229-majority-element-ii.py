class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        elem1 = None
        elem2 = None
        freq1 = 0
        freq2 = 0
        res = []

        for num in nums:
            if num == elem1 or num == elem2:
                if num == elem1:
                    freq1 += 1
                if num == elem2:
                    freq2 += 1
            elif freq1 == 0 or freq2 == 0:
                if freq1 == 0:
                    elem1 = num
                    freq1 = 1
                else:
                    elem2 = num
                    freq2 = 1
            else:
                freq1 -= 1
                freq2 -= 1

        if nums.count(elem1) > n // 3:
            res.append(elem1)
        if nums.count(elem2) > n // 3:
            res.append(elem2)
        return res
        