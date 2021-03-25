"""
simulation

O(NlogN)
"""
from typing import List
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N=len(deck)
        deck.sort(reverse=True)
        res = [0] * N
        q = deque(range(N))
        
        while q:
            i = q.popleft()　
            res[i] = deck.pop()
            
            if q:
                q.append(q.popleft())
        return res

"""
simpler code using rotate method of deque
"""
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N=len(deck)
        res = [0] * N
        q = deque(range(N))
        
        for n in sorted(deck):
            i = q.popleft()
            res[i] = n
            
            if q:
                q.rotate(-1)
        return res

s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
