"""
time: O(N), space: O(N)

 4
  \
   6
  / \
 5   7
 
 - recursively return small, large, which is actually the final answer
 - think what we need to return up to top node
 
 - if 6 is target
    - [4,5,6], [7] after split
    - when 7 is root node
        return None, 7
    - when 6 is root node
        # update small node
        return 6, 7
    - when 4 is root node
        # update small node
        return 4, 7
- if 5 is target
    - [4,5], [6,7] after split
    - when 5 is root node
        return 5, None
    - when 6 is root node
        # 6 is greater than target, think 6 is root node of large group
        return 5, 6 equals
    - when 4 is root node
        return 4, 6
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return None, None
        
        # target is in left
        if target < root.val:
            small, large = self.splitBST(root.left, target)
            root.left = large
            return small, root
        else:
            small, large = self.splitBST(root.right, target)
            root.right = small
            return root, large
        
