"""
Dijkstra
O(V+E)
"""
from typing import List
from collections import defaultdict
from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if not flights:
            return -1
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        heap = [(0, src, -1)]
        seen = {}
        while heap:
            cost, s, k = heappop(heap)
            if s == dst:
                return cost
            
            # use up k stops
            if k == K:
                continue
            k += 1
            
            for v, price in graph[s]:
                _cost = price + cost
                if v not in seen or seen[v][0] > _cost or seen[v][1] > k:
                    heappush(heap, (_cost, v, k))
                    seen[v] = (_cost, k)
        
        return -1

s = Solution()
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))
        
