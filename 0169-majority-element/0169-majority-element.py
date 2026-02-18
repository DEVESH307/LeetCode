class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mej_elem = None
        me_cnt = 0

        for num in nums:
            if me_cnt == 0:
                mej_elem = num
                me_cnt = 1  
            elif num == mej_elem:
                me_cnt += 1
            else:
                me_cnt -= 1

        return mej_elem