"""
(TLE)
add edge -> update all other nodes distance recursively
O(N^2)
"""

from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        
        dist = [0] * n
        
        def update_dist(node, d=2, parent=None):
            for ch in nodes[node]:
                if ch == parent:
                    continue
                dist[ch] = max(dist[ch], d)
                update_dist(ch, d+1, node)
        
        for a, b in edges:
            if a not in nodes and b not in nodes:
                dist[a] = dist[b] = 1
            elif a not in nodes:
                dist[a] = dist[b] + 1
                update_dist(b)
            else:
                dist[b] = dist[a] + 1
                update_dist(a)
            # print(a, b, dist)
            nodes[a].append(b)
            nodes[b].append(a)
        
        m = min(dist)
        ans = []
        for i in range(len(dist)):
            if dist[i] == m:
                ans.append(i)
        return ans

"""
topological sort
we want to find most dependent nodes
-> if we remove independent nodes(leaf nodes) one by one, finally most dependent nodes(centroids) are left

number of centroids in tree must be less than or equal to 2
"""
from collections import Counter, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        graph = defaultdict(list)
        in_degrees = Counter()
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            in_degrees[a] += 1
            in_degrees[b] += 1
        
        q = deque()
        # find most leaf node (most independent node)
        for node, deg in in_degrees.items():
            if deg == 1:
                q.append(node)
        
        remaining = n
        while len(q) > 0 and remaining > 2:
            remaining -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                
                in_degrees[node] -= 1
                for n in graph[node]:
                    in_degrees[n] -= 1
                    # now it's leaf node
                    if in_degrees[n] == 1:
                        q.append(n)
        
        return list(q)
                

s = Solution()
print(s.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(s.findMinHeightTrees(n = 1, edges = []))
print(s.findMinHeightTrees(n = 2, edges = [[0,1]]))
print(s.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
                
