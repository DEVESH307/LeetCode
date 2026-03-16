# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         ans1 = 0
#         ans2 = 0
#         xor_all = 0

#         for num in nums:
#             xor_all ^= num

#         pos = 0

#         while (xor_all & (1<<pos)) == 0:
#             pos += 1

#         mask = 1<<pos

#         for num in nums:
#             if num & mask == 0:
#                 ans1 ^= num
#             else:
#                 ans2 ^= num

#         return sorted([ans1, ans2])



class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0
        xor_all = 0

        for num in nums:
            xor_all ^= num

        # mask = (xor_all & (xor_all - 1)) ^ xor_all
        mask = xor_all & -xor_all

        for num in nums:
            if num & mask == 0:
                ans1 ^= num
            else:
                ans2 ^= num

        return sorted([ans1, ans2])