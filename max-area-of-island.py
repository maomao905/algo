"""
1が見つかったら、BFSでqueueに1を積んでいく、queueが空になったら、island１つを制覇
    queueから取り出したら、1を0に変えておく（重複カウントしないように)
time: O(RC)
space: O(RC)
"""
from typing import List
# from collections import deque
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         max_area = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     max_area = max(self.bfs(grid, i, j), max_area)
#         return max_area
# 
#     def bfs(self, grid, i, j):
#         areas = set()
#         q = deque([(i, j)])
#         while len(q) > 0:
#             _i, _j = q.popleft()
#             if (_i,_j) in areas:
#                 continue
#             areas.add((_i,_j))
#             grid[_i][_j] = 0
#             if _i-1 >= 0 and grid[_i-1][_j] == 1:
#                 q.append((_i-1,_j))
#             if _i+1 < len(grid) and grid[_i+1][_j] == 1:
#                 q.append((_i+1,_j))
#             if _j-1 >= 0 and grid[_i][_j-1] == 1:
#                 q.append((_i,_j-1))
#             if _j+1 < len(grid[0]) and grid[_i][_j+1] == 1:
#                 q.append((_i,_j+1))
#         return len(areas)
"""
DFS approach
time: O(RC)
space: O(RC)
"""
class Solution:
    def dfs(self, grid, r, c, seen):
        if not(0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return 0
        if grid[r][c] != 1 or (r,c) in seen:
            return 0
        
        seen.add((r, c))
        grid[r][c] = 0
        return 1 + self.dfs(grid, r+1, c, seen) + self.dfs(grid, r-1, c, seen) + self.dfs(grid, r, c-1, seen) + self.dfs(grid, r, c+1, seen)
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_area = max(max_area, self.dfs(grid, r, c, set()))
        return max_area
    

s = Solution()
input = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# input = [
# [1,1,0,0,0],
# [1,1,0,0,0],
# [0,0,0,1,1],
# [0,0,0,1,1]]
print(s.maxAreaOfIsland(input))
