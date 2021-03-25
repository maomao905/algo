# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS and add up the sum up to the leaf
time: O(N)
space: O(N)
"""
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        q = deque([(root.val, root)])
        
        while len(q) > 0:
            current_sum, node = q.popleft()
            if current_sum == sum and node.left is None and node.right is None:
                return True
            
            if node.left:
                q.append((current_sum + node.left.val, node.left))
            
            if node.right:
                q.append((current_sum + node.right.val, node.right))
            
        return False

"""
DFS
time: O(N)
space: O(logN) and O(N) in worst case e.g.) all the nodes exist in only left side untile the leaf
"""
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        stack = deque([(root.val, root)])
        
        while len(stack) > 0:
            current_sum, node = stack.pop()
            if current_sum == sum and node.left is None and node.right is None:
                return True
            
            if node.left:
                stack.append((current_sum + node.left.val, node.left))
            if node.right:
                stack.append((current_sum + node.right.val, node.right))
        
        return False

"""
recursion
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or \
            self.hasPathSum(root.right, sum)
