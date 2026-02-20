class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0

        for num in st:
            if num-1 not in st:
                curr_len = 0
                x = num
                while x in st:
                    x += 1
                    curr_len += 1

                ans = max(ans, curr_len)

        return ans
        