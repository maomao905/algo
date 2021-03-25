"""
DFS with memorization

O(K*M*N)
"""

class Solution:
    def findPaths(self, M: int, N: int, K: int, i: int, j: int) -> int:
        def dfs(i,j,k):
            if not(0<=i<M and 0<=j<N):
                return 1
            
            if k == 0:
                return 0
            
            if (i,j,k) not in memo:
                memo[i,j,k] = sum([dfs(_i,_j,k-1) for _i,_j in ((i+1,j),(i-1,j),(i,j-1),(i,j+1))]) % MOD
            return memo[i,j,k]
        
        MOD = 10**9+7
        memo = {}
        return dfs(i,j,K) % MOD

s = Solution()
print(s.findPaths(2,2,2,0,0))
print(s.findPaths(1,3,3,0,1))
        
