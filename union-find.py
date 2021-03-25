"""
rootのindexのvalueにはrootの集合のサイズにマイナスをつけたものが入る
root以下のindexのvalueには普通にrootのindexが入る
rootかどうかはマイナスかどうかで判断できる
"""
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
        # store the height of the tree
        # merge lower union to higher union (more efficient)
        # self.rank = [0] * n
    
    def find(self, x):
        """
        return root of x
        """
        # -1 means x is root itself
        if self.parents[x] < 0:
            return x
        else:
            # path compression
            # update the parent to directly connect to the root
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        # # 高い方に低い方をmergeする限りは高さ(rank)は変わらない
        # if self.rank[x] < self.rank[y]:
        #     self.parents[x] = y
        # else:
        #     self.parents[y] = x
        #     # xにxと同じ高さのyをmergeするから高さが1増える
        #     if self.rank[x] == self.rank[y]:
        #         self.rank[x] += 1
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        # union by size
        # rootの場合、マイナスの値が追加される
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        # xのrootには、rootが持つnodeの数の合計が入っている
        return -self.parents[self.find(x)]
    
    def list_roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
