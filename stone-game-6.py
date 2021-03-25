from typing import List

"""
(TLE)
try all possible cases

O(2^(N/2))
"""
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        def helper(stones, diff, is_alice):
            if not stones:
                if diff > 0:
                    return 1
                elif diff < 0:
                    return -1
                else:
                    return 0
            
            res = float('-inf') if is_alice else float('inf')
            seen = set()
            for s in stones:
                if s not in seen:
                    d = diff + (aliceValues[s] if is_alice else -bobValues[s])
                    stones.remove(s)
                    r = helper(stones, d, not is_alice)
                    if is_alice:
                        res = max(r, res)
                    else:
                        res = min(r, res)
                    stones.add(s)
                seen.add(s)
            return res
        
        N=len(aliceValues)
        stones = set(range(N))
        return helper(stones, 0, True)

"""
Alice takes a, Bob takes b
a1, a2
b1, b2

there are two possibilities
Alice takes a1 and Bob takes b2
Alice takes a2 and Bob takes b1

if choosing first stone is the best choice,
    a1-b2 > a2-b1 <=> a1 + b1 > a2 + b2

we can sort by a + b

O(NlogN)
"""

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        values = sorted(zip(aliceValues, bobValues), key=sum)
        
        alice = sum(map(lambda x: x[0], values[::-2])) # takes from the last
        bob = sum(map(lambda x: x[1], values[-2::-2])) # takes from the second last
        
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0

s = Solution()
print(s.stoneGameVI([1,3],[2,1]))
print(s.stoneGameVI([1,2],[3,1]))
print(s.stoneGameVI([2,4,3],[1,6,7]))
                
