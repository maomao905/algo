"""
time O(N) space O(N)
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()
        while p:
            parents.add(p)
            p = p.parent
        
        while q:
            if q in parents:
                return q
            q = q.parent
        return None
            
"""
time O(N) space O(1)
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cur_p, cur_q = p, q
        while cur_p != cur_q:
            cur_p = cur_p.parent if cur_p else q
            cur_q = cur_q.parent if cur_q else p
        return cur_p
