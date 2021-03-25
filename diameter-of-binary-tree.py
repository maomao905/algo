"""
max depth up to node = left subtree depth + right subtree depth
use dfs to get depth of each node

time: O(N)
space: O(N) in worst
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal max_diameter
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            max_diameter = max(max_diameter, diameter)
            # add 1 for the edge from current ndde to child node
            return max(left, right) + 1
        
        
        max_diameter = 0
        dfs(root)
        return max_diameter

from collections import deque
q = deque([1,2,3,4,5])
root = TreeNode(val=q.popleft())
node_q = deque([root])

while len(q) > 0:
    node = node_q.popleft()
    node.left = TreeNode(val=q.popleft())
    node.right = TreeNode(val=q.popleft())
    node_q.append(root.left)
    node_q.append(root.right)

s = Solution()
print(s.diameterOfBinaryTree(root))
