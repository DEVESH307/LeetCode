class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        word_set = set(wordDict)
        result = []

        def dfs(start, path):
            # base case: reached end of string
            if start == n:
                result.append(" ".join(path))
                return

            # try every possible end index
            for end in range(start + 1, n + 1):
                word = s[start:end]
                # if word in word_set and dfs(end):
                #     dfs(end, path + [word])

                if word in word_set:
                    path.append(word)     # choose
                    dfs(end, path)        # explore
                    path.pop()            # undo (backtrack)

        dfs(0, [])
        return result