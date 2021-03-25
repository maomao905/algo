"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(cur):
            last = None
            while cur:
                last = cur
                if cur.child is None:
                    cur = cur.next
                    continue
                    
                old_next = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                # get last node of children
                node = helper(cur.child)
                cur.child = None
                if not old_next:
                    return node
                node.next = old_next
                old_next.prev = node
                cur = old_next
            return last
            
        helper(head)
        return head
        
