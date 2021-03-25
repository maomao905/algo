"""
M: string length 
N: input list size
sort: O(NMlogM)
space: O(NM)
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            ht[sorted_s].append(s)
        
        return list(ht.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        
