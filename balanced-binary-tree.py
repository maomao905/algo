"""
height of all the leaf nodes
visite all nodes and check height of left subtree and right subtree differ by no more than 1
    -> recursively going up to the root node
DFS
    - recursion
    - stack

time: O(N)
space: O(H) O(N) in worst
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return 0, True
            
            left, left_balanced = dfs(node.left)
            right, right_balanced = dfs(node.right)
            
            return max(left, right) + 1, left_balanced and right_balanced and abs(left - right) <= 1
        
        _, balanced = dfs(root)
        return balanced



from collections import deque
def make(vals):
  val_q = deque(vals)
  root = TreeNode(val=val_q.popleft())
  node_q = deque([root])

  while len(val_q) > 0:
      node = node_q.popleft()
      
      left = val_q.popleft()
      if left:
          node.left = TreeNode(val=left)
      
      if len(val_q) > 0:
          right = val_q.popleft()
          if right:
              node.right = TreeNode(val=right)
      
      if node.left:
          node_q.append(node.left)
      if node.right:
          node_q.append(node.right)
  return root

s = Solution()
print(s.isBalanced(make([3,9,20,None,None,15,7])))
print(s.isBalanced(make([1,2,2,3,3,None,None,4,4])))
