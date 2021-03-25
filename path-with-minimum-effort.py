"""
Dikstra

always choose the shortest path using heap
keep track of visited cell and update if min_dist is less than old record
once we reach the goal exit

time O(NlogN) space O(N)
"""
from heapq import *
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0,0,0)] # difference, i, j
        
        M,N=len(heights),len(heights[0])
        seen = [[float('inf')] * N for _ in range(M)]
        while heap:
            diff, i, j = heappop(heap)
            
            if i == M-1 and j == N-1:
                return diff
            
            for di, dj in ((0,1),(1,0),(-1,0),(0,-1)):
                _i,_j = i+di,j+dj
                if 0 <= _i < M and 0 <= _j < N:
                    _diff = max(abs(heights[i][j] - heights[_i][_j]), diff)
                    # we need to update diff if diff is less than visited diff
                    if seen[_i][_j] > _diff:
                        heappush(heap, (_diff, _i, _j))
                        seen[_i][_j] = _diff

s = Solution()
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
