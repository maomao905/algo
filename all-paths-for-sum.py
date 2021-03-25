class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

"""
DFS
- accumulate the sum and store sum in stack
- it reaches the leaf node, then if sum == target, save in result
# time: O(NlogN)
#     - extend list costs O(logN) at most
# space: O(N^2), O(N) in worst
"""
from collections import deque

def traverse(node, sum):
    # define the end
    sum -= node.val
    if node.left is None and node.right is None:
        if sum == 0:
            return [deque([node.val])]
        return []
    
    all_paths = []
    if node.left:
        l_paths = traverse(node.left, sum)
        if len(l_paths):
            for p in l_paths:
                p.appendleft(node.val)
        all_paths.extend(l_paths)
    
    if node.right:
        r_paths = traverse(node.right, sum)
        if len(r_paths):
            for p in r_paths:
                p.appendleft(node.val)
        all_paths.extend(r_paths)
    
    return all_paths
    

def find_paths(root, sum):
  return traverse(root, sum)


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
