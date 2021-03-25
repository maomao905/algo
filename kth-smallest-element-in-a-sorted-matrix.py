"""
heap 
we put the cell of first column and every row in heap
we pop the smallest value from heap and push the new value from the row which had the value we popped out
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8

heap = [1,10,12]
1 pop 1 and push 5 [5,10,12]
2 pop 5 and push 9 [9,10,12]
3 pop 9            [10,12]
4 pop 10 and push 11 [11,12]
...

time: KlogK + KlogK = O(KlogK)
space: O(K)
"""

from typing import List
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        M,N=len(matrix),len(matrix[0])
        
        heap = []
        for i in range(min(k,M)):
            heappush(heap, (matrix[i][0], i, 0))
        
        cnt = 0
        for _ in range(k-1):
            # print(heap)
            _, i, j = heappop(heap)
            if j+1 < N:
                heappush(heap, (matrix[i][j+1], i, j+1))
        
        return heap[0][0]

s = Solution()
print(s.kthSmallest(matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],k = 8))
print(s.kthSmallest(matrix = [
   [ 0,  1,  1],
   [ 1,  1,  1],
   [ 1,  2,  2]
],k = 2))
        
        
        
        
