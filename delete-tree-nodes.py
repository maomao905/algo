"""
topological sort
1. start from leaf nodes which have no children and sum the value to parent node value
repeat this process up to root node

2. now we know nodes where value is zero, we need to make sure all children values should be zero

time O(N) space O(N)
"""
from collections import defaultdict, deque, Counter
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = defaultdict(list)
        in_degrees = Counter()
        N=len(parent)
        for i in range(N):
            if parent[i] == -1:
                continue
            tree[parent[i]].append(i)
            in_degrees[parent[i]] += 1
        
        q = deque([i for i in range(N) if i not in tree])
        
        zero_q = deque()
        while q:
            i = q.popleft()
            if value[i] == 0:
                zero_q.append(i)
            
            if parent[i] != -1:
                value[parent[i]] += value[i]
            
            in_degrees[parent[i]] -= 1
            if in_degrees[parent[i]] == 0:
                q.append(parent[i])
        
        while zero_q:
            i = zero_q.popleft()
            for ch in tree[i]:
                if value[ch] != 0:
                    zero_q.append(ch)
                    value[ch] = 0
        
        return N - value.count(0)

s = Solution()
print(s.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]))
print(s.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]))
print(s.deleteTreeNodes(nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]))
print(s.deleteTreeNodes(nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]))
print(s.deleteTreeNodes(38,
[-1,7,0,2,22,25,2,0,7,14,25,22,25,14,0,22,22,2,14,14,22,14,25,2,14,0,32,2,2,32,25,22,0,2,2,22,14,14],
[-95448,-60462,-61595,68758,68709,32611,22289,-39426,-78078,91853,-56848,26101,-87072,-32610,98615,22254,-70154,86962,-93287,12168,90664,49974,-13514,23360,-12832,-64062,-54784,73509,78689,-72481,-338,81909,-63543,-88910,65612,36464,44448,-29505]
))
                
