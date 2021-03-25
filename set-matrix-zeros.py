"""
in-place O(1) space

use first row and column as a flag for zero
we can mark flag only after we pass the first row and column, that's why it works
we have to keep track of whether first row and column itself is zero

in second pass,
we set zero in row and column using zero flag of first row and column

time: O(MN) space: O(1)
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_first_row_zero = False
        is_first_col_zero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = True
                    if j == 0:
                        is_first_col_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if is_first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            

s = Solution()
# s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
# s.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
