# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(node, depth=1):
            if node is None:
                return
            
            if depth < d-1:
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
            else:
                new_node_left = TreeNode(v)
                new_node_left.left = node.left
                node.left = new_node_left
                new_node_right = TreeNode(v)
                new_node_right.right = node.right
                node.right = new_node_right
        
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        else:
            dfs(root)
            return root
