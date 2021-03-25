"""
    3
   / \
  9  20
    /  \
   15   7

inorder (left -> root -> right) = [9,3,15,20,7]
postorder (left -> right -> root) = [9,15,7,20,3]

what we can dertermine from given order?
inorder -> determine from left to right
postorder -> determine from bottom to up
        　-> if it reverses, root to bottom

use postorder to decide root node and inorder to decide left subtree and right subtree

1. postorder [3] (root is 3)
inorder left subtree [3], right subtree [15,20,7]

2. root is 20 and left [3,15], right [7]
3. root is 7 and left [], right []

time and space: O(N)
"""

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_idx_map = {inorder[i]: i for i in range(len(inorder))}
        
        postorder_idx = len(postorder) - 1
        
        # [9,3,15,20,7]
        # root: 3 left: [9], right: [15,20,7]
        # root: 20 left: [15], right: [7]
        # root: 7  left > right return None
        # [9,15,7,20,3]
        #       ^    
        
        # left and right are inorder's range
        def build(left, right):
            if left > right:
                return
            
            nonlocal postorder_idx
            # decide root using postorder
            root_val = postorder[postorder_idx]
            root = TreeNode(val=root_val)
            
            postorder_idx -= 1
            
            # decide the left and right subtree boundary
            root.right = build(inorder_idx_map[root_val]+1, right)
            root.left = build(left, inorder_idx_map[root_val]-1)
            
            return root
        
        return build(0, len(inorder)-1)
        
