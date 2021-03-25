"""
BFS

time: O(MN) space: O(MN) in worst

DFS does not work because our goal is to fill INF with nearest distance, but DFS goes as much as it can 
even if there is other nearer gate from the INF
"""
from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31-1
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        while len(q) > 0:
            for _ in range(len(q)):
                i,j,d = q.popleft()
                
                for row,col in ((0,1), (0,-1), (-1, 0), (1, 0)):
                    _i, _j = i+row, j+col
                    if not (0 <= _i < len(rooms) and 0 <= _j < len(rooms[0])):
                        continue
                    
                    if rooms[_i][_j] == INF:
                        rooms[_i][_j] = d+1
                        q.append((_i, _j, d+1))
        
