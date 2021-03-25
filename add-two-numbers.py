"""
time: O(max(L1+L2))
space: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        
        carry = 0
        while l1 or l2:
            _sum = carry
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            
            carry = _sum // 10
            node.next = ListNode(val=_sum % 10)
            node = node.next
        
        if carry:
            node.next = ListNode(val=carry)
        
        return dummy.next
            
        
