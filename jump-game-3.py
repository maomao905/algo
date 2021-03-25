"""
brute-force
O(2^N) every index we have two choices, we jump to N indices at most

maybe there is a loop

DFS
store visited index in hash map
if we visit all indices and still cannot reach to 0, then return false

since we visit index at most once

time: O(N)
space: O(N)
"""

from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        def dfs(i):
            if not (0 <= i < len(arr)):
                return False
            
            if i in seen:
                return False
            
            if arr[i] == 0:
                return True
            
            if len(seen) >= len(arr)-1:
                return False
            
            seen.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])
        
        return dfs(start)

s = Solution()
print(s.canReach(arr = [4,2,3,0,3,1,2], start = 5))
print(s.canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(s.canReach(arr = [3,0,2,1,2], start = 2))
print(s.canReach(arr = [0,1], start = 1))
