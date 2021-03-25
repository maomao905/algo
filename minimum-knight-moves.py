"""
BFS
if distance does not get farer than 3 steps, it's possible to choose the path to reach the goal
"""
from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0)])
        seen = set([(0,0)])
        step = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == x and j == y:
                    return step
                dist = abs(i-x) + abs(j-y)
                for di, dj in ((1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)):
                    _i,_j = i+di,j+dj
                    if abs(x-_i) + abs(y-_j) - dist < 3 and (_i,_j) not in seen:
                        seen.add((_i,_j))
                        q.append((_i,_j))
                    
            step += 1

"""
DP

positive or negative does not matter
if (i,j) == (1,1),(0,2), it takes 2 steps
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}
        def dfs(i,j):
            if i+j == 0:
                return 0
            if i+j == 2:
                return 2
            if (i,j) not in memo:
                memo[i,j] = min(dfs(abs(i-1), abs(j-2)), dfs(abs(i-2), abs(j-1))) + 1
            return memo[i,j]
        
        return dfs(abs(x), abs(y))

s = Solution()
print(s.minKnightMoves(2,1))
print(s.minKnightMoves(5,5))
            
