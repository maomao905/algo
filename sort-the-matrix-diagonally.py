"""
MN matrix
assuming M<N
O((M+N)*MlogM)
"""

from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort_diagonal(i,j):
            res = []
            _i,_j=i,j
            while _i < M and _j < N:
                res.append(mat[_i][_j])
                _i+=1
                _j+=1
            
            res.sort()
            k = 0
            _i,_j = i,j
            while _i < M and _j < N:
                mat[_i][_j] = res[k]
                _i+=1
                _j+=1
                k += 1
            return res
        
        M,N=len(mat),len(mat[0])
        for j in range(N):
            sort_diagonal(0,j)
        
        for i in range(1,M):
            sort_diagonal(i,0)
        
        return mat

s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
                               
[[1, 3, 1, 1],
 [1, 2, 1, 2],
 [1, 2, 3, 2]]
