"""
divisible -> mod
subarray sum -> cumulative sum
=> how about cumulative mod sum

4,5,0,-2,-3,1 k=5
4 4 4 2  4  0 
  1 2    3  1
  
1 4 3 5 -2
1 0 3 3 1

time: O(N)
space: O(N)
"""

from typing import List
from collections import Counter
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cum = Counter({0: 1})
        ans = 0
        prev = 0
        for n in A:
            mod = (prev + n) % K
            ans += cum[mod] 
            cum[mod] += 1
            prev = mod
        
        return ans

s = Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
