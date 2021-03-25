"""
(WA)
DP

[[1,0,1],
 [1,1,0],
 [1,1,0]]

[[1,0,1],
 [2,2,0],
 [3,4,0]
]

[[0,1,1,0],
 [0,1,1,1],
 [1,1,1,0]]

[[0,1,2,0],
 [0,2,4,3],
 [1,4,7,0]]

this solution does not work in the case below
[[0,1,1],
 [1,1,0],
 [0,1,1]]

[[0,1,2],
 [1,3,0],
 [0,3,2]]

dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + 1
time and space: O(NM)
"""

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        cnt = 0
        N,M=len(mat),len(mat[0])
        dp = [[0] * (M+1) for _ in range(N+1)]
        
        for i in range(1,N+1):
            for j in range(1,M+1):
                if mat[i-1][j-1] == 1:
                    x = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
                    if dp[i-1][j] or dp[i][j-1]:
                        x = max(x, 1)
                    dp[i][j] = max(x + 1, 1)
                    cnt += dp[i][j]
        return cnt

"""
brute-force
count number of 1's up to current [i,j] as bottom-right corner and if we meet zero, we stop counting

O(M^2N^2)
"""

class Solution:
    def count_all(self, mat, i, j):
        cnt = 0
        col_end = 0
        for _i in reversed(range(i+1)):
            for _j in reversed(range(col_end, j+1)):
                if mat[_i][_j] == 0:
                    col_end = _j+1
                    break
                cnt += 1
        return cnt
        
    def numSubmat(self, mat: List[List[int]]) -> int:
        cnt = 0
        M,N=len(mat),len(mat[0])
        
        ans = 0
        for i in range(M):
            for j in range(N):
                old = ans
                if mat[i][j] == 1:
                    ans += self.count_all(mat, i, j)
                # print(ans-old)
        
        return ans
        
"""
DP

1. cumulate number column by column like below
[[1,0,1],
 [1,1,0],
 [1,1,0]]

[[1,0,1],
 [1,2,0],
 [1,2,0]]

2. cumulate by row toward left side, but if we meet higher number than current [i,j], we only count
the portion of current [i,j], if we encounter zero, stop counting O(M)

3,2,0 -> only count 2,2,0
because like the case and (i,j) = (3,2) , below, we cannot add 3 but only 2
don't count --> 1 0 0
                1 1 0
                1 1 0

time: O(MN^2), space: O(MN)
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M,N=len(mat),len(mat[0])
        
        for j in range(N):
            for i in range(1,M):
                if mat[i][j] == 0:
                    continue
                mat[i][j] += mat[i-1][j]
        
        ans = 0
        for i in range(M):
            for j in range(N):
                mi = mat[i][j]
                for k in reversed(range(j+1)):
                    mi = min(mi, mat[i][k])
                    if mi == 0:
                        break
                    
                    ans += mi
        return ans

"""
in above solution, in every cell, it goes back to left as long as it can, which takes O(N)
we can do the same thing in O(1) using monotonic stack

time and space O(MN)
"""

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M,N=len(mat),len(mat[0])
        
        # cumulate 1's by column
        for i in range(1,M):
            for j in range(N):
                if mat[i][j] == 1:
                    mat[i][j] = mat[i-1][j] + 1
        
        ans = 0
        for i in range(M):
            stack = []
            cnt = 0
            for j in range(N):
                """
                [[0,1,0],
                 [1,1,0],
                 [1,1,1]] <--- [2,3,1] after column cumulation
                
                (2) + (3 + 2) + (1 + 1 + 1) = 10 <-- above solution O(N^2)
                (2) + (2 + 3) + ((2 + 3) - (2 + 1) + 1) = 10 <-- current solution O(N)
                """
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    _j = stack.pop()
                    _jj = stack[-1] if stack else -1
                    cnt -= (mat[i][_j] - mat[i][j]) * (_j - _jj)
                    
                cnt += mat[i][j]
                ans += cnt
                stack.append(j)
        return ans
                    
        
        

s = Solution()

print(s.numSubmat(
[[1,0,1],
 [1,1,0],
 [1,1,0]]
))

print(s.numSubmat(
[[1,0,1,1,1,1,1],
 [1,1,0,0,0,1,1],
 [1,1,1,0,0,1,1],
 [1,0,1,0,1,0,1],
 [1,0,1,1,1,0,1],
 [1,1,0,1,1,1,1],
 [1,0,0,1,1,0,1]]
))

print(s.numSubmat(
 [[1,0,1],
 [1,1,0],
 [1,1,0]]))

print(s.numSubmat(
[[0,1,1,0],
 [0,1,1,1],
 [1,1,1,0]]
))

print(s.numSubmat(
[[1,0,1],
 [0,1,0],
 [1,0,1]]
))

print(s.numSubmat(
[[0,1,1],
 [1,1,0],
 [0,1,1]]
))
