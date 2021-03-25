"""
DP

O(N^2)
"""
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def helper(i,j):
            if i == N:
                return 0
            
            if (i,j) not in memo:
                mi = float('inf')
                for dj in (-1,0,1):
                    _j = j+dj
                    if 0<=_j<N:
                        mi = min(mi, helper(i+1,_j) + matrix[i][j])
                memo[i,j] = mi
            return memo[i,j]
        
        N=len(matrix)
        memo = {}
        return min(helper(0,j) for j in range(N))

s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(s.minFallingPathSum([[-19,57],[-40,-5]]))
            
