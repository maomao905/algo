class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)

from collections import deque
def make(vals):
  if len(vals) == 0:
      return None
  val_q = deque(vals)
  root = TreeNode(val=val_q.popleft())
  node_q = deque([root])

  while len(val_q) > 0:
      node = node_q.popleft()
      
      left = val_q.popleft()
      if left is not None:
          node.left = TreeNode(val=left)
      
      if len(val_q) > 0:
          right = val_q.popleft()
          if right is not None:
              node.right = TreeNode(val=right)
      
      if node.left:
          node_q.append(node.left)
      if node.right:
          node_q.append(node.right)
  return root

def show(root):
    if not root:
        return
    
    q = deque([root])
    
    res = []
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return res
            
