"""
backtrack

time O(N*2^N) space O(N)
"""

from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def helper(i, comb=[]):
            if i == N:
                res.append(''.join(comb))
                return
            
            if not comb or (comb and not comb[-1].isdigit()):
                for j in range(i,N):
                    comb.append(str(j-i+1))
                    helper(j+1, comb)
                    comb.pop()
            
            comb.append(word[i])
            helper(i+1, comb)
            comb.pop()
        
        N=len(word)
        res = []
        helper(0)
        return res

s = Solution()
print(s.generateAbbreviations('word'))
        
        
