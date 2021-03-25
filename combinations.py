"""
1-n, k numbers
backtracking
if we choose one of n for the first element(k left), then we will choose one of n-1 for the next element (k-1 left)
we continue k elements

number of combinations: nCk
time: nCk * k (number of all elements)
space: nCk * k
"""

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursive(comb, start):
            if len(comb) == k:
                res.append(list(comb))
            
            for j in range(start, n+1):
                comb.append(j)
                recursive(comb, j+1)
                comb.pop()
        
        res = []
        recursive([], 1)
        return res



s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))
