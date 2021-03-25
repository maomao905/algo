"""
A -> A' -> B -> B'
     A'   ->    B'

time: O(N) space: O(1)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        """
        A -> A' -> B -> B'
        """
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        
        """
        set random pointer in copied node
        """
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        """
        remove original nodes
        A' -> B' -> C'
        """
        cur = head.next
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        
        return head.next
