"""
union find
num of friend circles = number of connected component

time: O(N^2) space: O(N)
"""

from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = uf[find(y)]
        
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        
        return len(set([find(x) for x in uf]))

"""
DFS
time: O(N^2)
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in range(len(M)):
                if M[i][j] == 1:
                    dfs(j)
        
        cnt = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt
            
s = Solution()
print(s.findCircleNum(
[[1,1,0],
 [1,1,0],
 [0,0,1]]))
print(s.findCircleNum(
[[1,1,0],
 [1,1,1],
 [0,1,1]]
))
