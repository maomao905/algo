"""
["cha","r","act","ers"]
char - act
 | \
 r - ers
 
if x & y is empty, we can concatenate
try all combinations
O(2^N+NS) S: average length of string
"""

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        cands = [set()]
        for s in arr:
            # O(S)
            uniq_s = set(s)
            if len(s) != len(uniq_s):
                continue
            
            for cand in cands:
                # they are independent each other
                # O(26) = O(1)
                if not(cand & uniq_s):
                    cands.append(cand | uniq_s)
        
        return max(len(cand) for cand in cands)

s = Solution()
print(s.maxLength(['un', 'iq', 'ue']))
print(s.maxLength(['cha', 'r', 'act', 'ers']))
print(s.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"])) # 16
        
                
