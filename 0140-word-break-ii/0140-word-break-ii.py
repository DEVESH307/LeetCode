# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         n = len(s)
#         word_set = set(wordDict)
#         result = []

#         def dfs(start, path):
#             # base case: reached end of string
#             if start == n:
#                 result.append(" ".join(path))
#                 return

#             # try every possible end index
#             for end in range(start + 1, n + 1):
#                 word = s[start:end]
#                 # if word in word_set and dfs(end):
#                 #     dfs(end, path + [word])

#                 if word in word_set:
#                     path.append(word)     # choose
#                     dfs(end, path)        # explore
#                     path.pop()            # undo (backtrack)

#         dfs(0, [])
#         return result


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         word_set = set(wordDict)
#         memo = {}

#         def dfs(start):
#             # base case
#             if start == len(s):
#                 return [""]

#             # memo check
#             if start in memo:
#                 return memo[start]

#             res = []

#             for end in range(start + 1, len(s) + 1):
#                 word = s[start:end]

#                 if word in word_set:
#                     for sub in dfs(end):
#                         if sub:
#                             res.append(word + " " + sub)
#                         else:
#                             res.append(word)

#             memo[start] = res
#             return res

#         return dfs(0)


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         n = len(s)
#         word_set = set(wordDict)

#         # dp[i] will store list of sentences from index i
#         # None means "not computed yet"
#         dp = [None] * (n + 1)

#         def dfs(start):
#             if start == n:
#                 return [""]

#             if dp[start] is not None:
#                 return dp[start]

#             res = []

#             for end in range(start + 1, n + 1):
#                 word = s[start:end]

#                 if word in word_set:
#                     for sub in dfs(end):
#                         if sub:
#                             res.append(word + " " + sub)
#                         else:
#                             res.append(word)

#             dp[start] = res
#             return res

#         return dfs(0)


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         n = len(s)
#         word_set = set(wordDict)

#         # dp[i] = list of sentences that can form s[0:i]
#         dp = [[] for _ in range(n + 1)]
#         dp[0] = [""]   # base case

#         for i in range(1, n + 1):
#             for j in range(i):
#                 word = s[j:i]

#                 if word in word_set:
#                     for prev in dp[j]:
#                         if prev:
#                             dp[i].append(prev + " " + word)
#                         else:
#                             dp[i].append(word)

#         return dp[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        word_set = set(wordDict)

        # ---------- Step 1: DP pruning (Word Break I) ----------
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        if not dp[n]:
            return []

        # ---------- Step 2: DFS + Memo ----------
        memo = {}

        def dfs(start):
            if start == n:
                return [""]

            if start in memo:
                return memo[start]

            res = []

            for end in range(start + 1, n + 1):
                word = s[start:end]

                # pruning here
                if word in word_set and dp[end]:
                    for sub in dfs(end):
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[start] = res
            return res

        return dfs(0)