"""
binary search

O(logM+logN)
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N = len(matrix),len(matrix[0])
        
        def bsearch(l,r,get_val):
            while l<r:
                mid = (l+r)//2 + (r-l)%2
                v = get_val(mid)
                if v == target:
                    return mid
                if v > target:
                    r = mid-1
                else:
                    l = mid
            return l
        
        get_row_val = lambda i: matrix[i][0]
        i = bsearch(0,M-1, get_row_val)
        get_col_val = lambda j: matrix[i][j]
        j = bsearch(0,N-1,get_col_val)
        return matrix[i][j] == target

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
        
        
