"""
BFS
store nodes of each level in queue and connect it one by one
O(N) in worst

DFS
it's like BST
you need to connect to node which has next larger value

1. connect closest left right nodes
root.left.next = root.right

2. the only thing we have to care about is when they don't share same parent node (5 -> 6)
     1
    /  \
   2    3
  / \   / \
 4   5 6   7

5 = 2.right
6 = 3.left

-> node.right.next = node.next.left
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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node is None:
                return None, None
            
            if node.left:
                node.left.next = node.right
                
                # if node is root, we don't need to connect next pointer
                if node.next:
                    node.right.next = node.next.left
                
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return root
            
