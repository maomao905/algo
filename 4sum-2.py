"""
all A+B N^2 
all C+D N^2

2sum (A+B) + (C+D) -> O(N^2)

time: O(N^2) space O(N^2)
"""
from typing import List
from collections import Counter

class Solution:
    def merge(self, X, Y):
        cnt = Counter()
        for x in X:
            for y in Y:
                cnt[x+y] += 1
        return cnt
            
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        X = self.merge(A,B)
        Y = self.merge(C,D)
        
        ans = 0
        for x, cnt in X.items():
            if -x in Y:
                ans += cnt * Y[-x]
        return ans

s = Solution()
print(s.fourSumCount(A = [ 1, 2], B = [-2,-1], C = [-1, 2], D = [ 0, 2]))
            
