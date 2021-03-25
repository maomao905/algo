"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

time O(N) space O(N)
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()
        for node in tree:
            children.update(node.children)
        
        for node in tree:
            if node not in children:
                return node

"""
time O(N) space O(1)
"""                
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        xor = 0
        for node in tree:
            xor ^= node.val
            for node in node.children:
                xor ^= node.val
        
        for node in tree:
            if node.val == xor:
                return node
                
