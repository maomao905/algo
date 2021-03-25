"""
place mailbox as close to houses as possible
-> group houses and calculate distance from median of houses to mailbox

DP
allocate k mailboxes with minimum distance from median to mailbox

O(N^3*k)
"""

from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def median(i,j):
            mid = (i+j)//2
            return sum(abs(houses[mid] - pos) for pos in houses[i:j+1])
            
        N=len(houses)
        memo = {}
        def helper(i, remain):
            if remain == 0:
                return median(i,N-1)
            
            if (i,remain) not in memo:
                min_dist = float('inf')
                for j in range(i,N):
                    min_dist = min(min_dist, median(i,j) + helper(j+1, remain-1))
                memo[i,remain] = min_dist
            
            return memo[i,remain]
        
        houses.sort()
        r = helper(0, k-1)
        return r

"""
pre-calculate the median
O(N^3) for median calculation and O(N^2*k) for DP
O(N^3 + N^2*k)
"""
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def median(i,j):
            m = houses[(i+j)//2]
            return sum(abs(m - pos) for pos in houses[i:j+1])
            
        N=len(houses)
        memo = {}
        def helper(i, remain):
            if remain == 0:
                return medians[min(i,N-1),N-1]
            
            if i >= N:
                return float('inf')
            
            if (i,remain) not in memo:
                min_dist = float('inf')
                for j in range(i,N):
                    min_dist = min(min_dist, medians[i,j] + helper(j+1, remain-1))
                memo[i,remain] = min_dist
            
            return memo[i,remain]
        
        houses.sort()
        medians = {}
        for i in range(N):
            for j in range(i,N):
                medians[i,j] = median(i,j)
                
        return helper(0, k-1)

"""
calculate the median O(1) using cumulative sum
O(N^2*k)
"""
from itertools import accumulate
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def median(i,j):
            m1, m2 = (i+j)//2, (i+j+1)//2
            return (C[j+1] - C[m2]) - (C[m1+1] - C[i])
            
        N=len(houses)
        memo = {}
        def helper(i, remain):
            if remain == 0:
                return median(min(i,N-1),N-1)
            
            if i >= N:
                return float('inf')
            
            if (i,remain) not in memo:
                min_dist = float('inf')
                for j in range(i,N):
                    min_dist = min(min_dist, median(i,j) + helper(j+1, remain-1))
                memo[i,remain] = min_dist
            
            return memo[i,remain]
        
        houses.sort()
        C = [0] + list(accumulate(houses))
        
        return helper(0, k-1)

s = Solution()
print(s.minDistance([1,4,8,10,20],3))
print(s.minDistance([2,3,5,12,18],2))
print(s.minDistance([7,4,6,1],1))
print(s.minDistance([3,6,14,10],4))
print(s.minDistance([3,6],1))
        
