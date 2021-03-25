# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        seen = {}
        def dfs(node, ll):
            if node is None:
                return False
            
            if node not in memo:
                memo[node] = False
                # print(node.val, ll.val)
                if node.val == ll.val:
                    ll = ll.next
                    if ll is None:
                        memo[node] = True
                    else:
                        memo[node] = dfs(node.left, ll) or dfs(node.right, ll)
                
                if ll != head and node.val == head.val:
                    ll = ll.next
                    if ll is None:
                        memo[node] = True
                    else:
                        memo[node] |= dfs(node.left, head.next) or dfs(node.right, head.next)
            return memo[node]
        
        return dfs(root, head)
            
            
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(ll, node):
            if node is None:
                return False
            
            if head.val == node.val:
                return dfs(head.next, node.left) or dfs(head.next, node.right)
            
            if ll.val != node.val:
                return False
            
            if ll.next is None:
                return node.left is None or node.right is None
            
            return dfs(ll.next, node.left) or dfs(ll.next, node.right)
        
        return dfs(head, root)
        
        
