"""
DFS

max(edge sum) is the answer

time O(N) space O(N)
"""

from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(list)
        for sub, ma in enumerate(manager):
            subs[ma].append(sub)
        
        def dfs(i):
            if i not in subs:
                return 0
            
            return max(dfs(j) for j in subs[i]) + informTime[i]
            
        
        return dfs(headID)
        
s = Solution()
print(s.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
print(s.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
print(s.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
print(s.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(s.numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]))
