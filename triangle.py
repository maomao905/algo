"""
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

cumulative sum
if there are two possibilities, take smaller one

[
      [2],
     [5,6],
   [11,10,13],
  [15,11,18,16]
]

how can I look up ajacent element of previous row?
current previous
[1,2]    1
[2,3]    2
-> current index or current-1 index

O(N)
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                a = triangle[i-1][j-1] if j-1 >= 0 else float('inf')
                b = triangle[i-1][j] if j < len(triangle[i-1]) else float('inf')
                triangle[i][j] += min(a,b)
        
        return min(triangle[-1])

s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
))
