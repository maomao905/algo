"""
what makes straight line?
y = ax + b

we need two points to determine line and a and b 
a = (y1-y2)/(x1-x2)
b = y - ax

- 1/3 = 0.33333... we cannot use this, instead use Fraction
- if x1-x2 is 0, zero division error, use (x1, INF) pair

calculate a and b for all points and use hashmap to count number of points for each line
O(N^2)
"""
from typing import List
from fractions import Fraction
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def cal(x1, y1, x2, y2):
            if x1-x2 == 0:
                return x1, float('inf')
            a = Fraction(y1-y2, x1-x2)
            b = y1 - a*x1
            return a, b
        
        N=len(points)
        if N==1:
            return 1
        
        seen = defaultdict(set)
        
        for i in range(N):
            for j in range(i+1,N):
                a, b = cal(*points[i], *points[j])
                seen[a, b].update([tuple(points[i]), tuple(points[j])])
        
        return len(max(seen.values(), key=len))

s = Solution()
print(s.maxPoints([[1,1],[2,2],[3,3]]))
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(s.maxPoints([[0,0]]))
        
