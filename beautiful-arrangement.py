"""
create candidates map {value: index list}
1: 1,2,3   1
2: 2,4,6   1,2
3: 3,6,9   1,3
4: 4,8,12  1,2,4
5: 5,10    1,5

{
  1: [1,2,3,4,5]
  2: [1,2,4]
  3: [1,3]
  4: [1,2,4]
  5: [1,5]
}
available value list
[True, True, True, True, True]
after choosing the value, make it False

1 <= n <= 15 -> O(1) to create this map

recursively with backtrack
time O(N!) space O(N)
"""
from collections import defaultdict
class Solution:
    def countArrangement(self, n: int) -> int:
        cands = defaultdict(set)
        for i in range(1,n+1):
            x = i
            while x <= n:
                cands[x-1].add(i-1)
                cands[i-1].add(x-1)
                x += i
        val = [True] * n
        
        def recursive(i):
            if i == n:
                return 1
            
            cnt = 0
            for x in cands[i]:
                if not val[x]:
                    continue
                val[x] = False
                cnt += recursive(i+1)
                val[x] = True
            return cnt
        
        return recursive(0)

s = Solution()
print(s.countArrangement(1))
print(s.countArrangement(2))
                
                
            
        
