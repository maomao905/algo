"""
how to make the target sum
we need to know the sum range of each pair and find the most overlapping pair which minimize the move operations

1<=nums[i]<=limit

A + B
(1~limit) + B
A + (1~limit)
(1~limit) + (1~limit)


total range
2 <= limit*2

0 move
A+B

range of 1 move min(A,B)+1 ~ max(A,B)+limit
(1~limit) + B -> 1+B ~ limit+B
A + (1~limit) -> 1+A ~ limit+A

2 move
(1~limit) + (1~limit) -> 2 ~ limit*2

line sweeping to calculate how many moves needed for target sum in O(1)

O(N+S) S: max of nums
"""
from typing import List
from collections import Counter
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N=len(nums)
        cnt = Counter() # save A+B pair (0 move case)
        diff = Counter() # count one move case
        
        for i in range(N//2):
            a, b = nums[i], nums[N-i-1]
            mi = min(a, b) + 1
            mx = max(a, b) + limit
            diff[mi] -= 1
            diff[mx+1] += 1
            cnt[a+b] += 1
        
        ans = float('inf')
        cur = N # first assuming that we need two move for all pairs n/2 * 2 moves in worst case
        for s in range(2,max(cnt)+1):
            cur += diff[s]
            ans = min(ans, cur - cnt[s])
        return ans

s = Solution()        
print(s.minMoves([1,2,4,3],4))
