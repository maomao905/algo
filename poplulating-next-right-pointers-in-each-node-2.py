"""
BFS

time: O(N), space: O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

"""
DFS

if it's perfect binary tree
    node_left.next = node_right
    right_node.next = parent.next.left

if it's binary tree
    we have to continue to find the next node until it is found

preorder traversal

time: O(N) space: O(H)
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def get_next(node):
            next = None
            while node.next:
                next = node.next.left or node.next.right
                if next:
                    return next
                node = node.next
        
        def dfs(node):
            next = get_next(node)
            
            if node.right:
                node.right.next = next
                dfs(node.right)
            
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = next
                dfs(node.left)
            
        if not root:
            return None
        dfs(root)
        return root
