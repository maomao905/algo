from typing import List

"""
DFS
- mark visited land node as #
- number of route nodes equals the number of islands
time complexity: O(MN)
space complexity: O(MN)
"""

# # 136ms
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0
#         # row
#         for i in range(len(grid)):
#             # column
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.DFS(grid, i, j)
#                     count += 1
#         return count
# 
#     def DFS(self, grid, i, j):
#         if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
#             return
# 
#         grid[i][j] = '#'
#         self.DFS(grid, i-1, j)
#         self.DFS(grid, i+1, j)
#         self.DFS(grid, i, j-1)
#         self.DFS(grid, i, j+1)

"""
BFS
- mark visited land node as #
- 1がある限り、すべてのneighbor nodeを探し続けて、その次の深さに行って同じことを繰り返す
- queueがemptyになったら次のland nodeまでDFSで周る
time complexity: O(NM)
space complexity: min(N,M)
"""
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # row
        for i in range(len(grid)):
            # column
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '#'
                    while len(queue) > 0:
                        _i, _j = queue.popleft()
                        if 0 <= _i-1 and grid[_i-1][_j] == '1':
                            queue.append((_i-1, _j))
                            grid[_i-1][_j] = '#'
                        if _i+1 < len(grid) and grid[_i+1][_j] == '1':
                            queue.append((_i+1, _j))
                            grid[_i+1][_j] = '#'
                        if 0 <= _j-1 and grid[_i][_j-1] == '1':
                            queue.append((_i, _j-1))
                            grid[_i][_j-1] = '#'
                        if _j+1 < len(grid[0]) and grid[_i][_j+1] == '1':
                            queue.append((_i, _j+1))
                            grid[_i][_j+1] = '#'
        return count
grid = [
  ["1","1"],
  ["0","1"],
  ["0","0"],
]

s = Solution()
print(s.numIslands(grid))


        
        
