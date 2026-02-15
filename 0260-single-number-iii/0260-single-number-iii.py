# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         ans1 = 0
#         ans2 = 0
#         xor_two_nums = 0

#         for num in nums:
#             xor_two_nums ^= num

#         pos = 0

#         while (xor_two_nums & (1<<pos)) == 0:
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
        xor_two_nums = 0

        for num in nums:
            xor_two_nums ^= num

        mask = (xor_two_nums & (xor_two_nums - 1)) ^ xor_two_nums

        for num in nums:
            if num & mask == 0:
                ans1 ^= num
            else:
                ans2 ^= num

        return sorted([ans1, ans2])