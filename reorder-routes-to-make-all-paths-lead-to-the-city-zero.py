"""
it's tree and there is no cycle and only one direction from node to 0
That's why the only way to reach 0 is reverse the route
"""
from typing import List
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        
        seen = set()
        def dfs(node):
            seen.add(node)
            return sum(dfs(_node) + int(is_reverse) for _node, is_reverse in graph[node] if _node not in seen)
        
        return dfs(0)

s = Solution()
print(s.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(s.minReorder(5,[[1,0],[1,2],[3,2],[3,4]]))
print(s.minReorder(3,[[1,0],[2,0]]))
                
        
        
