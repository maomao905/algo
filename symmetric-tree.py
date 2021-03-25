"""
BFS using stack
pop two nodes each time
compare the values
push first node's left node, second node's right node, first nodes' right node, second nodes' left node

time: O(N)
space: O(N)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [root.left, root.right]
        
        while len(stack) > 0:
            l = stack.pop()
            r = stack.pop()
            
            l_val = l.val if l else None
            r_val = r.val if r else None
            
            if l_val != r_val:
                return False
            
            if not l and not r:
                continue
            
            stack.append(l.left)
            stack.append(r.right)
            stack.append(l.right)
            stack.append(r.left)
        
        return True

"""
recursion
time: O(N)
space: O(N) in worst
"""

class Solution:
    def is_mirror(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        return left.val == right.val and self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)


s = Solution()
print(s.isSymmetric(make([1,2,2,3,4,4,3])))
print(s.isSymmetric(make([1,2,2,None,3,None,3])))
