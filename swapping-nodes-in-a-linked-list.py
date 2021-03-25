# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
A: start from the kth node
B: start from the head

when A ends, B is at last kth node
"""
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        A = head
        for _ in range(k-1):
            A = A.next
        
        kth_head = A
        A = A.next
        B = head
        while A:
            A = A.next
            B = B.next
        kth_head.val, B.val = B.val, kth_head.val
        return head
        
