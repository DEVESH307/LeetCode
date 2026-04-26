# from typing import List

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False


# class Solution:
#     def build_trie(self, words):
#         root = TrieNode()
#         for word in words:
#             node = root
#             for ch in word:
#                 if ch not in node.children:
#                     node.children[ch] = TrieNode()
#                 node = node.children[ch]
#             node.is_end = True
#         return root

#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         root = self.build_trie(wordDict)
#         memo = {}

#         def dfs(start):
#             if start == n:
#                 return True

#             if start in memo:
#                 return memo[start]

#             node = root
#             for i in range(start, n):
#                 if s[i] not in node.children:
#                     break

#                 node = node.children[s[i]]

#                 if node.is_end and dfs(i + 1):
#                     memo[start] = True
#                     return True

#             memo[start] = False
#             return False

#         return dfs(0)



# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         word_set = set(wordDict)

#         def dfs(start):
#             if start == n:
#                 return True

#             for end in range(start + 1, n + 1):
#                 if s[start:end] in word_set and dfs(end):
#                     return True

#             return False

#         return dfs(0)


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         word_set = set(wordDict)
#         memo = {}

#         def dfs(start):
#             if start == n:
#                 return True

#             if start in memo:
#                 return memo[start]

#             for end in range(start + 1, n + 1):
#                 if s[start:end] in word_set and dfs(end):
#                     memo[start] = True
#                     return True

#             memo[start] = False
#             return False

#         return dfs(0)


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         word_set = set(wordDict)

#         dp = [-1] * (n + 1)

#         def dfs(start):
#             if start == n:
#                 return True

#             if dp[start] != -1:
#                 return dp[start]

#             for end in range(start + 1, n + 1):
#                 if s[start:end] in word_set and dfs(end):
#                     dp[start] = True
#                     return True

#             dp[start] = False
#             return False

#         return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]