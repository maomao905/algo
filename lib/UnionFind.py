class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.p[px] = self.p[py] = min(px, py)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
