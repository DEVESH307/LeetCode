# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # only add open paranthesis if open < n
#         # only add a closing paranthesis if close < open
#         # valid IFF open == closed == n

#         stack = []
#         res = []

#         def backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()

#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def is_valid(s):
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def dfs(s):
            if len(s) == 2 * n:
                if is_valid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        return res