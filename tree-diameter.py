"""
start from most independent edge and cut next independent edge one by one until less than 2 centroids remain
number of times we cut edges = radius
if 1 centroid remains, radius * 2
if 2 centroid remains, radius * 2 + 1 because there is an edge between centroids

topological sort

time: O(V+E) space: O(V+E)
"""

from typing import List
from collections import defaultdict, Counter, deque
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degrees = Counter()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            in_degrees[x] += 1
            in_degrees[y] += 1
        
        leaf_nodes = [node for node, deg in in_degrees.items() if deg == 1]
        q = deque(leaf_nodes)
        
        radius = 0
        while len(graph) > 2:
            for _ in range(len(q)):
                node = q.popleft()
                for neigh in graph[node]:
                    in_degrees[neigh] -= 1
                    # now it's leaf node
                    if in_degrees[neigh] == 1:
                        q.append(neigh)
                del graph[node]
            radius += 1
            # print(graph)
        
        if len(q) == 1:
            return radius * 2
        else:
            return radius * 2 + 1

s = Solution()
print(s.treeDiameter([[0,1],[0,2]]))
print(s.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
