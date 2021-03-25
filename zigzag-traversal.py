from collections import deque

"""
time: O(N) traverse all nodes
space: O(N/2) = O(N) we have N/2 nodes at most (at the lowest level) in queue
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
      return result
  queue = deque([root])
  
  left_to_right = True
  while len(queue) > 0:
      current_level = deque()
      for _ in range(len(queue)):
          node = queue.popleft()
          """
          current_levelのみをreverseすれば良い
          """
          if left_to_right:
              current_level.append(node.val)
          else:
              current_level.appendleft(node.val)
          
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
    
      left_to_right = not left_to_right
      result.append(list(current_level))
          
  # TODO: Write your code here
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
