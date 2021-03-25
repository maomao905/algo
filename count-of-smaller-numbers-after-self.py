"""
[5,2,6,1]
better to look from the right side

1 ->  6  ->   6 
     /       /
    1       2
           /
          1
          
             2             2
            / \    ->     / \
           1   6         1   6
                            /
                           5


we need to keep track of kind of sorted array                              
1 -> [] -> 0
6 -> [1] -> binary search -> 0
  -> insert and balance [1,6] O(logN)
2 -> [1,6] -> binary search -> 1
5 -> [1,2,6] -> binary search -> 2

sort and binary search takes O(logN) every step -> O(NlogN)
"""
from typing import List

class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
        self.less_count = 0
        self.eq_count = 1

"""
ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/370869/Multiple-solutions-with-very-detailed-comments-and-explanation  
https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm
"""



class AVL_Tree(object):
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key)
            root.less_count += 1
        else: 
            root.right = self.insert(root.right, key)
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        """
        right rotation
            2          1
           /          / \
          1   ->     0   2
         /
        0
        """
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
        
        """
        left rotation
        0           1
         \         / \
          1   ->  0   2
           \
            2
        """
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
        
        """
        left-right rotation
            2            2        1
           /            /        / \
          0     ->     1   ->   0   2
           \          /
            1        0
        """
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        
        """
        right-left rotation
           0           0               1
            \           \             / \
             2   ->      1     ->    0   2
            /             \
           1               2
        """
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root, 
  
    def leftRotate(self, z): 
        """
        left rotation
        0           1
         \         / \
          1   ->  0   2
           \
            2
        z = 0
        y = 1
        t2 = None
        
        y.left = z  (1.left = 0)
        z.right = t2 (0.right = None)
        """
  
        y = z.right
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
        """
        right rotation
            2          1
           /          / \
          1   ->     0   2
         /
        0
        z = 2
        y = 1
        """
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def get_node(self, root, n):
        node = root
        while True:
            if node.val == n:
                return node
            if node.val < n:
                node = node.right
            else:
                node = node.left
    
    def get_height(self, node):
        h = 0
        while node:
            node = node.left
            h += 1
        return h
    
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        h = self.get_height(root)
        leaf_left = 2**(h-1)
        leaf_right = 2**h - 1
        
        while leaf_left < leaf_right:
            mid = (leaf_left + leaf_right)//2 + 1
            cur = root
            for bit in bin(mid)[3:]:
                if bit == '0':
                    cur = cur.left
                else:
                    cur = cur.right
            
            if cur is None:
                leaf_right = mid-1
            else:
                leaf_left = mid
        
        return leaf_left
  
    def count_smaller_nums(self, root, n):
        node = self.get_node(root, n)
        return self.countNodes(node.left)
    
    def _print(self, root):
        q = deque([root])
        res = []
        while len(q) > 0:
            node = q.popleft()
            if not node:
                continue
            
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        print(res)
        
        
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = AVL_Tree()
        root = None
        res = []
        for n in reversed(nums):
            root = tree.insert(root, n)
            res.append(tree.count_smaller_nums(root, n))
            tree._print(root)
        
        return list(reversed(res))

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

"""
balanced binary tree
sortedlist

use bisect_left becuase we want the count of smaller numbers (it does not include the equal number)

O(NlogN)
"""
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N=len(nums)
        res = [0] * N
        sl = SortedList()
        for i in reversed(range(N)):
            j = sl.bisect_left(nums[i])
            res[i] = j
            sl.add(nums[i])
        return res

"""
binary indexed tree

O(NlogN)
"""
class BIT():
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (self.N+1)
        
    def update(self, i):
        i += 1
        while i <= self.N:
            self.tree[i] += 1
            i += i & -i
    
    def prefix_sum(self, i):
        _sum = 0
        i += 1
        while i:
            _sum += self.tree[i]
            i -= i & -i
        return _sum

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N=len(nums)
        rank = {n: i+1 for i, n in enumerate(sorted(set(nums)))}
        res = [0] * N
        bit = BIT(N+1)
        for i in reversed(range(N)):
            j = rank[nums[i]]
            res[i] = bit.prefix_sum(j-1)
            bit.update(j)
        return res
            
s = Solution()
print(s.countSmaller([5,2,6,1]))
print(s.countSmaller([5,2,2,2]))
print(s.countSmaller([-1]))
print(s.countSmaller([-1,-1]))
