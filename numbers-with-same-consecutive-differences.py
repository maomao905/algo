"""
O(2^n)
"""

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        memo = {}
        def helper(i):
            if i == 0:
                return list(range(10))
            
            end = 0 if i == n-1 else -1
            res = []
            mul = 10 ** i
            div = 10**(i-1)
            for _n in helper(i-1):
                m = _n // div
                for j in set([m+k,m-k]):
                    if end < j < 10:
                        res.append((j) * mul + _n)
            
            return res
        
        return helper(n-1)

s = Solution()
print(s.numsSameConsecDiff(3,7))
print(s.numsSameConsecDiff(5,2))
print(s.numsSameConsecDiff(2,2))
print(s.numsSameConsecDiff(2,0))
