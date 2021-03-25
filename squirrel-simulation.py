"""
find the first nut that makes maximum saving max(squirrel -> nut -> tree - (nut -> tree)*2)

O(N)
"""

from typing import List

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        N=len(nuts)
        max_saving = float('-inf')
        total = 0
        for i in range(N):
            _d = abs(nuts[i][0] - tree[0]) + abs(nuts[i][1] - tree[1])
            d = _d * 2
            saving = d - (_d + abs(squirrel[0] - nuts[i][0]) + abs(squirrel[1] - nuts[i][1]))
            if saving > max_saving:
                max_saving = saving
            total += d
        return total - max_saving

s = Solution()
print(s.minDistance(5,7,[2,2],[4,4],[[3,0],[2,5]]))
print(s.minDistance(5,
5,
[3,2],
[0,1],
[[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]]))
                
            
            
            
