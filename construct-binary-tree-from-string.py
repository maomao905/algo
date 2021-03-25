"""
"4(2(3)(1))(6(5))"
1. push value into stack
2. when ( is found, call recursive function
3. when ) is found, create node object and return the object

time: O(S) space: O(S)

"4
  (2(3)(1))
  (6(5))"
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return
        
        N = len(s)
        
        def get_value(i):
            if i < N and s[i] in '()':
                i += 1
            
            for j in range(i,N):
                if s[j] in '()':
                    val = s[i:j]
                    node = TreeNode(int(val)) if val else None
                    return node, j, s[j] == ')'
            return None, N
            
        
        def recursive(i):
            if i >= N:
                return None, i
            
            # if s[i] == ')':
            #     return None, i
            
            # 4
            node, i, end = get_value(i)
            if node is None or end:
                return node, i
            # print(node.val)
            
            node.left, i = recursive(i+1)
            node.right, i = recursive(i+1)
            
            return node, i
        
        return recursive(0)[0]

"""
1. extract value
    until s[i] == (, level += 1
    push value and level into value stack
2. if s[i] == ), pop stack, level -= 1
    push into node stack
    if there is a node which level is smaller than current node level,
        pop and node.left = x, node.right = y
time: O(N)
"""

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def push(i,j):
            val = s[i:j]
            if val:
                val_stack.append((int(val), level))
            
        def pop():
            if val_stack:
                val, _level = val_stack.pop()
                node = TreeNode(val)
                
                children = []
                while node_stack and _level < node_stack[-1][1]:
                    child_node, _ = node_stack.pop()
                    children.append(child_node)
                
                if children:
                    if len(children) == 2:
                        node.left = children[1]
                        node.right = children[0]
                    else:
                        node.left = children[0]
                node_stack.append((node, _level))
        
        if not s:
            return
        
        N = len(s)
        val_stack = []
        node_stack = []
        i = 0
        level = 0
        
        for j in range(N):
            if s[j] not in '()':
                continue
            
            push(i,j)
            i = j+1
            
            if s[j] == '(':
                level += 1
            elif s[j] == ')':
                pop()
                level -= 1
            
            # print(val_stack, node_stack, level)
        
        # if input is [4], we don't have parentheses
        push(i,N)
        pop()
        
        return node_stack[0][0]
                
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        N=len(s)
        if N==0:
            return

        paren = {}
        stack = []
        
        for i in range(N):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                paren[stack.pop()] = i
        
        def dfs(i, j):
            last = i
            while last < N and s[last] not in '()':
                last += 1
            
            val = s[i:last]
            node = TreeNode(int(val))
            if i + len(val) - 1 == j:
                return node

            i += len(val)
            if i in paren:
                left_end = paren[i]
                node.left = dfs(i+1, left_end-1)
                right_start = paren[i]+1
                if right_start in paren:
                    node.right = dfs(right_start+1, paren[right_start]-1)
            return node
        
        return dfs(0, N-1)
            
                        
from lib.Tree import *
s = Solution()
print(show(s.str2tree('4(2(3)(1))(6(5))')))
print(show(s.str2tree('4(2(3)(1))(6(5)(7))')))
print(show(s.str2tree('-4(2(3)(1))(6(5)(7))')))
print(show(s.str2tree('-4')))
