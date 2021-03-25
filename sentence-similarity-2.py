"""
union-find

if word1 and word2 are similar, root of word1 and word2 should be the same

O(N+P) N: num of words P: num of pairs
"""
from typing import List
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = uf[find(y)]
        
        if len(words1) != len(words2):
            return False
        
        for x, y in pairs:
            union(x, y)
        
        for i in range(len(words1)):
            union(words1[i], words1[i])
            union(words2[i], words2[i])
            if find(words1[i]) != find(words2[i]):
                return False
        return True

s = Solution()
print(s.areSentencesSimilarTwo(
  words1 = ["great", "acting", "skills"],
  words2 = ["fine", "drama", "talent"],
  pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
))
