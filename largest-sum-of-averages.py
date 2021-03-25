"""
in every index, partition or not as long as k > 0
use cumulative sum to get sum([i,j]) in O(1)

O(2^K) without memorization

O(N^2 * K) with memorization

memo[i,K] = sum of rest partitions
"""

from typing import List
from itertools import accumulate
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        def get_sum(i,j):
            i_sum = cum_sum[i-1] if i>0 else 0
            return cum_sum[j]-i_sum
        
        def helper(i, k):
            
            if k == 0 or i == N-1:
                return get_sum(i,N-1)/(N-i)
            
            if (i,k) not in memo:
                memo[i,k] = max(helper(j, k-1) + get_sum(i,j-1)/(j-i) for j in range(i+1,N))
            return memo[i,k]
        
        memo = {}
        N = len(A)
        cum_sum = list(accumulate(A))
        return helper(0, K-1)

s = Solution()
print(s.largestSumOfAverages([9,1,2,3,9],3))
print(s.largestSumOfAverages([10,10,10,9],3))
print(s.largestSumOfAverages([4,1,7,5,6,2,3],4))
# print(s.largestSumOfAverages([1, 2, 3, 4, 5, 6, 7],4))
