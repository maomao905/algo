"""
cumulative sum
   0 1 2
     
0  3 0 1
1  5 6 3
2  1 2 0

6 3
2 0
sum of this rectangle is
total sum - 3 0 1
            5        = total sum - (sum[0,2] + sum[2,0] - sum[0,0])
            1
sum(row1, col1, row2, col2) = cum_sum[row2, col2] - (cum_sum[row1-1, col2] + cum_sum[row2, col1-1] - cum_sum[row1-1, col1-1])

cum_sum[i, j] = cum_sum[i][j-1] + cum_sum[i-1][j] - cum_sum[i-1][j-1] + matrix[i][j]

time: O(1)
space: O(MN)
"""

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not len(matrix):
            return
        
        self.cum_sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.cum_sum[i+1][j+1] = self.cum_sum[i+1][j] + self.cum_sum[i][j+1] - self.cum_sum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cum_sum[row2+1][col2+1] - (self.cum_sum[row1][col2+1] + self.cum_sum[row2+1][col1] - self.cum_sum[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

m = NumMatrix(matrix)
print(m.sumRegion(2,1,4,3))
print(m.sumRegion(1,1,2,2))
print(m.sumRegion(1,2,2,4))
