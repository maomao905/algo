"""
union find

it does not work in this case: [[1],[],[0,3],[1]]
we cannot enter second room
"""
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        N=len(rooms)
        uf = {i:i for i in range(N)}
        for i in range(N):
            for room in rooms[i]:
                union(i, room)
        
        return len(set(find(i) for i in range(N))) == 1

"""
DFS
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        
        def dfs(i):
            seen.add(i)
            
            for j in rooms[i]:
                if j not in seen:
                    dfs(j)
        
        N=len(rooms)
        seen = set()
        dfs(0)
        return len(seen) == N

s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(s.canVisitAllRooms([[]]))
print(s.canVisitAllRooms([[1],[],[0,3],[1]]))
