"""
   5
 /    \
2      10
      /   \
     7     12
    / \    / \
   6   8  11 13

e.g.) delete 10
replace 10 with 7 and add 8's right node to 12
- find a target node O(logN)
- replace it with left node
- find right-most node left subtree O(logN)
- add right-most node'right node to the right node (12)
"""


from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        
        if root.val == key:
            right_most_node = root.left
            
            while right_most_node and right_most_node.right:
                right_most_node = right_most_node.right
            
            if right_most_node:
                right_most_node.right = root.right
            return root.left or root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root

s = Solution()
print(s.deleteNode(make([5,3,6,2,4,None,7]), 3))
