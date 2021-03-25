"""
[-2,0,3,5,3]
   +2    -2
      3
 -2    +2
 
 add [-2,0,3,5,3]
"""
from typing import List
from itertools import accumulate
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        addition = [0] * length
        
        for s, e, d in updates:
            addition[s] += d
            if e+1 < length:
                addition[e+1] -= d
        
        return list(accumulate(addition))

s = Solution()
print(s.getModifiedArray(5,[[1,3,2],[2,4,3],[0,2,-2]]))
