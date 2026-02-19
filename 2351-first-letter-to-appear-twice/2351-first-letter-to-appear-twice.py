class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()

        for ch in s:
            if ch in st:
                return ch
            else:
                st.add(ch)