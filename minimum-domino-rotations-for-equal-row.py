"""
target value must exist in every ith domino
- find the target value

[1,2,1,1,1,2,2,2]
[2,1,2,2,2,2,2,2]

O(N)
"""
from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N=len(A)
        cands = set([A[0],B[0]])
        for i in range(1,N):
            cands &= set([A[i],B[i]])
            if not cands:
                return -1
        
        target = cands.pop()
        return min(N-A.count(target), N-B.count(target))

s = Solution()
print(s.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(s.minDominoRotations([3,5,1,2,3],[3,6,3,3,4]))
print(s.minDominoRotations([1,2,1,1,1,2,2,2],[2,1,2,2,2,2,2,2]))
            
