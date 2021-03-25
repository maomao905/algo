"""
heap
O(NlogK)
"""

from typing import List
from heapq import *
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, key=lambda x: math.sqrt(x[0]**2 + x[1]**2))

"""
quick select
O(N)
"""

from random import randint

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def less(i, j):
            return arr[i][0] < arr[j][0]
            
        def partition(l, r, pivot):
            i = l
            # move pivot to the end
            arr[pivot], arr[r] = arr[r], arr[pivot]
            pivot = r
            # move smaller elements to the left
            # move greater elements to the right
            for j in range(l, r):
                if less(j, pivot):
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            # place pivot to the right index
            arr[r], arr[i] = arr[i], arr[r]
            return i
    
        def kth_smallest(l, r, k):
            if l == r:
                return l
            pivot = randint(l,r)
            pivot = partition(l, r, pivot)
            if pivot == k:
                return pivot
            elif k < pivot:
                # go left
                return kth_smallest(l, pivot-1, k)
            else:
                # go right
                return kth_smallest(pivot+1, r, k)
        
        N=len(points)
        if K==N:
            return points
        
        arr = [(x**2 + y**2, [x,y]) for x, y in points]
        return [p for _, p in arr[:kth_smallest(0, N-1, K)]]

s = Solution()
print(s.kClosest([[1,3],[-2,2]], K=1))
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))
print(s.kClosest([[0,1],[1,0]], K=2))
print(s.kClosest([[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]],1))
