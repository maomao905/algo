"""
greedy

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
sub  = [-2,-2,-2,3,3]

if sum(sub) < 0, we cannot travel around

calculate cumulative sum in anticlockwise
[3,6,4,2,0]

gas =  [3,1,1]
cost = [1,2,2]
sub =  [2,-1,-1]

time: O(N)
space: O(N)
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sub = [g-c for g, c in zip(gas, cost)]
        
        if sum(sub) < 0:
            return -1
        
        max_gas = -1
        max_idx = -1
        cum_sum = 0
        for i in reversed(range(len(sub))):
            cum_sum += sub[i]
            if cum_sum > max_gas:
                max_gas = cum_sum
                max_idx = i
        
        return max_idx

s = Solution()
print(s.canCompleteCircuit(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(s.canCompleteCircuit(gas  = [2,3,4], cost = [3,4,3]))
print(s.canCompleteCircuit([3,1,1], [1,2,2]))
