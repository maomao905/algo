"""
take max height from left, right

current units = min(max_left, max_right) - current height

height =         [0,1,0,2,1,0,1,3,2,1,2,1]
max from left =  [0,1,1,2,2,2,2,3,3,3,3,3]
max from right = [3,3,3,3,3,3,3,3,2,2,2,1]
units          = [0,0,1,0,1,2,1,0,0,1,0,0] -> sum(units) = 6

time and space: O(N)
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        N=len(height)
        max_left = [0] * N
        max_right = [0] * N
        
        max_left[0] = height[0]
        for i in range(1,N):
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right[-1] = height[-1]
        for i in reversed(range(N-1)):
            max_right[i] = max(max_right[i+1], height[i])
        
        ans = 0
        for i in range(N):
            ans += min(max_right[i], max_left[i]) - height[i]
        
        return ans

"""
two pointers
time O(N) space O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        N=len(height)
        l, r = 0, N-1
        
        ans = 0
        max_left = max_right = 0
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                ans += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                ans += max_right - height[r]
                r -= 1
        return ans


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
# print(s.trap([1,0,2]))
