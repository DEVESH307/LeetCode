class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = 0
        start = 0
        min_len = float('inf')

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start+min_len]