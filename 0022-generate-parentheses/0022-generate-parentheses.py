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


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []

#         def is_valid(s):
#             balance = 0
#             for ch in s:
#                 if ch == '(':
#                     balance += 1
#                 else:
#                     balance -= 1
#                 if balance < 0:
#                     return False
#             return balance == 0

#         def dfs(s):
#             if len(s) == 2 * n:
#                 if is_valid(s):
#                     res.append(s)
#                 return

#             dfs(s + '(')
#             dfs(s + ')')

#         dfs("")
#         return res


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []

#         def dfs(openN, closeN, path):
#             if openN == closeN == n:
#                 res.append(path)
#                 return

#             if openN < n:
#                 dfs(openN + 1, closeN, path + '(')

#             if closeN < openN:
#                 dfs(openN, closeN + 1, path + ')')

#         dfs(0, 0, "")
#         return res


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         memo = {}

#         def dfs(openN, closeN):
#             if openN == closeN == n:
#                 return [""]

#             if (openN, closeN) in memo:
#                 return memo[(openN, closeN)]

#             res = []

#             if openN < n:
#                 for s in dfs(openN + 1, closeN):
#                     res.append("(" + s)

#             if closeN < openN:
#                 for s in dfs(openN, closeN + 1):
#                     res.append(")" + s)

#             memo[(openN, closeN)] = res
#             return res

#         return dfs(0, 0)



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        dp[i].append("(" + left + ")" + right)

        return dp[n]