# class Solution:
#     def countVowels(self, word: str) -> int:
#         vowels = set("aeiouAEIOU")
#         n = len(word)
#         ans = 0

#         for s in range(n):
#             for e in range(s, n):
#                 for i in range(s, e+1):
#                     if word[i] in vowels:
#                         ans += 1
        
#         return ans


# class Solution:
#     def countVowels(self, word: str) -> int:
#         vowels = set("aeiouAEIOU")
#         n = len(word)
#         ans = 0

#         for s in range(n):
#             vowel_count = 0
#             for e in range(s, n):
#                 if word[e] in vowels:
#                     vowel_count += 1
#                 ans += vowel_count
        
#         return ans


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set("aeiouAEIOU")
        n = len(word)
        ans = 0

        for i in range(n):
            if word[i] in vowels:
               ans += (i+1)*(n-i)
        
        return ans