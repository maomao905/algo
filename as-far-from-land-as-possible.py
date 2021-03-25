"""
BFS
start from each land, expand the range one by one until visiting all water cells

time O(N) space O(N) N number of cells
"""
from typing import List

from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dist = -1
        
        q = deque()
        
        M,N = len(grid),len(grid[0])
        # push land cells into queue
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append((i,j))
        
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                
                for _i,_j in ((i,j-1),(i,j+1),(i+1,j),(i-1,j)):
                    if not(0<=_i<M and 0<=_j<N):
                        continue
                    if grid[_i][_j] == 0:
                        q.append((_i,_j))
                        grid[_i][_j] = 1
            dist += 1
        
        return -1 if dist <= 0 else dist
        
s = Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
