"""
max-heap
pop two stones everytime and push heavier stone back
continue this process until one stone or no stone is left
time: O(NlogN) space: O(N)
"""

from typing import List
from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x < y:
                heappush(stones, -(y-x))
        
        if not stones:
            return 0
        
        return -stones[0]
                
s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
