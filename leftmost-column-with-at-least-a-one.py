"""
binary search in each row
O(MlogN) 100 * log(100) <= 700
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List
class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat
    def get(self, row: int, col: int) -> int:
       return self.mat[row][col]
       
    def dimensions(self) -> List:
       return len(self.mat), len(self.mat[0])

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        M,N = mat.dimensions()
        leftmost = rightmost = N
        
        for i in range(M):
            # initialize r = N and if there is no one, l and r becomes N
            l,r = 0,rightmost
            while l<r:
                mid = l + (r-l)//2
                if mat.get(i,mid) == 0:
                    l = mid + 1
                else:
                    r = mid
            leftmost = min(l,leftmost)
            rightmost = l
        
        return -1 if leftmost == N else leftmost

"""
start in the top right corner,
move left as long as we have 1, if it's zero, move down and continue this

O(M+N)
"""

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        M,N = mat.dimensions()
        
        i,j = 0,N-1
        
        leftmost = N
        while i<M and 0 <= j:
            # there is no one up to j, so we go down
            if mat.get(i,j) == 0:
                i += 1
            else:
                leftmost = min(leftmost, j)
                j -= 1
        return -1 if leftmost == N else leftmost


s = Solution()
print(s.leftMostColumnWithOne(BinaryMatrix([[0,0],[1,1]])))
print(s.leftMostColumnWithOne(BinaryMatrix([[0,0],[0,1]])))
print(s.leftMostColumnWithOne(BinaryMatrix([[0,0],[0,0]])))
print(s.leftMostColumnWithOne(BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])))
