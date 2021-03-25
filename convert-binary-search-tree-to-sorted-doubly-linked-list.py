"""
in-place transformation
inorder traversal
1 -> 2 -> 3

node1.left = node5 (predecessor)
node1.right = node2 (successor)

node2.left = node1
node2.right = node3

node4.left = node3 --> node2 in BST
node4.right = node5

predecessor is basically smaller number
successor is basically larger number

time: O(N)
space: O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        small, large = self.inorder(root)
        small.left = large
        large.right = small
        return small
        
    def inorder(self, node):
        if node is None:
            return None, None
        small_left, large_left = self.inorder(node.left)
        if large_left:
            node.left = large_left
            large_left.right = node
        small_right, large_right = self.inorder(node.right)
        if small_right:
            node.right = small_right
            small_right.left = node
        return small_left or node, large_right or node
