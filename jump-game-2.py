"""
greedy

how much it can go further in one jump
- save the furthest position after current jump
- if current position is the current jump furthest, start new jump (but we already know furthest position for new jump)

O(N)
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        N=len(nums)
        cur_end = mx = 0
        ans = 0
        
        # N-1 because once we reach the N-2, we already know minimum jump to N-1
        for i in range(N-1):
            mx = max(mx, i + nums[i])
            if cur_end == i:
                ans += 1
                cur_end = mx
                # early return
                if cur_end >= N-1:
                    return ans
        return ans

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))
print(s.jump([2,1]))
print(s.jump([1,0]))
