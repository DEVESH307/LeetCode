# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = (x > 0) - (x < 0)
        
#         reversed_x = sign * int(str(abs(x))[::-1])

#         if reversed_x < -2**31 or reversed_x > 2**31 - 1:
#             return 0

#         return reversed_x


# class Solution:
#     def reverse(self, x: int) -> int:
#         INT_MIN = -2**31
#         INT_MAX = 2**31 - 1

#         sign = -1 if x < 0 else 1

#         # Convert to string, remove sign
#         s = str(abs(x))

#         # Reverse
#         rev = s[::-1]

#         # Convert back to integer
#         result = sign * int(rev)

#         # 32-bit range check
#         if result < INT_MIN or result > INT_MAX:
#             return 0

#         return result


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check overflow before rev * 10 + digit
            if rev > INT_MAX // 10:
                return 0

            if rev == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev