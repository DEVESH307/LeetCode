class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        def in_order(word1, word2):
            m, n = len(word1), len(word2)

            for i in range(min(m, n)):
                if word1[i] != word2[i]:
                    return rank[word1[i]] < rank[word2[i]]

            return m <= n

        for i in range(len(words)-1):
            if not in_order(words[i], words[i+1]):
                return False

        return True     