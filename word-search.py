"""
DFS (backtracking)
search 4 directions(actually 3) each time until it reaches the word length
keep track of the visited cells (mark # in visited cells)

K is the word length
time: O(MN 3^K)
space: O(K) for recursion stack
"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        
        def dfs(i, j, k):
            # finished all checks
            if k == len(word):
                return True
            
            if not (0 <= i < M and 0 <= j < N):
                return False
            
            match = False
            
            prev = board[i][j]
            # match, continue search
            if board[i][j] == word[k]:
                board[i][j] = '#'
                match |= dfs(i, j+1, k+1)
                match |= dfs(i+1, j, k+1) 
                match |= dfs(i, j-1, k+1)
                match |= dfs(i-1, j, k+1)
            
            if not match:
                board[i][j] = prev
                
            return match
        
        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True
        return False

s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED"
print(s.exist(board, word))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "SEE"
print(s.exist(board, word))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCB"
print(s.exist(board, word))
print(s.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))
            
