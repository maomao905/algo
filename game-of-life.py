"""
in-place, keep the original state
if 0 -> 1, put temp value of -1
if 1 -> 0, put temp value of 2

(i-1,j-1),(i-1,j),(i-1,j+1)
(i,j-1)           (i,j+1)
(i+1,j-1),(i+1,j),(i+1,j+1)

time: O(N) space: O(1)
"""

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M,N=len(board),len(board[0])
        
        for i in range(M):
            for j in range(N):
                val = board[i][j]
                cnt = 0
                
                for _i, _j in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                    if 0 <= _i < M and 0 <= _j < N:
                        cnt += int(board[_i][_j] >= 1)
                
                if cnt < 2 and val == 1:
                    val = 2
                elif 2 <= cnt <= 3 and val == 1:
                    val = 1
                elif cnt > 3 and val == 1:
                    val = 2
                elif cnt == 3 and val == 0:
                    val = -1
                
                board[i][j] = val
        
        for i in range(M):
            for j in range(N):
                val = board[i][j]
                if val == -1:
                    val = 1
                elif val == 2:
                    val = 0
                
                board[i][j] = val
        # print(board)

s = Solution()
s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
s.gameOfLife([[1,1],[1,0]])
                
        
