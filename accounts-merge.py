"""
union-find

L average account length
N number of accounts
time O(LNlogN) space O(L+N)
"""
from typing import List
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)
        
        names = {}
        for a in accounts:
            for i in range(1, len(a)):
                names[a[i]] = a[0]
                if i == 1:
                    union(a[i], a[i])
                else:
                    union(a[i], a[i-1])
        d = {}
        res = []
        for x in uf:
            root_email = find(x)
            if root_email not in d:
                res.append([names[root_email]])
                res[-1].append(x)
                d[root_email] = len(res)-1
            else:
                res[d[root_email]].append(x)
        
        for i in range(len(res)):
            res[i].sort()
        return res

s = Solution()
print(s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
                
        
            
            
