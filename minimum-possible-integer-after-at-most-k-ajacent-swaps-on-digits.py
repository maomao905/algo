"""
greedy

4321

1. create map for each number(0-9) and store the index for the number
1: [3]
2: [2]
3: [1]
4: [0]

2. iterate from zero and if we can consume k to move to front, do it
  increment all i-j indexes by 1 because ajacent elements move right
1432
1:[0] consume 3 from k -> k is 1 now
2:[3] move right
3:[2] move right
4:[1] move right

create map again O(N)
continue this process

O(N^2*k)

instead of updating all ajacent indexes, only keep track of how many steps moved from current index
use balanced binary tree because update is O(logN)

O(NlogN)
"""
from collections import deque, defaultdict
from sortedcontainers import SortedList
from string import digits
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        N=len(num)
        q = defaultdict(deque)
        
        for i in range(N):
            q[num[i]].append(i)
        
        res = list(num)
        seen = SortedList()
        for i in range(N):
            res[i] = num[i]
            for n in digits:
                if not q[n]:
                    continue
                
                # exact index considering all past swaps
                j = q[n][0] + len(seen) - seen.bisect(q[n][0])
                used = j-i # how many k it will consume
                if 0 <= used <= k:
                    k -= used
                    seen.add(q[n][0])
                    res[i] = num[q[n].popleft()]
                    break
        return ''.join(res)

s = Solution()
print(s.minInteger('4321',4))
print(s.minInteger('100',1))
print(s.minInteger('36789',1000))
print(s.minInteger('22',22))
print(s.minInteger('9438957234785635408',23))
