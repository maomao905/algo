from typing import List
class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = s.split()
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)):
                if len(res) < j+1:
                    res.append([])
                for _ in range(len(res[j]), i):
                    res[j].append(' ')
                res[j].append(w[j])
        
        return [''.join(res[i]) for i in range(len(res))]

from itertools import zip_longest
class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(w).rstrip() for w in zip_longest(*s.split(), fillvalue=' ')]
        
s = Solution()
print(s.printVertically('how are you'))
print(s.printVertically('to be or not to be'))
print(s.printVertically('contest is coming'))
