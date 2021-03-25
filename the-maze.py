"""
BFS

keep track of visited starting position (wall)
if we visit all spaces which are ajacent to walls, it cannot reach the destination

every starting position, going until hitting a wall
time O(MN) space O(M+N)
"""

from typing import List
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        M,N=len(maze),len(maze[0])
        q = deque([start])
        seen = set()
        
        while q:
            i,j = q.popleft()
            if [i,j] == destination:
                return True
            
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                _i,_j = i,j
                while 0 <= _i+di < M and 0 <= _j+dj < N and maze[_i+di][_j+dj] == 0:
                    _i += di
                    _j += dj
                
                if (_i,_j) not in seen:
                    q.append([_i,_j])
                    seen.add((_i,_j))
        return False    

s = Solution()            
print(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]))
print(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]))
print(s.hasPath(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]))
print(s.hasPath([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3],[3,0]))
        
