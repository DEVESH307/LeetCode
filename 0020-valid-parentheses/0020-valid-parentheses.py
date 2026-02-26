class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for ch in s:
            if ch not in mp:
                stack.append(ch)
            else:
                if not stack or stack.pop() != mp[ch]:
                    return False
        return not stack