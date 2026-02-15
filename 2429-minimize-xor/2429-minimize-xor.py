# class Solution:
#     def minimizeXor(self, num1: int, num2: int) -> int:
#         x = num1
#         cnt1 = x.bit_count()
#         cnt2 = num2.bit_count()

#         if cnt1 > cnt2:
#             excess = cnt1 - cnt2
#             for i in range(32):
#                 mask = (1 << i)
#                 if (num1 & mask) and excess:
#                     x ^= mask
#                     excess -= 1
        
#         if cnt1 < cnt2:
#             needed = cnt2 - cnt1
#             for i in range(32):
#                 mask = (1 << i)
#                 if not (num1 & mask) and needed:
#                     x |=  mask
#                     needed -= 1

#         return x

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x = num1
        cnt1 = num1.bit_count()
        cnt2 = num2.bit_count()

        if cnt1 > cnt2:
            for _ in range(cnt1 - cnt2):
                x &= x-1 # removes lowest set bit
        
        if cnt1 < cnt2:
            for _ in range(cnt2 - cnt1):
                x |= (x+1) & - (x+1) # add lowest unset bits

        return x

