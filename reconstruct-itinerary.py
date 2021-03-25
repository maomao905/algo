"""
DFS
"""

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(s):
            while graph[s]:
                d = graph[s].pop()
                dfs(d)
            # there is no plane from the source, which means that is the goal
            # we append final destination first, and reverse it at the end
            res.append(s)
            
        res = []
        graph = defaultdict(list)
        for s, d in tickets:
            graph[s].append(d)
            
        for s in graph:
            graph[s].sort(reverse=True)
        
        dfs('JFK')
        return res[::-1]

s = Solution()
# print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
        
            
