class Node:
    def __init__(self):
        self.l = ""
        self.r = ""
        self.pre = 0
        self.suf = 0
        self.best = 0
        self.len = 0

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [Node() for _ in range(4 * n)]

        def pull(i):
            a = tree[i * 2]
            b = tree[i * 2 + 1]
            c = tree[i]
            c.len = a.len + b.len
            c.l = a.l
            c.r = b.r
            c.pre = a.pre
            if a.pre == a.len and a.r == b.l:
                c.pre += b.pre
            c.suf = b.suf
            if b.suf == b.len and a.r == b.l:
                c.suf += a.suf
            c.best = max(a.best, b.best)
            if a.r == b.l:
                c.best = max(c.best, a.suf + b.pre)

        def build(i, l, r):
            if l == r:
                x = tree[i]
                x.l = x.r = s[l]
                x.pre = x.suf = x.best = x.len = 1
                return
            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            pull(i)

        def update(i, l, r, idx, ch):
            if l == r:
                x = tree[i]
                x.l = x.r = ch
                return
            m = (l + r) // 2
            if idx <= m:
                update(i * 2, l, m, idx, ch)
            else:
                update(i * 2 + 1, m + 1, r, idx, ch)
            pull(i)

        build(1, 0, n - 1)
        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1].best)

        return ans