# class Solution:
#     def minInsertions(self, s: str) -> int:
#         res = 0      # insertions
#         need = 0     # how many ')' we need

#         for c in s:
#             if c == '(':
#                 # If need is odd → we have 1 pending ')'
#                 if need % 2 == 1:
#                     res += 1   # insert one ')'
#                     need -= 1

#                 need += 2

#             else:  # ')'
#                 need -= 1

#                 if need < 0:
#                     # We have extra ')', need a '('
#                     res += 1
#                     need = 1   # this ')' needs one more ')'

#         return res + need


class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                stack.append('(')
                i += 1

            else:  # ')'
                # Check if it's a double "))"
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Single ')' → need one more ')'
                    res += 1
                    i += 1

                if stack:
                    stack.pop()
                else:
                    # No matching '(' → insert one
                    res += 1

        # Each remaining '(' needs "))" → 2 insertions each
        return res + 2 * len(stack)