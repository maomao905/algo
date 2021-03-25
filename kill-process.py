from typing import List
from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        ch = defaultdict(list)
        for p, pp in zip(pid, ppid):
            ch[pp].append(p)
        
        res = []
        def dfs(i):
            res.append(i)
            for j in ch[i]:
                dfs(j)
        
        dfs(kill)
        return res

s = Solution()
print(s.killProcess([1,3,10,5],[3,0,5,3], 5))
print(s.killProcess([1,3,10,5],[3,0,5,3], 3))
