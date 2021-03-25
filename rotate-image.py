"""
row:N,col:M
m[0][0] -> m[0][M-1]
m[0][M-1] -> m[N-1][M-1]
m[N-1][M-1] -> m[N-1][0]
m[N-1][0] -> m[0][0] <--- go back where it starts

3 -> 1 end
4 -> 2 end
"""

from typing import List
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(m)
        end = 1 if N%2 else 2
        
        i = 0
        for size in range(N,end,-2):
            temp = 0
            for j in range(size):
                temp = m[i][i+size-j]
                k = i+size-j
                m[i][k] = m[i+j][i+j]
                m[k][k] = m[]
                m[i+j][i+j]
            
            i += 1
        # TODO: 
            
        
