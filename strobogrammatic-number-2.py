"""
n = 1 0, 1, 8 -> 3
n = 2 11,69,88,96 -> 4
n = 3 <1,8><n=1><1,8>
n = 4 <1,8><n=2><1,8>
n = 5 <1,8><n=3><1,8>
n = 6 <1,8><n=4><1,8>
"""
from typing import List
from collections import deque
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        def helper(i):
            if i == 1:
                return [deque([j]) for j in ('0','1','8')]
            elif i == 2:
                return [deque([j]) for j in ('00','11','69','88','96')]
            
            res = []
            for q in helper(i-2):
                for s, e in (('0','0'),('1','1'),('8','8'),('6','9'),('9','6')):
                    new_q = q.copy()
                    new_q.appendleft(s)
                    new_q.append(e)
                    res.append(new_q)
            return res
        
        res = helper(n)
        return [''.join(q) for q in res if n == 1 or q[0][0] != '0']
        
s = Solution()
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(2))
        
        
