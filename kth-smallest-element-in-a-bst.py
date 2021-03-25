"""
traverse the bst and get the kth element
bst: in-order traversal (left -> root -> right)

time: O(N)
space: O(N) in worst
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = 0
        def dfs(root, cur):
            nonlocal ans
            if root is None:
                return cur
            
            if ans:
                return cur
            
            cur = dfs(root.left, cur)
            cur += 1
            if cur == k:
                ans = root.val
            cur = dfs(root.right, cur)
            
            return cur
        
        dfs(root, 0)
        return ans

"""
use stack
O(H+K) H is the height
    - we go down to a leaf and pop k times
O(H) for stack
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        cur = root
        while len(stack) > 0:
            while cur:
                if cur.left:
                    stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            
            if cur.right:
                stack.append(cur.right)
            cur = cur.right

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
# print(s.kthSmallest(make([3,1,4,None,2]), 1))
print(s.kthSmallest(make([5,3,6,2,4,None,None,1]), 3))
