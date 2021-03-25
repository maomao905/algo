"""
start from left and right
move the pointer of shorter line every time

proof
[5 1000 ... 3 2]
 ^            ^
 we want to move the left pointer to right to get 1000,
 but until the right is greater than 5, 1000 of the left never beats the 5 of the left
 because area is calculated by shorter height * width
 
 simpler proof
 when l < r, if we move r, it never increase the area, because shorter line matters
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        max_area = 0
        while l < r:
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([4,3,2,1,4]))
print(s.maxArea([1,2,1]))
