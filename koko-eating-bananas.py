"""
binary search
left=1, right=max(piles)
if koko can eat all with mid k, right = mid
otherwise, left = mid + 1,

every iteration, we need N iterations to check koko can eat all given k within H hours

O(Nlog(max of piples))
"""

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        N=len(piles)
        
        l,r = 1, max(piles)
        
        while l < r:
            mid = l + (r-l)//2
            need = sum(math.ceil(piles[i]/mid) for i in range(N))
            
            if need <= H:
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
print(s.minEatingSpeed([3,6,7,11],8))
print(s.minEatingSpeed([30,11,23,4,20],5))
print(s.minEatingSpeed([30,11,23,4,20],6))
print(s.minEatingSpeed([312884470],312884469)) # 2
print(s.minEatingSpeed([9,9,9],9))
print(s.minEatingSpeed([2,2],2))
print(s.minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184], 823855818))
print(s.minEatingSpeed([312884470],968709470))
