"""
number of moves = number of stones - number of connected component

connected component means a group where stones are connected in a way that they share row and column
we can remove stones as long as they share the row/column, which leaves one stone in a connected component

if we know number of connected component, we get the answer
using union find, we can get the number

BFS until there is no stone, which share the row and the column

time: O(N^2) space: O(N)
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # build hashmap to efficiently look up the shared row and column
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for idx in range(len(stones)):
            i, j = stones[idx]
            rows[i].append(idx)
            cols[j].append(idx)
        
        
        num_of_connected_component = 0
        visited = set()
        for i in range(len(stones)):
            if i in visited:
                continue
            
            num_of_connected_component += 1
            q = deque([i])
            
            while len(q) > 0:
                j = q.popleft()
                visited.add(j)
                
                row, col = stones[j]
                
                for idx in rows[row]:
                    if idx not in visited:
                        q.append(idx)
                
                for idx in cols[col]:
                    if idx not in visited:
                        q.append(idx)
        
        return len(stones) - num_of_connected_component

"""
union-find
time: O(NlogN)? O(N)?
space: O(N)
"""
class Solution:
    def removeStones(self, stones):
        uf = {}
        def find(x):
            # path compression
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)
        
        for x, y in stones:    
            union(x, ~y)
        
        return len(stones) - len(set(find(x) for x in uf))

s = Solution()
print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(s.removeStones([[0,0]]))
print(s.removeStones([[0,1],[2,1],[2,3],[3,3],[3,4],[5,4],[5,5],[6,5],[6,6]]))
print(s.removeStones([[0,8],[0,2],[2,2],[3,3],[4,4],[3,5],[4,6],[7,7],[8,8]]))
