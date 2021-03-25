"""
if knows(a, b) == 0: # a does not know b
    b is not celebrity
    a may be celebrity
else: # a knows b
    a is not celebrity
    b may be celebrity

thus, in every knows call we can reduce the celebrity candidates by one (becuase a or b is not celebrity)

cand = 0
for i in n:
    if knows(cand, i):
        cand = i
after we know the candidate
check if candidate is actually celebrity

for i in n:
    if knows(cand, i) or not knows(i, cand):
        return -1

we also can cache the knows API result using functools.lru_cache

time: O(N)
space: O(1)
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def knowsAPI(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(n):
            if self.knowsAPI(cand, i):
                cand = i

        for i in range(n):
            if i == cand:
                continue
            if self.knowsAPI(cand, i) or not self.knowsAPI(i, cand):
                return -1
        return cand
