class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set("+-*/")
        # print(operator)

        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    ans = operand2 + operand1
                elif token == '-':
                    ans = operand2 - operand1
                elif token == '*':
                    ans = operand2 * operand1
                elif token == '/':
                    ans = int(operand2/operand1)
                stack.append(ans)

        return stack[-1]