class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

"""
DFS
- recursive
    - in every node, we check the sum of all combinations including current node
        - check sum in reverse order
    - increment the path count if sum equals the given sum
    - backtrack the current path while we are going up the recursive call stack

time: O(N^2) in worst
    - traverse all N nodes
    - every time we check the sum up to N nodes
        - up to logN nodes in balanced binary tree
space: O(N) in worst
    - we save current path which has N nodes at most
    - up to logN nodes in balanced binary tree

"""
def count_paths(root, S):
    def recursive(node, current_path):
        if node is None:
            return 0
        
        current_path.append(node.val)
        
        cnt = 0
        sum = 0
        for val in current_path[::-1]:
            sum += val
            if sum == S:
                cnt += 1
        
        cnt += recursive(node.left, current_path)
        cnt += recursive(node.right, current_path)
        
        # backtrack
        current_path.pop()
        return cnt
    
    return recursive(root, [])


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
