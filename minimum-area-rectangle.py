"""
- {y: [x1,x2..]}
- fix two rows (y1 and y2)
- check all y1's x and calculate area

worst O(N^3)
"""
from typing import List
from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p = defaultdict(set)
        for x, y in points:
            p[y].add(x)
        
        y_list = list(p.keys())
        N=len(y_list)
        ans = float('inf')
        for i in range(N):
            for j in range(i+1,N):
                x_list = sorted(list(p[y_list[i]] & p[y_list[j]]))
                min_diff = float('inf')
                for k in range(1,len(x_list)):
                    min_diff = min(min_diff, x_list[k] - x_list[k-1])
                ans = min(ans, abs(y_list[i]-y_list[j]) * min_diff)
        return 0 if ans == float('inf') else ans

"""
brute-force
check all points

O(N^2)
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1-x2) * abs(y1-y2)
                    ans = min(area, ans)
            seen.add((x1,y1))
        return 0 if ans == float('inf') else ans

"""
fix two y axes
y1   y1

y2   y2

x1   x2

check all y1 and y2 for x1 and if there is another (y1, y2) pair in another x2, it's rectangle

worst O(N^2)
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        _x, _y = set(), set()
        for x, y in points:
            _x.add(x)
            _y.add(y)
        
        p = defaultdict(list)
        if len(_x) > len(_y):
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)
        
        seen = {}
        ans = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][i], p[x][j]
                    if (y1, y2) in seen:
                        area = (y1-y2) * (x - seen[y1, y2])
                        ans = min(area, ans)
                    seen[y1, y2] = x
        return ans if ans < float('inf') else 0

s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
