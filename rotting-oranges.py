"""
BFS

time O(N) space O(N)
"""
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        
        q = deque()
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        if fresh == 0:
            return 0
        
        ans = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for _i, _j in ((i,j-1),(i,j+1),(i-1,j),(i+1,j)):
                    if not(0<=_i<M and 0<=_j<N):
                        continue
                    if grid[_i][_j] == 1:
                        grid[_i][_j] = 2
                        fresh -= 1
                        q.append((_i,_j))
            ans += 1
            if fresh == 0:
                return ans
        return -1

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))
