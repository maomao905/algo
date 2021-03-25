# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: O(M) M: minimum node size 
space: O(logM)
"""
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 片方がnullの場合、もう片方を返すので、すべてのnodeをtraverseしなくてもminimum nodeだけで済む
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        print(t1.val)
        node = TreeNode(val=t1.val+t2.val)
        
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        
        return node
        
