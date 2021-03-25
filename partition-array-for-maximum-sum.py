"""
memorization

O(n*k^2)
"""

from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def helper(i):
            if i >= N:
                return 0
            
            if i not in memo:
                memo[i] = max(helper(j+1) + max(arr[i:j+1]) * (j-i+1) for j in range(i, min(i+k, N)))
            
            return memo[i]
        
        N=len(arr)
        return helper(0)

"""
memorization
keep track of max in k window

O(nk) 
"""
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def helper(i):
            if i >= N:
                return 0
            
            if i not in memo:
                best = float('-inf')
                mx = float('-inf')
                for j in range(i, min(i+k, N)):
                    mx = max(arr[j], mx)
                    best = max(best, helper(j+1) + mx * (j-i+1))
                
                memo[i] = best
            
            return memo[i]
        
        N=len(arr)
        return helper(0)

s = Solution()
print(s.maxSumAfterPartitioning([1,15,7,9,2,5,10],3))
print(s.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3],4))
print(s.maxSumAfterPartitioning([1],1))
print(s.maxSumAfterPartitioning([7,2],1))
                
