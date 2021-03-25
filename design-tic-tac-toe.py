"""
counter hash map
row (+) 
column (~ not) to avoid conflict with row
diagnal (n, ~n)

if player1 makes a move, 
     +row, +column and +diagnal if row-col == 0 or row+col == n-1
if player2 makes a move,
    -row, -column and -diagnal if row-col == 0 or row+col == n-1
when any of abs(row/col/diagnal count) == n, current player wins
    
time: O(1) per move space: O(N+N+2) = O(N)
"""
from collections import Counter
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.cnt = Counter()
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        c = 1 if player == 1 else -1
        self.cnt[row] += c
        self.cnt[~col] += c
        
        if row-col == 0:
            self.cnt[self.n] += c
        if row+col == self.n - 1:
            self.cnt[~self.n] += c
        
        for i in (row,~col,self.n,~self.n):
            if abs(self.cnt[i]) == self.n:
                return player
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
t = TicTacToe(3)
print(t.move(0,0,1))
print(t.move(0,2,2))
print(t.move(2,2,1))
print(t.move(1,1,2))
print(t.move(2,0,1))
print(t.move(1,0,2))
print(t.move(2,1,1))
