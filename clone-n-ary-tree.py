"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import deque
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        dummy = Node()
        q = deque([(root, dummy)]) # original node and clone parent node
        
        while q:
            node, parent = q.popleft()
            clone = Node(node.val)
            
            parent.children.append(clone)
            
            for ch in node.children:
                q.append((ch, clone))
        
        return dummy.children[0]
            
            
