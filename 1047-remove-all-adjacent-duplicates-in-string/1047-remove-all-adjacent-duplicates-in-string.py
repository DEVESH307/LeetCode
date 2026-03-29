class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack  = []

        for i, ch in enumerate(s):
            if not stack or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)        