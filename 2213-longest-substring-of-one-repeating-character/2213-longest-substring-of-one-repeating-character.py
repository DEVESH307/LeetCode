class Node:
    __slots__ = ("lch", "rch", "pref", "suff", "best", "length")

    def __init__(self, ch=""):
        if ch:
            self.lch = self.rch = ch
            self.pref = self.suff = self.best = self.length = 1
        else:
            self.lch = self.rch = ""
            self.pref = self.suff = self.best = self.length = 0


class SegmentTree:
    def __init__(self, s):
        self.s = list(s)
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def merge(self, left, right):
        if left.length == 0:
            return right
        if right.length == 0:
            return left

        res = Node()
        res.length = left.length + right.length
        res.lch = left.lch
        res.rch = right.rch

        res.pref = left.pref
        if (
            left.pref == left.length
            and left.rch == right.lch
        ):
            res.pref = left.length + right.pref

        res.suff = right.suff
        if (
            right.suff == right.length
            and left.rch == right.lch
        ):
            res.suff = right.length + left.suff

        res.best = max(left.best, right.best)

        if left.rch == right.lch:
            res.best = max(res.best, left.suff + right.pref)

        return res

    def build(self, node, l, r):
        if l == r:
            self.tree[node] = Node(self.s[l])
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.tree[node] = Node(ch)
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, ch)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, ch)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, st.n - 1, idx, ch)
            ans.append(st.tree[1].best)

        return ans