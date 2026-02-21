# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         words = title.strip().split()
#         n = len(words)

#         for i, word in enumerate(words):
#             if len(word) <= 2:
#                 words[i] = word.lower()

#             else:
#                 first = word[0].upper()
#                 rest = word[1:].lower()
#                 words[i] = first + rest

#         return " ".join(words)
        


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.strip().split()
        n = len(words)

        for i, word in enumerate(words):
            if len(word) <= 2:
                words[i] = word.lower()

            else:
                words[i] = word.capitalize()

        return " ".join(words)