"""
sort by (end, start)

O(NlogN)
"""

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        
        prev = float('-inf')
        cnt = 0
        for x, y in pairs:
            if prev >= x:
                continue
            cnt += 1
            prev = y
        
        return cnt

s = Solution()
print(s.findLongestChain([[1,2],[2,3],[3,4]]))
print(s.findLongestChain([[1,2],[3,10],[4,6],[7,111]]))
