"""
conditions
1. swappable -> order does not matter as long as characters are the same
2. trasform -> frequency should be the same
"""
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and Counter(c1.values()) == Counter(c2.values())


s = Solution()
print(s.closeStrings('abc', 'bca'))
print(s.closeStrings('a', 'aa'))
print(s.closeStrings('cabbba', 'abbccc'))
print(s.closeStrings('cabbba', 'aabbss'))
print(s.closeStrings("abbzzca", "babzzcz"))
        
        
            
