"""
we need to consider not only books so far but future books as well

DP
to what extent should we think and after the extent, the state is independent
and we don't have to think about anything before the point

[A]books before<---[B][C][D] shelf width -->

if D is current book, then A must be placed in different shelf,
B,C might be in the same shelf or different shelf
A          AB        ABC
---   or -----   or ------
BCD        CD         D

dp[D] = min(
    dp[A] + max(B,C,D), dp[B] + max(C,D), dp[C] + D
)

O(N^2)
"""


from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N=len(books)
        dp = [float('inf')] * N
        
        sum_width = 0
        max_height = 0
        start = 0
        for i in range(N):
            w, h = books[i]
            sum_width += w
            if sum_width > shelf_width:
                break
            max_height = max(max_height, h)
            dp[i] = max_height
            start = i
        
        for i in range(start+1,N):
            w, h = books[i]
            
            max_width = shelf_width - w
            max_height = h
            
            for j in reversed(range(i)):
                _w, _h = books[j]
                max_width -= _w
                dp[i] = min(dp[j] + max_height, dp[i])
                max_height = max(max_height, _h)
                if max_width < 0:
                    break
        
        # print(dp)
        return dp[-1]

s = Solution()
print(s.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4))
print(s.minHeightShelves([[1,3],[2,4],[3,2]], 6))
