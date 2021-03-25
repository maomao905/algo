"""
recursion
sum = sum(each node value * (level-1) * 10)

DFS
left -> right -> root (post order)

        4
       / \
      9   0
     / \
    5   1
   /
  6

when we add 4, we need to add left sum + right sum + 4000 + 400 + 40
4000 + 400 + 40 = 4 * 10^3 + 4 * 10^2 + 4 * 10^1
-> we cannot multiply by the one returned value from child nodes
-> child nodes need to return lists

dfs(node, level)
 if node is None:
     return [[0]]
 return [subtree.append(node.val) for subtree in dfs(node.left))] + [subtree.append(node.val) for subtree in dfs(node.right))]
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

"""
post-order approach
left -> right -> root
time: O(N^2)
"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return []
            if not node.left and not node.right:
                return [[str(node.val)]]
            
            left = []
            if node.left:
                left = dfs(node.left)
                for subtree in left:
                    subtree.append(str(node.val))
            
            right = []
            if node.right:
                right = dfs(node.right)
                for subtree in right:
                    subtree.append(str(node.val))
            return left + right
        
        _sum = 0
        res = dfs(root)
        for r in res:
            r.reverse()
            _sum += int(''.join(r))
        return _sum

"""
pre-order
root -> left -> right
root * 10 times + left.val + right.val

time: O(N)
space: O(N)
"""

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        def dfs(node, _sum):
            _sum = node.val + _sum * 10
            if node.left is None and node.right is None:
                res.append(_sum)
                return
            if node.left:
                dfs(node.left, _sum)
            if node.right:
                dfs(node.right, _sum)
        
        if root is None:
            return 0
        dfs(root, 0)
        return sum(res)

s = Solution()
print(s.sumNumbers(make([1,2,3])))
print(s.sumNumbers(make([4,9,0,5,1])))
print(s.sumNumbers(make([1,0])))

        
