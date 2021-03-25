from typing import List
from heapq import *
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        M,N=len(mat),len(mat[0])
        cnt = [None] * M
        for i in range(M):
            cnt[i] = (mat[i].count(1), i)
        
        return [c[1] for c in nsmallest(k, cnt)]

s = Solution()
print(s.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))
print(s.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2))
