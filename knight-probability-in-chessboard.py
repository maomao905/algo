"""
DFS
memorization

O(N^2K)
"""

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = {}
        dirs = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
        
        def dfs(i,j,k):
            if k == 0:
                return 1
            
            if (i,j,k) not in memo:
                cnt = 0
                for di,dj in dirs:
                    _i,_j = i+di,j+dj
                    if 0 <= _i < N and 0 <= _j < N:
                        cnt += dfs(_i,_j,k-1)
                memo[i,j,k] = cnt
            return memo[i,j,k]
            
        
        return dfs(r, c, K) / (8 ** K)

s = Solution()
# print(s.knightProbability(3,2,0,0))
print(s.knightProbability(3,3,0,0))
