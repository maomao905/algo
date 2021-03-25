"""
sorted by start time
[A, B]
if A's end time exceeds B's start time, we can merge

1. <--new--><---intervals--->
2. <--new-->
      <---intervals--->
3. <--intervals--><--new--><--intervals-->
4. <--intervals-->
              <--new--><--intervals-->
5. <--intervals-->
              <--new-->
                    <--intervals-->
6. <---intervals--->
              <--new-->
7. <---intervals---><--new-->
time: O(N) space: O(N)
"""

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        left, right = [], []
        for start, end in intervals:
            if end < new_start:
                left.append([start, end])
            elif start > new_end:
                right.append([start, end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        return left + [[new_start, new_end]] + right
                
s = Solution()
# print(s.insert([[1,3],[6,9]], [2,5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(s.insert([], [5,7]))
print(s.insert([[1,5]], [1,7]))
# print(s.insert([[1,5]], [2,3]))
# print(s.insert([[1,5]], [2,7]))
                
        
                
