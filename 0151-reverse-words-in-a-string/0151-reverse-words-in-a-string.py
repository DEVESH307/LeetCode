# class Solution:
#     def reverse(self, arr, i, j):
#         while i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1

#     def reverseWords(self, s: str) -> str:
#         s = " ".join(s.split())
#         n = len(s)
#         arr = list(s)

#         self.reverse(arr, 0, n-1)

#         i = 0
#         for j in range(n):
#             if arr[j] == " ":
#                 self.reverse(arr, i, j-1)
#                 i = j+1

#         self.reverse(arr, i, n-1)

#         return "".join(arr)


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
