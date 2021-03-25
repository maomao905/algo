"""
1. sort each row O(N^2logN)
2. DP
    memo key is i,prev_j O(N) since prev_j has only two choices
    j can be found in O(1) since it is sorted

O(N^2logN)
"""
from typing import List

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        def helper(i,prev_j):
            if i == N:
                return 0
            
            if (i,prev_j) not in memo:
                mi = float('inf')
                for n, j in (arr[i][0], arr[i][1]):
                    if prev_j == j:
                        continue
                    mi = min(mi, helper(i+1,j) + n)
                memo[i,prev_j] = mi
                # print((i,prev_j),mi+n)
            return memo[i,prev_j]
        
        N=len(arr)
        if N==1:
            return 0
        
        memo = {}
        for i in range(N):
            arr[i] = sorted([(n,j) for j, n in enumerate(arr[i])])
        return helper(0,-1)

"""
1. heap to get first 2 elements for each row O(N^2)
2. DP O(N)
O(N^2)
"""
from heapq import *
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        def helper(i,prev_j):
            if i == N:
                return 0
            
            if (i,prev_j) not in memo:
                mi = float('inf')
                for n, j in (arr[i][0], arr[i][1]):
                    if prev_j == j:
                        continue
                    mi = min(mi, helper(i+1,j) + n)
                memo[i,prev_j] = mi
                # print((i,prev_j),mi+n)
            return memo[i,prev_j]
        
        N=len(arr)
        if N==1:
            return 0
        
        memo = {}
        for i in range(N):
            arr[i] = [(n,j) for j, n in enumerate(arr[i])]
            arr[i] = nsmallest(2, arr[i])
        return helper(0,-1)

s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
        
        
