# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         st = set()

#         for ch in s:
#             if ch in st:
#                 return ch
#             else:
#                 st.add(ch)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = [0]*26

        for ch in s:
            if freq[ord(ch)-ord('a')] == 1:
                return ch
            else:
                freq[ord(ch)-ord('a')] += 1