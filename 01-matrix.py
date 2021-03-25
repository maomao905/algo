from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M,N=len(matrix),len(matrix[0])
        q = deque()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    q.append((i,j))
        
        seen = set()
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                
                for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
                    _i = i+di
                    _j = j+dj
                    if not(0<=_i<M and 0<=_j<N):
                        continue
                    # print(_i,_j)
                    if matrix[_i][_j] != 0 and (_i,_j) not in seen:
                        matrix[_i][_j] = d
                        q.append((_i,_j))
                        seen.add((_i,_j))
        return matrix

s = Solution()
# print(s.updateMatrix(
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# ))
print(s.updateMatrix(
[[0,0,0],
 [0,1,0],
 [1,1,1]]
))
print(s.updateMatrix(
[[0,1,0],
 [0,1,0],
 [0,1,0],
 [0,1,0],
 [0,1,0]]
))
                
