from collections import defaultdict
from typing import List

"""
two pointers
time: O(N) space: O(N)
"""

class WordDistance:

    def __init__(self, words: List[str]):
        self.seen = defaultdict(list)
        for i in range(len(words)):
            self.seen[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        seen1 = self.seen[word1]
        seen2 = self.seen[word2]
        
        w1 = w2 = 0
        
        min_dist = float('inf')
        while w1 < len(seen1) and w2 < len(seen2):
            dist = seen1[w1] - seen2[w2]
            min_dist = min(min_dist, abs(dist))
            if dist > 0:
                w2 += 1
            else:
                w1 += 1
        return min_dist

# Your WordDistance object will be instantiated and called as such:
wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(wd.shortest('coding','practice'))
print(wd.shortest('makes','coding'))
