"""
M x N matrix

target = 18

start from right-most column
1. find the closest larger number in the column (19)
    - binary search
2. find the closest smaller number in the row (12)
    - binary search
3. repeat step 1 (26)
4. repeat step 2 (18)
    
time: O(NlogM + MlogN)
space: O(1)

but, we cannot access column values easily, it takes O(N) to get all values in the column
-> it can access easily actually
    just taking mid index in binary search, we don't need to get all values beforehand

so, just move one by one (left row or down column)
time: O(M + N)
space: O(1)
"""

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        i, j = 0, N-1
        
        while i < M and 0 <= j:
            v = matrix[i][j]
            if v == target:
                return True
            
            if v < target:
                i += 1
            else:
                j -= 1
        
        return False

s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
print(s.searchMatrix([[-5]], -5))
        
