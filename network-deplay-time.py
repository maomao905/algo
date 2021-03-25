"""
DFS
- start from K and as long as there is additional path, keep traversing, and save the minimum time to take to the node
- there is an unreacheable node, which means there is no path to the node in the input
    - to find such nodes, we keep track of visited nodes

time: O(N^N) when we choose node A, A connects to up to N-1 nodes except for A, and it applies to all N nodes
space: O(E+N) O(E) for stroing all edges in graph and O(E) for recursion stack
"""

from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited = defaultdict(int)
        
        graph = defaultdict(list)
        for s, d, w in times:
            graph[s].append((d, w))
        
        # to speed up
        [graph[s].sort(key=lambda x: x[1]) for s in graph]
        
        def dfs(s, w):
            visited[s] = w
            if s not in graph:
                return
            
            for d, _w in graph[s]:
                W = w + _w
                if d not in visited or W < visited[d]:
                    dfs(d, W)
        
        dfs(K, 0)
        if len(visited) < N:
            return -1
        
        return max(w for w in visited.values())

"""
naive Djikstra algorithm
find the shortest-path node every time and mark it visited, continue this process until all nodes are visited
it's kind of like BFS

time: O(N^N) every time we check the distance to all the other nodes
space: O(N+E)
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float('inf')] * N
        
        visited = {}
        
        graph = defaultdict(list)
        
        for s, d, w in times:
            graph[s-1].append((d-1, w))
            
        dist[K-1] = 0
        
        while len(visited) < N:
            # find the minimum time node
            shortest_node, shortest_dist = None, float('inf')
            for i in range(len(dist)):
                if i not in visited:
                    if dist[i] < shortest_dist:
                        shortest_node = i
                        shortest_dist = dist[i]
            
            # there may be a node which has no incoming edges, so that the node will never be updated
            if shortest_node is None:
                break
            
            visited[shortest_node] = True
            
            # update the distance
            for j, w in graph[shortest_node]:
                if j not in visited:
                    dist[j] = min(shortest_dist + w, dist[j])
                    
        ans = max(dist)
        if ans == float('inf'):
            return -1
        return ans


"""
Djikstra algorithm using heap
find the shortest path in O(1) using heap, and add 

# first find the shortest path from the origin O(1)
# push all ajacent nodes with updated distance log(E)
# get the shortest path in O(1) and mark visited
# continue this step all nodes are visited

time: O(ElogE) E: num of edges
space: O(E+N) E for heap and graph, N for visited hash map
"""

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        edges = defaultdict(list)
        
        for s, d, w in times:
            edges[s].append((d, w))
        
        heap = [(0, K)]
        res = [0] * N
        visited = {}
        
        while len(heap) > 0:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            res[node-1] = dist
            
            visited[node] = True
            
            for d, w in edges[node]:
                heapq.heappush(heap, (w + dist, d))
        
        return max(res) if len(visited) == N else -1

s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))
print(s.networkDelayTime([[1,2,1],[2,1,3]],2,2))
            
