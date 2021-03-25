"""
(TLE)

count (j,k) pair grid[i][j] == 1 and grid[i][k] == 1
add previously counted same pair to answer

O(MN^2)
"""
from typing import List
from collections import Counter

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        cnt = Counter()
        ans = 0
        for i in range(M):
            for j in range(N-1):
                for k in range(j+1, N):
                    if grid[i][j] == 1 and grid[i][k] == 1:
                        ans += cnt[j,k]
                        cnt[j,k] += 1
        return ans

"""
fix two rows or fix two columns
cnt = sum of number of row1[i] == row2[i]
ans += cnt * (cnt-1) // 2 (combinations of two)
O(max(M,N)*(min(M,N)^2))
"""
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        ans = 0
        for i in range(M-1):
            for j in range(i+1,M):
                same = len([k for k in range(N) if grid[i][k] == 1 and grid[j][k] == 1])
                ans += same * (same-1) // 2
        return ans

s = Solution()
print(s.countCornerRectangles(
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
))
print(s.countCornerRectangles(
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
))
print(s.countCornerRectangles(
[[1,1,1,1]]
))
