"""
DFS 'O' as much as we can
if the 'O' is on the border, return False otherwise return True and replace it with 'X'
in order to avoid visiting the same cell, 
visit only right and down cell
we store the visited cell

O(4N) = O(N)
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        island = 1
        unknown = 0
        not_island = -1
        
        def dfs(i,j):
            if (i,j) in visited:
                return [], False
            visited[(i,j)] = unknown
            
            if board[i][j] == 'X':
                return [], True
            
            # on boarder
            if i in (0, N-1) or j in (0, M-1):
                visited[(i,j)] = not_island
                return [], False
            
            res = [(i,j)]
            for _i,_j in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if (_i,_j) in visited:
                    if visited[(_i,_j)] in [unknown, island]:
                        continue
                    elif visited[(_i,_j)] == not_island:
                        visited[(i,j)] = not_island
                        return [], False
                        
                r, is_island = dfs(_i,_j)
                if not is_island:
                    visited[(i,j)] = not_island
                    return [], False
                
                res.extend(r)
            
            return res, True
            
        
        if len(board) == 0:
            return
        N,M=len(board),len(board[0])
        
        visited = {}
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    res, is_island = dfs(i,j)
                    if is_island:
                        for _i, _j in res:
                            visited[(i,j)] = island
                            board[_i][_j] = 'X'
        # print(board)

["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","O","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]]

["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","X","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]]


["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","O","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]]
s = Solution()
s.solve(
[['X','X','X','X'],
['X','O','O','X'],
['X','X','O','X'],
['X','O','X','X']])
