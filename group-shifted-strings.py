"""
mod when the difference is negative
[az, ba]
az 1-26 = -25 = -25 % 26 = 1
ba 2-1 = 1

O(NS) N: length of input, S average length of word
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strings:
            shift = []
            for i in range(1,len(s)):
                diff = ord(s[i-1]) - ord(s[i])
                shift.append(diff%26)
            res[tuple(shift)].append(s)
        
        return list(res.values())

s = Solution()
print(s.groupStrings(['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z']))
            
