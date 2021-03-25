"""
O(MN)
"""
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def helper(i,j):
            if i == M-1 and j == N-1:
                return grid[i][j], grid[i][j]
            
            if grid[i][j] == 0:
                return 0, 0
            
            if (i,j) not in memo:
                mi, mx = float('inf'), float('-inf')
                for di,dj in ((0,1),(1,0)):
                    _i,_j = i+di,j+dj
                    if 0<=_i<M and 0<=_j<N:
                        _mi, _mx = helper(_i,_j)
                        mi = min(mi, _mi)
                        mx = max(mx, _mx)
                mi, mx = grid[i][j] * mi, grid[i][j] * mx
                memo[i,j] = min(mi, mx), max(mi, mx)
            return memo[i,j]
                    
        M,N=len(grid),len(grid[0])
        memo = {}
        ans = helper(0,0)[1]
        return ans % (10**9+7) if ans >= 0 else -1
        
s = Solution()
print(s.maxProductPath([[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]))
print(s.maxProductPath([[1,-2,1],
               [1,-2,1],
               [3,-4,1]]))
print(s.maxProductPath([[1, 3],
               [0,-4]]))
print(s.maxProductPath([[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]))
