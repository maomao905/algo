"""
DP
- pre palindrome check O(N^2) in any (i,j)
- memorization O(N^2)
"""
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def minCut(self, s: str) -> int:
        def helper(i):
            if i >= N:
                return 0
            
            if memo[i] == -1:
                min_cuts = float('inf')
                for j in range(i,N):
                    if palindrome[i][j]:
                        min_cuts = min(min_cuts, helper(j+1) + 1)
                memo[i] = min_cuts
            return memo[i]
        
        N=len(s)
        palindrome = [[False] * N for _ in range(N)]
        for i in reversed(range(N)):
            for j in range(i,N):
                if j-i<2:
                    palindrome[i][j] = s[i] == s[j]
                else:
                    palindrome[i][j] = s[i] == s[j] and palindrome[i+1][j-1]
        memo = [-1] * N
        return helper(0) - 1

s = Solution()
print(s.minCut('aab'))
print(s.minCut('a'))
print(s.minCut('abbabad'))
